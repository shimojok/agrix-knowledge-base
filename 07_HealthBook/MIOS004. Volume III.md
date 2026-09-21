# HealthBook–PMOS Master Plan

## Volume III

# MIOS Knowledge Architecture

### Version 1.0 (English)

---

# 1. Purpose

The MIOS Knowledge Architecture defines how biological knowledge is represented, managed, connected, validated, and consumed throughout the Metabolic Intelligence Operating System.

Rather than storing information as isolated datasets, MIOS organizes all scientific knowledge into interoperable knowledge assets governed by common semantic standards.

The objective is to transform distributed biological information into a reusable intelligence infrastructure.

---

# 2. Knowledge Architecture Overview

The knowledge architecture consists of seven logical components.

```
Scientific Knowledge

↓

Knowledge Assets

↓

Ontology

↓

Knowledge Graph

↓

MI Registry

↓

Reasoning Engine

↓

AI Agents
```

Each component performs a single responsibility while remaining independent from implementation technologies.

---

# 3. Knowledge Asset Model

Every scientific resource is managed as a Knowledge Asset.

A Knowledge Asset is defined as a version-controlled, machine-readable, semantically identifiable unit of biological knowledge.

Each asset shall include:

- Unique Identifier
- Version
- Source
- Scientific Domain
- Owner Repository
- Validation Status
- Ontology Reference
- Knowledge Graph Reference
- Evidence Level

Knowledge Assets are immutable once released.

Updates are published as new versions.

---

# 4. Knowledge Domains

MIOS Version 1.0 defines the following core knowledge domains.

|Domain|Description|
|---|---|
|Clinical|Disease models and clinical concepts|
|Phenotype|Questionnaire and phenotype definitions|
|Metabolism|Metabolic pathways and reactions|
|Nutrition|Nutrients and dietary components|
|Microbiome|Gut microbial taxonomy and functions|
|MBT55|Functional microbial library|
|Kampo|Kampo metabolic knowledge|
|Animal Medicine|Animal-derived medicinal resources|
|Hormone|Endocrine regulation|
|Energy|ATP and mitochondrial metabolism|
|Biomarker|Laboratory markers|
|Simulation|Intervention models|
|FHIR|Clinical interoperability|
|Ontology|Semantic vocabulary|
|Registry|MI Code definitions|

Each domain is maintained independently while remaining interoperable through standardized identifiers.

---

# 5. Repository Structure

Knowledge Assets are stored within the **healthbook-json-library** repository.

```
healthbook-json-library/

core/

clinical/

phenotype/

metabolism/

nutrition/

microbiome/

mbt/

kampo/

animal_medicine/

hormone/

energy/

biomarker/

simulation/

fhir/

ontology/

registry/

schema/

examples/
```

Each directory contains JSON resources, schema definitions, documentation, and validation examples.

---

# 6. Knowledge Asset Lifecycle

Every Knowledge Asset follows the same lifecycle.

```
Draft

↓

Scientific Review

↓

Technical Validation

↓

Ontology Mapping

↓

Knowledge Graph Registration

↓

Release

↓

Version Control

↓

Archive
```

Only released assets are available to production AI agents.

---

# 7. Ontology Layer

The ontology provides semantic consistency across all knowledge domains.

Every entity shall define:

- Identifier
- Preferred Name
- Synonyms
- Scientific Definition
- Parent Class
- Child Classes
- Relationships
- External References

Ontology definitions remain independent from application logic.

---

# 8. Knowledge Graph Layer

The Knowledge Graph integrates every Knowledge Asset into a unified semantic network.

Each graph element consists of:

**Node**

Represents biological entities.

Examples:

- Disease
- Symptom
- Metabolite
- Nutrient
- Hormone
- Microorganism
- MBT Function
- Kampo Formula

**Edge**

Represents semantic relationships.

Examples:

- activates
- inhibits
- produces
- consumes
- associated_with
- regulates
- predicts
- improves
- aggravates

All graph relationships are explicitly defined.

No implicit relationships are permitted.

---

# 9. MI Registry

