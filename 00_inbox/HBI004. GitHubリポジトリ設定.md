MI_Coreは、中身はありません。削除します。貴方の言うとおり、HealthBook_Integratedにしましょう。

---

承知しました。

## GitHubリポジトリ設定

**リポジトリ名**: `HealthBook-Integrated`

以下の情報を確認・設定してください：

| 項目 | 設定値（案） |
|------|-------------|
| リポジトリ名 | `HealthBook-Integrated` |
| 公開/非公開 | Public（推奨） |
| README言語 | 英語（国際展開を考慮） |
| ライセンス | MIT（オープンソース） |

---

## 今後の作業予定

| フェーズ | 項目 | 内容 | 完了 |
|---------|------|------|------|
| 1-1 | データ準備 | ✅ 問診200項目（英語） | ✅ |
| 1-2 | データ準備 | ✅ 137疾病マトリックス（英語） | ✅ |
| 1-3 | データ準備 | MBT漢方代謝ライブラリー（英語） | 🔄 実行中 |
| 2 | コアエンジン | 統合推論エンジン実装 | ⏳ |
| 3 | デモ | 実行例・Game3連携 | ⏳ |
| 4 | ドキュメント | README, API仕様 | ⏳ |

---

### 次のステップ

**フェーズ1-3: MBT漢方代謝ライブラリー（英語版）** を生成します。

`mbt_kampo_library_final_array.json`（294処方）の英語化は規模が大きいため、まず**主要フィールドの英語化仕様**を提示します：

```json
{
  "version": "2.44.0",
  "total_formulas": 293,
  "formulas": [
    {
      "id": "F001",
      "name": "Kakkonto",
      "category": "Common cold, stiff shoulders, muscle pain",
      "main_herbs": ["Pueraria Root", "Ephedra Herb", "Cinnamon Bark", ...],
      "components": { ... },
      "indications": {
        "primary": ["Common cold", "Stiff shoulders", "Muscle pain", "Headache"],
        "secondary": ["Rhinitis", "Mastitis", "Eye redness"],
        "contraindications": ["Hypertension", "Heart disease", "Excessive sweating"]
      },
      "mbt55_optimization": { ... }
    }
  ]
}
```

この形式で進めてよろしいですか？