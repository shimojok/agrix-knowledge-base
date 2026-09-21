# HealthBook / MBT55 / HealthBook-MBT55-Unified
# プロジェクト移管プロンプト（PMO継続指示書）
# 作成日: 2026-05-11
# 前セッション完了状態を引き継いで即座に作業を継続すること。

---

## あなたの役割

あなたはPMOです。
以下の全コンテキストと完了状態を読み込み、
**フェーズ2（フェノタイピングエンジン）の実装**から即座に着手してください。

---

## プロジェクト概要

MBT55微生物群（立山連峰山麓由来）が「生薬・ポリフェノールなどの複合有機物を
分解・代謝し、ヒトに有用な代謝産物を生成する」プロセスを全代謝経路レベルで
トレースし、以下のシステムとして統合する。

### システム三層構造

```
Layer 3: 臨床応用層（HealthBook Demo）
         200問診 → フェノタイピング → 疾病リスク → 漢方・ファイトケミカル推奨

Layer 2: 代謝解析層（全代謝経路 + MBT Probiotics）
         生薬・ポリフェノール → 微生物分解 → 活性代謝物 → PATH_01〜05活性化マップ

Layer 1: 微生物生態学基盤層（M3-BioSynergy）
         120菌種動態 / ハイパーサイクル / 栄養カスケード
```

---

## 統合リポジトリ

**メイン**: https://github.com/shimojok/HealthBook-MBT55-Unified

関連リポジトリ（参照用）:
- https://github.com/shimojok/M3-BioSynergy
- https://github.com/shimojok/HealthBook-Integrated
- https://github.com/shimojok/M3-BioSynergy-Core
- https://github.com/shimojok/HealthBook-AI
- https://github.com/shimojok/BioNexus-Core

---

## 完了済み成果物（再実装不要）

### データ構造（全て完成済み）
| ファイル | 内容 | 場所 |
|---------|------|------|
| questionnaire_200_jp_new.json | 浜田式200問診（日本語版） | data/ |
| questionnaire_200_en_new.json | 浜田式200問診（英語版） | data/ |
| disease_matrix_137_json.md | 137疾病×ICD-11×漢方処方対応 | data/ |
| kampo_metabolic_library_json.md | 293漢方処方×MBT55経路ライブラリー | data/ |
| 病気と食生活の関係シート.xlsx | 浜田式 食生活×93疾患マトリックス | data/ |
| ファイトケミカル分類_索引ページ.xlsx | 下條式ファイトケミカル分類 | data/ |

### React フロントエンド（完成済み v5.0）
| ファイル | 内容 |
|---------|------|
| healthbook_v5.jsx | 日英バイリンガル全200問UI（App.jsx として配置） |
| healthbook-platform-v5.zip | GitHub + Azure Static Web Apps デプロイ一式 |

**v5.0の特徴:**
- 全200問（食習慣50 + 生活習慣50 + 症状98 + 総合2）日英完全実装
- 135疾患マトリックス × 293漢方処方 × MBT55五経路 統合
- 疾患タップで推奨漢方が展開、ICD-11コード・エビデンスレベル付き
- Azure Static Web Apps 自動デプロイ設定済み（.github/workflows/）
- リアルタイム日英切り替え（lang state で全UI連動）

### フェーズ1（Layer 2 代謝解析層）— 完成済み ✅

**完成ファイル:**
```
src/layer2_metabolism/
├── __init__.py
└── metabolic_pathway_db.py     ← MetabolicPathwayDatabase クラス

data/pathways/
└── master_pathways.json        ← 22種基質の完全代謝経路DB

tests/
└── test_metabolic_pathway_db.py
```

