# HealthBook–PMOS Master Plan

## Volume VI

# MIOS State Engine & MI Code Architecture

### Version 1.0 (English)

---

# 1. Purpose

The MIOS State Engine defines the standard methodology for representing, tracking, evaluating, and predicting metabolic state transitions within the Metabolic Intelligence Operating System.

Rather than allowing each AI Agent to describe metabolic conditions using free-text or proprietary formats, MIOS establishes a unified state representation through standardized MI Codes.

The State Engine provides the common language that enables all AI Agents to collaborate deterministically.

---

# 2. Design Objective

The State Engine has four objectives.

1. Represent every metabolic state using standardized State Codes.
    
2. Track transitions between metabolic states over time.
    
3. Quantify evidence supporting each state.
    
4. Enable every AI Agent to communicate using identical semantic structures.
    

State information becomes a reusable computational object rather than a textual interpretation.

---

# 3. Fundamental Architecture

The State Engine consists of six logical layers.

```
Observation

↓

Phenotype

↓

Metabolic State

↓

State Transition

↓

Intervention

↓

Outcome
```

Every analysis performed within MIOS is represented through these six stages.

---

# 4. Observation Layer

The Observation Layer represents objective or subjective observations collected from the individual.

Observation sources include:

- Questionnaire
- Laboratory Data
- Medical History
- Nutrition Assessment
- Lifestyle Information
- Wearable Devices
- Imaging Results
- Clinical Examination

Each observation receives an Observation Code.

Observations never contain conclusions.

---

# 5. Phenotype Layer

The Phenotype Layer aggregates multiple observations into functional biological patterns.

Each phenotype includes:

- Phenotype Code
- Confidence Score
- Evidence References
- Observation References
- Associated Biological Systems

Multiple phenotypes may coexist simultaneously.

---

# 6. Metabolic State Layer

The Metabolic State Layer represents the current functional condition of the organism.

Representative state domains include:

- Energy
- Glucose
- Lipid
- Amino Acid
- Hormone
- Microbiome
- Immune
- Inflammation
- Oxidative Stress
- Detoxification

Every state receives a unique State Code.

The collection of State Codes forms the Metabolic State Vector.

---

# 7. State Transition Layer

The State Transition Layer records changes between metabolic states.

Examples include:

- Stable
- Improving
- Declining
- Compensating
- Recovering
- Progressive
- Unknown

Transitions are always time-dependent.

Historical state trajectories remain preserved.

---

# 8. Intervention Layer

Every intervention receives an Intervention Code.

Representative intervention domains include:

- Nutrition
- Lifestyle
- Exercise
- Sleep
- Probiotics
- Prebiotics
- MBT55
- Kampo
- Animal Medicine

An intervention never modifies a State directly.

Instead, it proposes an expected transition.

---

# 9. Outcome Layer

The Outcome Layer evaluates whether the expected transition occurred.

Each outcome contains:

- Outcome Code
- Expected State
- Observed State
- Difference Score
- Confidence Score
- Evidence References

Outcomes contribute to future learning.

---

# 10. MI Code Standard

Every computational object within MIOS receives an MI Code.

Standard categories include:

|Prefix|Object|
|---|---|
|OBS|Observation|
|PHE|Phenotype|
|STA|State|
|PAT|Pathway|
|INT|Intervention|
|OUT|Outcome|
|EVD|Evidence|
|AGT|Agent|
|SIM|Simulation|
|REP|Report|

MI Codes are globally unique.

Once assigned, they never change.

---

# 11. State Object

Every State Object contains:

- State Code
- Domain
- Biological Description
- Evidence References
- Confidence Score
- Timestamp
- Version
- Source Agents

State Objects become nodes within the Knowledge Graph.

---

# 12. Communication Model

Agents exchange State Objects rather than narrative conclusions.

Standard communication sequence:

```
Observation

↓

Phenotype

↓

State

↓

Evidence

↓

Simulation

↓

Recommendation
```

This guarantees reproducible reasoning across all implementations.

---

# 13. Registry Management

The MI Registry maintains:

