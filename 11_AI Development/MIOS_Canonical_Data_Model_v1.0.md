# MIOS Canonical Data Model v1.0
## Metabolic Intelligence Operating System

**Document ID:** MIOS-CDM-001  
**Version:** 1.0.0  
**Status:** Draft for architecture freeze  
**Canonical Domain:** HealthBook MIOS  
**Supersedes:** none  
**Primary purpose:** MIOSの全データ、Knowledge Asset、推論状態、AI Agent間通信、Workflow、Knowledge Graph、Digital Twinを共通データモデルで接続する。

---

## 1. Scope

MIOS Canonical Data Model（CDM）は、HealthBook MIOSを構成するデータを「何を入力し、何を推論し、何を受け渡し、何を保存するか」という共通モデルとして定義する。

本仕様は、以下を対象とする。

- HealthBook入力データ
- Metabolic Snapshot
- Phenotype
- Metabolic State
- Metabolic Deviation
- MI Score
- Pathway Hypothesis
- Disease-MI Matrix
- Knowledge Asset
- MI Object
- MI Code
- AI Agent
- Workflow Event
- Evidence
- Intervention Candidate
- Simulation Result
- Recommendation
- Digital Twin
- Knowledge Graph参照

本仕様は、各オブジェクトの詳細JSON Schemaそのものではない。詳細Schemaは本CDMを親契約として個別Specificationで定義する。

---

## 2. Architecture Position

```text
                    ┌──────────────────────┐
                    │   HealthBook Input   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Metabolic Snapshot   │
                    └──────────┬───────────┘
                               ↓
                    ┌──────────────────────┐
                    │   MI Object Layer    │
                    └──────────┬───────────┘
                               ↓
          ┌────────────────────┼────────────────────┐
          ↓                    ↓                    ↓
    MI Core Engines       Knowledge Graph       AI Agents
          │                    │                    │
          └────────────────────┼────────────────────┘
                               ↓
                    ┌──────────────────────┐
                    │ Workflow / Orchestrator│
                    └──────────┬───────────┘
                               ↓
             ┌─────────────────┼──────────────────┐
             ↓                 ↓                  ↓
       Pathway Hypothesis  Simulation       Recommendation
             │                 │                  │
             └─────────────────┼──────────────────┘
                               ↓
                    ┌──────────────────────┐
                    │   Metabolic Digital  │
                    │       Twin           │
                    └──────────────────────┘
```

---

## 3. Design Principles

### 3.1 Canonical Object Principle

同一情報をAgentごとに別形式で持たず、共通Objectを参照する。

### 3.2 Observation / Inference Separation

観測された事実とAIによる推論を分離する。

```text
Observation ≠ Inference
```

### 3.3 Knowledge / Logic Separation

Knowledge Assetと実行ロジックを分離する。

```text
Knowledge Asset → JSON / Graph / Ontology
Execution Logic → Engine / Agent / Workflow
```

### 3.4 Evidence Traceability

推論・介入候補・Recommendationは、可能な範囲でKnowledge AssetおよびEvidenceへ追跡可能でなければならない。

### 3.5 Versioned Contract

Canonical Objectはschema_versionを持ち、破壊的変更はmajor versionを変更する。

---

# 4. Canonical Object Hierarchy

```text
MIOS Entity
│
├── Observation
│
├── Metabolic Snapshot
│   ├── nutrition
│   ├── gut_status
│   ├── hormone_state
│   ├── microbiome
│   ├── musculo_fascial
│   └── symptoms
│
├── Phenotype
│
├── Metabolic State
│
├── Metabolic Deviation
│
├── MI Score
│
├── Pathway Hypothesis
│
├── Disease-MI Mapping
│
├── Knowledge Asset
│
├── MI Object
│
├── Agent / Workflow
│
├── Intervention Candidate
│
├── Simulation Result
│
├── Recommendation
│
├── Evidence
│
└── Digital Twin
```

---

# 5. Common Metadata Envelope

すべてのCanonical Objectは、原則として以下の共通メタデータを持つ。

```json
{
  "id": "stable-unique-id",
  "type": "CanonicalObjectType",
  "schema_version": "1.0.0",
  "status": "draft",
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601",
  "provenance": [],
  "evidence_refs": [],
  "dependency_refs": []
}
```