**MetabolicPathwayDatabase の主要API:**
```python
db = MetabolicPathwayDatabase(data_dir="data/pathways")

# 基質ID → 活性代謝物予測（温度補正あり）
trace = db.predict_metabolites("S001")           # 葛根 → エクオール
trace = db.predict_metabolites("S006")           # 人参 → コンパウンドK
trace = db.predict_metabolites("S007")           # 鹿茸 → IGF-1類縁体（3段階）

# 複合処方スクリーニング
result = db.screen_formulation(["S001","S006","S009"])   # シナジースコア付き
result = db.screen_formulation(["S007","S008","S014"])   # MKS16マラリアプロトコル

# 疾病コード → 推奨基質
recs = db.recommend_substrates_for_disease("D006")       # 糖尿病

# 複数基質のPATH活性スコア一括取得
scores = db.get_pathway_scores_for_substrates(["S001","S002","S005"])

# 活性代謝物 → 産生基質の逆引き
sources = db.find_substrates_producing_metabolite("equol")
```

**動作確認済みデータ（フェーズ1完了基準 全クリア）:**
- 基質数: 22種（PMO基準: 20種以上 ✅）
- メタ株数: 5群（MBT_META_01〜05 ✅）
- 22/22 基質すべての代謝物予測成功 ✅
- PATH_01〜05 活性スコア計算（例: S001葛根 → PATH_01:1.0, PATH_05:0.83）✅
- D006糖尿病推奨基質: 黄連・緑茶・人参・桂皮・地黄 ✅
- MKS16マラリアプロトコル（鹿茸+地龍+青蒿）シナジー: 0.58 ✅

**5つのMBT55メタ株（確定）:**
| メタ株 | 分類 | 経路 | 核心通貨 |
|--------|------|------|---------|
| MBT_META_01 | Bacillus sp.（立山浄土菌群） | PATH_01 | 乳酸 |
| MBT_META_02 | Atopostipes sp.（立山目無菌群） | PATH_02 | キノン |
| MBT_META_03 | Bacillus sp.（立山剣・薬師菌群） | PATH_05 | エクオール/コンパウンドK |
| MBT_META_04 | Clostridium sp.（立山龍王菌群） | PATH_04 | フルボ酸 |
| MBT_META_05 | 乳酸菌＋酪酸産生菌群 | PATH_03 | 酪酸 |

---

## 未完了タスク（これから対応）

### 🔴 フェーズ2（最高優先度）— 今すぐ着手

**目的:** 200項目問診 → PATH_01〜05 の定量スコア変換

**実装場所:** `src/layer2_metabolism/phenotyping_engine.py`

**要件:**
1. 問診項目 → 代謝ブロックの重み行列を定義
   - 例: Q2（朝食欠食） → PATH_03: -0.85, PATH_05: -0.60
   - 例: Q55（運動不足） → PATH_03: -0.92, PATH_02: -0.70
   - 例: Q9（塩分好き） → PATH_02: -0.90
   - 全200問 × 5経路の重み行列（PHENOTYPING_WEIGHTS辞書）
2. `calculate_path_scores(answers: dict) -> dict` 関数
   - 入力: {qid: "よくある"|"ときどき"|"なし"} または英語版
   - 出力: {"PATH_01": 0.72, "PATH_02": -0.45, ...}（-1.0〜+1.0）
3. `PhenotypeProfile` データクラス
   - path_scores, dominant_pathway, deficient_pathways, phenotype_label
4. `classify_phenotype(path_scores) -> str` 関数
   - 例: "代謝症候群型", "腸内環境不全型", "神経疲弊型", etc.
5. questionnaire_200_jp_new.json の `metabolic_impact` フィールドを活用すること
6. 日英バイリンガル対応（lang="ja"|"en"）

**フェーズ1との接続:**
```python
# フェーズ2の出力がフェーズ3の入力になる
path_scores = phenotyping_engine.calculate_path_scores(answers)
# → フェーズ3: MBT Probiotics スクリーニングに渡す
strain_recs = probiotic_screener.recommend(path_scores, disease_ids)
```

---

### 🔴 フェーズ3（最高優先度）— フェーズ2完了後

**目的:** 菌株 × 基質 × 代謝産物のスクリーニングエンジン

