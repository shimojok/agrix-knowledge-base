# `/09-Documents/PMOS-Architecture-Book/06-PMOS-Data-and-Knowledge-Flow.md`

## 6. PMOSデータ・知識フロー・アーキテクチャ

### 6.1 基本設計思想

PMOSでは、「データ(Data)」「情報(Information)」「知識(Knowledge)」「インテリジェンス(Intelligence)」「意思決定(Decision)」を明確に区別する。

一般的な情報システムでは、データベースから取得したデータをアプリケーションが処理し、画面へ表示する構造が採用される。

PMOSでは、この構造を拡張し、知識資産を中心とした五層モデルを採用する。

データは知識へ変換され、知識は意味構造へ整理され、意味構造はAIによる推論へ利用され、その結果が経営判断や社会的インパクト評価へ接続される。

このため、PMOSにおいて最も重要な資産はデータベースではなくKnowledge Assetである。

---

### 6.2 データライフサイクル

PMOSでは、すべての情報は統一されたライフサイクルを経る。

```text
Observation

↓

Data

↓

Information

↓

Knowledge Asset

↓

Knowledge Registry

↓

Knowledge Graph

↓

Semantic Index

↓

AI Intelligence

↓

Decision

↓

Executive Dashboard

↓

Planetary Impact
```

Observationは観測・計測・文献・設計・専門知識などの一次情報である。

Dataでは構造化・非構造化を問わず取得した情報を保存する。

Informationでは文脈を付与し、再利用可能な情報単位へ整理する。

Knowledge Assetでは意味を持つ成果物として登録される。

Knowledge Registryで一意識別され、Knowledge Graphにより意味的に接続される。

Semantic IndexはKnowledge AssetをAI検索可能な状態へ変換する。

AI Intelligenceでは複数Knowledge Assetを統合して推論を実施する。

Decisionでは経営判断や政策判断へ利用可能な情報として整理する。

Executive Dashboardではその結果を視覚化し、Planetary Impactとして提示する。

---

### 6.3 Data Layer

Data LayerはPMOS全体の最下層である。

ここでは生データを保持する。

対象となるデータは以下である。

- センサーデータ
    
- 土壌分析データ
    
- 微生物解析データ
    
- 医療データ
    
- アンケートデータ
    
- 気候データ
    
- 農業統計
    
- 財務データ
    
- 文献データ
    
- 実験記録
    

Data Layerでは意味付けを行わない。

データ品質と保存性のみを保証する。

---

### 6.4 Information Layer

Information Layerではデータを利用可能な情報へ整理する。

例えば、

土壌分析結果は「土壌有機物含有量」「pH」「EC」「微生物群集構造」などの意味を持つ情報へ変換される。

HealthBookでは回答データを質問群・症状群・代謝群へ整理する。

PBPEでは統計値をKPI候補へ変換する。

この段階ではまだKnowledge Assetにはならない。

---

### 6.5 Knowledge Asset Layer

InformationがPMOSへ正式登録される段階でKnowledge Assetとなる。

Knowledge Assetには必ず以下の属性を付与する。

- Knowledge ID
    
- Repository
    
- Domain
    
- Category
    
- Version
    
- Owner
    
- Semantic Tags
    
- Related Assets
    
- Source
    
- License
    
- Validation Status
    

Knowledge AssetはMarkdownだけではない。

JSON、CSV、YAML、RDF、OWL、画像、図面、スライド、動画シナリオ、AI Prompt、ADRもKnowledge Assetとなる。

Knowledge AssetはPMOS全体で唯一の知識単位である。

---

### 6.6 Knowledge Registry Layer

Knowledge RegistryはKnowledge Asset管理台帳である。

Registryは以下を管理する。

- Asset識別
    
- Version管理
    
- Repository管理
    
- Dependency管理
    
- Semantic Tag管理
    
- Owner管理
    
- Status管理
    
- Publication管理
    

Knowledge RegistryはGitHub全体を横断する唯一の知識インデックスとなる。

Repositoryが増加してもRegistry構造は変化しない。

---

### 6.7 Knowledge Graph Layer

Knowledge GraphではKnowledge Registryの情報を意味ネットワークへ変換する。

主要ノードは以下である。

- Repository
    
- Knowledge Asset
    
- Dataset
    
- Ontology
    
- AI Agent
    
- Dashboard
    
- KPI
    
- Domain
    
- Demonstration
    
- Stakeholder
    

主要リレーションは以下である。

- IMPLEMENTS
    
- DEPENDS_ON
    
- REFERENCES
    
- GENERATES
    
- ANALYZES
    
- VISUALIZES
    
- SUPPORTS
    
- DERIVED_FROM
    

Knowledge GraphはAI推論の基盤であり、Repositoryの構造そのものを可視化する役割も担う。

---

### 6.8 Semantic Index Layer

Knowledge Graphだけでは高速検索は困難である。

そこでSemantic Indexを構築する。

Semantic IndexではKnowledge Assetをベクトル化し、意味検索を実現する。

検索対象は以下である。

- Architecture
    
- Specification
    
- ADR
    
- KPI
    
- Prompt
    
- Dashboard
    
- Demonstration
    
- Reference Model
    

検索結果はKnowledge IDとして返却される。

AIエージェントはKnowledge IDを利用して正式なKnowledge Assetを取得する。

これにより、ベクトル検索結果とGitHub資産との一貫性が維持される。

---

### 6.9 Intelligence Layer

Intelligence Layerでは複数Knowledge Assetを統合し、新しい知識を生成する。

AIエージェントはKnowledge Assetを書き換えない。

AIは以下を担当する。

- Context生成
    
- 推論
    
- 比較
    
- 要約
    
- 可視化
    
- KPI生成
    
- Dashboard生成
    
- Report生成
    

知識管理と推論を分離することで、Knowledge Assetの信頼性を維持する。

---

### 6.10 Executive Layer

Executive LayerはPMOSの最終出力層である。

ここではKnowledge AssetやKnowledge Graphを直接表示しない。

経営層が理解できる形へ変換する。

代表的な成果物は以下である。

- Executive Dashboard
    
- Planetary Intelligence Report
    
- Partner Package
    
- Strategic Proposal
    
- Interactive Demonstration
    
- Board Presentation
    

すべての表示内容はKnowledge IDまで追跡可能であり、意思決定の根拠を確認できる。

---

### 6.11 Repository間のデータフロー

PMOSではRepository同士が直接データを共有しない。

Knowledge Registryを中心とする一方向構造を採用する。

```text
Repository

↓

Knowledge Asset

↓

Knowledge Registry

↓

Knowledge Graph

↓

Semantic Index

↓

AI Agent

↓

Executive Dashboard

↓

Decision Support
```

これによりRepository間の結合度を低く保ちながら、AIはPMOS全体を一つの知識体系として利用できる。

---

### 6.12 データ・知識フロー・アーキテクチャの特徴

PMOSでは、データそのものを価値の中心とは考えない。

価値の中心は、検証・構造化・意味付け・再利用可能性を備えたKnowledge Assetにある。

Knowledge AssetはKnowledge Registryによって統治され、Knowledge Graphによって意味的に接続され、Semantic IndexによってAIが検索可能となる。

その結果として、AGRIX、HealthBook、PBPE、M3、BioNexus-Coreなど異なるドメインは、共通の知識基盤の上で協調動作し、Planetary Metabolic Intelligenceを実現する。