### Required Semantics

| Field | Meaning |
|---|---|
| id | 永続的識別子 |
| type | Object種別 |
| schema_version | Schema version |
| status | Object lifecycle |
| created_at | 作成時刻 |
| updated_at | 更新時刻 |
| provenance | 出典・生成履歴 |
| evidence_refs | Evidenceへの参照 |
| dependency_refs | 依存Objectへの参照 |

---

# 6. Observation

Observationは「観測されたデータ」を表す。

対象例：

- バイタル
- 検査値
- 問診回答
- 生活習慣
- 腸内環境情報
- ホルモン情報
- 表現型情報
- 東洋医学的観察

Observationは、AIによる解釈を直接格納しない。

```json
{
  "id": "OBS-000001",
  "type": "Observation",
  "schema_version": "1.0.0",
  "status": "validated",
  "subject_ref": "PERSON-000001",
  "domain": "symptoms",
  "code": "thumb_pain",
  "value": {
    "type": "qualitative",
    "value": "present"
  },
  "observed_at": "ISO-8601",
  "source": "questionnaire"
}
```

---

# 7. Metabolic Snapshot

Metabolic Snapshotは、個体の一定時点における統合された状態入力を表す。

既存設計で使用されている主要marker domainは以下である。

```text
nutrition
gut_status
hormone_state
microbiome
musculo_fascial
symptoms
```

またHealthBook-MIのData Integration Layerでは、バイタル、血液検査、生活習慣、MBT55、ウェアラブル、舌診・脈診・問診などを統合対象としている。

```json
{
  "id": "SNAP-000001",
  "type": "MetabolicSnapshot",
  "schema_version": "1.0.0",
  "status": "validated",
  "subject_ref": "PERSON-000001",
  "snapshot_at": "ISO-8601",
  "markers": {
    "nutrition": [],
    "gut_status": [],
    "hormone_state": [],
    "microbiome": [],
    "musculo_fascial": [],
    "symptoms": []
  },
  "observation_refs": []
}
```

---

# 8. Phenotype

Phenotypeは、Observation群から抽出された表現型パターンを表す。

MIOSでは少なくとも以下のPattern Layerを扱う。

- Metabolic Pattern
- Neural Pattern
- Endocrine Pattern
- Inflammatory Pattern
- Microbiome-MBT55 Pattern

Phenotypeは「疾患診断」ではなく、状態表現として扱う。

---

# 9. Metabolic State

Metabolic Stateは、複数のPhenotype、Observation、Pathway情報を統合した代謝状態表現である。

```text
Observation
   ↓
Phenotype
   ↓
Metabolic State
```

状態は単一数値ではなく、複数MI軸と関連Pathwayを参照可能な構造とする。

---

# 10. Metabolic Deviation

Metabolic Deviationは、Metabolic Stateにおいて標準状態からの偏位として扱う推論Objectである。

既存HealthBook-MI設計では、D001〜D090として代謝偏位コードを生成する構想が記録されている。一方、Disease-MI Matrix v2ではDxxxが疾病エントリIDとしても使用されているため、**このID体系は混同を避けるため今後のMI Code Standardで正式分離する必要がある。**

これは本CDMでは未解決事項として保持する。

```text
Metabolic Deviation
 ├── deviation_id
 ├── domain
 ├── direction
 ├── severity
 ├── confidence
 └── evidence_refs
```

---

# 11. MI Score

MI Scoreは、MI Engineが算出する軸別の状態指標である。

NHB053ではMI-AcetylCoAおよびMI-Estrobolomeを0〜1で扱い、他MI軸と同一スケールにする設計が記録されている。

```json
{
  "id": "MIS-000001",
  "type": "MIScore",
  "axis": "MI-Estrobolome",
  "value": 0.0,
  "scale": {
    "min": 0.0,
    "max": 1.0
  },
  "calculation_refs": [],
  "evidence_refs": []
}
```

**重要:** 0〜1の数値は「臨床的重症度」を意味するとは本資料群では定義されていない。意味付けは各MI Engine Specificationで固定する。

---

