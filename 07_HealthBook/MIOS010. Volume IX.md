# HealthBook–PMOS Master Plan

## Volume IX

# MIOS Knowledge Assets & Library Architecture

### Version 1.0 (English)

---

# 1. Purpose

The MIOS Knowledge Assets & Library Architecture defines the standardized knowledge infrastructure that powers every reasoning process within the Metabolic Intelligence Operating System (MIOS).

Unlike conventional healthcare platforms that depend primarily on Large Language Models or static medical databases, MIOS separates **knowledge assets** from **reasoning engines**.

Scientific knowledge is organized into structured, version-controlled libraries that can evolve independently from AI models.

The Knowledge Assets become the permanent scientific memory of the MIOS ecosystem.

---

# 2. Design Philosophy

The architecture follows six principles.

- Knowledge is a reusable asset.
- Scientific evidence is independently versioned.
- Every knowledge object has semantic meaning.
- Libraries evolve without changing AI architecture.
- Knowledge is machine-readable before becoming human-readable.
- Every reasoning process references structured knowledge assets.

Knowledge Assets therefore become the foundation of explainable metabolic intelligence.

---

# 3. Knowledge Asset Architecture

The MIOS Knowledge Library is organized into five layers.

```
Scientific Sources

↓

Knowledge Assets

↓

JSON Libraries

↓

Knowledge Graph

↓

Metabolic Intelligence Engine
```

Each layer has independent lifecycle management.

---

# 4. Core Knowledge Asset Categories

Version 1.0 defines the following core libraries.

|Library|Purpose|
|---|---|
|Disease Library|Disease knowledge|
|Phenotype Library|Phenotype definitions|
|Metabolic Pathway Library|Metabolic pathways|
|Biomarker Library|Laboratory biomarkers|
|Nutrition Library|Nutritional science|
|Microbiome Library|Gut microbiome knowledge|
|Hormone Library|Endocrine regulation|
|ATP Library|Cellular energy metabolism|
|MBT55 Functional Library|MBT55 biological functions|
|Kampo Metabolic Library|Kampo metabolism|
|Animal Medicine Library|Animal-derived medicinal resources|
|Intervention Library|Intervention knowledge|
|Outcome Library|Clinical outcomes|

Every library is independently maintained.

---

# 5. Disease Library

The Disease Library standardizes disease knowledge.

Version 1.0 includes:

- 137 Disease Matrix
- Disease Codes
- Disease Relationships
- Associated Phenotypes
- Related Biomarkers
- Associated Metabolic States
- Confidence Levels

Diseases are represented as semantic objects rather than diagnostic labels.

---

# 6. Phenotype Library

The Phenotype Library contains standardized phenotype definitions.

Each phenotype includes:

- Phenotype Code
- Functional Description
- Clinical Characteristics
- Observation Rules
- Confidence Rules
- Related States

Phenotypes are reusable across all MIOS applications.

---

# 7. Metabolic Pathway Library

The Pathway Library represents biological pathways.

Representative pathways include:

- Glycolysis
- TCA Cycle
- Fatty Acid Oxidation
- Amino Acid Metabolism
- Short-Chain Fatty Acid Production
- Bile Acid Metabolism
- Urolithin Production
- Equol Production
- ATP Synthesis

Each pathway becomes a semantic node within the Knowledge Graph.

---

# 8. MBT Knowledge Libraries

MIOS introduces dedicated knowledge assets unavailable in conventional healthcare systems.

Version 1.0 includes:

- MBT55 Functional Library
- MBT Kampo Metabolic Library
- Animal Medicine Library
- Nutritional Cascade Library
- Hypercycle Library
- Biosecurity Library

These libraries represent biological functions rather than pharmaceutical products.

---

# 9. JSON Library Standard

Every library is stored using standardized JSON schemas.

Each Knowledge Object contains:

- Knowledge ID
- Name
- Definition
- Category
- Ontology Reference
- Evidence References
- Version
- Relationships
- Confidence

JSON becomes the canonical storage format.

---

# 10. Library Registry

Every library is registered within the MI Registry.

Registry metadata includes:

- Library ID
- Version
- Owner
- Validation Status
- Dependencies
- Release Date
- Change History

Registry management guarantees traceability.

---

# 11. Knowledge Versioning

Scientific knowledge changes continuously.

Every library therefore follows semantic versioning.

Example:

```
Disease Library

v1.0

↓

v1.1

↓

v2.0
```

Previous versions remain permanently available.

---

# 12. Relationship with AI Agents

AI Agents never contain scientific knowledge internally.

Instead they retrieve structured knowledge from Knowledge Assets.

Example:

```
Phenotype Agent

↓

Phenotype Library

↓

Knowledge Graph

↓

Reasoning
```

This architecture separates intelligence from knowledge.

---

# 13. Relationship with HealthBook

