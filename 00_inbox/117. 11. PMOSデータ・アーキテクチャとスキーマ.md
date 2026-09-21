# `/09-Documents/PMOS-Architecture-Book/11-PMOS-Data-Architecture-and-Schema.md`

## 11. PMOSデータ・アーキテクチャとスキーマ

### 11.1 基本方針

PMOSのData Architectureは、特定のデータベース製品を中心に設計しない。

PMOSでは、データを「保存するもの」としてだけではなく、Knowledge Assetへ変換され、Knowledge Graph、AI Agent、Dashboardへ流通する基盤資産として扱う。

したがって、PMOSのデータアーキテクチャでは以下を分離する。

```text
Data
  ↓
Metadata
  ↓
Knowledge Asset
  ↓
Semantic Model
  ↓
Knowledge Graph
  ↓
AI Context
  ↓
Executive Intelligence
```

この分離により、データベース、ベクトルDB、グラフDB、LLMなどの技術変更が発生しても、PMOSの知識モデルを維持できる。

---

## 11.2 データ階層

PMOSではデータを六つの階層に分類する。

### Layer 1 — Raw Data

観測・取得された一次データ。

### Layer 2 — Structured Data

JSON、CSV、FHIR、SQLなどの構造化データ。

### Layer 3 — Metadata

データの出典、意味、Version、Owner、Domainなどを定義する。

### Layer 4 — Knowledge Asset

意味的に整理され、再利用可能となった知識単位。

### Layer 5 — Semantic Data

OntologyとKnowledge Graphによって接続された知識。

### Layer 6 — Intelligence Output

AIによって生成された分析、KPI、Dashboard、Report。

```text
Raw
 ↓
Structured
 ↓
Metadata
 ↓
Knowledge
 ↓
Semantic
 ↓
Intelligence
```

---

## 11.3 共通識別子

PMOSでは、すべての主要データオブジェクトに永続的な識別子を付与する。

主要IDは以下である。

```text
Repository ID
Knowledge ID
Dataset ID
Agent ID
Graph Node ID
KPI ID
Dashboard ID
Task ID
Trace ID
Version ID
```

これらの識別子はRepositoryを越えて利用可能でなければならない。

ファイル名、URL、データベース内部IDだけに依存してはならない。

---

## 11.4 Knowledge Asset Schema

Knowledge Assetは共通スキーマを持つ。

```text
KnowledgeAsset

├── id
├── name
├── type
├── domain
├── repository
├── version
├── status
├── owner
├── source
├── description
├── tags
├── dependencies
├── related_assets
├── validation
└── timestamps
```

このスキーマをPMOS全体の基本Knowledge Contractとする。

---

## 11.5 Dataset Schema

DatasetはKnowledge Assetとは区別する。

Datasetには以下を定義する。

```text
Dataset

├── id
├── name
├── source
├── domain
├── schema
├── format
├── version
├── license
├── provenance
├── quality
└── update_frequency
```

DatasetはKnowledge Assetを生成する入力として利用される。

---

## 11.6 Provenance

PMOSではデータの出典を必ず追跡可能にする。

Provenanceは以下を記録する。

- Source
    
- Author
    
- Repository
    
- Created Date
    
- Transformation
    
- Version
    
- Validation
    
- Derived Asset
    

これにより、DashboardやExecutive Reportの情報がどこから生成されたかを追跡できる。

---

## 11.7 Version Architecture

Knowledge Asset、Dataset、Schema、Agent、DashboardはすべてVersion管理する。

基本構造は以下である。

```text
Asset v1.0
   ↓
Asset v1.1
   ↓
Asset v1.2
   ↓
Asset v2.0
```

Version変更時には、変更理由と依存関係を記録する。

Architecture変更はADRによって管理する。

---

## 11.8 Data Contract

Repository間で共有されるデータにはData Contractを設定する。

Data Contractでは以下を定義する。

- Input
    
- Output
    
- Schema
    
- Required Fields
    
- Optional Fields
    
- Data Type
    
- Version
    
- Validation Rule
    
- Owner
    

これにより、AGRIX、HealthBook、PBPE、M3など異なるRepository間でデータ構造を統一できる。

---

## 11.9 Domain Data Model

PMOSではDomainごとに独自データモデルを持つことを許容する。

ただし、Domain Data Modelは共通Metadata Schemaに適合する必要がある。

例えばAGRIXでは、

```text
Soil
Crop
Microbiome
Fermentation
Carbon
```

HealthBookでは、

```text
Person
Phenotype
Metabolite
Nutrition
Disease
Biomarker
```

PBPEでは、

```text
Impact
KPI
Cost
Carbon
Finance
Registry
```

などのDomain Modelを持つ。

これらは共通Knowledge IDによってPMOSへ統合される。

---

## 11.10 Graph Data Model

Knowledge GraphではDomain Data Modelを直接コピーしない。

GraphではEntityとRelationshipへ変換する。

例えば、

```text
Soil
  │
  ├── HAS_MICROBIOME
  │
  ├── SUPPORTS
  │
  ▼
Crop
  │
  ├── PRODUCES
  ▼
Food
  │
  ├── AFFECTS
  ▼
Human Health
```

この構造によって、異なるDomainのデータを共通の意味空間へ統合する。

---

## 11.11 Vector Index Schema

PineconeなどのSemantic Indexでは、Knowledge Assetを直接保存するのではなく、検索用のVector Representationを保持する。

Vector Recordには以下を持たせる。

```text
Vector ID
Knowledge ID
Repository
Domain
Asset Type
Version
Semantic Tags
Embedding
Metadata
```

重要なのは、Vector Indexを**Source of Truthにしない**ことである。

PineconeはSemantic Retrieval Layerであり、正式な知識はGitHub Repositoryに存在する。

---

## 11.12 Data Quality

PMOSではデータ品質を以下の観点で管理する。

- Completeness
    
- Consistency
    
- Accuracy
    
- Timeliness
    
- Provenance
    
- Version Integrity
    
- Schema Integrity
    
- Semantic Integrity
    

特にSemantic Integrityを重視する。

形式上正しいJSONであっても、Ontology上の意味が不整合であればKnowledge Assetとして利用できない。

---

## 11.13 Security and Access

PMOSではデータへのアクセス権をRepository、Knowledge Asset、Agent、Userの各レベルで管理する。

```text
User
 ↓
Role
 ↓
Repository Permission
 ↓
Knowledge Permission
 ↓
Agent Permission
 ↓
Data Access
```

公開Knowledgeと非公開Knowledgeを明確に分離する。

---

## 11.14 Data Lifecycle

```text
Create
 ↓
Validate
 ↓
Register
 ↓
Version
 ↓
Index
 ↓
Graph
 ↓
AI Use
 ↓
Dashboard
 ↓
Archive / Update
```

このライフサイクルをGitHubとCI/CDによって自動化する。

---

## 11.15 PMOS Data Architectureの特徴

PMOSのData Architectureでは、データベースを中心に据えない。

中心にあるのは**Knowledge Contract**である。

```text
Data
 ↓
Data Contract
 ↓
Knowledge Asset
 ↓
Knowledge Contract
 ↓
Knowledge Graph
 ↓
AI Context
 ↓
Executive Intelligence
```

この構造によって、データソース、Database、Vector DB、Graph DB、LLMが交換可能になる。

PMOSは特定のデータベースやAIモデルに依存せず、**知識構造そのものをプラットフォームの中核資産として保持する。**