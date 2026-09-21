# HealthBook–PMOS Master Plan

## Volume II

# MIOS Reference Architecture

### Version 1.0

---

# 1. Architectural Principles

MIOS (Metabolic Intelligence Operating System) is designed as a knowledge-centric intelligence architecture rather than a conventional application architecture.

The primary objective of MIOS is to transform heterogeneous biological information into executable metabolic intelligence through standardized knowledge assets, semantic relationships, and coordinated AI agents.

The architecture follows six fundamental principles.

**Knowledge First**

Knowledge assets constitute the primary source of intelligence. Algorithms and AI agents operate on structured knowledge rather than isolated datasets.

**Metabolic State First**

All analyses are performed on metabolic states instead of disease labels. Diseases are regarded as observable consequences of metabolic state transitions.

**Composable Intelligence**

Every analytical function is implemented as an independent AI agent with clearly defined responsibilities, allowing new agents to be added without modifying the existing architecture.

**Semantic Interoperability**

Every biological entity is represented through standardized identifiers, ontology definitions, and MI Codes to enable semantic communication across repositories.

**Explainable Reasoning**

Every recommendation must be traceable through explicit evidence paths represented within the Knowledge Graph.

**Open Architecture**

Every component of MIOS is version-controlled, repository-managed, and independently extensible.

---

# 2. Architectural Layers

MIOS is organized into seven logical layers.

```
Presentation Layer

↓

Application Layer

↓

Agent Layer

↓

Reasoning Layer

↓

Knowledge Layer

↓

Data Layer

↓

Infrastructure Layer
```

Each layer has clearly defined responsibilities and communicates only through standardized interfaces.

---

# 3. Presentation Layer

The Presentation Layer provides human interaction.

Reference implementations include:

- HealthBook Web Platform
- Clinical Dashboard
- Digital Twin Viewer
- Knowledge Graph Explorer
- Executive Analytics Dashboard
- API Console

This layer contains no medical reasoning.

Its responsibility is limited to visualization, interaction, and workflow management.

---

# 4. Application Layer

The Application Layer orchestrates business workflows.

Major application services include:

- Patient Registration
- Questionnaire Management
- Clinical Assessment
- Phenotype Analysis
- Metabolic Analysis
- Nutrition Assessment
- Report Generation
- Simulation Management
- FHIR Export

Applications invoke AI agents through standardized service contracts.

Business logic is intentionally separated from scientific reasoning.

---

# 5. Agent Layer

The Agent Layer performs domain-specific reasoning.

Every agent receives structured input, evaluates its own knowledge domain, and produces standardized outputs.

The initial MIOS agent library consists of:

|Agent|Responsibility|
|---|---|
|Data Intake Agent|Data validation and normalization|
|Clinical Agent|Clinical interpretation|
|Phenotype Agent|Phenotype inference|
|Nutrition Agent|Nutritional reasoning|
|Metabolism Agent|Metabolic pathway analysis|
|Microbiome Agent|Gut microbiome reasoning|
|Hormone Agent|Endocrine interpretation|
|MBT Agent|MBT55 functional analysis|
|Kampo Agent|Kampo metabolic analysis|
|Animal Medicine Agent|Animal medicine reasoning|
|Knowledge Graph Agent|Graph synchronization|
|Simulation Agent|Intervention modeling|
|Recommendation Agent|Personalized recommendations|
|Supervisor Agent|Workflow coordination|

Agents never communicate through natural language.

They exchange standardized MI Codes, structured evidence objects, and state identifiers.

---

# 6. Reasoning Layer

The Reasoning Layer integrates outputs from multiple agents.

Its primary responsibilities include:

- Evidence aggregation
- Conflict detection
- Confidence evaluation
- State transition analysis
- Root-cause inference
- Intervention prioritization
- Simulation execution

This layer does not generate new biological knowledge.

Instead, it transforms distributed evidence into coherent metabolic intelligence.

All reasoning results remain explainable through explicit evidence paths.

---

# 7. Knowledge Layer

The Knowledge Layer represents the scientific foundation of MIOS.

Knowledge is organized into four structural components.

**Knowledge Assets**

Structured JSON libraries maintained within version-controlled repositories.

**Ontology**

Standardized definitions of biological entities, concepts, and relationships.

**Knowledge Graph**

A semantic graph connecting all biological entities through explicit relationships.

**MI Registry**

A centralized registry assigning unique identifiers to every knowledge object, state, and evidence element.

The Knowledge Layer evolves independently from software implementation.

Scientific updates are managed through repository version control.

---

# 8. Data Layer

The Data Layer stores structured information originating from both users and knowledge repositories.

Major data categories include:

- Patient Profiles
- Questionnaire Responses
- Clinical Measurements
- Laboratory Data
- Nutritional Records
- Metabolic Profiles
- Phenotype Vectors
- Simulation Results
- Knowledge Libraries
- FHIR Resources

Data integrity is validated before entering the reasoning pipeline.

