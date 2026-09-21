主要なHealthBook Platform v5コードの構造説明をお願いします。

---

HealthBook Platform v5.0 のコード構造を体系的に解説します。

---

## 全体アーキテクチャ

```
healthbook_v5.jsx（単一ファイル構成）
│
├── 1. 言語定数 T             ← 日英UI文字列
├── 2. 問診データ Q           ← 全200問（日英）
├── 3. 疾病マトリックス DM    ← 浜田式135疾患
├── 4. MBT55経路 MBT55        ← 5代謝経路
├── 5. 疾病→経路マップ D2P
├── 6. 推論エンジン runEngine()
└── 7. UI HealthBookV5        ← React本体
```

---

## 1. 言語定数 `T`

```javascript
const T = {
  en: { title, subtitle, startBtn, ansOpts:["Often","Sometimes","No"], steps:[...], ... },
  ja: { title, subtitle, startBtn, ansOpts:["よくある","ときどき","なし"], steps:[...], ... }
};
```

**役割：** UIに表示するすべての文字列を日英で定義。`lang` stateが `"ja"` か `"en"` かによって `t = T[lang]` で切り替わります。ボタンラベル・回答選択肢・解析ステップメッセージまですべてここで管理しています。

---

## 2. 問診データ `Q`

```javascript
const Q = {
  "1": {
    qe: "Meal times are irregular",   // 英語問診文
    qj: "食事の時間が不定である",      // 日本語問診文
    cat: "eating_habits",              // カテゴリ
    rf:  ["不規則型"],                 // ← 食生活マトリックス列名（推論キー）
    me:  "Disrupted digestive rhythm → autonomic nervous system load",
    mj:  "消化リズムの乱れ → 自律神経負荷",
    w:   0.7                           // 重み係数
  },
  // ... 全200問
};
```

**重要な設計思想：** `rf`（リスク因子）は **日本語のマトリックス列名** で統一されています。英語問診のリスク因子（`irregular`, `breakfast_skipping` 等）を変換マッピング辞書でこの形式に変換済みです。これにより推論エンジンは言語に関係なく同一ロジックで動作します。

```
questionnaire_200_en_new.json  →  EN_TO_MATRIX_RF辞書  →  rf:["不規則型"]
questionnaire_200_jp_new.json  →  FULL_RF_MAP辞書      →  rf:["不規則型"]
                                                              ↓
                                                    DM の rf列と照合（推論）
```

---

## 3. 疾病マトリックス `DM`

```javascript
const DM = {
  "糖尿病": {
    did: "D006",          // ICD-11 disease_matrix_137_kampo.json のID
    ev:  "B",             // エビデンスレベル A/B/C
    rf:  [                // 浜田式リスク因子リスト（病気と食生活の関係シート）
      "不規則型", "欠食型（朝食抜き）", "甘物", "間食多い", ...
    ],
    km:  [                // 推奨漢方処方（disease_matrix_137_kampo.json から）
      { id:"F018", n:"瓜呂根湯", p:["PATH_01"], m:["MBT55-001"] },
      { id:"F251", n:"茯苓飲",   p:["PATH_04"], m:["MBT55-003"] },
    ]
  }
};
```

**3つのデータソースが統合されています：**

```
病気と食生活の関係シート.xlsx  →  rf（食生活リスク因子）
disease_matrix_137_kampo.json  →  did（ICD-11コード）+ km（漢方処方ID）
kampo_metabolic_library.json   →  km.n（処方名）+ km.p（MBT55経路）
```

---

## 4. 推論エンジン `runEngine()`

v5の核心部分です。5ステップで動作します。

