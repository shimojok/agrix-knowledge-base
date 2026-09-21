## 🗃️PBPE金融モデル構築 PBPE-Dashboard DeepSeek

[GitHub - shimojok/PBPE-Dashboard · GitHub](https://github.com/shimojok/PBPE-Dashboard)

## 1. リポジトリ

| 項目             | 内容                                                       |
| -------------- | -------------------------------------------------------- |
| **リポジトリ名**     | `PBPE-Dashboard`                                         |
| **GitHub URL** | `https://github.com/shimojok/PBPE-Dashboard`             |
| **ブランチ**       | `main`                                                   |
| **コミット数**      | 50コミット                                                   |
| **主要言語**       | TypeScript 46.9%, Python 35.6%, Solidity 14.4%, CSS 2.7% |

### ディレクトリ構造
```
PBPE-Dashboard/
├── README.md / README_JA.md          # 日英README
├── CONTRIBUTING.md / CONTRIBUTING_JA.md  # 貢献ガイドライン
├── requirements.txt                   # Python依存関係
├── dashboard/                         # Reactフロントエンド
│   ├── src/components/               # UIコンポーネント（5つ）
│   ├── src/models/                   # フロントエンドモデル
│   └── package.json                  # npm依存関係
├── contracts/                         # スマートコントラクト
│   ├── CarbonBackedCoffee.sol        # 炭素担保コーヒートークン
│   ├── YieldLinkedToken.sol          # 収量連動トークン
│   └── RegenerativeBond.sol          # 再生型債券
├── models/                            # Python計算エンジン
│   ├── coffee_impact.py              # 収益・炭素計算
│   ├── carbon_sequestration.py       # 炭素隔離モデル
│   └── financial_engine.py           # 金融工学モデル
├── azure/                             # Azure設定
│   ├── arm_templates/                # デプロイテンプレート
│   ├── functions/                    # Azure Functions
│   └── digital_twins/                # Digital Twins定義
├── docs/                              # 詳細ドキュメント
│   ├── ja/ (6ファイル)
│   └── en/ (6ファイル)
└── proposals/                         # 提案書類
    ├── Starbucks_Proposal_PBPE_Coffee.md
    └── Gates_Foundation_Executive_Summary.md
```

---

## 2. 目的

**PBPE（Planetary Bio-Phenome Engine：惑星生命圏フェノームエンジン）**は、農業生産を測定可能・検証可能・金融化可能な気候資産に変換する、世界初の統合プラットフォームです。

### 中核的ミッション
> **「コーヒー1杯が地球を再生する」**
> *コーヒー購入 = 炭素隔離 = 気候変動ファイナンス資産*

### 対象ステークホルダー
| 対象 | 提供価値 |
|------|---------|
| **コーヒー生産者** | 収入110%増、7つの新規収入源 |
| **焙煎・飲料企業** | スコープ3削減、調達安定化 |
| **投資家** | 新規気候資産クラスへの投資機会 |
| **国際機関** | SDGs達成への貢献 |

---

## 3. 内容と特徴

### 4層アーキテクチャ

| レイヤー | 名称 | 機能 |
|---------|------|------|
| **第1層** | MBT55バイオ層 | 病害抑制（85%）、土壌再生、炭素固定 |
| **第2層** | AGRIXフェノミクス層 | リアルタイム計測、AI分析、炭素定量化 |
| **第3層** | SafelyChain検証層 | 暗号的MRV、トークン化、二重計上防止 |
| **第4層** | MABC金融層 | 債券発行、トークン化、ポートフォリオ管理 |

### 主要数値成果

| 指標 | 数値 | 意義 |
|------|------|------|
| 農場レベルROI | **17.8倍** | 投資1ドル→17.80ドル |
| システム乗数 | **94.1倍** | 農場1ドル→総経済価値94.10ドル |
| 炭素隔離量 | **2.5 tCO₂e/ha/年** | 年間125本の植林相当/ha |
| 農家収入増加 | **+110%** | 1,850→3,892ドル/ha |
| さび病抑制率 | **85%** | 発生率60%→9% |
| 10年NPV（500万ha） | **724億ドル** | 割引率8% |
| 市場創出規模 | **1,875-5,900億ドル** | 10年累計 |

### 技術スタック

| コンポーネント | 技術 |
|---------------|------|
| フロントエンド | React 18, TypeScript, D3.js, Recharts, TailwindCSS |
| バックエンド | Python 3.9, FastAPI, NumPy, SciPy |
| ブロックチェーン | Solidity 0.8.19, Hardhat, OpenZeppelin |
| クラウド | Microsoft Azure (Functions, Digital Twins, Cosmos DB) |

---

## 4. 可能なデモの内容

### 4.1 フロントエンドデモ（Reactダッシュボード）

```bash
cd /workspaces/PBPE-Dashboard/dashboard
npm run dev
```

**確認できること：**
- 5つのタブ（Dashboard, Carbon Ledger, Impact Simulator, Yield Predictor, Finance Engine）
- 資本フローのSankeyダイアグラム
- 炭素隔離量の推移グラフ
- シミュレーションパラメータの操作と結果反映
- 金融商品一覧とポートフォリオ分析

### 4.2 Pythonモデルデモ

```bash
cd /workspaces/PBPE-Dashboard
python models/demo.py
```

**確認できること：**
- 農家収益計算の詳細内訳
- 炭素隔離動態シミュレーション
- システム乗数効果（94.1倍）
- 投資収益率（IRR 187%）
- ポートフォリオ最適化結果

### 4.3 スマートコントラクトデモ（準備中）

```bash
cd /workspaces/PBPE-Dashboard/contracts
npx hardhat compile
```

**確認できること：**
- 炭素担保トークンの発行ロジック
- 収量連動トークンの決済メカニズム
- 再生型債券の利払い計算

---

## 5. Dashboardの有無

| 項目 | 状態 |
|------|------|
| **ダッシュボードの有無** | ✅ **あり** |
| **開発環境** | Codespacesで動作確認済 |
| **アクセス方法** | `npm run dev` → `http://localhost:3000` |
| **デプロイ** | 未（ローカル開発サーバーのみ） |

### 現在の動作状況

| 機能 | 状態 | 備考 |
|------|------|------|
| Dashboard（メイン） | ✅ 正常 | 資本フロー、主要KPI表示 |
| Carbon Ledger | ✅ 正常 | 期間切替は要修正 |
| Impact Simulator | ✅ 正常 | Baseline/MBT55切替動作 |
| Yield Predictor | ✅ 正常 | グラフ表示 |
| Finance Engine | ✅ 正常 | Market Dataタブ修正済 |
| ダークモード | ✅ 適用済 | 黒背景に変更済 |

---

## 6. Dashboardの表示機能

### タブ別機能一覧

| タブ | 表示内容 | インタラクション |
|------|---------|-----------------|
| **Dashboard** | 総炭素隔離量、アクティブ農家数、総ロック価値、資本フロー図、主要KPI | 期間切替、レポート出力 |
| **Carbon Ledger** | 炭素隔離トレンド、累積貯留量、クレジット発行状況、農場別実績、検証履歴 | 期間切替（7d/30d/90d/1y）、エクスポート |
| **Impact Simulator** | 収量・収益・炭素のシミュレーション、Baseline vs MBT55比較、SDGs貢献度 | パラメータ調整、シナリオ切替 |
| **Yield Predictor** | 収量予測（信頼区間付き）、気象予報、病害リスク評価、栽培推奨 | 農場選択、予測期間変更 |
| **Finance Engine** | 債券一覧、ポートフォリオ配分、炭素価格推移、コーヒー価格推移、債券指数 | タブ切替（Bonds/Portfolio/Market）、取引実行 |

### 主要KPI表示

| 指標 | 表示値 |
|------|--------|
| 総炭素隔離量 | 1.25M tCO₂e |
| アクティブ農家数 | 50,000 |
| 総ロック価値 | $5.0B |
| コーヒー購入量 | 400M kg |
| 農家ROI | 17.8x |
| システム乗数 | 94.1x |

### グラフ・チャート種類

| 種類 | 使用箇所 |
|------|---------|
| Sankeyダイアグラム | 資本フロー可視化 |
| AreaChart | 炭素隔離トレンド |
| LineChart | 累積炭素、価格推移 |
| BarChart | 収益比較、病害リスク |
| PieChart | 炭素クレジット配分、ポートフォリオ配分 |
| ComposedChart | 収量予測（信頼区間付き） |
| RadialBarChart | SDGs貢献度 |

---

## 補足：今後の課題

| 課題 | 優先度 | 対応予定 |
|------|--------|---------|
| Carbon Ledger期間切替の動的更新 | 中 | useEffect修正 |
| Comparisonモードの完全実装 | 低 | 後日対応 |
| スマートコントラクトのテスト実行 | 中 | Hardhat環境整備中 |
| Azureへのデプロイ | 低 | 必要時に対応 |
| スターバックス/ゲイツ財団への提案 | 高 | 提案書類完成済 |

---

このまとめは、2026年4月11日時点の `PBPE-Dashboard` リポジトリの状態を反映しています。