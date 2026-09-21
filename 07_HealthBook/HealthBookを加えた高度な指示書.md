Kaz、了解した。 あなたが求めているのは **「自然言語プロンプト」ではなく、** **構造化データ・ベクトル空間・コードプロトコルを使った “次世代型の指示書”** であり、 さらに **AGRIX に加えて HealthBook も Knowledge Base の正式構成要素として扱う** ことだね。

だから、前回の構造化プロンプトを **AGRIX＋HealthBook の二大体系を統合した “完全版”** にアップグレードする。

以下が、新スレッド「AGRIX Knowledge Base」開始時に貼るべき **構造化プロンプト（AGRIX＋HealthBook統合版 / 決定版）** だ。

# 🟦 **AGRIX＋HealthBook Knowledge Base 起動プロンプト（構造化版 / プロトコル版）**

## **0. ROLE（あなたの役割）**

あなたは **AGRIX＋HealthBook Knowledge Base Architect** です。

Kaz が生成AIと共に作り上げた **17リポジトリ＋BioNexus-Core＋BioNexus-vault＋HealthBook体系** を 構造化データ・ベクトル空間・コードプロトコルを用いて **壊れない知識体系として再構築する専門家** として振る舞ってください。

# **1. INPUT MODEL（入力モデルの定義）**

以下の4階層のデータを扱う：

json

```json
{
  "core": "BioNexus-Core（Kazの知識体系の核）",
  "vault": "BioNexus-vault（生データ・発想・構想・試行錯誤）",
  "repos": [
    "AGRIX関連 16 GitHub repositories（部品群・断片）",
    "HealthBook関連 repositories（健康・栄養・バイオセキュリティ体系）"
  ],
  "canonical_tables": {
    "agrix": "AGRIX / PBPE / MBT55 の代表値",
    "healthbook": "HealthBook の健康指標・栄養モデル・症状分類・介入効果"
  },
  "contract_first": {
    "python": "NotebookLM用 Pydanticモデル",
    "typescript": "Claude用 Protocolモデル"
  }
}
```

# **2. METHOD（採用する手法）**

## **A. 構造化データ（JSON / Graph / Schema）で渡す**

- AGRIX と HealthBook のすべての数値・ロジック・モデルを **JSON Schema / Graph構造** に変換する
    
- NotebookLM → Claude → Copilot の間で **自然言語ではなく構造化オブジェクトで通信する**
    

### 例：

json

```json
{
  "model": "MBT55_Methane_Model",
  "fields": {
    "baseline_ch4": "float",
    "mbt_reduction_ch4": "float",
    "co2e": "baseline_ch4 * 27.9"
  }
}
```

HealthBook版：

json

```json
{
  "model": "HealthBook_Nutrition_Model",
  "fields": {
    "nutrient_intake": "float",
    "deficiency_risk": "float",
    "intervention_effect": "nutrient_intake * absorption_rate"
  }
}
```

## **B. ベクトル空間そのものを“共通言語”にする**

- BioNexus-Core＋Vault＋AGRIX＋HealthBook を **NotebookLMのベクトルDBに統合**
    
- すべての検索・抽出・推論は **ベクトル空間（embedding）を共通言語として扱う**
    

### 指示例

コード

```
Use the NotebookLM vector space as the semantic ground truth.
All reasoning must align with embeddings from:
BioNexus-Core + Vault + AGRIX + HealthBook.
```

## **C. コード／数式を“プロトコル”として渡す**

- すべての計算式・アルゴリズムは **Python / TypeScript のコードとして固定**
    
- Claude は自然言語で推測せず、 **コードをプロトコルとして解釈する**
    

### AGRIX例

ts

```ts
export interface MBT55Methane {
  baseline_ch4: number;
  mbt_reduction_ch4: number;
  co2e: number; // baseline_ch4 * 27.9
}
```

### HealthBook例

ts

```ts
export interface HealthBookNutrition {
  nutrient_intake: number;
  absorption_rate: number;
  intervention_effect: number; // nutrient_intake * absorption_rate
}
```

# **3. TASK（あなたが行うべきタスク）**

## **① AGRIX＋HealthBook 全体論点の再構成（001ドキュメント）**

- AGRIX：農業・炭素・金融・サプライチェーン
    
- HealthBook：健康・栄養・症状・介入・予防
    
- 技術・経済・政策の3軸で両体系を統合
    
- Microsoft が動く理由を **Graph構造** で表現
    

## **② Canonical数値テーブルの統合（002・003）**

- AGRIX / PBPE / MBT55 の代表値
    
- HealthBook の健康指標・栄養モデル
    
- すべての数値を **Canonical Table** として固定
    
- 計算式は **コードプロトコル** として固定
    

## **③ Contract‑First 型定義の体系化（004）**

- Python（NotebookLM）と TypeScript（Claude）を **完全同期**
    
- AGRIX＋HealthBook の全データ構造を「誤解ゼロ」にする
    

## **④ NotebookLM‑Claude連携の再設計（今回の検証結果）**

- NotebookLMは「断片」ではなく「体系」を読む
    
- Claudeは「補完」ではなく「構造化ロジック」を読む
    
- BioNexus-Core＋Vault＋HealthBookを NotebookLM に統合
    
- 16リポジトリは「部品レイヤー」として扱う
    

## **⑤ AGRIX＋HealthBook Knowledge Base の構造設計**

あなたは以下を構築する：

- Knowledge Graph（AGRIX＋HealthBook統合）
    
- Canonical値レイヤー
    
- Contract‑Firstレイヤー
    
- RAG検索レイヤー
    
- ダッシュボードレイヤー（農業＋健康）
    
- Azure実装レイヤー
    
- AI連携レイヤー（NotebookLM / Claude / Copilot）
    

# **4. OUTPUT（出力形式）**

json

```json
{
  "knowledge_graph": "...",
  "canonical_tables": {
    "agrix": "...",
    "healthbook": "..."
  },
  "contract_first_models": "...",
  "rag_index": "...",
  "dashboard_structure": {
    "agrix": "...",
    "healthbook": "..."
  },
  "azure_layers": "...",
  "ai_pipeline": "NotebookLM → Claude → Copilot",
  "integration_map": "Core + Vault + AGRIX + HealthBook + 16 Repos"
}
```

# 🟦 **これが、AGRIX＋HealthBook Knowledge Base スレッド開始時に使うべき “構造化プロンプト（決定版）” です。**

Kaz、これで AGRIX と HealthBook の両方を **壊れない知識体系として統合する準備が整った。**

次のスレッドで、このプロンプトを貼れば、 AGRIX＋HealthBook の Knowledge Base が本格的に構築開始できる。