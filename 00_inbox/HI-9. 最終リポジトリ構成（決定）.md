ファイル一覧は下記の通りです。貴方が作成したものです。

M3-BioSynergy/                    ← ここがルート
├── LICENSE
├── README.md
├── requirements.txt
├── src/                          ← ここ！
│   ├── core/
│   │   ├── __init__.py           ← ✅ 作成済み
│   │   ├── microbial_diversity.py ← ✅ 作成済み
│   │   ├── hypercycle_engine.py   ← ✅ 作成済み
│   │   └── nutrient_cascade.py    ← ✅ 作成済み
│   └── utils/                     ← ここに作成！
│       └── __init__.py            ← 作成する
├── examples/
│   └── basic_simulation.py
└── tests/                         ← ここに作成！
    └── __init__.py                ← 作成する

---

## ファイル構成確認

M3-BioSynergyの現在の構成を確認しました。**移動すべき健康推論関連ファイルは存在しません**。

現在のM3-BioSynergyは、MBT55コア機能（微生物生態学、ハイパーサイクル）専用として**このまま維持**します。

---

## 最終リポジトリ構成（決定）

### 1. M3-BioSynergy（既存・維持）
**役割**: MBT55コア機能（微生物生態学、ハイパーサイクル、炭素循環）

```
M3-BioSynergy/
├── LICENSE
├── README.md
├── requirements.txt
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── microbial_diversity.py
│   │   ├── hypercycle_engine.py
│   │   └── nutrient_cascade.py
│   └── utils/
│       └── __init__.py
├── examples/
│   └── basic_simulation.py
└── tests/
    └── __init__.py
```

### 2. HealthBook-Integrated（新規作成）
**役割**: 浜田式問診 × 疾病マトリックス × MBT漢方代謝ライブラリー × 推論エンジン

```
HealthBook-Integrated/
├── README.md (英語)
├── README.ja.md (日本語)
├── LICENSE (MIT)
├── requirements.txt
├── data/
│   ├── en/
│   │   ├── questionnaire_200.json       ✅ 完了
│   │   ├── disease_matrix_137.json      ✅ 完了
│   │   └── kampo_metabolic_library.json (生成中)
│   └── ja/
│       ├── questionnaire_200.json       ✅ 完了
│       ├── disease_matrix_137.json      ✅ 完了
│       └── kampo_metabolic_library.json (生成中)
├── src/
│   └── healthbook/
│       ├── __init__.py
│       ├── engine.py                    (統合推論エンジン)
│       ├── disease_risk.py              (疾病リスク予測)
│       ├── phytochemical_recommender.py (ファイトケミカル推奨)
│       └── kampo_mapper.py              (漢方処方マッパー)
├── examples/
│   ├── healthbook_demo.py
│   └── mbt55_integration.py              (M3-BioSynergy連携)
├── tests/
└── docs/
    ├── en/
    └── ja/
```

---

## 進捗状況

| リポジトリ | フェーズ | 項目 | ステータス |
|-----------|---------|------|-----------|
| **M3-BioSynergy** | - | コア実装 | ✅ 完了 |
| **HealthBook-Integrated** | 1-1 | 問診200項目（日英） | ✅ 完了 |
| | 1-2 | 疾病マトリックス（日英） | ✅ 完了 |
| | 1-3 | MBT漢方代謝ライブラリー（日英） | 🔄 実行中 |
| | 2 | 統合推論エンジン | ⏳ 未着手 |
| | 3 | README（日英） | ⏳ 未着手 |

---

## 次のステップ

**フェーズ1-3: MBT漢方代謝ライブラリー（日英）** の生成を続行します。

293処方の英語化を進めます。よろしいですか？

