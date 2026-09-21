# MIOS MI Code Standard v1.0

**Document ID:** MIOS-MIC-001  
**Version:** 1.0.0  
**Status:** Draft for architecture freeze  
**Parent:** MIOS Canonical Data Model v1.0 / MI Object Schema v1.0

## 1. Purpose

MI Codeは、MIOS内で生成・受け渡しされる**代謝インテリジェンスを一意に識別し、分類し、状態を追跡するためのCanonical Identifier**である。

MI Codeそのものに医学的意味や診断結果を直接埋め込まない。

```text
MI Code
   ↓
Identity / Classification
   ↓
MI Object
   ↓
Agent Processing
```

したがって、MI Codeは「AI Agent間の共通言語」に近い役割を持つが、推論内容そのものはMI Objectのpayloadに保持する。

---

## 2. Design Principle

MIOSでは以下を明確に分離する。

```text
MI Code
＝ 何のObjectか／どの分類か／どの状態か

MI Object
＝ そのObjectが保持する情報

Agent
＝ その情報を処理する能力

Workflow
＝ Agentを動かす順序・条件

Knowledge Graph
＝ Object間の関係
```

この分離により、

```text
Agent A
   ↓ MI Code + MI Object
Agent B
   ↓ MI Code + MI Object
Agent C
```

という多Agent構造を形成できる。

---

# 3. MI Code Architecture

MI Code v1.0は、以下の階層で管理する。

```text
MIOS
 │
 ├── Domain
 │
 ├── Object Class
 │
 ├── Subclass
 │
 ├── Instance
 │
 └── State / Version
```

概念的には、

```text
MIOS
 └── DOMAIN
      └── OBJECT CLASS
           └── SUBCLASS
                └── INSTANCE
                     └── STATE
```

とする。

---

# 4. Namespace

Canonical namespace：

```text
MIOS
```

将来的な外部連携を考慮し、

```text
MIOS:<domain>:<class>:<subclass>:<instance>:<state>
```

というCanonical representationを採用する。

例：

```text
MIOS:PATHWAY:EQUOL:FUNCTIONAL_CAPACITY:001:VALIDATED
```

ただし、これは**機械可読Canonical Code表現**であり、UI表示用名称とは分離する。

---

# 5. Domain Registry

v1.0ではDomainを以下の概念領域に分類する。

```text
OBS
PHN
MET
DEV
SCR
PTH
DIS
KNO
INT
SIM
REC
EVD
WF
DT
```

意味：

|Code|Domain|
|---|---|
|OBS|Observation|
|PHN|Phenotype|
|MET|Metabolic State|
|DEV|Metabolic Deviation|
|SCR|MI Score|
|PTH|Pathway|
|DIS|Disease-MI|
|KNO|Knowledge|
|INT|Intervention|
|SIM|Simulation|
|REC|Recommendation|
|EVD|Evidence|
|WF|Workflow|
|DT|Digital Twin|

これらはMI Object Type Registryとの対応を持つ。

---

# 6. Object Class

Domain内ではObject Classを定義する。

例えばPathway：

```text
PTH
 ├── SCFA
 ├── EQUOL
 ├── UROLITHIN_A
 └── ...
```

ただし、既存Reference Pathway Setに存在しないPathwayをv1.0のCanonical Pathwayとして勝手に追加しない。

したがって、**Registryに登録されていないコードはCanonical MI Codeとして扱わない。**

---

# 7. Instance

同一Classに複数のObjectが存在する場合、Instance IDを付与する。

```text
MIOS:PTH:EQUOL:FUNCTIONAL_CAPACITY:001
MIOS:PTH:EQUOL:FUNCTIONAL_CAPACITY:002
```

Instanceは「Equolそのもの」ではなく、

> Equolに関する特定のMI Object

を識別する。

これにより、Knowledge Asset、Hypothesis、Evidence、Simulation Resultなどを混同しない。

---

# 8. State

