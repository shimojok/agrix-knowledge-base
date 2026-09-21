---
tag: AgriWare
---
DS001
```
project-root/
├── app/
│   ├── api/
│   │   ├── agrix/                      # AGRIX-OS API
│   │   │   ├── soil-telemetry/route.ts
│   │   │   ├── she-score/route.ts
│   │   │   ├── vscore/route.ts
│   │   │   └── hypercycle/route.ts     # MBT55ハイパーサイクル診断
│   │   ├── msc/                        # MSC（MBT Sustainable Cycle）
│   │   │   ├── biosecurity/route.ts    # バイオセキュリティ
│   │   │   ├── biocontrol/route.ts     # バイオコントロール
│   │   │   ├── carbon-sequestration/route.ts  # 炭素隔離
│   │   │   └── nutrient-cascade/route.ts      # 栄養カスケード
│   │   ├── safetychain/                # SafetyChain™ API
│   │   │   ├── product/route.ts
│   │   │   ├── pricing/route.ts
│   │   │   └── certificate/route.ts
│   │   └── pbpe/                       # PBPE Marketplace API
│   │       ├── marketplace/route.ts    # 取引所
│   │       ├── carbon-credit/route.ts  # 炭素クレジット
│   │       └── valuation/route.ts      # 資産評価
│   ├── dashboard/
│   │   ├── agrix/                      # 生産者向け
│   │   │   ├── page.tsx               # 土壌ダッシュボード
│   │   │   └── components/
│   │   │       ├── SoilTelemetry.tsx
│   │   │       ├── SHEscore.tsx
│   │   │       └── HypercycleStatus.tsx
│   │   ├── safetychain/                # 消費者向け
│   │   │   ├── page.tsx               # SafetyChainダッシュボード
│   │   │   └── components/
│   │   │       ├── VScoreCard.tsx
│   │   │       ├── FunctionalityCard.tsx
│   │   │       └── CertificateViewer.tsx
│   │   └── pbpe/                       # 投資家・トレーダー向け
│   │       ├── page.tsx               # PBPE市場ダッシュボード
│   │       └── components/
│   │           ├── MarketOverview.tsx
│   │           ├── CarbonCreditTrading.tsx
│   │           └── AssetValuation.tsx
│   └── page.tsx                        # 統合トップページ
├── lib/
│   ├── agrix/
│   │   ├── soilDynamics.ts
│   │   ├── sheEngine.ts
│   │   └── hypercycleModel.ts          # MBT55ハイパーサイクル演算
│   ├── msc/
│   │   ├── biosecurityEngine.ts
│   │   ├── carbonSequestration.ts
│   │   └── nutrientCascade.ts
│   ├── safetychain/
│   │   ├── vscoreModel.ts
│   │   ├── functionalityIndex.ts
│   │   └── certificateBuilder.ts
│   └── pbpe/
│       ├── pricingModel.ts             # 4レイヤー価格
│       ├── carbonCreditEngine.ts
│       └── valuationEngine.ts          # 資産評価エンジン
├── types/
│   ├── agrix.types.ts
│   ├── msc.types.ts
│   ├── safetychain.types.ts
│   └── pbpe.types.ts
└── prisma/
    ├── schema.prisma                   # データベーススキーマ（統合）
    └── seed.ts
```

lib/agrix/hypercycleModel.ts
lib/msc/carbonSequestration.ts
lib/safetychain/integratedEngine.ts
lib/pbpe/marketplaceEngine.ts
app/dashboard/agrix/page.tsx
app/dashboard/safetychain/page.tsx
app/dashboard/pbpe/page.tsx

DS002
```
app/api/agrix/
├── agents/                         # AIエージェントAPI
│   ├── hypercycle/route.ts         # Agent-1実行
│   ├── biosecurity/route.ts        # Agent-2実行
│   ├── biocontrol/route.ts         # Agent-3実行
│   └── resource-cascade/route.ts   # Agent-4実行
├── orchestrate/route.ts            # 4エージェント統合実行（全体診断）
└── acain/                          # インターフェースゲートウェイ
    ├── to-safetychain/route.ts     # SafetyChain向け標準化出力
    └── to-pbpe/route.ts            # PBPE向け標準化出力
```

app/api/agrix/orchestrate/route.ts
app/dashboard/agrix/page.tsx

