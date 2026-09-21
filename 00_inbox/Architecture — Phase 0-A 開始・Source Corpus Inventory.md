# Architecture — Phase 0-A 開始・Source Corpus Inventory

## 結論

**Phase 0-A「HealthBook-MIOS Source Corpus Inventory & Source Registry v1.0」へ正式に着手しました。**

今回のInventoryでは、まだArchitectureの再設計・Canonical昇格・内容の統合は行いません。

まず確認できたSourceを、

```text
SOURCE CORPUS
      ↓
SOURCE INVENTORY
      ↓
SOURCE REGISTRY
      ↓
ARCHITECTURE GENEALOGY
      ↓
RECONCILIATION QUEUE
```

へ固定します。

特に重要なのは、アップロードされた `healthbook-mios.zip` が単なるコードZIPではなく、**Git履歴を含むHealthBook-MIOS統合Repositoryそのもの**であり、内部に過去のHealthBook/MI/MIOS時系列資料まで含んでいることです。

---

# 1. Source Corpus 現在確認値

| Source                        | Type                |                   現在確認できた内容 | Role                        |
| ----------------------------- | ------------------- | --------------------------: | --------------------------- |
| HealthBook-MI-Probiome-OS.txt | Repomix             |           Repository + Code | Technical Source            |
| HealthBook-AI.txt             | Repomix             |      Repository + Data/Code | Technical Source            |
| HealthBook-Integrated.txt     | Repomix             |      Repository + Data/Code | Legacy Technical Source     |
| HealthBook-MBT55-Unified.txt  | Repomix             | Repository + Data/Code/Docs | Integrated Legacy Source    |
| healthbook-mios.zip           | Original Repository |        **442 source files** | Primary / Provenance Source |

RepomixはRepository内容のSemantic Analysis用、ZIPはOriginal Structure / Provenance Verification用として**別Source IDで管理**します。

Repomix自体もread-onlyのpacked representationであることが明記されています。

---

# 2. Original Repository Verification

`healthbook-mios.zip` を直接検査した結果：

```text
healthbook-mios/
├── .git/
├── 2026-04-24_MBT Probiotics/
├── 2026-05-18_HealthBook-MI/
├── 2026-06-07_MI構築追加内容/
├── 2026-07-03_MI-Probiome/
├── 2026-07-28_MIOS/
├── 2026-08-10_HealthBook_MIOS/
└── root-level canonical/data/code artifacts
```

### Repository規模

```text
ZIP entries              499
Total files              476
Source files excluding
.git                      442

Markdown                 404
JSON                      23
Python                    13
CSV                        2
```

したがって、**Phase 0-AのPrimary Source Corpusとして442 source filesを登録可能**です。

---

# 3. Architecture Genealogy Source Folders

ZIP内部で6つの時系列Architecture Corpusを確認しました。

| Sequence | Folder                     | Files | Architecture Role                        |
| -------: | -------------------------- | ----: | ---------------------------------------- |
|       01 | 2026-04-24_MBT Probiotics  |    22 | MBT Probiotics / metabolic precursor     |
|       02 | 2026-05-18_HealthBook-MI   |   127 | HealthBook-MI foundation                 |
|       03 | 2026-06-07_MI構築追加内容        |    49 | MI architecture expansion                |
|       04 | 2026-07-03_MI-Probiome     |    55 | MI-Probiome OS                           |
|       05 | 2026-07-28_MIOS            |    62 | MIOS constitutional / architecture layer |
|       06 | 2026-08-10_HealthBook_MIOS |    92 | Latest HealthBook-MIOS integration       |

合計：

**407 files**

残り **35 files** はRoot-level artifactsです。

---

# 4. Root-level Canonical / Implementation Assets

ZIPのRootには以下の35 Artifactを確認しました。

### Core Data

```text
animal_metabolic_library.json
disease_matrix_137.json
kampo_metabolic_library.json
master_pathways.json
phenotype_weight_matrix.json
probiotic_matrix.json
questionnaire_200_en.json
questionnaire_200_jp.json
questionnaire_pathway_matrix.json
pathway_food_map.json
substrate_metabolite_graph.json
strain_conversion_matrix.json
pathway_definition.json
```

### Engines / Connectors

```text
inference_engine.py
pathway_database.py
phenotype_engine.py
phenotyping_engine.py
recommendation_engine.py
screening_engine.py
metabolite_mapper.py
metabolite_disease_mapper.py
gut_metabolism_connector.py
cascade_connector.py.md.py
fhir_exporter.py
mbt55_integration.py
healthbook_demo.py
```

### MIOS Schema / Governance Candidates