MI Codeの末尾にStateを持たせる。

基本State：

```text
DRAFT
VALIDATED
APPROVED
DEPRECATED
ARCHIVED
```

Execution stateはMI CodeそのものではなくWorkflow Event側で管理する。

```text
MI Object Lifecycle
        ↓
MI Code State

Execution Lifecycle
        ↓
Workflow Event
```

---

# 9. Version

VersionはCode identityと分離する。

```text
MIOS:PTH:EQUOL:FUNCTIONAL_CAPACITY:001
```

に対して、

```text
schema_version = 1.0.0
object_version = 1.0
```

を別管理する。

これにより、

```text
Code
≠
Schema Version
≠
Knowledge Version
≠
Object Version
```

を保証する。

---

# 10. MI Code and MI Object

Canonical relation：

```text
MI Code
   │
   └── identifies
           ↓
       MI Object
```

例：

```json
{
  "mi_code": "MIOS:PTH:EQUOL:FUNCTIONAL_CAPACITY:001",
  "mi_object_id": "MIO-000101",
  "object_type": "PathwayHypothesis"
}
```

つまり、

**MI Codeは識別子、MI Objectは実体**

である。

---

# 11. Agent Handoff

Agent間では、MI Codeだけを渡すのではなく、

```text
MI Code
+
MI Object
+
Task ID
+
Provenance
```

を渡す。

```text
Agent A
   │
   ├── MI Code
   ├── MI Object
   ├── Task
   └── Provenance
   ↓
Agent B
```

これにより、Agent Bは、

> 「何についての情報か」

だけでなく、

> 「どのObjectで、どのTaskから来て、誰が生成したか」

を判断できる。

---

# 12. Registry

MI Codeは自由生成しない。

```text
Agent
  ↓
Code Request
  ↓
MI Code Registry
  ↓
Unique Code
  ↓
MI Object
```

Registryが管理する最低項目：

```text
mi_code
domain
object_class
subclass
instance
state
owner
created_at
version
status
parent_code
```

---

# 13. Collision Prevention

同一Codeを異なる意味に再利用してはならない。

```text
Code Collision
      ↓
Registry Validation
      ↓
REJECT
```

既存Codeの意味を変更する場合は、

```text
旧Code
 ↓
DEPRECATED
 ↓
新Code
```

とする。

既存履歴を書き換えない。

---

# 14. State Transition

Canonical transition：

```text
DRAFT
  ↓
VALIDATED
  ↓
APPROVED
  ↓
DEPRECATED
  ↓
ARCHIVED
```

許可されない直接遷移：

```text
DRAFT → ARCHIVED
DRAFT → APPROVED
```

などは、Governance Ruleとして禁止する。

---

# 15. Conflict

Agent AとAgent Bが同じ対象について異なるMI Objectを生成しても、Codeを上書きしない。

```text
                  ┌─ Object A
Input → Agents ───┤
                  └─ Object B
                       ↓
                 Conflict Event
                       ↓
                  Adjudication
                       ↓
                 Resolution Object
```

必要に応じて新しいMI Objectを発行する。

---

# 16. Knowledge Graph

MI CodeはKnowledge GraphのNode Identityとして使用可能。

```text
MIOS:PTH:EQUOL:...
       │
       ├── derived_from
       │       ↓
       │   MetabolicSnapshot
       │
       ├── related_to
       │       ↓
       │   Phenotype
       │
       ├── supported_by
       │       ↓
       │   Evidence
       │
       └── generated_by
               ↓
             Agent
```

Edge vocabulary自体はKnowledge Graph Specification v1.0で正式確定する。

---

# 17. JSON Representation

```json
{
  "mi_code": {
    "namespace": "MIOS",
    "domain": "PTH",
    "object_class": "EQUOL",
    "subclass": "FUNCTIONAL_CAPACITY",
    "instance": "001",
    "state": "VALIDATED"
  },
  "canonical_code": "MIOS:PTH:EQUOL:FUNCTIONAL_CAPACITY:001:VALIDATED",
  "schema_version": "1.0.0"
}
```

