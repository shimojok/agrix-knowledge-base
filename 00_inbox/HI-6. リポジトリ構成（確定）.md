ごめんなさい。昨日下記のリポジトリを設定しましたが、HealthBook_Integratedに変更します。

M3-BioSynergy/
├── LICENSE                              ✅ MITライセンス
├── src/core/
│   ├── __init__.py                      ✅ モジュール定義
│   ├── microbial_dynamics.py            ✅ 既存
│   ├── microbial_diversity.py           ✅ 120菌種多様性モデル
│   ├── hypercycle_engine.py             ✅ ハイパーサイクルエンジン
│   └── nutrient_cascade.py              ✅ 栄養カスケード
├── tests/
│   └── __init__.py                      ✅ テストモジュール
└── src/utils/
    └── __init__.py                      ✅ ユーティリティモジュール

M3-BioSynergyは、MBT55のバイオセキュリティ機能やハイパーサイクル向けとしましょう。

---

承知しました。リポジトリ構成を明確に分けます。

---

## リポジトリ構成（確定）

### 1. M3-BioSynergy（既存）
**役割**: MBT55のコア機能（微生物生態学、ハイパーサイクル、炭素循環）

```
M3-BioSynergy/
├── LICENSE                              ✅ MIT
├── src/core/
│   ├── microbial_dynamics.py            ✅ 120菌種動態
│   ├── microbial_diversity.py           ✅ 多様性モデル
│   ├── hypercycle_engine.py             ✅ ハイパーサイクル
│   ├── nutrient_cascade.py              ✅ 栄養カスケード
│   └── carbon_flow.py                   （予定）
├── tests/
└── src/utils/
```

### 2. HealthBook-Integrated（新規）
**役割**: 浜田式問診 × 疾病マトリックス × MBT漢方代謝ライブラリーの統合システム

```
HealthBook-Integrated/
├── README.md                            (英語)
├── README.ja.md                         (日本語)
├── LICENSE                              (MIT)
├── data/
│   ├── en/
│   │   ├── questionnaire_200.json       ✅ 完了
│   │   ├── disease_matrix_137.json      ✅ 完了
│   │   └── kampo_metabolic_library.json (準備中)
│   └── ja/
│       ├── questionnaire_200.json       ✅ 完了
│       ├── disease_matrix_137.json      ✅ 完了
│       └── kampo_metabolic_library.json (準備中)
├── src/
│   └── healthbook/
│       ├── __init__.py
│       ├── engine.py                    (統合推論エンジン)
│       ├── disease_risk.py              (疾病リスク予測)
│       ├── phytochemical_recommender.py (ファイトケミカル推奨)
│       └── kampo_mapper.py              (漢方処方マッパー)
├── examples/
│   ├── healthbook_demo.py
│   └── game3_integration.py
├── tests/
└── requirements.txt
```

---

## 進捗状況（更新）

| リポジトリ | フェーズ | 項目 | ステータス |
|-----------|---------|------|-----------|
| **M3-BioSynergy** | - | コア実装 | ✅ 完了 |
| | - | ライセンス | ✅ MIT |
| **HealthBook-Integrated** | 1-1 | 問診200項目（日英） | ✅ 完了 |
| | 1-2 | 疾病マトリックス（日英） | ✅ 完了 |
| | 1-3 | MBT漢方代謝ライブラリー（日英） | 🔄 実行中 |
| | 2 | 統合推論エンジン | ⏳ 未着手 |
| | 3 | README（日英） | ⏳ 未着手 |

---

## 次のステップ

**フェーズ1-3: MBT漢方代謝ライブラリー（日英）** を生成します。

`mbt_kampo_library_final_array.json`（293処方）から、日英両方のJSONを生成します。

**サンプル（F001 葛根湯 / Kakkonto）**：

```json
{
  "id": "F001",
  "name_ja": "葛根湯",
  "name_en": "Kakkonto",
  "category_ja": "感冒・肩こり・筋肉痛",
  "category_en": "Common cold, stiff shoulders, muscle pain",
  "main_herbs_ja": ["葛根", "麻黄", "桂枝", "芍薬", "甘草", "生姜", "大棗"],
  "main_herbs_en": ["Pueraria Root", "Ephedra Herb", "Cinnamon Bark", "Peony Root", "Licorice", "Ginger", "Jujube"],
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
  }
}
```

この形式で全293処方を生成します。よろしいですか？