- MI Codes
- State Definitions
- Version History
- Deprecation Status
- Relationships
- Ontology Mapping

Registry synchronization is mandatory before every software release.

---

# 14. Relationship with Knowledge Graph

Every State Object becomes a Knowledge Graph node.

Edges describe:

- causes
- activates
- suppresses
- predicts
- improves
- worsens
- regulates

State transitions are therefore represented as graph evolution rather than text.

---

# 15. Expected Outcome

The MIOS State Engine establishes a universal semantic language for metabolic intelligence.

Instead of exchanging textual interpretations, AI Agents exchange standardized State Objects identified by immutable MI Codes.

This architecture enables deterministic communication, explainable reasoning, longitudinal metabolic modeling, and reusable computational knowledge across every MIOS application.

**End of Volume VI (English)**

---

# HealthBook-PMOS総合計画書

## 第6巻

# MIOS State Engine & MI Code アーキテクチャ

### Version 1.0（日本語版）

---

# 1. 目的

MIOS State Engineは、Metabolic Intelligence Operating System（MIOS）において、人体の代謝状態を統一的な形式で表現・追跡・解析・予測するための標準仕様である。

従来の医療AIでは、「脂質代謝異常」「インスリン抵抗性」などの解釈がAIごとに異なり、相互利用が困難である。

MIOSでは、すべての代謝状態を**MI Code**によって表現し、AIエージェント間で共通の意味を持つ「State Object」として交換する。

State Engineは、MIOS全体の「代謝言語（Metabolic Language）」として機能する。

---

# 2. 基本目的

State Engineは次の4つの目的を持つ。

1. すべての代謝状態をState Codeとして標準化する。
    
2. 時系列に沿って代謝状態の変化を記録する。
    
3. 各状態に対するEvidenceを管理する。
    
4. AIエージェント間の通信をMI Codeによって統一する。
    

これにより、代謝状態は自然言語ではなく、再利用可能な計算オブジェクトとして扱われる。

---

# 3. State Engine全体構造

MIOSでは、人体の代謝を以下の6層で表現する。

```
Observation

↓

Phenotype

↓

Metabolic State

↓

State Transition

↓

Intervention

↓

Outcome
```

この6層は、すべての解析プロセスで共通に利用される。

---

# 4. Observation Layer

Observation Layerは、利用者から取得した事実データを管理する。

入力対象は以下とする。

- 200項目問診
- 血液検査
- 尿検査
- 身体計測
- 栄養調査
- 食生活
- 睡眠
- 運動
- 医療記録
- FHIRデータ
- ウェアラブルデータ
- 腸内細菌検査

Observationには解釈を含めない。

すべてObservation Code（OBS）を付与する。

例

```
OBS-000231
空腹時血糖 = 108 mg/dL
```

---

# 5. Phenotype Layer

Phenotype LayerではObservationを統合し、生体機能の特徴を抽出する。

Phenotype Objectには以下を保持する。

- Phenotype Code
- Confidence Score
- Observation Reference
- Evidence Reference
- 関連する生体システム

例

```
PHE-00451

軽度インスリン抵抗性フェノタイプ

Confidence：0.87
```

一人の利用者は複数のPhenotypeを同時に持つことができる。

---

# 6. Metabolic State Layer

Metabolic State Layerは現在の代謝状態を表現する。

代表的なState Domainは以下とする。

- エネルギー代謝
- 糖代謝
- 脂質代謝
- タンパク質代謝
- アミノ酸代謝
- 腸内代謝
- ATP産生
- ミトコンドリア機能
- ホルモン代謝
- 免疫代謝
- 炎症
- 酸化ストレス
- 解毒機能

各状態にはState Codeを付与する。

例

```
STA-ENERGY-00231

ATP産生低下
```

```
STA-GLUCOSE-00124

糖代謝補償状態
```

すべてを統合したものをMetabolic State Vectorと呼ぶ。

---

# 7. State Transition Layer

State Transition Layerは代謝状態の変化を記録する。

標準状態は以下とする。

- Stable
- Improving
- Declining
- Progressive
- Recovering
- Compensating
- Unknown

例