Every semantic object receives a globally unique MI Identifier.

Examples include:

- Knowledge IDs
- Node IDs
- Edge IDs
- Agent IDs
- State IDs
- Evidence IDs
- Simulation IDs

Identifiers never change after publication.

Deprecated identifiers remain reserved.

---

# 10. Scientific Evidence

Every Knowledge Asset shall contain evidence metadata.

Minimum metadata includes:

- Scientific Source
- Evidence Category
- Evidence Version
- Publication Year
- Confidence Level
- Validation Status

Evidence metadata enables transparent reasoning and future scientific updates.

---

# 11. AI Consumption Model

AI Agents never access raw repositories directly.

Instead, the execution flow is:

```
Knowledge Assets

↓

Ontology

↓

Knowledge Graph

↓

Reasoning Engine

↓

AI Agents
```

This architecture guarantees that all agents operate on the same validated semantic model.

---

# 12. Versioning Policy

Every Knowledge Asset follows semantic versioning.

```
Major.Minor.Patch
```

Major versions indicate structural changes.

Minor versions indicate scientific expansion.

Patch versions indicate corrections without semantic modification.

Older versions remain reproducible.

---

# 13. Expected Outcome

The MIOS Knowledge Architecture establishes a standardized scientific foundation capable of supporting explainable metabolic intelligence.

Instead of embedding biological knowledge directly into application logic, MIOS separates scientific knowledge from software implementation through structured Knowledge Assets, Ontology, Knowledge Graph, and Registry services.

This architecture enables continuous scientific evolution while maintaining stable software behavior.

**End of Volume III (English)**

---

# HealthBook-PMOS総合計画書

## 第3巻

# MIOS ナレッジ・アーキテクチャ

### Version 1.0（日本語版）

---

# 1. 目的

MIOSナレッジ・アーキテクチャは、Metabolic Intelligence Operating System（MIOS）において、生物学的知識をどのように表現し、管理し、相互接続し、検証し、AIが利用するかを定義する標準仕様である。

MIOSでは、知識を単なるデータベースとして管理しない。

すべての科学的知識は、意味情報を保持したKnowledge Assetとして構造化され、Ontology、Knowledge Graph、MI Registryを介して統合される。

本仕様の目的は、分散した科学情報を再利用可能な代謝インテリジェンス基盤へ変換することである。

---

# 2. ナレッジ・アーキテクチャ全体構造

MIOSの知識基盤は、7つの論理コンポーネントで構成される。

```
Scientific Knowledge

↓

Knowledge Assets

↓

Ontology

↓

Knowledge Graph

↓

MI Registry

↓

Reasoning Engine

↓

AI Agents
```

各コンポーネントは単一責務を持ち、実装技術とは独立して管理される。

---

# 3. Knowledge Assetモデル

Knowledge Assetは、MIOSにおける最小の知識単位である。

Knowledge Assetとは、

**「バージョン管理され、機械可読であり、意味情報を持つ科学知識」**

として定義する。

各Knowledge Assetは、最低限以下の情報を保持する。

- Knowledge ID
- 名称
- バージョン
- 科学分野
- 管理リポジトリ
- 作成者
- 検証状態
- Ontology参照
- Knowledge Graph参照
- Evidence Level

公開済みKnowledge Assetは変更しない。

更新は新しいバージョンとして管理する。

---

# 4. 知識ドメイン

MIOS Version 1.0では、以下の知識ドメインを標準とする。

|知識ドメイン|内容|
|---|---|
|Clinical|137疾病リスクモデル|
|Phenotype|200項目問診・フェノタイプ定義|
|Metabolism|代謝経路・代謝反応|
|Nutrition|栄養ライブラリー|
|Microbiome|腸内細菌ライブラリー|
|MBT55|MBT55機能ライブラリー|
|Kampo|MBT漢方代謝ライブラリー|
|Animal Medicine|動物生薬ライブラリー|
|Hormone|ホルモン・内分泌|
|Energy|ATP・ミトコンドリア|
|Biomarker|血液・尿などのバイオマーカー|
|Simulation|介入シミュレーション|
|FHIR|医療データ連携|
|Ontology|意味定義|
|Registry|MI Code管理|

