# MIOS Metabolic Snapshot Schema v1.0

**Document ID:** MIOS-MSS-001  
**Version:** 1.0.0  
**Status:** Draft for architecture freeze  
**Parent:** MIOS Canonical Data Model v1.0

## 1. Purpose

Metabolic Snapshotは、HealthBook MIOSが個体の一定時点の観測情報を、後続のPhenotyping、MI Engine、Pathway、Disease-MI、Solution Screening、Digital Twin処理へ渡すためのCanonical Input Objectである。

本仕様は「健康／疾病の最終判断」を定義しない。Snapshotは観測状態を構造化し、後続Agentが再利用できる境界を定義する。

## 2. Source-Aligned Domain Structure

既存HealthBook-MI設計で確認できるSnapshot marker domains：

```text
nutrition
gut_status
hormone_state
microbiome
musculo_fascial
symptoms
```

既存のHealthBook-MI Data Integration Layerでは、以下も統合対象として記載されている。

```text
Vitals
Blood Tests
Lifestyle
MBT55
Wearables
Tongue / Pulse / Questionnaire
```

したがって、v1.0ではこれらを「observation source / observation domain」として保持し、個別の臨床解釈をSnapshot Schemaへ埋め込まない。

## 3. Canonical Structure

```text
MetabolicSnapshot
│
├── identity
├── subject_ref
├── snapshot_at
├── source_refs
├── observations
│
├── domains
│   ├── nutrition
│   ├── gut_status
│   ├── hormone_state
│   ├── microbiome
│   ├── musculo_fascial
│   └── symptoms
│
├── laboratory
├── vitals
├── lifestyle
├── mbt55
├── wearables
│
├── phenotype_refs
├── prior_snapshot_refs
└── provenance
```

## 4. Common Metadata

Required:

```json
{
  "id": "SNAP-000001",
  "type": "MetabolicSnapshot",
  "schema_version": "1.0.0",
  "status": "draft"
}
```

Recommended:

```text
created_at
updated_at
subject_ref
snapshot_at
provenance
source_refs
observation_refs
```

## 5. Observation Boundary

Snapshotに格納される値はObservationとして扱う。

```text
Raw Observation
      ↓
Metabolic Snapshot
      ↓
Phenotype / MI Engine
```

重要な境界：

```text
Observation
≠
Phenotype
≠
Diagnosis
≠
Recommendation
```

Snapshot自体は因果推論結果を生成しない。

## 6. Laboratory

検査データは、基準範囲内／範囲外だけで情報を失わないよう、原値・単位・基準情報・時点・出典を保持できる構造とする。

例：

```json
{
  "observation_id": "LAB-000001",
  "code": "example_code",
  "value": 0,
  "unit": "example_unit",
  "reference_range": {
    "low": null,
    "high": null,
    "source": null
  },
  "observed_at": "ISO-8601"
}
```

本仕様では、特定検査項目の臨床閾値や診断基準を新規定義しない。

## 7. Nutrition

Nutrition domainは食事・栄養関連Observationへの参照を保持する。

```json
{
  "domain": "nutrition",
  "observation_refs": []
}
```

NutritionからPathwayを直接断定せず、後続Nutrition Agent / Pathway AgentがKnowledge Assetを参照して解析する。

## 8. Gut Status

Gut statusは、消化管関連の症状・状態・観察値への参照を保持する。

MBT55やmicrobiome情報と同一Objectに混在させず、参照関係で連結する。

## 9. Hormone State

Hormone stateはホルモン関連Observationへの参照を保持する。

既存HealthBook-MI資料では、Neuro-Endocrine、Hormone、EstrobolomeがMI reasoning domainとして扱われている。

ただし、Snapshotでは「ホルモン異常」という診断的意味を付与せず、観測値／問診／関連情報を保持する。

## 10. Microbiome

Microbiome domainは、微生物そのものだけでなく、後続のFunctional Layerで扱う機能情報への参照を許容する。

```text
Microbiome Observation
       ↓
Functional Capacity
       ↓
Metabolite Pathway
```

