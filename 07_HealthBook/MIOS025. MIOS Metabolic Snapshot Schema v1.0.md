はい、一直線の実装ルートで進めてください。

---

# Architecture

**一直線の実装ルートを継続し、次工程「MIOS Metabolic Snapshot Schema v1.0」を実文書＋JSON Schemaとして作成しました。**

今回の位置づけは明確です。

```text
MIOS Canonical Data Model v1.0
            │
            ▼
MIOS Metabolic Snapshot Schema v1.0  ← 今回
            │
            ▼
MIOS MI Object Schema v1.0
            │
            ▼
MIOS MI Code Standard v1.0
            │
            ▼
Agent Registry
            │
            ▼
Agent-to-Agent Protocol
            │
            ▼
Knowledge Graph Schema
            │
            ▼
Workflow DSL
            │
            ▼
Engines / Reference Implementation
```

既存HealthBook-MI資料で確認できるSnapshotの主要領域、

```text
nutrition
gut_status
hormone_state
microbiome
musculo_fascial
symptoms
```

をCanonical domainとして採用しています。

また、Data Integration Layerで既に示されている、

```text
Vitals
Blood Tests
Lifestyle
MBT55
Wearables
Tongue / Pulse / Questionnaire
```

をObservation sourceとして扱う構造にしました。

重要なのは、**SnapshotそのものにAIの診断・因果推論・Recommendationを混在させない**ことです。

```text
Observation
     ↓
Metabolic Snapshot
     ↓
Phenotype
     ↓
Metabolic State
     ↓
MI Object
```

というデータ境界を固定しました。

---

# Data Flow

今回のSchemaで、特に重要なのがこの境界です。

```text
┌─────────────────────────────┐
│       DATA INTAKE           │
│                             │
│ Questionnaire               │
│ Laboratory                  │
│ Vitals                      │
│ Lifestyle                   │
│ Wearables                   │
│ MBT55                       │
│ Symptoms                    │
└──────────────┬──────────────┘
               ↓
┌─────────────────────────────┐
│   METABOLIC SNAPSHOT         │
│                             │
│ nutrition                   │
│ gut_status                  │
│ hormone_state               │
│ microbiome                  │
│ musculo_fascial             │
│ symptoms                    │
└──────────────┬──────────────┘
               ↓
       ┌───────┴────────┐
       ↓                ↓
  Phenotyping       MI Engines
       ↓                ↓
       └───────┬────────┘
               ↓
          MI Object
               ↓
        Agent Network
```

これにより、ユーザーが最初に問題提起された

> 「血液検査の各項目が正常範囲でも、複数の症状・代謝偏位を統合して解析する」

というHealthBook MIOSの基本思想を、**データ構造として後続Agentに渡せる形**にしています。

ただし、今回のSchema自体が「正常値なのに異常」といった医学的結論を定義しているわけではありません。そこは後続のPhenotype / MI Engine / Pathway仕様で扱います。

---

# Repository Structure

今回の実ファイルです。

### Normative Specification

[MIOS_Metabolic_Snapshot_Schema_v1.0.md](sandbox:/mnt/data/MIOS_Metabolic_Snapshot_Schema_v1.0/MIOS_Metabolic_Snapshot_Schema_v1.0.md)

### JSON Schema

[mios_metabolic_snapshot.schema.json](sandbox:/mnt/data/MIOS_Metabolic_Snapshot_Schema_v1.0/mios_metabolic_snapshot.schema.json)

### Package

[MIOS_Metabolic_Snapshot_Schema_v1.0.zip](sandbox:/mnt/data/MIOS_Metabolic_Snapshot_Schema_v1.0.zip)

---

# Governance

今回、ハルシネーション防止のため、**既存資料にない医学的閾値や診断ルールは追加していません。**

例えばLaboratoryについては、

```text
raw value
unit
reference range
source
observed_at
```

を保持できる構造にしましたが、

> 「この数値ならこの疾患」

という新規ルールは定義していません。

また、既存資料で確認できる

```text
MI-AcetylCoA
MI-Estrobolome
MI-Mitochondria
```

などについても、Snapshotでは**観測・参照対象**として扱い、Score計算ロジックをここに混ぜていません。

これはArchitectureとして重要です。

```text
Schema
  ≠
Clinical Rule
  ≠
Inference Engine
  ≠
Recommendation
```

それぞれを分離します。

---

# 次工程

次は予定どおり、**MIOS MI Object Schema v1.0**です。

ここから一気に重要度が上がります。

```text
Metabolic Snapshot
        ↓
   MI Object
        ↓
┌───────┼────────┬────────┐
↓       ↓        ↓        ↓
Phenotype Pathway Disease  Solution
Agent    Agent    Agent    Agent
        ↓
  Management Agent
```

つまり、以前ご質問された

> **「PBPE 7桁コードのような共通コードをAgent間で渡し、管理Agentが全体を調整できるか」**

という構想を、次の **MI Object → MI Code → Agent Protocol** で実体化していきます。

**次工程は「MIOS MI Object Schema v1.0」に直ちに進みます。**