DS003
```
app/api/agrix/
├── agents/
│   ├── hypercycle/route.ts          # Agent-1
│   ├── biosecurity/route.ts         # Agent-2
│   ├── biocontrol/route.ts          # Agent-3
│   ├── resource-cascade/route.ts    # Agent-4
│   ├── msc-operation/route.ts       # Agent-5 【NEW】
│   └── carbon-asset/route.ts        # Agent-6 【NEW】
├── orchestrate/                     # 全エージェント統合診断
│   ├── full/route.ts                # 6エージェント一括実行
│   └── light/route.ts               # 主要3エージェント（高速版）
└── acain/                           # インターフェースゲートウェイ
    ├── to-safetychain/route.ts      
    ├── to-pbpe/route.ts             
    ├── to-insurance/route.ts        # 【NEW】保険リスク評価出力
    └── to-government/route.ts       # 【NEW】政府報告用標準フォーマット
```

types/tenant.types.ts
app/dashboard/agrix/page.tsx（修正版）
lib/agrix/agents/mscOperation.ts
app/api/agrix/acain/to-insurance/route.ts

DS004
lib/gates-dashboard/gatesCalculator.ts
app/gates-dashboard/page.tsx
app/api/gates-dashboard/calculate/route.ts

DS005
```
app/dashboard/
├── agrix/
│   ├── page.tsx                    # 統合ダッシュボード（生産者ランディング）
│   ├── modules/
│   │   ├── mbt55-ecosystem/        # Module 1: MBT55エコシステム
│   │   │   ├── page.tsx
│   │   │   └── components/
│   │   │       ├── MicrobiomeComposition.tsx
│   │   │       ├── DecomposerActivity.tsx
│   │   │       └── HypercycleStatus.tsx
│   │   ├── msc-production/         # Module 2: MSC資材生産
│   │   │   ├── page.tsx
│   │   │   └── components/
│   │   │       ├── HumusProduction.tsx
│   │   │       ├── FertilizerProfile.tsx
│   │   │       └── FeedQuality.tsx
│   │   ├── carbon-accounting/      # Module 3: 炭素・GHGアカウンティング
│   │   │   ├── page.tsx
│   │   │   └── components/
│   │   │       ├── SOCDashboard.tsx
│   │   │       ├── SequestrationTrend.tsx
│   │   │       ├── MethaneReduction.tsx
│   │   │       └── GatesTarget.tsx
│   │   ├── learning/               # Module 4: 生産者学習・実践
│   │   │   ├── page.tsx
│   │   │   └── components/
│   │   │       ├── LearningPath.tsx
│   │   │       ├── Simulator.tsx
│   │   │       └── PrescriptionEngine.tsx
│   │   └── acain-gateway/          # Module 5: ACAINゲートウェイ
│   │       ├── page.tsx
│   │       └── components/
│   │           ├── SafetyChainExport.tsx
│   │           ├── PBPEExport.tsx
│   │           └── MicrosoftIntegration.tsx
│   └── gates-dashboard/            # ビル・ゲイツ氏専用（別ルート）
│       └── page.tsx
```

types/mbt55.types.ts
types/msc/humus.types.ts
types/msc/fertilizer.types.ts
types/msc/feed.types.ts
types/carbon-accounting.types.ts
types/learning.types.ts
types/simulator.types.ts
types/prescription.types.ts
types/acain.types.ts

DS006
```
lib/agrix/module1/
├── types/
│   ├── mbt55.types.ts          # MBT55コア型定義
│   ├── hypercycle.types.ts     # ハイパーサイクル関連型
│   ├── biocontrol.types.ts     # バイオコントロール型
│   └── biosecurity.types.ts    # バイオセキュリティ型
├── engines/
│   ├── hypercycle.engine.ts    # Agent-1: ハイパーサイクル演算
│   ├── biosecurity.engine.ts   # Agent-2: バイオセキュリティ演算
│   ├── biocontrol.engine.ts    # Agent-3: バイオコントロール演算
│   └── decomposer.engine.ts    # Agent-4: 分解菌活性演算
├── orchestrate/
│   └── full.ts                 # 全エージェント統合診断
└── index.ts                    # モジュール公開API
```

lib/agrix/module1/types/mbt55.types.ts
lib/agrix/module1/types/hypercycle.types.ts
lib/agrix/module1/types/biocontrol.types.ts
lib/agrix/module1/types/biosecurity.types.ts
lib/agrix/module1/engines/hypercycle.engine.ts
lib/agrix/module1/engines/biosecurity.engine.ts
lib/agrix/module1/engines/biocontrol.engine.ts
lib/agrix/module1/engines/decomposer.engine.ts
lib/agrix/module1/orchestrate/full.ts  統合オーケストレーション（全エージェント実行）
lib/agrix/module1/index.ts
app/api/agrix/module1/orchestrate/route.ts
app/dashboard/agrix/modules/mbt55-ecosystem/page.tsx

