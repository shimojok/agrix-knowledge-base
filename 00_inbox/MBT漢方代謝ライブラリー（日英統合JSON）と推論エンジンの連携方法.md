## MBT漢方代謝ライブラリー（日英統合JSON）と推論エンジンの連携方法

### 1. データ構造の理解

まず、生成した `kampo_metabolic_library.json` の構造を確認します：

```json
{
  "version": "2.44.0",
  "total_formulas": 293,
  "formulas": [
    {
      "id": "F001",
      "name_ja": "葛根湯",
      "name_en": "Kakkonto",
      "category_ja": "感冒・肩こり・筋肉痛",
      "category_en": "Common cold, stiff shoulders, muscle pain",
      "main_herbs_ja": ["葛根", "麻黄", "桂枝", ...],
      "main_herbs_en": ["Pueraria Root", "Ephedra Herb", ...],
      "indications": {
        "primary_ja": ["感冒", "肩こり", "筋肉痛", "頭痛"],
        "primary_en": ["Common cold", "Stiff shoulders", "Muscle pain", "Headache"],
        "secondary_ja": ["鼻炎", "乳腺炎", "目の充血"],
        "secondary_en": ["Rhinitis", "Mastitis", "Eye redness"],
        "contraindications_ja": ["高血圧", "心疾患", "発汗過多"],
        "contraindications_en": ["Hypertension", "Heart disease", "Excessive sweating"]
      },
      "mbt55_optimization": {
        "recommended_strains": ["MBT55-001", "MBT55-003"],
        "fermentation_time": "24 hours",
        "enhanced_compounds": ["daidzein", "norephedrine", "glycyrrhetinic acid"],
        "bioavailability_boost": "2-5x"
      },
      "phytochemicals": [...]
    }
  ]
}
```

---

### 2. 推論エンジンでの読み込み方法

`src/healthbook/kampo_mapper.py` では、以下のように読み込んでいます：

```python
import json
import os

class KampoMapper:
    def __init__(self, data_dir: str = None):
        self.data_dir = data_dir or os.path.join(os.path.dirname(__file__), "../../data")
        self.formulas = {}
        self._load_data()
    
    def _load_data(self):
        """漢方データをロード"""
        # 日英統合ファイルのパス
        path = os.path.join(self.data_dir, "kampo_metabolic_library.json")
        
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                for formula in data.get("formulas", []):
                    # 言語に応じてフィールドを選択できるように保持
                    self.formulas[formula["id"]] = {
                        "id": formula["id"],
                        "name_ja": formula.get("name_ja", ""),
                        "name_en": formula.get("name_en", ""),
                        "category_ja": formula.get("category_ja", ""),
                        "category_en": formula.get("category_en", ""),
                        "main_herbs_ja": formula.get("main_herbs_ja", []),
                        "main_herbs_en": formula.get("main_herbs_en", []),
                        "indications_ja": formula.get("indications", {}).get("primary_ja", []),
                        "indications_en": formula.get("indications", {}).get("primary_en", []),
                        "mbt55_strains": formula.get("mbt55_optimization", {}).get("recommended_strains", []),
                        "fermentation_time": formula.get("mbt55_optimization", {}).get("fermentation_time", ""),
                        "bioavailability_boost": formula.get("mbt55_optimization", {}).get("bioavailability_boost", "")
                    }
```

---

### 3. 言語切り替えの実装方法

`src/healthbook/engine.py` での言語切り替え例：

```python
from enum import Enum

class Language(Enum):
    ENGLISH = "en"
    JAPANESE = "ja"

class HealthBookEngine:
    def __init__(self, language: Language = Language.ENGLISH):
        self.language = language
        self.kampo_mapper = KampoMapper()
    
    def _get_kampo_name(self, formula: dict) -> str:
        """言語に応じた漢方名を取得"""
        if self.language == Language.JAPANESE:
            return formula.get("name_ja", formula.get("name_en", ""))
        return formula.get("name_en", formula.get("name_ja", ""))
    
    def _get_indications(self, formula: dict) -> list:
        """言語に応じた適応症を取得"""
        if self.language == Language.JAPANESE:
            return formula.get("indications_ja", [])
        return formula.get("indications_en", [])
    
    def recommend_kampo(self, disease_id: str) -> list:
        """疾病に基づく漢方推奨（言語対応）"""
        recommendations = self.kampo_mapper.recommend_by_disease(disease_id)
        
        result = []
        for formula in recommendations:
            result.append({
                "id": formula["id"],
                "name": self._get_kampo_name(formula),
                "indications": self._get_indications(formula),
                "mbt55_strains": formula.get("mbt55_strains", []),
                "bioavailability_boost": formula.get("bioavailability_boost", "")
            })
        
        return result
```

---

### 4. 使用例