HealthBook serves as the first reference implementation of the MIOS Knowledge Asset Architecture.

The platform integrates:

- 200 Questionnaire Library
- 137 Disease Library
- Metabolic Pathway Library
- Nutrition Library
- MBT55 Functional Library
- MBT Kampo Metabolic Library
- Animal Medicine Library
- Hormone Library
- Biomarker Library
- ATP Library
- Knowledge Graph

Together these libraries provide the scientific foundation for metabolic reasoning.

---

# 14. GitHub Repository Architecture

The Knowledge Assets are managed through the dedicated repository:

```
healthbook-json-library
```

Representative structure:

```
healthbook-json-library/

├── disease/
├── phenotype/
├── pathway/
├── biomarker/
├── nutrition/
├── microbiome/
├── hormone/
├── atp/
├── mbt55/
├── kampo/
├── animal-medicine/
├── intervention/
├── ontology/
├── schema/
├── registry/
└── version/
```

Every library follows identical governance rules, schema validation, and semantic version control.

---

# 15. Expected Outcome

The MIOS Knowledge Assets & Library Architecture transforms scientific knowledge into structured computational assets.

Rather than embedding knowledge inside AI models, MIOS manages biological intelligence through reusable, version-controlled libraries connected by the Knowledge Graph.

This architecture enables transparent reasoning, collaborative AI development, reproducible scientific updates, and long-term scalability across HealthBook, AGRIX, PBPE, and the broader PMOS ecosystem.

**End of Volume IX (English)**

---

# HealthBook-PMOS総合計画書

## 第9巻

# MIOS Knowledge Assets & Library アーキテクチャ

### Version 1.0（日本語版）

---

# 1. 目的

MIOS Knowledge Assets & Library Architectureは、Metabolic Intelligence Operating System（MIOS）の知識基盤を標準化するためのアーキテクチャである。

MIOSでは、大規模言語モデル（LLM）の内部知識や固定的な医療データベースに依存するのではなく、**科学知識そのものを独立したKnowledge Assetとして管理**する。

Knowledge Assetsは、AIエージェント、Knowledge Graph、Metabolic Intelligence Engineが共通利用する「科学的知識資産」であり、HealthBook Platform全体の長期的な知識基盤となる。

---

# 2. 基本設計思想

Knowledge Assetsは以下の6つの原則に従う。

- 知識は再利用可能な資産である
- 科学的根拠は独立して管理する
- すべての知識は意味構造を持つ
- ライブラリーはAIとは独立して進化する
- 人が読む前にAIが理解できる構造を持つ
- すべての推論はKnowledge Assetsを参照する

知識はモデル内部ではなく、管理可能な資産として蓄積される。

---

# 3. Knowledge Assets全体構造

Knowledge Assetsは5層構造で管理する。

```
Scientific Sources

↓

Knowledge Assets

↓

JSON Libraries

↓

Knowledge Graph

↓

Metabolic Intelligence Engine
```

各層は独立して更新できる。

Knowledge Assetsの更新によってAIアーキテクチャを変更する必要はない。

---

# 4. Core Knowledge Assets

Version 1.0では以下を標準ライブラリーとして定義する。

|ライブラリー|内容|
|---|---|
|Questionnaire Library|200項目問診|
|Disease Library|137疾病リスクマトリクス|
|Phenotype Library|フェノタイプ定義|
|Metabolic Pathway Library|代謝経路|
|Biomarker Library|血液・尿検査|
|Nutrition Library|栄養学|
|Microbiome Library|腸内細菌|
|Hormone Library|ホルモン・内分泌|
|ATP Library|ATP・ミトコンドリア|
|MBT55 Functional Library|MBT55機能|
|MBT Kampo Metabolic Library|MBT漢方代謝|
|Animal Medicine Library|動物生薬|
|Nutritional Cascade Library|栄養カスケード|
|Hypercycle Library|MBT55ハイパーサイクル|
|Biosecurity Library|バイオセキュリティ|
|Intervention Library|介入方法|
|Outcome Library|改善結果|

各ライブラリーは独立したKnowledge Assetとして管理する。

---

# 5. Disease Library

Disease Libraryは137疾病を標準化する。

保持項目は以下とする。

- Disease Code
- 疾患名称
- 疾患定義
- 関連フェノタイプ
- 関連代謝状態
- 関連代謝経路
- 関連バイオマーカー
- 信頼度
- Evidence
- Version

疾患は診断名ではなく、代謝知識として管理される。

---

# 6. Phenotype Library

Phenotype Libraryはフェノタイピングの標準定義を保持する。

各Phenotype Objectは以下を持つ。

- Phenotype Code
- 定義
- 判定条件
- 関連Observation
- 関連State
- Confidence Rule
- Evidence

HealthBook全体で共通利用される。

---

# 7. Metabolic Pathway Library

