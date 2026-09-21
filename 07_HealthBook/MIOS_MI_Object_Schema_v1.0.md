# MIOS MI Object Schema v1.0

**Document ID:** MIOS-MIO-001  
**Version:** 1.0.0  
**Status:** Draft for architecture freeze  
**Parent:** MIOS Canonical Data Model v1.0  
**Input Contract:** MIOS Metabolic Snapshot Schema v1.0

## 1. Purpose

MI Object（Metabolic Intelligence Object）は、MIOS内のAI Agent、Engine、Workflow、Knowledge Graph間で構造化された代謝インテリジェンスを受け渡すためのCanonical Objectである。

```text
Metabolic Snapshot
        ↓
     MI Object
        ↓
┌───────┼────────┬────────┐
↓       ↓        ↓        ↓
Phenotype Pathway Disease Solution
 Agent    Agent    Agent    Agent
        ↓
  Governance / Orchestrator
```

MI Objectは自然言語メッセージではなく、Agent-to-Agent processing contractとして機能する。

## 2. Scope

v1.0で定義するもの：

- MI Object envelope
- Object type
- Task identity
- Producer / Consumer
- Input / Output references
- Payload boundary
- Confidence representation
- Evidence / Provenance
- Dependencies
- Status
- Parent / Child relation
- Knowledge Graph linkage
- Agent execution trace

本仕様では詳細確定しないもの：

- MI Codeの桁構造
- Agent-to-Agent transport protocol
- Workflow DSL
- 臨床判断ルール
- 個別Pathwayの医学的因果ルール
- FHIR Resource mapping

## 3. Core Principle

```text
MI Code
   = identity / classification / state reference

MI Object
   = structured intelligence payload

Agent
   = processing capability

Workflow
   = orchestration logic

Knowledge Graph
   = relationship layer
```

PBPE 7-digit classificationをそのままMIOSへ移植せず、MI CodeとMI Objectを別仕様として管理する。

## 4. Canonical Envelope

```json
{
  "mi_object_id": "MIO-000001",
  "object_type": "PathwayHypothesis",
  "schema_version": "1.0.0",
  "status": "draft",
  "task_id": "TASK-000001",
  "producer_agent": "AGENT-PATHWAY-001",
  "consumer_agents": [],
  "input_refs": [],
  "payload": {},
  "confidence": null,
  "evidence_refs": [],
  "dependency_refs": [],
  "provenance": []
}
```

## 5. Required Fields

| Field | Required | Meaning |
|---|---:|---|
| mi_object_id | Yes | MI Object identifier |
| object_type | Yes | MI Object class |
| schema_version | Yes | Schema version |
| status | Yes | Lifecycle state |
| task_id | Yes | Workflow task identifier |
| producer_agent | Yes | Producing Agent |
| input_refs | Yes | Input Object references |
| payload | Yes | Domain payload |

## 6. Object Types

```text
Observation
MetabolicSnapshot
Phenotype
MetabolicState
MetabolicDeviation
MIScore
PathwayHypothesis
DiseaseMIMapping
KnowledgeAsset
InterventionCandidate
SimulationResult
Recommendation
Evidence
WorkflowEvent
DigitalTwinState
```

Agent自身はMI Objectではなく、Agent RegistryのEntityとして扱う。

## 7. Task / Producer / Consumer

```text
Workflow
   ↓
Task
   ↓
Agent
   ↓
MI Object
```

Producerは生成主体、Consumerは次に利用するAgentを表す。Consumerを省略する場合はWorkflow Orchestratorがルーティングできる。

## 8. Input References

原データを無制限に複製せず、Canonical Objectを参照する。

```json
{
  "input_refs": [
    "SNAP-000001",
    "PHENO-000021"
  ]
}
```

## 9. Payload

Payloadはobject_typeごとのdomain dataを格納する。

```json
{
  "object_type": "PathwayHypothesis",
  "payload": {
    "pathway_ref": "PATH-EQUOL",
    "hypothesis_type": "functional_capacity",
    "related_phenotype_refs": [],
    "related_metabolic_state_refs": []
  }
}
```