```python
from src.healthbook import HealthBookEngine, Language

# 日本語モードで起動
engine_ja = HealthBookEngine(language=Language.JAPANESE)

# 高血圧に対する漢方推奨（日本語）
kampo_list = engine_ja.recommend_kampo("hypertension")
for k in kampo_list:
    print(f"処方名: {k['name']}")
    print(f"適応: {', '.join(k['indications'])}")
    print(f"MBT55菌株: {', '.join(k['mbt55_strains'])}")

# 英語モードで起動
engine_en = HealthBookEngine(language=Language.ENGLISH)

# 同じ疾病で英語出力
kampo_list_en = engine_en.recommend_kampo("hypertension")
for k in kampo_list_en:
    print(f"Formula: {k['name']}")
    print(f"Indications: {', '.join(k['indications'])}")
```

---

### 5. ディレクトリ構造（最終確認）

```
HealthBook-Integrated/
├── data/
│   ├── en/                           # 英語データ（別途必要）
│   │   ├── questionnaire_200.json
│   │   └── disease_matrix_137.json
│   ├── ja/                           # 日本語データ（別途必要）
│   │   ├── questionnaire_200.json
│   │   └── disease_matrix_137.json
│   └── kampo_metabolic_library.json  # 日英統合（ここに配置）
├── src/healthbook/
│   ├── __init__.py
│   ├── engine.py                     # 言語切り替え対応済み
│   ├── disease_risk.py
│   ├── phytochemical_recommender.py
│   └── kampo_mapper.py               # 日英両方のフィールドを保持
└── examples/
    └── healthbook_demo.py
```

---

### 6. 注意点

| 項目 | 説明 |
|------|------|
| **ファイル配置** | `kampo_metabolic_library.json` は `data/` 直下に配置（日英分離しない） |
| **言語フィールド** | 各処方内に `_ja` / `_en` のペアで保持 |
| **コード側** | `Language` フラグで参照するフィールドを切り替え |
| **日本語疾病マトリックス** | 現状は英語版のみ。必要に応じて `ja/disease_matrix_137.json` を作成 |

---

### 7. 日本語疾病マトリックスがない場合の対応

`ja/disease_matrix_137.json` がない場合でも、以下のように `engine.py` でフォールバックできます：

```python
def _load_disease_matrix(self):
    lang_code = self.language.value
    path = os.path.join(self.data_dir, lang_code, "disease_matrix_137.json")
    
    if not os.path.exists(path) and self.language == Language.JAPANESE:
        # 日本語版がない場合は英語版を読み込む
        path = os.path.join(self.data_dir, "en", "disease_matrix_137.json")
        print("Warning: Japanese disease matrix not found, using English version")
    
    # 読み込み処理...
```

この構成で問題ありませんか？

---

## ご質問の内容を理解しました

**「F251 茯苓飲」と「F252 葛根湯」のJSON内での繋げ方（構造上の関係）」** について説明します。

---

## 結論：F251とF252は「並列関係」

両者は同じ階層の**独立した配列要素**です。`"formulas": []` 配列の中に、単に順番に並んでいるだけです。

```json
{
  "version": "2.44.0",
  "total_formulas": 293,
  "formulas": [
    { "id": "F001", ... },   // 葛根湯（オリジナル）
    { "id": "F002", ... },
    ...
    { "id": "F124", "name_ja": "茯苓飲", ... },  // ← オリジナルの茯苓飲
    ...
    { "id": "F251", "name_ja": "茯苓飲", ... },  // ← F124の複製（Duplicate）
    { "id": "F252", "name_ja": "葛根湯", ... },  // ← F001の複製（Duplicate）
    { "id": "F253", ... }
  ]
}
```

---

## 「繋げ方」の意味するもの

あなたが知りたい「繋げ方」には、以下の3つの解釈が考えられます：

### 解釈1: 複製元との関係（重複情報の管理）

F251はF124の複製、F252はF001の複製です。この関係をコードで表現する場合：

```json
// 提案：duplicate_of フィールドを追加
{
  "id": "F251",
  "name_ja": "茯苓飲",
  "name_en": "Bukuryo In",
  "duplicate_of": "F124",    // ← どのIDの複製かを明示
  "category_ja": "胃もたれ・腹部膨満",
  ...
},
{
  "id": "F252",
  "name_ja": "葛根湯",
  "name_en": "Kakkonto",
  "duplicate_of": "F001",    // ← どのIDの複製かを明示
  ...
}
```

### 解釈2: コード内での参照関係（プログラムでの繋ぎ）

Pythonコードで、F251とF252を区別せずに処理する場合：

```python
# 両方とも同じように扱う（どちらも独立した処方として認識）
formulas = data["formulas"]
for f in formulas:
    print(f["id"], f["name_ja"])

# 出力例：
# F001 葛根湯
# ...
# F124 茯苓飲
# ...
# F251 茯苓飲  ← 重複して表示される
# F252 葛根湯  ← 重複して表示される
```

