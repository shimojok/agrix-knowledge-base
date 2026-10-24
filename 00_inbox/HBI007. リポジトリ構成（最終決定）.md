はい、お願いします。M3-BioSynergy（既存）リポジトリは、そのまま残しますか？

---

## リポジトリ構成（最終決定）

### 1. M3-BioSynergy（既存）→ **そのまま残す**
**役割**: MBT55のコア機能（微生物生態学、ハイパーサイクル、炭素循環）

```
M3-BioSynergy/
├── src/core/
│   ├── microbial_dynamics.py      ✅ 120菌種動態
│   ├── microbial_diversity.py     ✅ 多様性モデル
│   ├── hypercycle_engine.py       ✅ ハイパーサイクル
│   └── nutrient_cascade.py        ✅ 栄養カスケード
└── ...
```

**理由**:
- 既存のコード資産を維持
- MBT55のバイオセキュリティ機能はこちらで管理
- 今後も独立して発展可能

---

### 2. HealthBook-Integrated（新規）→ **新規作成**
**役割**: 浜田式問診 × 疾病マトリックス × MBT漢方代謝ライブラリーの統合システム

**両リポジトリの連携**:
```
HealthBook-Integrated
    ↓ (データ連携)
M3-BioSynergy (MBT55最適化計算)
```

---

## 進捗状況（更新）

| リポジトリ | フェーズ | 項目 | ステータス |
|-----------|---------|------|-----------|
| **M3-BioSynergy** | - | コア実装 | ✅ 完了（維持） |
| **HealthBook-Integrated** | 1-1 | 問診200項目（日英） | ✅ 完了 |
| | 1-2 | 疾病マトリックス（日英） | ✅ 完了 |
| | 1-3 | MBT漢方代謝ライブラリー（日英） | 🔄 実行中 |
| | 2 | 統合推論エンジン | ⏳ 未着手 |
| | 3 | README（日英） | ⏳ 未着手 |

---

## フェーズ1-3: MBT漢方代謝ライブラリー（日英）生成開始

**方針**:
- 元のJSON（293処方）を基に日英両方生成
- 英語名は漢方処方の標準英訳を使用
- 生薬名はJPS（日本薬局方）英語名に準拠

**生成対象**:
- `data/ja/kampo_metabolic_library.json`
- `data/en/kampo_metabolic_library.json`

---

### サンプル（F001 葛根湯 / Kakkonto）

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
  },
  "phytochemicals": [
    {
      "name_ja": "プエラリン",
      "name_en": "puerarin",
      "type_ja": "イソフラボン配糖体",
      "type_en": "isoflavone glycoside",
      "pathway": "PATH_01",
      "clinical_effects_ja": ["肩こり改善", "頭痛改善", "発汗促進"],
      "clinical_effects_en": ["Shoulder stiffness relief", "Headache relief", "Sweating promotion"]
    }
  ]
}
```

全293処方についてこの形式で生成します。進めてよろしいですか？