代謝経路ライブラリーは人体代謝を構造化する。

対象例は以下である。

- 解糖系
- TCAサイクル
- 脂肪酸β酸化
- アミノ酸代謝
- 短鎖脂肪酸生成
- 胆汁酸代謝
- ウロリチンA生成
- エクオール生成
- ATP産生
- ミトコンドリア電子伝達系

各経路はPathway NodeとしてKnowledge Graphへ登録される。

---

# 8. MBT Knowledge Assets

HealthBook独自のKnowledge Assetsを以下とする。

- MBT55 Functional Library
- MBT漢方代謝ライブラリー
- 動物生薬ライブラリー
- 栄養カスケードライブラリー
- MBT55 Hypercycle Library
- Biosecurity Library

これらは医薬品データベースではなく、生物学的機能ライブラリーとして設計される。

---

# 9. JSON Library標準

すべてのKnowledge AssetsはJSONで管理する。

標準項目は以下とする。

- Knowledge ID
- Name
- Category
- Description
- Ontology
- Evidence
- Relationships
- Version
- Confidence
- Source

JSONはKnowledge Assetの正本（Single Source of Truth）となる。

---

# 10. Knowledge Registry

Knowledge Registryでは全ライブラリーを管理する。

管理項目は以下である。

- Library ID
- Version
- Owner
- Validation Status
- Dependencies
- Release Date
- Change History

RegistryはKnowledge Assetsのガバナンスを担う。

---

# 11. バージョン管理

Knowledge AssetsはSemantic Versioningを採用する。

例

```
Disease Library

v1.0

↓

v1.1

↓

v1.2

↓

v2.0
```

旧バージョンは削除せず保持する。

これにより、過去の解析結果も再現できる。

---

# 12. AIエージェントとの関係

AIエージェントは科学知識を内部に保持しない。

必要な知識をKnowledge Assetsから取得する。

標準フローは以下である。

```
Phenotype Agent

↓

Phenotype Library

↓

Knowledge Graph

↓

Reasoning Engine
```

AIと知識を分離することで、ライブラリー更新時にもAIの再設計を不要とする。

---

# 13. HealthBookとの関係

HealthBook Platformは、MIOS Knowledge Assets Architectureの最初の実装システムとなる。

HealthBookでは以下のライブラリーを統合利用する。

- 200項目問診ライブラリー
- 137疾病ライブラリー
- フェノタイプライブラリー
- 代謝経路ライブラリー
- 栄養ライブラリー
- 腸内細菌ライブラリー
- ホルモンライブラリー
- ATPライブラリー
- MBT55 Functional Library
- MBT漢方代謝ライブラリー
- 動物生薬ライブラリー
- 栄養カスケードライブラリー
- Hypercycle Library
- Biosecurity Library

これらがHealthBookの科学的推論基盤を構成する。

---

# 14. GitHubリポジトリ構造

Knowledge Assetsは専用リポジトリで管理する。

```
healthbook-json-library/

├── questionnaire/
├── disease/
├── phenotype/
├── pathway/
├── biomarker/
├── nutrition/
├── microbiome/
├── hormone/
├── atp/
├── mbt55/
├── kampo/
├── animal-medicine/
├── nutritional-cascade/
├── hypercycle/
├── biosecurity/
├── intervention/
├── ontology/
├── schema/
├── registry/
└── version/
```

すべてのライブラリーは共通JSONスキーマ、共通Ontology、共通Version管理ルールに従う。

---

# 15. MIOS独自の「Knowledge Assets Platform」

MIOSの独自性は、**AIではなく「知識そのもの」を資産化する点**にある。

HealthBookでは、137疾病、200項目問診、フェノタイピング、代謝経路、MBT55ハイパーサイクル、栄養カスケード、MBT漢方代謝ライブラリー、動物生薬ライブラリー、ATP代謝、ホルモン、腸内細菌などを、それぞれ独立したKnowledge Assetとして管理する。

AIエージェントはこれらのKnowledge Assetsを組み合わせて推論を行い、新しい知識が追加された場合でも、ライブラリーの更新のみで対応できる。

---

# 16. 到達目標

MIOS Knowledge Assets & Library Architectureは、科学知識をAIモデルから切り離し、**構造化・バージョン管理・再利用可能なKnowledge Asset**として管理するための標準仕様である。

Knowledge AssetsはKnowledge Graph、Metabolic Intelligence Engine、State Engine、およびマルチAIエージェントの共通知識基盤として機能し、HealthBook Platformにおける説明可能な代謝推論を支える。

さらに、この知識資産基盤はHealthBookに留まらず、AGRIXの土壌・植物代謝ライブラリー、PBPEのPlanetary Knowledge Assetsへと拡張され、PMOS全体の共通ナレッジ基盤として発展する。

**（第9巻 日本語版 完了）**

[[MIOS011. Volume X]]