**実装場所:** `src/layer2_metabolism/probiotic_screener.py`

**要件:**
1. `MBT55StrainMatrix` クラス（5メタ株 × 基質 × 代謝産物の対応表）
2. `screen_probiotics(path_scores, disease_ids, available_substrates)` 関数
   - 入力: フェーズ2のpath_scores + 疾病リスク上位 + 処方中の生薬
   - 出力: 推奨菌株セット + 期待される活性代謝物 + 投与プロトコル
3. MBT_META_01〜05 の機能スコアリングロジック
4. HealthBook v5.0のDMデータ（疾患×漢方）との統合

---

### 🟡 フェーズ4（中優先度）— フェーズ2・3完了後

**目的:** エンドツーエンドの統合デモ完成

**実装場所:** React v5.0への追加 + Streamlit（HealthBook-AI連携）

**完成フロー:**
```
問診200問
  ↓ フェーズ2
PATH_01〜05 スコア（定量値付き）
  ↓ Layer 2 (フェーズ1)
代謝経路ブロック特定 + 活性代謝物予測
  ↓ フェーズ3
推奨MBT55菌株セット + 漢方処方
  ↓ React v5.0 新タブ追加
「代謝経路詳細」タブ（PATH定量バー・代謝物リスト・推奨菌株）
```

---

## PMO成功基準（最終完了条件）

- [ ] PATH_01〜05の経路活性スコアが問診から計算できる ← **フェーズ2で達成**
- [x] 主要な生薬・ポリフェノール（20種以上）の代謝経路がトレースできる ✅
- [x] MBT55菌株（5株以上）の機能マトリックスが完成する ✅
- [ ] 入力「問診＋症状」→ 出力「推奨菌株＋漢方＋期待効果」が一貫動作 ← **フェーズ3・4で達成**

---

## 重要な設計思想・制約事項

### MBT55ハイパーサイクル理論（必ず遵守）
- 3段階酵素カスケード反応（一次分解→生体変換→活性代謝物生成）
- 核心通貨: 乳酸（界面）/ キノン（電子）/ 酪酸（抗炎症）/ フルボ酸（ミネラル）/ エクオール（ホルモン）
- dH₂/dt≈0 理論（立山龍王菌群による電子消散）

### フェノタイピング重み行列の設計原則
- 食習慣（Q1-50）: 食生活マトリックス列名と直接対応
- 生活習慣（Q51-100）: PATH_03（糖代謝）とPATH_04（酸化還元）への影響が大きい
- 症状（Q101-198）: 代謝ブロックの下流指標として扱う
- よくある: intensity=1.0、ときどき: intensity=0.6、Often/Sometimes も同様

### データフォーマット規約
- 問診ID: 文字列 ("1"〜"200")
- 疾病ID: ICD-11ベース ("D001"〜"D137", "D_malaria"等)
- 漢方ID: F番号 ("F001"〜"F293")
- 基質ID: S番号 ("S001"〜"S022")
- メタ株: "MBT_META_01"〜"MBT_META_05"
- PATH: "PATH_01"〜"PATH_05"
- 言語: lang="ja"|"en"（全モジュールで統一）

---

## 報告形式（各フェーズ完了時）

1. **実装したファイル一覧**（パス付き）
2. **主要APIの使用例**（コード付き）
3. **テスト実行結果**（PASSED/FAILED数）
4. **PMO成功基準との対応**（チェックリスト更新）
5. **残課題と次フェーズへの引き渡し事項**

---

## 即時アクション

以下を今すぐ実行してください：

1. `src/layer2_metabolism/phenotyping_engine.py` の実装開始
2. `PhenotypeWeightMatrix` — 全200問 × 5経路の重み行列定義
3. `PhenotypingEngine` クラス実装
4. `tests/test_phenotyping_engine.py` 作成・実行
5. フェーズ2完了報告（上記報告形式に従って）

質問があれば聞いてください。なければ即座にコードを書き始めてください。