各ドメインは独立して保守されるが、共通識別子により相互接続される。

---

# 5. リポジトリ構造

Knowledge Assetは **healthbook-json-library** に保存する。

```
healthbook-json-library/

core/

clinical/

phenotype/

metabolism/

nutrition/

microbiome/

mbt/

kampo/

animal_medicine/

hormone/

energy/

biomarker/

simulation/

fhir/

ontology/

registry/

schema/

examples/
```

各フォルダには以下を格納する。

- JSONデータ
- JSON Schema
- ドキュメント
- サンプルデータ
- バリデーション定義

---

# 6. Knowledge Assetライフサイクル

Knowledge Assetは以下の手順で管理する。

```
Draft

↓

Scientific Review

↓

Technical Validation

↓

Ontology Mapping

↓

Knowledge Graph Registration

↓

Release

↓

Version Control

↓

Archive
```

公開版のみがHealthBook PlatformおよびAIエージェントから利用される。

---

# 7. Ontology層

Ontologyは知識全体の意味的一貫性を維持する。

各Ontologyエンティティは以下を定義する。

- Ontology ID
- 標準名称
- 同義語
- 科学的定義
- 上位概念
- 下位概念
- 関連概念
- 外部参照

Ontologyはアプリケーションから独立して管理される。

---

# 8. Knowledge Graph層

Knowledge GraphはKnowledge Assetを意味的に接続する推論基盤である。

Knowledge GraphはNodeとEdgeで構成される。

## Node

Nodeは生物学的実体を表現する。

例

- 疾患
- 症状
- 代謝産物
- 栄養素
- ホルモン
- 腸内細菌
- MBT55機能
- 漢方処方

## Edge

EdgeはNode間の意味的関係を表現する。

標準関係は以下とする。

- activates
- inhibits
- produces
- consumes
- regulates
- associated_with
- predicts
- improves
- aggravates

すべてのEdgeは明示的に定義する。

暗黙的な関係は保持しない。

---

# 9. MI Registry

MI RegistryはMIOS全体で利用される識別子を一元管理する。

対象は以下とする。

- Knowledge ID
- Node ID
- Edge ID
- Agent ID
- State ID
- Evidence ID
- Simulation ID

一度公開した識別子は変更しない。

廃止した識別子も再利用しない。

---

# 10. 科学的エビデンス

すべてのKnowledge AssetはEvidence情報を保持する。

最低限管理する項目は以下とする。

- 科学的情報源
- エビデンス区分
- エビデンスバージョン
- 発表年
- 信頼度
- 検証状態

Evidence情報により、推論の透明性と将来の知識更新を保証する。

---

# 11. AIによる知識利用モデル

AIエージェントはJSONファイルを直接参照しない。

標準的な知識利用フローは以下とする。

```
Knowledge Assets

↓

Ontology

↓

Knowledge Graph

↓

Reasoning Engine

↓

AI Agents
```

この構造により、すべてのAIエージェントは同一の意味体系と検証済み知識を利用する。

---

# 12. バージョン管理

Knowledge Assetはセマンティックバージョニングを採用する。

```
Major.Minor.Patch
```

- Major：構造変更
- Minor：知識追加・科学的拡張
- Patch：誤記修正・軽微修正

旧バージョンも再現可能な状態で保持する。

---

# 13. 到達目標

MIOSナレッジ・アーキテクチャは、説明可能な代謝インテリジェンスを実現するための知識基盤を提供する。

生物学的知識をアプリケーション内部へ埋め込むのではなく、Knowledge Asset、Ontology、Knowledge Graph、およびMI Registryとして独立管理することで、科学の進歩とソフトウェア実装を分離する。

この構造により、知識資産は継続的に進化できる一方で、HealthBook Platformや将来のMIOSアプリケーションは安定した推論基盤を維持できる。

**（第3巻 日本語版 完了）**

[[MIOS005. Volume IV]]