# 12. MI Engine

既存資料から確認できるCore Engine：

```text
MI-Metabolic
MI-Neuro-Endocrine
MI-Inflammation
MI-MBT55
MI-Oriental-Medicine
```

追加された軸：

```text
MI-AcetylCoA
MI-Estrobolome
MI-Mitochondria
```

MI Engineは、

```text
Input Object
   ↓
Analysis
   ↓
MI Score / State
   ↓
Pathway Hypothesis
```

を生成する。

---

# 13. Disease-MI Mapping

Disease-MI Matrix v2では、各疾病Entryに以下を持つ設計が確定している。

```text
disease_id
name
name_en
category
description
core_pathways
deviation_codes
snapshot_markers
related_mi_engines
intervention_focus
```

core_pathwaysには現在、

```text
acetylcoa
estrobolome
mitochondria
mbt55
inflammation
```

がある。

Disease-MI Mappingは、

```text
Metabolic Snapshot
      ↓
snapshot marker matching
      ↓
Dxxx contribution
      ↓
MI-axis aggregation
      ↓
MI Score
```

という既存設計を受ける。

---

# 14. Pathway Hypothesis

Pathway Hypothesisは、Observation / Phenotype / Metabolic State / Knowledge Graphから導出される「検討対象となる経路仮説」を表す。

MIOSで明示されているReference Pathway：

- Equol
- Urolithin A
- SCFA

主要追加軸：

- AcetylCoA
- Estrobolome
- Mitochondria
- Bile Acid
- Aromatic Amino Acid

MBT55の既存設計ではSCFA、Bile Acid、Aromatic AAが中核モジュールとして扱われる。

---

# 15. Knowledge Asset

Knowledge Assetは、MIOSが推論に利用する外部・内部知識を表す。

HealthBookの既存ライブラリー：

```text
200 Questionnaire
137 Disease Matrix
Metabolic Pathway
Nutrition
Hormone
ATP
Microbiome
MBT Kampo
Animal Materia Medica
Biomarker
Evidence
Registry
Ontology
Simulation
```

Knowledge Assetには必ずRegistry上の識別子を付与する。

---

# 16. MI Object

MI Objectは、AI Agent間で受け渡すCanonical Intelligence Objectである。

```text
Agent A
   │
   │ MI Object
   ▼
Agent B
   │
   │ MI Object
   ▼
Agent C
```

MI ObjectはNatural Language Messageそのものではなく、構造化された入力・出力契約である。

基本構造：

```json
{
  "mi_object_id": "MIO-000001",
  "object_type": "PathwayHypothesis",
  "schema_version": "1.0.0",
  "task_id": "TASK-000001",
  "producer_agent": "AGENT-PATHWAY-001",
  "input_refs": [],
  "payload": {},
  "confidence": null,
  "evidence_refs": [],
  "status": "draft"
}
```

詳細Schemaは **MI Object Schema v1.0** で別途固定する。

---

# 17. MI Code

MI Codeは、MIOS Agent Network内でObject、Task、State、Workflowを識別・追跡するためのコード体系として設計する。

現時点では、PBPE 7-digit classificationを着想源とした概念が存在するが、桁構成・namespace・state transition・registry・collision rulesは未確定である。

したがって本CDMでは、

```text
MI Code = identifier / classification layer
MI Object = data / intelligence payload layer
```

として分離する。

正式仕様は **MI Code Standard v1.0** で決定する。

---

# 18. Agent

Agentは、特定のCapabilityを持つ推論・変換・取得・検証・Simulation・Recommendation主体である。

既存Agent群：

```text
Intake
Questionnaire
Laboratory
Phenotype
Nutrition
Pathway
Disease Risk
Hormone
ATP
Microbiome
MBT55
Kampo
Animal Materia Medica
Simulation
Recommendation
Governance
```

Agentは以下を明示する。

```text
agent_id
version
capabilities
input_types
output_types
knowledge_dependencies
mi_engine_dependencies
state
```

---

# 19. Workflow Event

Workflow EventはAgent実行およびObject状態変化を記録する。

最低限、

```text
event_id
workflow_id
task_id
agent_id
event_type
timestamp
input_refs
output_refs
status
```