```
STA-GUT-0012

Compensating

↓

Improving
```

時間軸を保持することで、代謝変化を追跡できる。

---

# 8. Intervention Layer

Intervention Layerでは改善介入を管理する。

対象は以下とする。

- 栄養改善
- 運動
- 睡眠改善
- プロバイオティクス
- プレバイオティクス
- MBT55
- MBT漢方
- 動物生薬
- 生活習慣改善

各介入にはIntervention Codeを付与する。

例

```
INT-MBT-00021

MBT55導入
```

介入はStateを書き換えない。

期待されるState Transitionのみを定義する。

---

# 9. Outcome Layer

Outcome Layerでは介入後の結果を評価する。

保持項目は以下とする。

- Outcome Code
- 期待State
- 実測State
- 差分スコア
- Confidence
- Evidence

例

```
OUT-00451

Expected

STA-GUT-0008

↓

Observed

STA-GUT-0010

Improved
```

OutcomeはLearning Engineへ蓄積される。

---

# 10. MI Code体系

MIOSでは、すべてのオブジェクトにMI Codeを付与する。

|Prefix|対象|
|---|---|
|OBS|Observation|
|PHE|Phenotype|
|STA|State|
|PAT|Pathway|
|INT|Intervention|
|OUT|Outcome|
|EVD|Evidence|
|AGT|Agent|
|SIM|Simulation|
|REP|Report|

MI Codeは世界で一意であり、一度発行したコードは変更しない。

---

# 11. State Object

State ObjectはState Engineの最小単位である。

State Objectは以下を保持する。

- State Code
- Domain
- Biological Description
- Evidence Reference
- Confidence
- Timestamp
- Version
- Source Agent

State ObjectはKnowledge GraphのNodeとなる。

---

# 12. エージェント通信モデル

AIエージェントは自然言語では通信しない。

State Objectを交換する。

標準通信フローは以下とする。

```
Observation

↓

Phenotype

↓

State

↓

Evidence

↓

Simulation

↓

Recommendation
```

この方式により、すべての推論は再現可能となる。

---

# 13. MI Registry

MI Registryでは以下を管理する。

- MI Code
- State定義
- バージョン履歴
- 廃止履歴
- Ontology対応
- Node対応
- Edge対応

ソフトウェアリリース時にはRegistryとの同期を必須とする。

---

# 14. Knowledge Graphとの統合

State ObjectはKnowledge Graph上ではNodeとして登録される。

Node間は以下のEdgeで接続される。

- causes
- activates
- inhibits
- regulates
- predicts
- improves
- worsens
- produces
- consumes

State Transitionは、Knowledge Graphの時間的変化として管理される。

---

# 15. MIOS独自の「State Intelligence」

MIOSの最大の特徴は、**疾患を診断単位とせず、「代謝状態（Metabolic State）」をAIエージェント間で共有する共通言語とした点**にある。

各AIエージェントは診断名ではなく、

- Observation
- Phenotype
- State
- Pathway
- Evidence
- Intervention
- Outcome

という一貫した情報構造で推論を行う。

これにより、フェノタイピング、代謝経路解析、腸内環境解析、ホルモン解析、MBT55機能解析、MBT漢方代謝解析など、異なる専門領域のAIエージェントが同じ「代謝状態」を共有しながら協調推論を実現できる。

---

# 16. 到達目標

MIOS State Engine & MI Codeアーキテクチャは、人体代謝を「状態（State）」として表現・管理・共有するための共通基盤を提供する。

従来の医療AIが診断結果や個別データの解析を中心としてきたのに対し、MIOSでは**代謝状態・状態遷移・介入・結果を一貫したMI Code体系で管理**し、Knowledge Graphおよびマルチエージェント・アーキテクチャと連携することで、説明可能かつ再利用可能な代謝インテリジェンスを実現する。

このState Engineは、HealthBook Platformのみならず、将来的にはAGRIX、PBPEを含むPMOS全体で共通利用される「代謝状態オペレーティングシステム」の中核仕様となる。

**（第6巻 日本語版 完了）**

[[MIOS008. Volume VII]]