---

# 18. Registry Entry

```json
{
  "mi_code": "MIOS:PTH:EQUOL:FUNCTIONAL_CAPACITY:001",
  "namespace": "MIOS",
  "domain": "PTH",
  "object_class": "EQUOL",
  "subclass": "FUNCTIONAL_CAPACITY",
  "instance": "001",
  "state": "VALIDATED",
  "version": "1.0.0",
  "status": "active"
}
```

---

# 19. PBPE 7-Digitとの関係

PBPEの分類思想から学ぶことはできるが、MIOSでは同一仕様にはしない。

```text
PBPE
 └── Impact / Asset Classification

MIOS
 └── Metabolic Intelligence Classification
```

したがって、

**PBPE Code → MI Code**

という単純変換ではなく、

```text
PBPE Classification
        │
        │ conceptual reference
        ↓
MIOS MI Code Architecture
```

とする。

---

# 20. Agent Governance

Agentが自由に新しいCanonical Codeを作成してはいけない。

```text
Agent
  ↓
propose
  ↓
Registry
  ↓
validate
  ↓
issue
  ↓
MI Code
```

これにより、複数Agentを増やしても分類体系が崩れない。

---

# 21. Architecture

ここまでの仕様を統合すると、

```text
                 ┌──────────────────┐
                 │  Knowledge Graph │
                 └────────▲─────────┘
                          │
                 ┌────────┴─────────┐
                 │     MI Object    │
                 │     Schema       │
                 └────────▲─────────┘
                          │
                 ┌────────┴─────────┐
                 │      MI Code     │
                 │      Registry   │
                 └────────▲─────────┘
                          │
                 ┌────────┴─────────┐
                 │      Agents      │
                 └────────▲─────────┘
                          │
                 ┌────────┴─────────┐
                 │ Metabolic        │
                 │ Snapshot         │
                 └──────────────────┘
```

この時点で、以前構想された

> **「データ診断 → 解析 → 代謝経路解析 → フェノタイピング → 複数Agent → 管理Agent」**

を支える**共通識別・状態管理層**が定義されました。

---

# Repository Structure

今回の成果物として、GitHubでは以下を配置します。

```text
mios-specification-suite/
│
├── specifications/
│   ├── canonical-data-model/
│   ├── metabolic-snapshot/
│   ├── mi-object/
│   └── mi-code/
│       ├── MIOS_MI_Code_Standard_v1.0.md
│       └── mi_code.schema.json
│
├── registries/
│   ├── domain_registry.json
│   ├── object_class_registry.json
│   └── mi_code_registry.json
│
└── adr/
    └── ADR-MIC-001-MI-Code-Architecture.md
```

**Input**

```text
Metabolic Snapshot
MI Object
Knowledge Asset
Agent output
```

**Output**

```text
Canonical MI Code
Registry Entry
State
Reference
```

**依存関係**

```text
Canonical Data Model
        ↓
Metabolic Snapshot
        ↓
MI Object
        ↓
MI Code
```

**次に扱うスレッド**

`HealthBook MIOS / Architecture & Implementation`

---

# Next Architecture Step

次は予定どおり **MIOS Agent Registry v1.0** です。

ここで初めて、

```text
Agent ID
Agent Type
Capability
Input MI Code
Output MI Code
Dependencies
Authority
State
Version
```

を正式定義し、

```text
              Management / Orchestrator Agent
                         │
        ┌────────────────┼────────────────┐
        ↓                ↓                ↓
   Data Agent       Phenotype Agent   Pathway Agent
        ↓                ↓                ↓
        └────────────────┼────────────────┘
                         ↓
                  Disease-MI Agent
                         ↓
                  Solution Agent
```

という**MIOS Multi-Agent Architecture**へ接続します。