を持つ。

---

# 20. Evidence

EvidenceはKnowledge Assetまたは推論結果を支持する情報源を表す。

Evidence Objectは少なくとも、

```text
evidence_id
source
source_type
provenance
version
status
linked_objects
```

を持つ。

MIOSは「推論結果」と「Evidence」を同一Objectとして扱わない。

---

# 21. Intervention Candidate

Intervention Candidateは、Metabolic State / Pathway Hypothesis / Knowledge Assetsから生成された介入候補である。

既存設計では、

- 漢方
- 食事
- 生活習慣
- 運動
- サプリメント

などが対象となる。

RecommendationとIntervention Candidateは分離する。

```text
Candidate
   ↓
Screening
   ↓
Simulation
   ↓
Recommendation
```

---

# 22. Simulation Result

Simulation Resultは、介入候補に対してWorkflow/Simulation Agentが生成する評価結果。

Simulation ResultはRecommendationそのものではない。

```text
Intervention Candidate
       ↓
Simulation
       ↓
Simulation Result
       ↓
Recommendation Candidate
```

---

# 23. Recommendation

Recommendationは、Evidence、Pathway Hypothesis、Simulation Result、個体状態を統合した最終候補Object。

医療上の最終判断を自動確定するものではなく、HealthBook MIOSの設計上はEvidence-linked decision-support outputとして扱う。

---

# 24. Digital Twin

Digital Twinは個体の長期的Metabolic Stateを保持する。

```text
Historical Observations
        ↓
Historical Snapshots
        ↓
Phenotypes
        ↓
Metabolic States
        ↓
Interventions
        ↓
Simulation Results
        ↓
Current Digital Twin
```

Digital Twinは単一Snapshotではなく、時系列状態を保持する。

---

# 25. Knowledge Graph Mapping

CDM ObjectとGraph Nodeの対応：

| CDM Object | Graph Role |
|---|---|
| Observation | Node |
| Phenotype | Node |
| Metabolic State | Node |
| Disease | Node |
| Pathway | Node |
| Metabolite | Node |
| Microbial Function | Node |
| Intervention | Node |
| Evidence | Node |
| Agent | Node |
| Digital Twin | Node |
| causes_or_contributes_to | Edge |
| transforms_to | Edge |
| produces | Edge |
| signals | Edge |
| modulates | Edge |
| evidenced_by | Edge |
| generated_by | Edge |

---

# 26. Provenance

MIOSでは、Agentが生成したObjectについて、最低限以下のTraceを維持する。

```text
task_id
agent_id
input_object_id
output_object_id
knowledge_asset_id
schema_version
execution_id
timestamp
```

これにより、

```text
Input
 ↓
Agent
 ↓
Knowledge
 ↓
Inference
 ↓
Output
```

を追跡可能にする。

---

# 27. State Model

Generic Object State：

```text
draft
 ↓
validated
 ↓
approved
 ↓
deprecated
 ↓
archived
```

Workflow State：

```text
created
 ↓
ready
 ↓
running
 ↓
waiting
 ↓
completed
```

異常時：

```text
failed
cancelled
```

詳細なState TransitionはMI Code StandardおよびWorkflow DSLで固定する。

---

# 28. Dependency Model

```text
MIOS Constitution
       ↓
Specifications
       ↓
Canonical Data Model
       ↓
Object Schemas
       ↓
Registries
       ↓
Core Engines
       ↓
Agents / Workflow
       ↓
HealthBook Platform
```

Knowledge AssetsはLogicとは独立して管理し、Schema Contractを介してEngine / Agentから参照する。

---

# 29. Canonical Repository Mapping

```text
healthbook-json-library
        │
        ├── Questionnaire
        ├── Disease-MI
        ├── Pathways
        ├── Nutrition
        ├── Hormone
        ├── Microbiome
        ├── MBT Kampo
        ├── Animal Materia Medica
        ├── Biomarker
        ├── Evidence
        └── Ontology

mios-core
        └── Canonical Object / State / Registry

mios-ai-agents
        └── Agent implementations

mios-workflow-engine
        └── Workflow / Orchestration

mios-knowledge-graph
        └── Nodes / Edges / Ontology

mios-digital-twin
        └── longitudinal state

mios-api
        └── external interface

healthbook-platform
        └── reference application
```

