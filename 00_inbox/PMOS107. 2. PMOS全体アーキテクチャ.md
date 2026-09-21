第２ファイルに進んでください。

---

# `/09-Documents/Project-Phoenix-Master-Plan-02-PMOS-Architecture.md`

## 2. PMOS全体アーキテクチャ

### 2.1 アーキテクチャの基本原則

Planetary Metabolic Operating System（PMOS）は、個別アプリケーションを統合するためのプラットフォームではない。PMOSは、知識、データ、AI、意思決定、可視化を一つのメタアーキテクチャとして統治するためのAIネイティブ・プラットフォームである。

PMOSの設計単位はソフトウェアコンポーネントではなく、「Knowledge Asset」を最小構成要素とする。すべてのドキュメント、設計書、データモデル、アルゴリズム仕様、AIエージェント仕様、KPI定義、ダッシュボード仕様はKnowledge Assetとして管理され、GitHub上でバージョン管理される。

この構造により、実装コード、仕様書、説明資料、デモシナリオは分離されることなく、一つの知識体系として継続的に進化する。

PMOSでは、ソースコードはKnowledge Assetを実証するための実装であり、知識体系そのものではない。この原則により、AIエージェントはコードだけではなく、設計思想、仕様、ADR、KPI、知識グラフを同一レベルの知識として参照できる。

---

### 2.2 レイヤードアーキテクチャ

PMOSは七つのレイヤーで構成される。

```
Layer 7  Executive Intelligence

Layer 6  AI Collaboration

Layer 5  Semantic Intelligence

Layer 4  Knowledge Assets

Layer 3  Repository Platform

Layer 2  Data Foundation

Layer 1  Governance
```

Layer 1（Governance）は全体統治を担当する。PMOS Constitution、Project Charter、ADR、Repository Atlas、Coding Standards、Documentation Standards、Release Policyを管理し、全リポジトリ共通のガバナンスを提供する。

Layer 2（Data Foundation）はJSON、CSV、YAML、Markdown、FHIR、RDF、OWLなどのデータフォーマットを統一し、Knowledge Registryを通じて識別子、メタデータ、バージョンを管理する。

Layer 3（Repository Platform）はGitHubを中心とした知識公開基盤である。すべての成果物はGitリポジトリとして管理され、Issue、Pull Request、Release、Project Boardを通じてライフサイクル管理を行う。

Layer 4（Knowledge Assets）はPMOSの中心層である。Architecture Book、Knowledge Registry、Ontology、KPI定義、AI仕様書、Dashboard仕様書、データ辞書、ユースケース、ADRを統合し、AIが直接参照可能な知識資産として保持する。

Layer 5（Semantic Intelligence）はKnowledge Graphを用いてRepository間の概念、データ、AIエージェント、KPI、ダッシュボードを意味的に接続する。ノードとリレーションシップを定義し、構造化推論を可能にする。

Layer 6（AI Collaboration）はKnowledge GraphとPineconeを組み合わせ、各AIエージェントが共通知識資産を参照しながら協調動作する。AI間通信は自然言語だけではなく、Knowledge Asset IdentifierとMetabolic Intelligence Codeを利用する。

Layer 7（Executive Intelligence）はダッシュボード、デモンストレーション、レポート生成を担当し、経営層や戦略パートナーに対してPMOS全体の価値を視覚的に提示する。

---

### 2.3 Repository Architecture

PMOSでは、リポジトリを機能単位ではなく役割単位で分類する。

第一群はGovernance Repositoryである。ここでは憲章、標準、ADR、運用規則を管理する。

第二群はKnowledge Repositoryである。BioNexus-Coreを中核とし、Knowledge Registry、Ontology、Knowledge Graph、Reference Modelを保持する。

第三群はDomain Repositoryである。AGRIX、HealthBook、PBPE、M3など、各ドメインの知識資産と仕様を保持する。

第四群はIntelligence Repositoryである。AI Agent、Prompt Specification、Reasoning Flow、Semantic Communication、Evaluation Frameworkを管理する。

第五群はPresentation Repositoryである。Executive Dashboard、Interactive Demonstration、Presentation Assets、Partner Packageを管理する。

各Repositoryは独立して運用される一方で、Knowledge Registryを介して相互参照されるため、全体として一つの知識ネットワークを形成する。

---

### 2.4 Knowledge Architecture

Knowledge Architectureは、PMOSの最重要構成要素である。

Knowledge Assetは以下の共通メタデータを持つ。

- Knowledge ID
- Repository
- Category
- Domain
- Version
- Status
- Owner
- Dependency
- Related Asset
- Semantic Tag
- Created Date
- Updated Date

これらはKnowledge Registryで一元管理され、Knowledge Graphのノード属性として利用される。

Knowledge Assetは文書だけではなく、JSON定義、AI Prompt、UI仕様、KPI、データモデル、ワイヤーフレームも含む。

各Knowledge Assetは唯一のKnowledge IDを持ち、Repositoryを越えて再利用される。

---

### 2.5 Semantic Architecture

Semantic Layerでは、Knowledge Graphが中核となる。

Knowledge Graphは以下の主要ノードタイプを持つ。

- Repository
- Knowledge Asset
- Domain
- Dataset
- AI Agent
- Dashboard
- KPI
- Use Case
- Stakeholder
- Decision
- Demonstration

ノード間は以下のリレーションで接続される。

- DEPENDS_ON
- IMPLEMENTS
- GENERATES
- REFERENCES
- VISUALIZES
- ANALYZES
- EVALUATES
- BELONGS_TO
- DERIVED_FROM
- RELATED_TO

この構造により、AIエージェントは単なる全文検索ではなく、「あるKPIを実現するAIエージェントはどのKnowledge Assetに依存し、どのダッシュボードに反映されるか」といった多段階推論を実行できる。

---

### 2.6 Repository間のデータフロー

PMOSでは、データはRepositoryからRepositoryへ直接流れない。

すべての情報はKnowledge Registryを経由する。

```
Author

↓

GitHub Repository

↓

Knowledge Asset

↓

Knowledge Registry

↓

Knowledge Graph

↓

Pinecone Vector Index

↓

AI Agent Collaboration

↓

Executive Dashboard

↓

Interactive Demonstration
```

この一方向フローにより、知識の重複管理を防ぎ、すべてのAIエージェントが同一の知識基盤を共有できる。

---

### 2.7 アーキテクチャの新規性

PMOSの新規性は、AIを中心に据えた点ではなく、「知識資産を第一級オブジェクトとして統治するRepository中心設計」にある。

従来のソフトウェア開発では、コードが主であり、設計書や仕様書は補助的な存在であった。PMOSでは、Architecture Book、Knowledge Registry、Knowledge Graph、AI Agent Specification、Dashboard Specificationを同一レベルのKnowledge Assetとして管理し、AI・人間・GitHub・デモ環境が共通の知識体系を参照する。

これにより、プロジェクト全体が「ソフトウェア製品」ではなく、「AIネイティブな知識プラットフォーム」として継続的に発展できる構造を実現する。