```text
mios_mi_object.schema.json
mios_metabolic_snapshot.schema.json
mios_canonical_object_envelope.schema.json
mi_object_type_registry.v1.0.json
```

### Reconciliation Assets

```text
MBT_Kampo_Full_Inventory_v1.0.json
MBT_Kampo_File_Inventory_v1.0.csv
MBT_Kampo_Cross_Source_Difference_Matrix_v1.0.csv
MBT_Kampo_Cross_Source_Structural_Reconciliation_v1.0.json
```

これは非常に重要です。

**既にSource Corpus内部に、今回Phase 0で作るべきInventory/Reconciliation成果物の前身が存在しています。**

したがって、これらを新規Canonical化するのではなく、

```text
Existing Artifact
       ↓
Inventory
       ↓
Provenance Verification
       ↓
Status Classification
       ↓
Re-use / Supersede / Reconcile
```

として扱います。

---

# 5. Git Provenance

Original ZIPには `.git` が含まれています。

確認されたRemote：

```text
https://github.com/shimojok/healthbook_mios.git
```

Branch：

```text
main
```

HEAD：

```text
44f631b552fd4888438fe6491da810fdcf28e6c7
```

Git logから、少なくとも以下の履歴を確認できます。

```text
5367cde...  Initial commit
44f631b...  Initial commit
```

最新commit timestampは、

```text
2026-08-29 22:38:34 +09:00
```

です。

したがって、このZIPは単なるExportではなく、**Git provenanceを保持したPrimary Repository Source**として扱います。

---

# 6. 4 Repository Technical Source Inventory

## REPO-001 — HealthBook-MI-Probiome-OS

Repository構造：

```text
ai_agents/
engines/
data/
interfaces/
platform/
ui/
tests/
README.md
```

確認された主要Engine：

```text
Phenotyping
Probiotics Screening
Estrobolome
Endocrine Axis
Acetyl-CoA / ATP
Inflammation / Immune
Oriental Medicine
Disease Matrix
```

さらに、

```text
SnapshotBuilder
EngineOrchestrator
CausalMap
MedicalPipeline
InsurancePipeline
ProbioticsPipeline
```

というOS型構造が存在します。

AI Agent層も、

```text
Triage
Risk Explanation
Clinical Assistant
Insurance Underwriting
Explainability
```

まで実装されています。

**Architecture Role：MI-Probiome OS prototype/reference implementation**

---

# 7. REPO-002 — HealthBook-AI

Repository構造：

```text
api/
dashboard/
data/
disease/
graphs/
mbt55/
metabolic_graph/
ontology/
phenotype/
recommendation/
src/
```

主要Data：

```text
questionnaire_200_en.json
questionnaire_200_jp.json
disease_matrix_137.json
kampo_metabolic_library.json
animal_metabolic_library.json
```

主要Integration：

```text
Inference Engine
Metabolite Mapper
Gut Metabolism Connector
Cascade Connector
FHIR Exporter
```

UIはStreamlitベースで、200Q → pathway → disease risk → metabolites → FHIRという流れを持ちます。

**Architecture Role：Inference / AI implementation source**

---

# 8. REPO-003 — HealthBook-Integrated

Repository自身のREADMEに、

> This repository has been archived.

と明記されています。

また後継としてHealthBook-AIを指定しています。

主要構造：

```text
data/en/
data/ja/
data/kampo/

src/healthbook/
├── engine.py
├── disease_risk.py
├── kampo_mapper.py
└── phytochemical_recommender.py
```

**Architecture Role：LEGACY / historical implementation**

したがって、現時点ではCanonical候補ではなく、

```text
LEGACY SOURCE
      ↓
Migration Reference
```

として扱います。

---

# 9. REPO-004 — HealthBook-MBT55-Unified

Repositoryには、

```text
dashboard/
data/
docs/
src/
tests/
```

が存在し、

```text
PATH_01–05
MBT_META_01–05
200Q
137 Disease Matrix
Kampo
MBT55
Metabolic Pathways
Phenotyping
Probiotics Screening
```

を統合しています。

Changelogでは、

```text
200 Questionnaire
→ PATH_01–05
→ Disease Risk
→ Kampo
→ Meta-Strain
→ Metabolites
```

というFull Pipelineが明記されています。

**Architecture Role：Integrated legacy/reference implementation**

---

# 10. MIOS Constitutional Source

さらにSource Corpus内には、すでにMIOS Constitution相当の文書が存在します。

確認された原則：

```text
Knowledge Before Algorithms
Explainable Intelligence
Modular Intelligence
Scientific Governance
Human-Centered AI
Continuous Evolution
Planetary Perspective
```