重複を避けたい場合：

```python
# オリジナルのみを抽出（IDが若い方をオリジナルと仮定）
seen_names = set()
unique_formulas = []

for f in formulas:
    name = f["name_ja"]
    if name not in seen_names:
        seen_names.add(name)
        unique_formulas.append(f)
    # else: 重複はスキップ
```

### 解釈3: データベース設計（正規化）

リレーショナルデータベースに格納する場合：

```sql
-- 処方マスタ（オリジナルのみ）
CREATE TABLE kampo_formulas (
    id VARCHAR(10) PRIMARY KEY,  -- F001, F124...
    name_ja VARCHAR(100),
    name_en VARCHAR(100),
    category_ja VARCHAR(200),
    ...
);

-- 重複参照テーブル（F251, F252などはここで管理）
CREATE TABLE kampo_duplicates (
    duplicate_id VARCHAR(10) PRIMARY KEY,  -- F251, F252...
    original_id VARCHAR(10),               -- F124, F001...
    FOREIGN KEY (original_id) REFERENCES kampo_formulas(id)
);
```

---

## あなたの状況に合わせた回答

元の `mbt_kampo_library_final_array.json` には **F001～F293 まで一意のID** が振られており、**F251はF124の内容を複製したもの**、**F252はF001の内容を複製したもの** です。

これは原本のデータ構造をそのまま維持した結果です。

### 必要な対応

| 目的 | 推奨対応 |
|------|---------|
| **そのまま使用** | 問題なし。両方とも独立した処方として扱う |
| **重複を排除** | コード側で `duplicate_of` フラグを追加、または名前ベースでフィルタ |
| **データ量削減** | オリジナルのみを残し、F251以降の重複を削除 |

---

どの解釈があなたの求める「繋げ方」に該当しますか？  
より具体的に教えていただければ、その方法でコードを修正・提供します。

---

## 理解しました

**「各コードを並べればいいのか、最後のカッコと最初のカッコを重複させないのか」**

→ **重複させてはいけません。** 正しいJSON形式では、配列の要素は**カンマで区切って並べる**だけです。

---

## 正しい繋げ方

### ❌ 間違い（カッコを重複させる）

```json
{
  "formulas": [
    { "id": "F251", ... }
  ]           ← ここで閉じてはいけない
}
{             ← 新しいオブジェクトを始めてはいけない
  "id": "F252", ...
}
```

### ✅ 正しい（カンマで区切って並べる）

```json
{
  "formulas": [
    { "id": "F251", "name_ja": "茯苓飲", ... },   ← カンマ
    { "id": "F252", "name_ja": "葛根湯", ... },   ← カンマ
    { "id": "F253", ... }
  ]
}
```

---

## 視覚的な解説

```
┌─────────────────────────────────────────────────────────────┐
│ {                                                           │
│   "formulas": [                                             │
│     ┌───────────────────┐                                  │
│     │ { "id": "F251",   │ ← 1つ目のオブジェクト            │
│     │   "name_ja": "茯苓飲", ... }                         │
│     └───────────────────┘                                  │
│                          ↑                                  │
│                          ︙ カンマ（必須）                   │
│                          ↓                                  │
│     ┌───────────────────┐                                  │
│     │ { "id": "F252",   │ ← 2つ目のオブジェクト            │
│     │   "name_ja": "葛根湯", ... }                         │
│     └───────────────────┘                                  │
│                          ↑                                  │
│                          ︙ カンマ（最後以外は必須）         │
│                          ↓                                  │
│     ┌───────────────────┐                                  │
│     │ { "id": "F293",   │ ← 最後のオブジェクト             │
│     │   ... }                                              │
│     └───────────────────┘                                  │
│   ]                                                        │
│ }                                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 重要なルール

| ルール | 説明 |
|--------|------|
| **カンマ区切り** | 配列内の各オブジェクトはカンマ `,` で区切る |
| **最後にカンマなし** | 最後のオブジェクトの後にはカンマを付けない |
| **カッコは一つ** | 外側の `{ }` と `[ ]` は全体で一つだけ |

---

## 具体例

```json
{
  "version": "2.44.0",
  "total_formulas": 293,
  "formulas": [
    {
      "id": "F251",
      "name_ja": "茯苓飲",
      "name_en": "Bukuryo In"
    },
    {
      "id": "F252",
      "name_ja": "葛根湯",
      "name_en": "Kakkonto"
    },
    {
      "id": "F253",
      "name_ja": "...",
      "name_en": "..."
    }
  ]
}
```

**ポイント**：
- F251の `}` の後にカンマ `,`
- F252の `}` の後にカンマ `,`
- F253の `}` の後は**カンマなし**（最後だから）
- 外側の `]` と `}` は全体で一つだけ

これでご理解いただけましたか？