本仕様はPathwayの真偽や医学的効果を規定しない。

## 10. Confidence

推論確度を表現する任意フィールド。

```json
{
  "confidence": {
    "value": 0.0,
    "scale": {"min": 0.0, "max": 1.0},
    "method_ref": null
  }
}
```

0〜1の意味は各Engine / Agent Specificationで定義する。臨床的確率等と同一視しない。

## 11. Evidence / Provenance

```text
Evidence
    ↓
supports
    ↓
MI Object
```

推論ObjectとEvidenceは別Objectとして管理する。

Provenanceでは可能な範囲で以下を保持する。

```text
source_refs
agent_id
task_id
execution_id
timestamp
schema_version
```

## 12. Dependencies

```json
{
  "dependency_refs": [
    "KB-MICROBIOME-001",
    "PATH-EQUOL-001"
  ]
}
```

Knowledge Assetのversion変更時に推論結果を再評価できる構造とする。

## 13. State

Object lifecycle：

```text
draft → validated → approved → deprecated → archived
```

Execution-specific state：

```text
created → ready → running → completed
                    ├→ failed
                    └→ cancelled
```

Object lifecycleとExecution stateは概念的に分離する。

## 14. Parent / Child

```text
MIO-ROOT
 ├── MIO-PHENO
 ├── MIO-PATHWAY
 │    ├── MIO-EQUOL
 │    └── MIO-SCFA
 └── MIO-SOLUTION
```

## 15. Agent Handoff Contract

```text
Agent A
   │
   ├── task_id
   ├── mi_object_id
   ├── object_type
   ├── payload
   ├── evidence_refs
   └── provenance
   ↓
Agent B
```

Transport protocolはこのSchemaの外側に置く。

## 16. Governance / Orchestration

Governance Agent / Orchestratorは、Domainの医学的正否を単独で決定する主体ではない。

主な役割：

```text
validate schema
check references
check dependencies
check state
route object
record provenance
detect conflict
```

## 17. Conflict Handling

異なるAgentの矛盾したObjectを上書きしない。

```text
Object A
Object B
   ↓
Conflict Event
   ↓
Governance / Adjudication
   ↓
Resolution Object
```

## 18. Knowledge Graph

MI ObjectはGraph Nodeとして登録可能。

```text
MI Object
   ├── generated_by → Agent
   ├── derived_from → Snapshot
   ├── supported_by → Evidence
   ├── depends_on → Knowledge Asset
   ├── related_to → Phenotype
   └── proposes → Intervention
```

正式Edge vocabularyはKnowledge Graph Specificationで確定する。

## 19. Digital Twin

```text
Snapshot
   ↓
MI Object
   ↓
State Interpretation
   ↓
Digital Twin State
```

MI Objectが直接Digital Twinを更新するかはWorkflow / Governance仕様で決定する。

## 20. Validation

```text
1. JSON syntax
2. MI Object Schema
3. object_type validation
4. reference validation
5. registry validation
6. provenance validation
7. evidence validation
8. workflow validation
```

失敗時は元Objectを破棄せずValidation Eventを生成する。

## 21. Minimal Valid Object

```json
{
  "mi_object_id": "MIO-000001",
  "object_type": "Phenotype",
  "schema_version": "1.0.0",
  "status": "draft",
  "task_id": "TASK-000001",
  "producer_agent": "AGENT-PHENOTYPE-001",
  "input_refs": ["SNAP-000001"],
  "payload": {}
}
```

## 22. Architecture Boundary

```text
MI Code
   │ identifies
   ▼
MI Object
   │ processed by
   ▼
Agent
   │ coordinated by
   ▼
Workflow
   │ connected to
   ▼
Knowledge Graph
```

## 23. Next Specification

次は **MIOS MI Code Standard v1.0**。

ここで、

```text
Namespace
Hierarchy
Classification
Registry
State
Transition
Version
Collision
```

を正式定義する。

その後、

```text
MI Code
   +
MI Object
   +
Agent Registry
```

を接続し、Agent Networkの共通識別・追跡基盤を完成させる。
