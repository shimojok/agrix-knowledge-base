なお、日本人にも閲覧させますので、日英ファイル双方を作成し、別リポジトリにするか、日英切り替えにするなどしてください。

---

承知しました。

## 言語対応方針

**案：日英切り替え方式（単一リポジトリ）**

```
HealthBook-Integrated/
├── README.md (英語)
├── README.ja.md (日本語)
├── data/
│   ├── en/
│   │   ├── questionnaire_200.json
│   │   ├── disease_matrix_137.json
│   │   └── kampo_metabolic_library.json
│   └── ja/
│       ├── questionnaire_200.json
│       ├── disease_matrix_137.json
│       └── kampo_metabolic_library.json
├── src/
│   └── healthbook/
│       ├── __init__.py
│       ├── engine.py
│       └── ...
└── docs/
    ├── en/
    └── ja/
```

**メリット**：
- リポジトリ管理が一元化
- コードは共通、データのみ言語切替
- GitHub Pagesで言語選択可能

---

## 進捗状況（更新）

| フェーズ | 項目 | ステータス |
|---------|------|-----------|
| 1-1 | 問診200項目（日英） | ✅ 日本語: 完了 / 🔄 英語: 完了 |
| 1-2 | 137疾病マトリックス（日英） | ✅ 日本語: 完了 / 🔄 英語: 完了 |
| 1-3 | MBT漢方代謝ライブラリー（日英） | ⏳ 未着手 |
| 2 | 統合推論エンジン | ⏳ 未着手 |
| 3 | デモシステム | ⏳ 未着手 |
| 4 | README（日英） | ⏳ 未着手 |

---

### 次ステップ

**フェーズ1-3: MBT漢方代謝ライブラリー（日英）**

元のJSON（日本語）を基に、以下の構造で日英両方生成します：

```json
{
  "id": "F001",
  "name_ja": "葛根湯",
  "name_en": "Kakkonto",
  "category_ja": "感冒・肩こり・筋肉痛",
  "category_en": "Common cold, stiff shoulders, muscle pain",
  "main_herbs_ja": ["葛根", "麻黄", ...],
  "main_herbs_en": ["Pueraria Root", "Ephedra Herb", ...],
  "indications": {
    "primary_ja": ["感冒", "肩こり", ...],
    "primary_en": ["Common cold", "Stiff shoulders", ...]
  }
}
```

これで進めてよろしいですか？