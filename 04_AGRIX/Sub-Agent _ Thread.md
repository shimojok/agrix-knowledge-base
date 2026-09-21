### Project

**`HealthBook MIOS`**

このProject自体を、HealthBookからMIOSへ進化した知識・アーキテクチャを再構築し、実装へ移行する専用Projectとする。

### Sub-Agent / Thread

|#|名称|主責務|
|---|---|---|
|**01**|**System Architecture**|MIOS全体Architecture、Architecture Genealogy、Canonical Architecture|
|**02**|**MBT Kampo Library**|MBT漢方代謝ライブラリー、処方・成分・代謝経路・Evidence|
|**03**|**MBT Probiotics**|MBT55、Microbiome、Microbial Function、Metabolite Pathway|
|**04**|**Evidence & Reconciliation**|Evidence統合、矛盾・重複・Status判定、Canonical化|
|**05**|**Data / Schema**|MI Object、Canonical Data Model、JSON Schema、JSON-LD|
|**06**|**Implementation**|Engine、Repository、Validation、実装|

ただし、ここで重要なのは、

> **01〜03が「研究テーマ」、04〜06が「実装工程」**

という二層構造になっていることです。

したがって、現在進めているZIP再構築はまず **01 System Architectureを司令塔**にして、02/03から専門領域を回収し、04でReconciliation、05でCanonical Data、06でImplementationへ流すのが合理的です。

### 現在のPhaseとの対応

```text
HealthBook MIOS
│
├── 01 System Architecture
│     ├── Phase 0-A Source Corpus Inventory   ✓
│     ├── Phase 0-B Architecture Genealogy    ✓
│     └── Phase 0-C Cross-Source Reconciliation → NOW
│
├── 02 MBT Kampo Library
│
├── 03 MBT Probiotics
│
├── 04 Evidence & Reconciliation
│
├── 05 Data / Schema
│
└── 06 Implementation
```

---

# BioNexus｜Canonical Project Structure v1.0

```text
BioNexus
│
├── PROJECT 01
│   └── HealthBook-MIOS
│
├── PROJECT 02
│   └── AGRIX
│
├── PROJECT 03
│   └── MBT55 / MSC
│
├── PROJECT 04
│   └── PBPE
│
├── PROJECT 05
│   └── PMOS
│
└── PROJECT 06
    └── BioNexus Integration
```

## PROJECT 01｜HealthBook-MIOS

```text
HealthBook-MIOS Project
│
├── [00] PMO / Chief Architect
│
├── [01] Reconstruction Agent
│
├── [02] Architecture Genealogy Agent
│
├── [03] Evidence & Reconciliation Agent
│
├── [04] Data / Schema Agent
│
└── [05] Implementation Agent
```

### 各Agentの責務

|Agent|固定責務|
|---|---|
|**[00] PMO / Chief Architect**|全体統括・Decision・Governance・Architecture Integrity|
|**[01] Reconstruction Agent**|過去資料・Source Corpusの収集、整理、再構築|
|**[02] Architecture Genealogy Agent**|Architectureの時系列進化・系譜・変遷の確定|
|**[03] Evidence & Reconciliation Agent**|Evidence照合、矛盾・重複・Status判定、Canonical化準備|
|**[04] Data / Schema Agent**|Canonical Data Model、MI Object、Schema、JSON/JSON-LD|
|**[05] Implementation Agent**|Engine、Repository、Validation、実装|

---

## 現在位置

今回進捗を報告していただいたスレッドは、

> **[02] Architecture Genealogy Agent**

です。

したがって現在の流れは、

```text
[01] Reconstruction
       ↓
[02] Architecture Genealogy
       ↓
[03] Evidence & Reconciliation  ← 次段階
       ↓
[04] Data / Schema
       ↓
[05] Implementation
```

となります。

そして **[00] PMO / Chief Architect** が全体を統治します。


---