```javascript
function runEngine(answers) {

  // Step 1: 回答からアクティブなリスク因子を収集（重み付き）
  const activeRFs = {};
  Object.entries(answers).forEach(([qid, ans]) => {
    const intensity = (ans==="よくある"||ans==="Often") ? 1.0 : 0.6;
    Q[qid].rf.forEach(rf => {
      activeRFs[rf] = Math.max(activeRFs[rf]||0, intensity * Q[qid].w);
    });
  });

  // Step 2: 疾病リスクスコア算出（マッチ率 × 重み）
  const scores = {};
  Object.entries(DM).forEach(([disease, v]) => {
    let s = 0;
    v.rf.forEach(rf => { if (activeRFs[rf]) s += activeRFs[rf]; });
    scores[disease] = { score: s / v.rf.length, ev: v.ev };
  });

  // Step 3: MBT55 五経路の介入優先度を算出
  const pAct = { PATH_01:0, PATH_02:0, PATH_03:0, PATH_04:0, PATH_05:0 };
  sorted.slice(0,10).forEach(([disease]) => {
    DM[disease].km.forEach(k => {
      k.p.forEach(p => { pAct[p] += 0.15; });  // 漢方の経路から積算
    });
  });

  // Step 4: 漢方処方マッチング（上位疾患から重複排除）
  const kampoMap = {};
  sorted.slice(0,8).forEach(([disease, {score}]) => {
    DM[disease].km.forEach(k => {
      if (!kampoMap[k.id]) kampoMap[k.id] = { ...k, forDisease: disease, diseaseScore: score };
    });
  });

  // Step 5: 予防スコア算出（上位10疾患の平均リスクから逆算）
  const score = Math.round((1 - avgRisk) * 100);

  return { sorted, activeRFs, impacts, pAct, kampoRecs, score };
}
```

**データの流れ：**

```
answers（問診回答）
    ↓ Q[qid].rf × intensity × weight
activeRFs（リスク因子マップ）
    ↓ DM[disease].rf との一致率
scores（疾患別リスクスコア）
    ↓ DM[disease].km の PATH
pAct（MBT55経路活性度）
    ↓ 上位疾患の km を集約
kampoRecs（推奨漢方処方）
```

---

## 5. UIの状態管理

```javascript
// 8つのstateで画面全体を管理
const [lang,            setLang]            = useState("ja");    // 言語
const [screen,          setScreen]          = useState("intro"); // 現在の画面
const [answers,         setAnswers]         = useState({});      // 問診回答
const [catIdx,          setCatIdx]          = useState(0);       // 問診カテゴリ
const [page,            setPage]            = useState(0);       // 問診ページ
const [results,         setResults]         = useState(null);    // 分析結果
const [tab,             setTab]             = useState("risk");  // 結果タブ
const [expandedDisease, setExpandedDisease] = useState(null);    // 展開中の疾患
```

---

## 6. 画面遷移フロー

```
intro
  ↓ 問診開始ボタン
questionnaire（16ページ × 10問/ページ）
  │  eating_habits(5p) → lifestyle(5p) → symptoms(6p) → comprehensive
  ↓ 最終ページで「分析実行」
analyzing（7ステップのアニメーション）
  ↓ runEngine() 実行後
results（5タブ）
  ├── 疾病リスク（タップで漢方展開）
  ├── 漢方処方（293処方から選定）
  ├── MBT55経路（5経路バーチャート）
  ├── 代謝解析（問診→代謝インパクト一覧）
  └── API（JSON出力プレビュー）
```

---

## 7. 言語切り替えの仕組み

最もシンプルで強力な部分です。

```javascript
// どの画面にも共通で表示されるトグルコンポーネント
const LangToggle = () => (
  <div>
    {["ja","en"].map(l => (
      <button onClick={() => setLang(l)}>
        {l==="ja" ? "🇯🇵 日本語" : "🇺🇸 English"}
      </button>
    ))}
  </div>
);

// 使用例（問診）
const qText = lang==="ja" ? q.qj : q.qe;   // 問診文を切り替え
const mText = lang==="ja" ? q.mj : q.me;   // 代謝説明を切り替え
const label = t.catLabel[q.cat];            // カテゴリ名を切り替え
```

`lang` stateが変わるだけで、`t = T[lang]` を通じてUIの全文字列が即座に再レンダリングされます。**推論ロジックは言語非依存**のため、解析結果は変わりません。

---

## GitHub リポジトリとの対応

```
shimojok/HealthBook-Integrated/
│
├── data/ja/questionnaire_200.json    → Q の qj・mj フィールドの元データ
├── data/en/questionnaire_200.json    → Q の qe・me フィールドの元データ
├── data/ja/disease_matrix_137_kampo.json → DM の did・ev・km の元データ
├── data/kampo_metabolic_library.json → DM.km の name・pathway の元データ
│
└── frontend/src/App.jsx              ← healthbook_v5.jsx（本ファイル）
```

現在のReact版はこれら4つのJSONをビルド時にコンパイル済みの定数として内包しています。将来Azure Functionsに移行する際は、これらをAPI呼び出しに置き換えるだけで対応できます。