---

# 30. FHIR Boundary

FHIRはCanonical Data Modelそのものではなく、相互運用境界として扱う。

```text
MIOS Canonical Data Model
          ↓
FHIR Mapping Layer
          ↓
FHIR-compatible output
```

具体的Resource Mappingは別Specificationで定義する。

---

# 31. Security Boundary

Canonical Data Modelは「データ契約」であり、実行可能コードを含めない。

Agent-generated codeは別Artifactとして扱い、

```text
Generated Code
 → Validation
 → Sandbox
 → Execution
 → Result Object
```

という境界を置く。

---

# 32. Open Architectural Decisions

本v1.0で未確定として明示的に残す項目：

1. MI Codeの桁構造
2. MI Objectの完全JSON Schema
3. Metabolic Snapshotの完全JSON Schema
4. Agent-to-Agent Protocol
5. Agent Registry Schema
6. Workflow DSLの完全仕様
7. Evidence Provenance Schema
8. Knowledge Graphの物理実装
9. FHIR Resource Mapping
10. Endocrine / Estrobolome / Equol Ontology
11. MBT55 Functional Ontology
12. Digital Twin State Transition

これらを推測で埋めず、次の仕様書で個別に確定する。

---

# 33. Implementation Sequence

システムアーキテクチャ完成までの順序を固定する。

```text
[01] Canonical Data Model          ← THIS DOCUMENT
          ↓
[02] Metabolic Snapshot Schema
          ↓
[03] MI Object Schema
          ↓
[04] MI Code Standard
          ↓
[05] Agent Registry
          ↓
[06] Agent-to-Agent Protocol
          ↓
[07] Knowledge Graph Schema
          ↓
[08] Workflow DSL
          ↓
[09] Disease-MI Matrix Validation
          ↓
[10] Endocrine / Estrobolome / Equol
          ↓
[11] MBT55 Functional Ontology
          ↓
[12] Solution Screening Engine
          ↓
[13] Digital Twin State Model
          ↓
[14] FHIR Mapping
          ↓
[15] GitHub Reference Implementation
```

---

# 34. Architecture Completion Definition

MIOS Architecture is considered structurally complete when:

```text
Every major data type
        ↓
has a canonical object
        ↓
has a JSON Schema
        ↓
has a registry entry
        ↓
has provenance
        ↓
can be consumed by an Agent
        ↓
can participate in a Workflow
        ↓
can be represented in the Knowledge Graph
        ↓
can be traced into the Digital Twin
```

この条件を満たすことを「アーキテクチャ完成」と定義する。

---

# 35. Governance

本CDMはHealthBook MIOSのCanonical Data Contractの親仕様とする。

変更時は以下を要求する。

```text
Change
 ↓
Impact Analysis
 ↓
ADR
 ↓
Schema Update
 ↓
Validation
 ↓
Version
 ↓
Registry Update
```

Master Planの追加はArchitecture completionのKPIとしない。

---

# 36. Source Boundary

本仕様で確定した内容のうち、既存資料に明示されているものは、その定義を保持した。

一方、以下は本仕様で**新規に細部を確定していない**。

- MI Codeの具体的桁構造
- Agent Protocolの通信仕様
- Graph DB製品選定
- FHIR Resourceの具体的対応
- Endocrine/Estrobolome ontologyの詳細
- MBT55 functional ontologyの詳細

これらは今後の個別仕様で確定する。

---

## 37. Final Canonical Statement

> **MIOS Canonical Data Model v1.0 defines the common object boundary through which HealthBook MIOS represents observations, metabolic states, deviations, pathways, knowledge, agents, workflows, evidence, interventions, simulations and longitudinal digital-twin states.**

これにより、HealthBook MIOSは「複数のAIが個別に推論するシステム」から、

```text
Canonical Data
      +
Canonical Knowledge
      +
Canonical Objects
      +
Canonical Codes
      +
Agents
      +
Workflow
      +
Knowledge Graph
      +
Digital Twin
```

を一つの統治されたシステムとして実装するための基礎を持つ。
