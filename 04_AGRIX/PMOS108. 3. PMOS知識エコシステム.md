# `/09-Documents/Project-Phoenix-Master-Plan-03-Knowledge-Ecosystem.md`

## 3. PMOS知識エコシステム

### 3.1 知識エコシステムの目的

Project Phoenixにおける知識エコシステムは、PMOSを構成するすべての知識資産を一元的に管理し、人間とAIが同一の知識体系を共有することを目的とする。

本エコシステムでは、ソースコード、仕様書、データモデル、設計書、AIエージェント仕様、ダッシュボード仕様、デモシナリオは、それぞれ独立した成果物ではなく、一つのKnowledge Assetとして統一的に扱われる。

Knowledge Assetは単なる文書ではない。設計意図、依存関係、利用範囲、バージョン、関連リポジトリ、対象AIエージェントまでを含む自己記述型の知識単位であり、Knowledge Registryによって一意に識別される。

PMOSでは、このKnowledge Assetを中心に据えることで、リポジトリ数やドメイン数が増加しても全体構造を維持しながら継続的に拡張できる。

---

### 3.2 Knowledge Assetの分類

Knowledge Assetは機能ではなく役割によって分類される。

第一分類はGovernance Assetである。

これにはPMOS Constitution、Project Charter、Architecture Decision Record、Repository Standard、Documentation Standard、Release Policyが含まれる。

第二分類はArchitecture Assetである。

Architecture Book、Reference Architecture、Repository Blueprint、Data Flow、System Context Diagram、Domain Modelなどが含まれる。

第三分類はKnowledge Assetである。

Knowledge Registry、Ontology、Taxonomy、Vocabulary、Reference Model、Metadata Definition、Terminologyが含まれる。

第四分類はDomain Assetである。

AGRIX、HealthBook、PBPE、M3、BioNexus-Coreなど各ドメインの仕様書、データ辞書、業務モデル、評価指標を管理する。

第五分類はAI Assetである。

AI Agent Specification、Prompt Definition、Reasoning Flow、Memory Strategy、Agent Capability、Semantic Communication Protocolなどが含まれる。

第六分類はPresentation Assetである。

Executive Dashboard、UI Wireframe、Interactive Demonstration、Presentation Story、Partner Package、Illustration、図表などが管理対象となる。

この分類により、知識資産は実装方法ではなく目的ごとに整理される。

---

### 3.3 Knowledge Registry

Knowledge RegistryはPMOS全体の知識資産台帳である。

すべてのKnowledge Assetは登録時にKnowledge IDを付与される。

Knowledge IDは永続的な識別子であり、ファイル名や保存場所が変更されても同一資産として扱われる。

Registryには以下の情報が保持される。

- Knowledge ID
    
- Asset Name
    
- Repository
    
- Domain
    
- Category
    
- Version
    
- Status
    
- Owner
    
- Source Repository
    
- Related Repository
    
- Parent Asset
    
- Child Asset
    
- Semantic Tags
    
- Dependency
    
- Last Review
    
- Publication Status
    

Knowledge RegistryはKnowledge Graph生成の唯一の基準情報となる。

GitHub上のMarkdownやJSONだけでなく、画像、図面、スライド、動画シナリオについてもKnowledge Assetとして登録する。

---

### 3.4 Repository間の知識共有

PMOSではRepository同士が直接知識を複製しない。

RepositoryはKnowledge Registryを介して知識を共有する。

例えばHealthBookがAGRIXの土壌代謝モデルを参照する場合、AGRIX Repositoryからファイルをコピーするのではなく、Knowledge Registryに登録されたKnowledge IDを参照する。

PBPEがHealthBookの評価指標を利用する場合も同様である。

この方式により、一つのKnowledge Assetを更新すれば、そのKnowledge IDを参照するすべてのRepositoryへ変更内容が反映される。

知識の重複管理を避けることで、保守性と整合性を維持する。

