# `/09-Documents/Project-Phoenix-Master-Plan-04-PMOS-Repository-Ecosystem.md`

## 4. PMOSリポジトリエコシステム

### 4.1 リポジトリ設計方針

Project Phoenixでは、GitHubを単なるソースコード管理システムとして利用しない。

GitHubはPMOS全体の公開知識基盤（Official Knowledge Platform）であり、設計書、仕様書、データモデル、AIエージェント仕様、知識グラフ定義、デモ資産、実装コードを統一的に管理する基盤である。

各Repositoryは単独で完結することを目的とせず、PMOS全体を構成する知識ネットワークの一部として設計される。

そのため、すべてのRepositoryは共通のディレクトリ構造、命名規則、README構成、ADR管理方式、Knowledge ID体系を採用する。

Repositoryの役割はコードの保管ではなく、知識資産を長期的に維持・公開・再利用することである。

---

### 4.2 リポジトリ階層

PMOSではRepositoryを六つの階層に分類する。

第一階層はGovernance Repositoryである。

ここではプロジェクト全体の運用を定義する。

代表的な内容は以下である。

- PMOS Constitution
    
- Project Charter
    
- Repository Atlas
    
- ADR
    
- Development Standards
    
- Documentation Standards
    
- Release Policy
    

第二階層はCore Repositoryである。

PMOS全体の知識基盤を管理する。

中心となるRepositoryはBioNexus-Coreであり、Knowledge Registry、Ontology、Reference Model、Knowledge Assetsを保持する。

第三階層はDomain Repositoryである。

各ドメイン固有の知識資産を管理する。

対象は以下である。

- AGRIX
    
- HealthBook
    
- PBPE
    
- M3-Core-Engine
    
- M3-BioSynergy-Core
    

第四階層はIntelligence Repositoryである。

AIエージェント、Semantic Communication、Prompt Specification、Reasoning Model、Agent Registryを保持する。

第五階層はPresentation Repositoryである。

Executive Dashboard、UI、Interactive Demonstration、Presentation Assetsを保持する。

第六階層はIntegration Repositoryである。

Repository間連携、CI/CD、Knowledge同期、GitHub Actions、Deployment Templateなどを管理する。

---

### 4.3 BioNexus-Core

BioNexus-CoreはPMOSの中核Repositoryである。

すべてのKnowledge Assetは最終的にBioNexus-Coreで管理される。

主な構成は以下である。

```text
BioNexus-Core

Governance

Knowledge Registry

Ontology

Knowledge Graph

Reference Models

Knowledge Assets

Shared Schemas

Semantic Metadata

Templates

Documentation
```

BioNexus-Coreにはドメイン固有ロジックを実装しない。

AGRIXやHealthBookなどのRepositoryが公開する知識資産を統合し、Knowledge RegistryとKnowledge Graphを生成する役割を担う。

---

### 4.4 AGRIX Repository

AGRIX Repositoryは農業ドメインのKnowledge Assetを管理する。

対象範囲は以下である。

- Soil Intelligence
    
- Soil Microbiome
    
- Carbon Cycle
    
- Nitrogen Cycle
    
- Fermentation Technology
    
- Crop Productivity
    
- Climate Impact
    
- AgriWare
    
- SafetyChain
    
- Dashboard Assets
    

AGRIXでは、土壌代謝、微生物ネットワーク、資源循環、炭素固定などを知識モデルとして管理し、AIエージェントが利用可能な形式で公開する。

---

### 4.5 HealthBook Repository

HealthBook Repositoryはヒト代謝およびフェノタイピング領域を管理する。

対象は以下である。

- Questionnaire
    
- Phenotype Models
    
- Disease Knowledge
    
- Nutrition
    
- Metabolism
    
- Kampo Library
    
- Biomarkers
    
- FHIR Mapping
    
- Dashboard Assets
    

HealthBookは診断ソフトウェアではなく、代謝知識プラットフォームとして位置付けられる。

---

### 4.6 PBPE Repository

PBPE RepositoryはPlanetary Impact評価を担当する。

主な構成要素は以下である。

- Impact Registry
    
- Impact Models
    
- KPI Definitions
    
- Financial Indicators
    
- Climate Indicators
    
- Biosecurity Indicators
    
- Executive Reports
    
- Dashboard Assets
    

PBPEはKnowledge Graphから取得した情報を集約し、Planetary Impactとして可視化する。

---

### 4.7 M3 Repository群

M3-Core-EngineはPMOS全体の代謝モデルを保持する。

対象は以下である。

- Metabolic Model
    
- Resource Flow
    
- Transformation Rules
    
- Biological Network
    
- Metabolic Parameters
    

M3-BioSynergy-Coreは複数ドメインを横断する相互作用モデルを管理する。

例えば、

- Soil ⇔ Crop
    
- Crop ⇔ Food
    
- Food ⇔ Human
    
- Human ⇔ Environment
    

などの関係をKnowledge Assetとして保持する。

---

### 4.8 AI Repository

AI RepositoryはPMOSの知能層を管理する。

内容は以下である。

- Agent Registry
    
- Prompt Library
    
- Reasoning Models
    
- Memory Specification
    
- Semantic Communication
    
- Context Models
    
- Workflow Definitions
    
- Evaluation Framework
    

AI Repositoryには業務知識は保持しない。

AIがどのKnowledge Assetを利用するかだけを定義する。

---

### 4.9 Dashboard Repository

Dashboard Repositoryは経営層向け可視化を担当する。

標準モジュールは以下である。

- Executive Overview
    
- Planetary Intelligence
    
- Agriculture
    
- Human Health
    
- Climate
    
- Biosecurity
    
- Finance
    
- Knowledge Graph
    
- Repository Status
    
- AI Collaboration
    
- Demonstration
    

すべての表示データはKnowledge Registryを起点とする。

Dashboard Repositoryは独自データを持たない。

---

### 4.10 Demonstration Repository

Demonstration RepositoryはPMOSを説明するためのデモ環境を保持する。

主な成果物は以下である。

- Demo Story
    
- Demo Script
    
- Demo Dataset
    
- UI Prototype
    
- Executive Scenario
    
- Interactive Walkthrough
    
- Presentation Assets
    
- Video Storyboard
    

デモは製品説明ではなく、PMOSという知識プラットフォーム全体の価値を体験できる構成とする。

---

### 4.11 Repository共通構造

すべてのRepositoryは共通ディレクトリ構造を採用する。

```text
docs/
architecture/
knowledge/
ontology/
schemas/
datasets/
agents/
dashboards/
examples/
adr/
templates/
.github/
README.md
CHANGELOG.md
LICENSE
```

この構造により、Repositoryが異なってもKnowledge Assetの配置場所と管理方法は統一される。

---

### 4.12 Repository間連携

Repository同士は直接依存しない。

すべてのRepositoryはKnowledge Registryを通じて接続される。

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

Dashboard

↓

Executive Demonstration
```

この一方向構造により、Repositoryの独立性を維持しながら、PMOS全体として一貫した知識ネットワークを形成する。

---

### 4.13 リポジトリエコシステムの特徴

PMOSのRepository Ecosystemは、ソフトウェアを中心に構築される一般的なGitHub組織とは異なる。

Repositoryの価値はコード量ではなく、Knowledge Assetの品質、再利用性、意味構造、AI利用可能性によって評価される。

各Repositoryは単体でも公開可能である一方、Knowledge RegistryとKnowledge Graphを介して統合されることで、Planetary Metabolic Operating Systemという一つのAIネイティブ・プラットフォームを構成する。