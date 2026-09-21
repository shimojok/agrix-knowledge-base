ご提示いただいた環境（Codespaces）のツリー構造に基づき、`PBPE-Marketplace` プロジェクトの正確なディレクトリ構成を以下にまとめました。

Plaintext

```
PBPE-Marketplace/
├── 00_Overview/
│   └── PBPE_Marketplace_Integration_EN.md
├── README.md
├── api/
│   ├── IO_Spec_PBPE_API.md
│   ├── openapi/
│   │   ├── openapi.yaml
│   │   └── pbpe-marketplace.yaml
│   ├── python/
│   │   ├── pbpe.py
│   │   ├── products.py
│   │   ├── rating_engine.py
│   │   └── settlements.py
│   └── typescript/
│       ├── index.ts
│       ├── pbpe.ts
│       ├── products.ts
│       ├── rating-engine.ts
│       └── settlements.ts
├── backend/
│   ├── main.py
│   ├── models/
│   │   ├── bonds.py
│   │   ├── credits.py
│   │   ├── impact.py
│   │   ├── insurance.py
│   │   ├── products.py
│   │   └── users.py
│   └── routers/
│       ├── bonds.py
│       ├── credits.py
│       ├── dashboard.py
│       ├── impact.py
│       ├── insurance.py
│       ├── products.py
│       └── users.py
├── desktop.ini
├── docs/
│   ├── README/
│   │   └── PBPE_Marketplace_README_EN.md
│   ├── api/
│   ├── architecture/
│   ├── credits/
│   ├── dashboard/
│   ├── data-model/
│   ├── deployment/
│   ├── diagrams/
│   ├── economic-model/
│   ├── evidence/
│   ├── finance/
│   ├── governance/
│   ├── identity/
│   ├── index.md
│   ├── integration/
│   ├── pitch/
│   ├── pitch-deck/
│   ├── smart-contracts/
│   ├── ui/
│   ├── usecases/
│   └── whitepaper/
├── engine/
│   ├── pbpe-impact-engine/
│   ├── rating-engine/
│   └── settlement-engine/
├── examples/
│   ├── impact-intent-7lines/
│   ├── pbpe-product-examples/
│   └── settlement-simulation/
├── frontend/
│   ├── next-env.d.ts
│   ├── package-lock.json
│   ├── package.json
│   ├── src/
│   │   ├── App.tsx
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   └── styles/
│   └── tsconfig.json
├── ledger/
│   ├── prisma/
│   └── schema/
├── modules/
│   └── pbpe-biosecurity/
└── ui/
    ├── README.md
    └── pages/
```

※ディレクトリ内のファイル詳細（docs配下の個別のマークダウンファイル等）については、以前いただいた `tree` コマンドの結果通りです。

こちらのディレクトリ構造に基づき、特定のディレクトリの設計方針について詳細な提案や、CI/CDパイプラインへの組み込み方法など、お手伝いできることはありますか？