そして、

```text
Constitution
↓
Standards
↓
Specifications
↓
Reference Architectures
↓
Reference Implementations
↓
Applications
```

という階層が定義されています。

これは今回のHealthBook-MIOS Architecture Governanceと非常に重要な関係を持ちます。

ただし、**Phase 0ではこれを新たにCanonicalとして再決定しません。**

まず既存Artifactとして登録します。

---

# 11. Existing MIOS Architecture Artifacts

特に重要なArchitecture候補として、ZIPから以下を確認しました。

```text
MIOS Architecture Book v1.0
MIOS Reference Architecture
MIOS Canonical Data Model v1.0
MIOS Canonical Data Model & Data Contract v1.0
MIOS Microbiome Functional Architecture v1.0
MIOS Microbiome Functional Ontology v1.0
MIOS KG Schema v1.0
MIOS KG JSON Schema v1.0
MIOS KG Reference Dataset & Validation Suite v1.0
MIOS KG Reference Pathway Set v1.0
MIOS KG Automated Validation Specification v1.0
MIOS Architecture Specification v1.0
MIOS System Specification v1.0
MIOS KG Implementation Specification v1.0
MIOS Health Profile Schema v1.0
```

さらにLegacy Audit / Reconciliation系：

```text
HealthBook Legacy Asset Audit
HealthBook 4 Repository Verification
HealthBook 4 Repository Audit
Cross-Architecture Audit
Data / Engine Dependency Audit
Canonical Source Decision
Canonical Data Reconciliation
Canonical Evidence & Provenance Reconciliation
Evidence Claim Inventory
P0 Evidence Validation
200Q Functional Mapping
MBT Kampo Full Inventory
```

まで存在します。

つまり今回のProjectは**ゼロからArchitectureを作るProjectではありません。**

既存の成果物を、

```text
Historical Architecture
        ↓
Evidence / Provenance
        ↓
Status Classification
        ↓
Canonical Reconciliation
        ↓
Implementation
```

へ再統治するProjectです。

---

# 12. Preliminary Source Status Matrix

現段階では、以下を**暫定Inventory Status**とします。

| Asset Group               | Preliminary Status       | 理由                                   |
| ------------------------- | ------------------------ | ------------------------------------ |
| HealthBook-Integrated     | LEGACY                   | Repository自身がArchived                |
| HealthBook-AI             | LEGACY / REFERENCE       | 後継実装として存在                            |
| HealthBook-MBT55-Unified  | LEGACY / REFERENCE       | 統合実装                                 |
| HealthBook-MI-Probiome-OS | REFERENCE IMPLEMENTATION | MI-Probiome OS構造                     |
| 2026-05 HealthBook-MI     | HISTORICAL               | Genealogy Source                     |
| 2026-06 MI                | HISTORICAL               | Genealogy Source                     |
| 2026-07 MI-Probiome       | HISTORICAL               | Genealogy Source                     |
| 2026-07 MIOS              | ARCHITECTURE SOURCE      | MIOS architecture formation          |
| 2026-08 HealthBook-MIOS   | CURRENT SOURCE CANDIDATE | 最新Architecture Corpus                |
| MIOS schemas              | CANONICAL CANDIDATE      | ただし再検証必要                             |
| MBT Kampo inventories     | RECONCILIATION SOURCE    | Cross-source differences存在           |
| 200Q                      | CANONICAL CANDIDATE      | Identity/Mapping validation required |
| 137 Disease Matrix        | CANONICAL CANDIDATE      | Legacy reconciliation required       |
| KG Reference Pathways     | CANONICAL CANDIDATE      | Existing specificationあり             |
| Evidence claims           | RECONCILIATION REQUIRED  | Provenance validation必要              |

**CANONICAL CANDIDATE ≠ CANONICAL確定**です。

---

# 13. 重要な発見

今回のPhase 0-Aで、最も重要なことが一つ判明しました。

## HealthBook-MIOSは既に「三層Source Corpus」になっています

```text
                ┌─────────────────────────┐
                │ Historical Research     │
                │ 2026-04 → 2026-08       │
                └────────────┬────────────┘
                             ↓
                ┌─────────────────────────┐
                │ Existing Repositories   │
                │ 4 HealthBook Repos      │
                └────────────┬────────────┘
                             ↓
                ┌─────────────────────────┐
                │ healthbook-mios.git     │
                │ Integrated Corpus       │
                └─────────────────────────┘
```

さらに最新Repository自身が、

```text
Source Notes
+
Legacy Assets
+
Canonical Candidates
+
Schemas
+
Reconciliation Artifacts
+
Implementation
```