---

# 9. Infrastructure Layer

The Infrastructure Layer provides execution environments.

Reference technologies include:

- GitHub
- GitHub Actions
- GitHub Pages
- Azure
- Container Runtime
- Object Storage
- Graph Database
- Relational Database
- Vector Search Engine
- FHIR Server

The infrastructure remains technology-independent.

Alternative cloud providers may replace any implementation without affecting MIOS specifications.

---

# 10. Repository Architecture

Each repository has a single architectural responsibility.

|Repository|Responsibility|
|---|---|
|mios-constitution|Governance|
|mios-architecture-book|Architecture|
|mios-language|MI Language|
|mios-mi-code|MI Code Registry|
|mios-ontology|Ontology|
|mios-knowledge-graph|Knowledge Graph|
|mios-state-engine|State Engine|
|mios-agent-runtime|Agent Runtime|
|mios-digital-twin|Digital Twin|
|healthbook-json-library|Knowledge Assets|
|healthbook-platform|Reference Application|
|healthbook-agents|HealthBook Agents|
|mios-reference-demo|Reference Demonstration|

No repository duplicates responsibilities assigned to another repository.

---

# 11. Information Flow

The standard execution pipeline follows a deterministic sequence.

```
Patient Input

↓

Data Intake Agent

↓

Phenotype Agent

↓

Metabolism Agent

↓

Knowledge Graph Update

↓

Reasoning Engine

↓

Simulation Agent

↓

Recommendation Agent

↓

HealthBook Report
```

Every intermediate state is recorded as structured evidence and linked through MI Codes.

This enables complete traceability from original input to final recommendation.

---

# 12. Architectural Outcome

The MIOS Reference Architecture establishes a standardized framework for constructing metabolic intelligence systems.

Instead of centering intelligence around isolated algorithms, MIOS defines intelligence as the coordinated interaction of knowledge assets, semantic standards, state transitions, and specialized AI agents.

HealthBook represents the first implementation of this architecture, while the underlying specifications are intended to support future applications across healthcare, agriculture, and planetary metabolic systems.

---

**End of Volume II — MIOS Reference Architecture**

---

# HealthBook-PMOS総合計画書

## 第2巻

# MIOS リファレンス・アーキテクチャ

### Version 1.0（日本語版）

---

# 1. アーキテクチャ原則

MIOS（Metabolic Intelligence Operating System）は、従来の業務アプリケーションのような機能中心のシステムではなく、**知識を中心に推論を行う代謝インテリジェンス基盤**として設計される。

MIOSの目的は、多様な生体情報を、標準化された知識資産、意味体系（Ontology）、Knowledge Graph、およびAIエージェントによって統合し、再利用可能な代謝インテリジェンスへ変換することである。

MIOSは、以下の6つの基本原則に基づいて構築される。

### Knowledge First

知識資産をシステムの中心に据える。

AIモデルやアルゴリズムは個別のデータを直接処理するのではなく、標準化された知識資産を利用して推論を実行する。

---

### Metabolic State First

解析対象は疾病ではなく、代謝状態である。

疾病は最終結果であり、MIOSは代謝状態の変化とその因果経路を解析対象とする。

---

### Composable Intelligence

各解析機能は独立したAIエージェントとして実装する。

エージェント間は共通仕様のみで連携し、新たな解析機能を追加しても既存エージェントへ影響を与えない構造とする。

---

### Semantic Interoperability

すべての知識資産にはMI Code、Ontology、および標準識別子を付与し、リポジトリ間・エージェント間で意味情報を共有する。

---

### Explainable Reasoning

すべての推論結果はKnowledge Graph上の証拠経路によって説明可能でなければならない。

推論過程は追跡可能であり、最終的な提案までの根拠を確認できる。

---

### Open Architecture

すべての仕様、知識資産、リポジトリはバージョン管理され、独立して拡張できるオープンアーキテクチャを採用する。

---

# 2. アーキテクチャ階層

MIOSは7層構造で構成される。

```
プレゼンテーション層

↓

アプリケーション層

↓

AIエージェント層

↓

推論エンジン層

↓

知識基盤層

↓

データ層

↓

インフラストラクチャ層
```

各層は責務を明確に分離し、標準化されたインターフェースのみを介して連携する。

---

# 3. プレゼンテーション層

プレゼンテーション層は利用者とのインターフェースを提供する。

主な構成は以下とする。

- HealthBook Web Platform
- 臨床ダッシュボード
- Digital Twin Viewer
- Knowledge Graph Viewer
- Executive Dashboard
- API Console

この層では推論を行わず、情報の入力・表示・可視化のみを担当する。

---

# 4. アプリケーション層

アプリケーション層は業務フローを制御する。

主要サービスは以下で構成される。

- 利用者登録
- 問診管理
- 健診データ管理
- フェノタイプ解析
- 代謝解析
- 栄養解析
- レポート生成
- シミュレーション管理
- FHIR出力