DS007
```
lib/agrix/module2/
├── types/
│   ├── humus.types.ts          # MBT腐植質関連型
│   ├── fertilizer.types.ts     # 発酵肥料関連型
│   └── feed.types.ts           # 発酵飼料関連型
├── engines/
│   ├── humus.engine.ts         # 腐植質生産エンジン
│   ├── fertilizer.engine.ts    # 発酵肥料生産エンジン
│   └── feed.engine.ts          # 発酵飼料生産エンジン
├── orchestrate/
│   └── full.ts                 # 3資材統合生産計画
└── index.ts                    # モジュール公開API
```

lib/agrix/module2/types/humus.types.ts
lib/agrix/module2/types/fertilizer.types.ts
lib/agrix/module2/types/feed.types.ts
lib/agrix/module2/engines/humus.engine.ts
lib/agrix/module2/engines/fertilizer.engine.ts
lib/agrix/module2/engines/feed.engine.ts
lib/agrix/module2/orchestrate/full.ts
lib/agrix/module2/index.ts
app/api/agrix/module2/orchestrate/route.ts
app/dashboard/agrix/modules/msc-production/page.tsx

DS008
```
lib/agrix/module3/
├── types/
│   ├── soil-organic-carbon.types.ts    # SOC関連型
│   ├── sequestration.types.ts          # 炭素隔離関連型
│   ├── methane.types.ts               # メタン削減関連型
│   └── ghg-accounting.types.ts        # 総合GHGアカウンティング型
├── engines/
│   ├── soc.engine.ts                  # SOC計測・予測エンジン
│   ├── sequestration.engine.ts        # 炭素隔離エンジン
│   ├── methane.engine.ts              # メタン削減エンジン
│   └── ghg-accounting.engine.ts       # 総合GHGアカウンティングエンジン
├── orchestrate/
│   └── full.ts                        # 全アカウンティング統合実行
└── index.ts                           # モジュール公開API
```


DS009
```
lib/agrix/module4/
├── types/
│   ├── learning.types.ts          # 学習コンテンツ型
│   ├── simulator.types.ts         # シミュレーター型
│   └── prescription.types.ts      # 処方提案型
├── engines/
│   ├── learning.engine.ts         # 学習進捗管理エンジン
│   ├── simulator.engine.ts        # MBT55シミュレーションエンジン
│   └── prescription.engine.ts     # 処方提案エンジン
├── orchestrate/
│   └── full.ts                    # 学習→シミュレーション→処方の統合
└── index.ts                       # モジュール公開API
```

DS010

```
lib/agrix/module5/
├── types/
│   ├── safetychain-gateway.types.ts   # SafetyChain出力型
│   ├── pbpe-gateway.types.ts          # PBPE出力型
│   ├── insurance-gateway.types.ts     # 保険出力型
│   ├── government-gateway.types.ts    # 政府出力型
│   └── microsoft-gateway.types.ts     # マイクロソフト出力型
├── engines/
│   ├── safetychain.gateway.ts
│   ├── pbpe.gateway.ts
│   ├── insurance.gateway.ts
│   ├── government.gateway.ts
│   └── microsoft.gateway.ts
├── orchestrate/
│   └── full.ts                         # 全ゲートウェイ統合実行
└── index.ts
```

DS011
進捗状況

```
lib/agrix/
├── module1/                          # ✅ 完全実装（14ファイル）
│   ├── types/                        # 4つの型定義ファイル
│   ├── engines/                      # 4つのエンジン
│   ├── orchestrate/                  # 統合実行
│   └── index.ts
├── module2/                          # ✅ 完全実装（11ファイル）
│   ├── types/                        # 3つの型定義
│   ├── engines/                      # 3つのエンジン
│   ├── orchestrate/                  # 統合実行
│   └── index.ts
├── module3/                          # ✅ 完全実装（13ファイル）
│   ├── types/                        # 4つの型定義
│   ├── engines/                      # 4つのエンジン
│   ├── orchestrate/                  # 統合実行
│   └── index.ts
├── module4/                          # ✅ 完全実装（10ファイル）
│   ├── types/                        # 3つの型定義
│   ├── engines/                      # 3つのエンジン
│   ├── orchestrate/                  # 統合実行
│   └── index.ts
└── module5/                          # 🔵 設計完了（実装待ち）
    ├── types/                        # 設計済み
    └── (engines/orchestrate 未実装)

app/api/agrix/
├── module1/orchestrate/route.ts      # ✅ 実装済み
├── module2/orchestrate/route.ts      # ✅ 実装済み
├── module3/orchestrate/route.ts      # ✅ 実装済み
├── module4/orchestrate/route.ts      # ✅ 実装済み
└── module5/                          # 🔵 未実装

app/dashboard/agrix/modules/
├── mbt55-ecosystem/page.tsx          # ✅ 実装済み
├── msc-production/page.tsx           # ✅ 実装済み
├── carbon-accounting/                # 🔵 設計済み（未実装）
├── learning/page.tsx                 # ✅ 実装済み
└── acain-gateway/                    # 🔵 未実装

app/gates-dashboard/page.tsx          # ✅ 実装済み（ビル・ゲイツ専用）
```