---

### 3.5 Ontology

PMOS Ontologyは知識エコシステム全体の概念定義を統一する。

Ontologyでは以下の主要クラスを定義する。

- Organization
    
- Repository
    
- Knowledge Asset
    
- Dataset
    
- Domain
    
- AI Agent
    
- Dashboard
    
- Executive Report
    
- KPI
    
- Demonstration
    
- Stakeholder
    
- Technology
    
- Metabolic Process
    
- Biological Process
    
- Decision
    

各クラスには属性と関係が定義される。

例えばRepositoryクラスはKnowledge Assetを保持し、Knowledge AssetはAI Agentによって利用され、AI AgentはDashboardを生成し、DashboardはExecutive Reportへ利用される。

OntologyはKnowledge Graph構築時のスキーマとして利用される。

---

### 3.6 Taxonomy

TaxonomyはKnowledge Assetを階層構造で分類する。

最上位カテゴリは以下とする。

- Governance
    
- Architecture
    
- Knowledge
    
- Agriculture
    
- Healthcare
    
- Environment
    
- Climate
    
- Biosecurity
    
- Finance
    
- AI
    
- Dashboard
    
- Demonstration
    
- Integration
    
- Operations
    
- Release
    

各カテゴリはさらにDomain単位へ細分化される。

例えばAgricultureにはSoil、Crop、Microbiome、Fermentation、Carbon、Productivityなどが含まれる。

HealthcareにはPhenotype、Metabolism、Nutrition、Disease、Microbiome、Kampo、FHIRなどを配置する。

TaxonomyはRepository構造とは独立して管理されるため、一つのKnowledge Assetを複数カテゴリへ意味的に所属させることができる。

---

### 3.7 Knowledge Graphとの統合

Knowledge Registryに登録されたKnowledge Assetは、自動的にKnowledge Graphのノード候補となる。

Knowledge Graphでは、Knowledge IDをノード識別子として利用する。

各ノードにはRepository、Domain、Category、Version、Semantic Tagが属性として付与される。

Repository間の依存関係、AIエージェントとの利用関係、KPIとの対応関係はリレーションシップとして生成される。

これにより、「PBPE Dashboardが参照するHealthBook評価指標」「AGRIXの代謝モデルに依存するAI Agent」「Executive Reportに表示されるKPIの出典」といった関係をグラフ構造で追跡できる。

Knowledge GraphはAIの推論基盤であると同時に、PMOS全体の構造を可視化する設計図としても機能する。

---

### 3.8 BioNexus-Coreの役割

BioNexus-CoreはPMOS知識エコシステムの中核Repositoryである。

Obsidian Vaultで整理・検証された知識は、BioNexus-CoreへKnowledge Assetとして登録される。

BioNexus-Coreでは知識の品質管理、メタデータ管理、Knowledge Registry更新、Ontology更新、Knowledge Graph生成用データ作成を実施する。

AGRIX、HealthBook、PBPE、M3などの各RepositoryはBioNexus-Coreを通じて知識を公開・共有する。

そのため、BioNexus-Coreは単なる文書保管庫ではなく、PMOS全体の知識供給基盤として位置付けられる。

---

### 3.9 知識エコシステムの拡張性

PMOSでは、新しいRepositoryやAI Agentを追加する場合でも、既存構造を変更する必要はない。

新規RepositoryはKnowledge Registryへ登録し、Ontologyへ必要な概念を追加し、Knowledge Graphへノードとリレーションを生成するだけで統合できる。

この拡張方式により、PMOSは農業、医療、環境、金融、生物多様性など新たなドメインを継続的に追加しながら、一貫した知識体系を維持できる。

知識エコシステム全体は、GitHubを公開基盤、BioNexus-Coreを知識基盤、Knowledge Registryを管理基盤、Knowledge Graphを意味基盤、AI Agentを推論基盤として連携し、Project Phoenixの中核インフラを構成する。