個別菌の存在だけから機能発現を断定しない。

## 11. Musculo-Fascial

既存設計に従い、筋骨格・筋膜関連の症状／Phenotypeへの入力領域を保持する。

ここでもSnapshotはObservation boundaryを維持する。

## 12. Symptoms

Symptomsは200-item questionnaire等から取得される症状Observationへの参照を保持する。

```text
Questionnaire
     ↓
Observation
     ↓
Snapshot.symptoms
     ↓
Phenotyping
```

## 13. MBT55

MBT55情報は独立domainとして保持し、一般Microbiome情報と混同しない。

```text
mbt55
├── observation_refs
├── product_refs
└── evidence_refs
```

既存資料でMBT55がSCFA、Bile Acid、Aromatic Amino Acid等のmetabolic modulesと関連付けられているため、SnapshotではMBT55に関する観測・使用状況・参照情報を保持し、代謝効果そのものは後続Engineの出力とする。

## 14. Wearables

Wearablesは時系列Observationのsourceとして扱う。

```text
wearable observation
       ↓
Snapshot reference
       ↓
Temporal analysis
```

Snapshotにすべてのraw time-seriesを複製することは必須としない。

## 15. Phenotype References

PhenotypeはSnapshotから生成されるため、Snapshot内部に結果を埋め込むのではなくreferenceで接続する。

```json
{
  "phenotype_refs": [
    "PHENO-000001"
  ]
}
```

## 16. Prior Snapshots

Longitudinal analysisのため、過去Snapshotへの参照を許可する。

```json
{
  "prior_snapshot_refs": [
    "SNAP-000000"
  ]
}
```

Digital TwinはSnapshotの履歴を利用して形成される。

## 17. Provenance

すべての重要Observationについて、可能な範囲で以下を保持する。

```text
source
source_type
acquired_at
entered_by
transformation
validation_status
```

## 18. State

Snapshot lifecycle:

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

`validated`は構造・データ整合性が確認された状態であり、臨床的妥当性を意味しない。

## 19. JSON Schema

Canonical JSON Schemaでは以下を必須とする。

```text
id
type
schema_version
status
subject_ref
snapshot_at
```

domain fieldsは存在しない場合も許容する。

## 20. Validation Layers

```text
1. JSON Syntax
        ↓
2. JSON Schema
        ↓
3. Object Integrity
        ↓
4. Registry Reference
        ↓
5. Provenance
        ↓
6. Domain Validation
```

## 21. Example

```json
{
  "id": "SNAP-000001",
  "type": "MetabolicSnapshot",
  "schema_version": "1.0.0",
  "status": "validated",
  "subject_ref": "PERSON-000001",
  "snapshot_at": "2026-08-23T00:00:00+09:00",
  "domains": {
    "nutrition": {
      "observation_refs": []
    },
    "gut_status": {
      "observation_refs": []
    },
    "hormone_state": {
      "observation_refs": []
    },
    "microbiome": {
      "observation_refs": []
    },
    "musculo_fascial": {
      "observation_refs": []
    },
    "symptoms": {
      "observation_refs": []
    }
  },
  "laboratory": {
    "observation_refs": []
  },
  "vitals": {
    "observation_refs": []
  },
  "lifestyle": {
    "observation_refs": []
  },
  "mbt55": {
    "observation_refs": []
  },
  "wearables": {
    "observation_refs": []
  },
  "phenotype_refs": [],
  "prior_snapshot_refs": [],
  "provenance": []
}
```

## 22. Architecture Decision

Metabolic Snapshot v1.0は、

```text
DATA INTAKE
    ↓
CANONICAL SNAPSHOT
    ↓
INTELLIGENCE PROCESSING
```

の境界を固定する。

SnapshotにAI推論結果、Disease判定、Treatment Recommendationを直接混在させない。

## 23. Next Contract

次の実装契約は **MI Object Schema v1.0**。

理由：

```text
Metabolic Snapshot
      ↓
MI Object
      ↓
Agent-to-Agent communication
```

この順序で初めて、複数Agentを同一データ契約で接続できる。