アプリケーションはAIエージェントを呼び出す役割のみを持ち、科学的推論は保持しない。

---

# 5. AIエージェント層

AIエージェント層は、それぞれ専門領域を担当する独立した推論モジュールで構成される。

各エージェントは共通仕様に従い、入力を解析し、MI Codeおよび証拠情報を出力する。

初期構成は以下とする。

|AIエージェント|役割|
|---|---|
|Data Intake Agent|データ正規化・検証|
|Clinical Agent|臨床情報解析|
|Phenotype Agent|フェノタイプ解析|
|Nutrition Agent|栄養解析|
|Metabolism Agent|代謝経路解析|
|Microbiome Agent|腸内環境解析|
|Hormone Agent|ホルモン・内分泌解析|
|MBT Agent|MBT55解析|
|Kampo Agent|MBT漢方解析|
|Animal Medicine Agent|動物生薬解析|
|Knowledge Graph Agent|Knowledge Graph更新|
|Simulation Agent|介入シミュレーション|
|Recommendation Agent|改善提案生成|
|Supervisor Agent|全体制御|

エージェント同士は自然言語では通信せず、MI Code・Evidence・State Codeを用いて連携する。

---

# 6. 推論エンジン層

推論エンジン層は複数エージェントの解析結果を統合する。

主な機能は以下である。

- 証拠統合
- 矛盾検出
- 信頼度評価
- 状態遷移解析
- 根本原因推論
- 介入候補順位付け
- シミュレーション実行

この層は新しい知識を生成するのではなく、知識資産から得られた証拠を統合し、一貫した代謝推論を形成する。

---

# 7. 知識基盤層

知識基盤層はMIOS全体の科学的基盤となる。

以下の4要素で構成される。

### Knowledge Assets

GitHubで管理されるJSONライブラリー群。

### Ontology

生物学的概念・用語・関係性を定義する意味体系。

### Knowledge Graph

知識資産をノードとエッジで接続した推論基盤。

### MI Registry

MI Code、State Code、Evidence Codeなどを一元管理するレジストリ。

知識基盤はアプリケーションとは独立して更新・管理される。

---

# 8. データ層

データ層では利用者データおよび知識データを管理する。

対象データは以下とする。

- 利用者基本情報
- 問診回答
- 健診データ
- 血液検査データ
- 栄養情報
- フェノタイプベクトル
- 代謝プロファイル
- シミュレーション結果
- Knowledge Assets
- FHIRリソース

すべてのデータは推論前に正規化・検証される。

---

# 9. インフラストラクチャ層

インフラストラクチャ層はMIOSの実行環境を提供する。

標準構成例は以下とする。

- GitHub
- GitHub Actions
- GitHub Pages
- Azure
- コンテナ実行環境
- オブジェクトストレージ
- グラフデータベース
- リレーショナルデータベース
- ベクトル検索エンジン
- FHIRサーバー

特定クラウドへの依存を避け、クラウド非依存の構成を維持する。

---

# 10. リポジトリアーキテクチャ

各リポジトリは単一責務を持つ。

|リポジトリ|責務|
|---|---|
|mios-constitution|統治・基本方針|
|mios-architecture-book|アーキテクチャ|
|mios-language|MI Language|
|mios-mi-code|MI Code管理|
|mios-ontology|Ontology|
|mios-knowledge-graph|Knowledge Graph|
|mios-state-engine|状態遷移管理|
|mios-agent-runtime|AIエージェント実行基盤|
|mios-digital-twin|Digital Twin|
|healthbook-json-library|Knowledge Assets|
|healthbook-platform|リファレンスアプリケーション|
|healthbook-agents|AIエージェント群|
|mios-reference-demo|デモシステム|

各リポジトリは責務を重複させず、標準仕様を共有して連携する。

---

# 11. 標準情報フロー

MIOSにおける標準的な処理フローは以下とする。

```
利用者データ入力

↓

Data Intake Agent

↓

Phenotype Agent

↓

Metabolism Agent

↓

Knowledge Graph更新

↓

Reasoning Engine

↓

Simulation Agent

↓

Recommendation Agent

↓

HealthBookレポート生成
```

各処理段階ではEvidenceとMI Codeが記録され、入力から最終提案まで追跡可能な構造を維持する。

---

# 12. アーキテクチャの到達目標

MIOSリファレンス・アーキテクチャは、代謝インテリジェンスを中心としたシステムを構築するための標準基盤を提供する。

MIOSは単一のAIモデルではなく、

- Knowledge Assets
- Ontology
- Knowledge Graph
- State Engine
- MI Code
- AIエージェント

を統合したアーキテクチャとして設計される。

HealthBookは、その最初のリファレンス実装であり、この仕様は将来的にAGRIXやPBPEなどPMOS配下の他システムへ展開可能な共通基盤として位置付けられる。

**（第2巻 日本語版 完了）**

[[MIOS004. Volume III]]