を既に内包しています。

したがって、**次に必要なのは「設計」ではなくSource Control Planeです。**

---

# 14. Phase 0-A Registry Architecture

GitHub側では以下を正式な配置候補とします。

```text
HealthBook-MIOS/
│
├── 00_governance/
│   └── source_registry/
│       ├── source_registry_v1.0.json
│       ├── repository_registry_v1.0.json
│       ├── file_manifest_v1.0.csv
│       ├── note_inventory_v1.0.csv
│       ├── architecture_document_inventory_v1.0.csv
│       ├── evidence_inventory_v1.0.csv
│       ├── decision_inventory_v1.0.csv
│       └── architecture_genealogy_v1.0.json
│
├── 02_source_archive/
│
├── 03_architecture_history/
│
└── 04_reconciliation/
    └── reconciliation_queue_v1.0.json
```

---

# 15. Data Flow

```text
4 Repomix TXT
      │
      ├─────────────┐
      │             │
Original ZIP ───────┤
      │             │
      ↓             ↓
Repository      Historical
Structure       Notes
      │             │
      └──────┬──────┘
             ↓
       SOURCE REGISTRY
             ↓
       FILE MANIFEST
             ↓
       NOTE INVENTORY
             ↓
    ARCHITECTURE GENEALOGY
             ↓
   RECONCILIATION QUEUE
```

ここではまだ、

```text
Canonical Data Model
KG
Evidence Model
Clinical Model
AI Agent Model
```

を変更しません。

---

# 16. Phase 0-A KPI

Inventory完了基準を数値化します。

| KPI                                 |               Target |
| ----------------------------------- | -------------------: |
| Primary Repository Source Coverage  |             **100%** |
| Source File Registration            | **442 / 442 = 100%** |
| Historical Folder Registration      |     **6 / 6 = 100%** |
| Repomix Registration                |     **4 / 4 = 100%** |
| Git Provenance Capture              |             **100%** |
| Duplicate Classification            |             **100%** |
| Supersession Classification         |             **100%** |
| Canonical Candidate Classification  |             **100%** |
| Unverified Claims                   |            **0件を目標** |
| P0 Evidence Conflicts before Freeze |               **0件** |

---

# 17. Phase 0-A 現在地

```text
PHASE 0
│
├── 0-A Source Corpus Inventory
│   ├── Repository Inventory       ✓
│   ├── ZIP Provenance             ✓
│   ├── Historical Folders         ✓
│   ├── File Count                 ✓
│   ├── Root Artifact Inventory    ✓
│   └── Preliminary Classification ✓
│
├── 0-B Architecture Genealogy
│   └── NEXT
│
└── 0-C Reconciliation Queue
    └── AFTER 0-B
```

### 現時点の確定事項

**Source Corpusの存在・構造・規模・主要Artifact群については確認完了。**

一方、

**全442ファイルについての個別 `File → Note → Date → Version → Role → Dependency → Duplicate → Superseded → Canonical Candidate` の完全台帳化はまだ未完了**です。

ここはPhase 0-Aの次工程として機械的に埋めるべきです。

---

# Repository Governance

**Target Repository**

```text
HealthBook-MIOS
```

**Primary Input**

```text
healthbook-mios.zip
```

**Secondary Semantic Sources**

```text
HealthBook-MI-Probiome-OS.txt
HealthBook-AI.txt
HealthBook-Integrated.txt
HealthBook-MBT55-Unified.txt
```

**Dependencies**

```text
Source Registry
    ↓
Architecture Genealogy
    ↓
Reconciliation Queue
    ↓
Canonical Architecture
```

**扱うスレッド**

```text
HealthBook-MIOS
└── Canonical Architecture & Implementation PMO
```

Phase 0-Aでは**Architecture再設計スレッドへ先行移行しません。**

---

# Next Action

次は **Phase 0-Aの完全版**として、ZIP内407件の時系列Note/Architecture Documentと35件のRoot Artifactを、さらにRepomix 4 RepositoryとCross-Source比較し、

```text
SOURCE ID
REPOSITORY
FOLDER
FILE
NOTE NUMBER
NOTE TITLE
DATE
VERSION
SOURCE TYPE
ARCHITECTURE ROLE
DATA ROLE
EVIDENCE ROLE
DEPENDENCY
DUPLICATE
SUPERSEDED
CANONICAL CANDIDATE
STATUS
```

まで落とし込んだ **`MIOS Source Registry v1.0`** を作成するのが正しい一直線の工程です。

**このSource Registry v1.0をPhase 0-Aの正式Artifactとして確定し、全442 Source Fileの完全Inventoryへ進めますか？**