DS016

app/gates-dashboard/page.tsx（一部修正・追加）
lib/bridge/python-bridge.ts
lib/agrix/module1/types/data-model.types.ts
lib/agrix/module1/adapters/data-model-adapter.ts
lib/agrix/module1/engines/hypercycle.engine.ts（書き換え版）
lib/agrix/module1/engines/biosecurity.engine.ts（書き換え版）
lib/agrix/module1/engines/biocontrol.engine.ts（書き換え版）
lib/agrix/module1/orchestrate/full.ts（一部修正）
lib/agrix/module5/mappers/pbpe-mapper.ts

DS017

```
agrix-os/                          # メインリポジトリ
├── .gitmodules                    # MBT-Biosecurity-Engineをサブモジュールとして指定
├── package.json                   # Next.js依存関係
├── requirements.txt               # Python依存関係（科学モデル用）
├── README.md                      # プロジェクト概要（英語＋日本語）
├── docs/
│   ├── architecture.md            # システムアーキテクチャ図
│   ├── api-reference.md           # APIリファレンス
│   ├── deployment.md              # デプロイ手順
│   └── presentation/              # ビル・ゲイツ氏プレゼン資料
│       ├── slide-deck.md          # スライド内容
│       └── demo-script.md         # デモスクリプト
├── app/                           # Next.js App Router
│   ├── api/agrix/                 # AGRIX API Routes（Module 1-5）
│   ├── dashboard/                 # ダッシュボードページ
│   └── gates-dashboard/           # ビル・ゲイツ専用ページ
├── lib/
│   ├── agrix/                     # AGRIXコアモジュール
│   │   ├── module1/               # ✅ 実装済み（ラッパー版に更新）
│   │   ├── module2/               # ✅ 実装済み（変更なし）
│   │   ├── module3/               # ✅ 実装済み（微調整予定）
│   │   ├── module4/               # ✅ 実装済み（変更なし）
│   │   └── module5/               # 🔵 実装予定
│   ├── bridge/                    # Pythonブリッジ
│   │   └── python-bridge.ts       # ✅ コード提示済み
│   └── types/                     # 共有型定義
│       └── data-model.types.ts    # ✅ Data_Model.json準拠
├── scripts/
│   ├── setup.sh                   # 環境セットアップスクリプト
│   └── run-models.py              # Pythonモデルを呼び出すラッパー
└── submodules/
    └── MBT-Biosecurity-Engine/    # git submodule（既存リポジトリ）
```


DS018
現状の総括

```
agrix-os/                          # メインリポジトリ（新規作成）
├── .gitmodules                    # MBT-Biosecurity-Engineをサブモジュール指定
├── package.json                   # Next.js依存関係
├── requirements.txt               # Python科学モデル用
├── README.md                      # 英語（＋日本語）
├── docs/
│   ├── architecture.md            # システムアーキテクチャ図
│   ├── api-reference.md           # APIリファレンス
│   ├── deployment.md              # デプロイ手順
│   ├── data-model-schema.md       # Data_Model.jsonの解説
│   └── presentation/              # ビル・ゲイツ氏プレゼン資料
│       ├── slide-deck.md
│       └── demo-script.md
├── app/
│   ├── api/agrix/                 # AGRIX API Routes
│   │   ├── module1/               # ✅ 実装済み（ラッパー版）
│   │   ├── module2/               # ✅ 実装済み
│   │   ├── module3/               # ✅ 実装済み（微調整予定）
│   │   ├── module4/               # ✅ 実装済み
│   │   └── module5/               # 🔵 実装予定
│   ├── dashboard/                 # 生産者ダッシュボード
│   └── gates-dashboard/           # ビル・ゲイツ専用ページ
├── lib/
│   ├── agrix/                     # AGRIXコアモジュール
│   │   ├── module1/               # （ラッパー版に更新済み）
│   │   ├── module2/
│   │   ├── module3/
│   │   ├── module4/
│   │   └── module5/               # 🔵 実装予定
│   ├── bridge/                    # Pythonブリッジ
│   │   └── python-bridge.ts       # ✅ コード提示済み
│   └── types/                     # 共有型定義
│       └── data-model.types.ts    # ✅ Data_Model.json準拠
├── scripts/
│   ├── setup.sh                   # 環境セットアップ
│   └── run-models.py              # Pythonモデルラッパー
└── submodules/
    └── MBT-Biosecurity-Engine/    # git submodule（既存リポジトリ）
```







