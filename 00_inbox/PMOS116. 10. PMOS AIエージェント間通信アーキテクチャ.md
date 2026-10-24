# `/09-Documents/PMOS-Architecture-Book/10-PMOS-AI-Agent-Communication-Architecture.md`

## 10. PMOS AIエージェント間通信アーキテクチャ

### 10.1 基本方針

PMOSのAIエージェントは、個別のLLMアプリケーションとして独立して動作するのではなく、共通のKnowledge Architectureを介して協調する。

エージェント間通信において重要なのは、自然言語そのものではなく、**「何の知識を、どのVersionで、どのRepositoryから取得し、どの目的で利用しているか」**を機械的に追跡できることである。

そのためPMOSでは、自然言語による会話の上に、構造化されたSemantic Communication Layerを配置する。

```text
Natural Language
       │
       ▼
Semantic Communication
       │
       ├── Knowledge ID
       ├── Repository ID
       ├── Domain
       ├── Asset Version
       ├── Task ID
       └── Relationship
       │
       ▼
Knowledge Graph
       │
       ▼
AI Agents
```

---

## 10.2 Communication Layer

AI Agent間通信は五つの層で構成する。

```text
Layer 5  Executive Intent

Layer 4  Agent Task

Layer 3  Semantic Context

Layer 2  Knowledge Reference

Layer 1  Transport
```

Transport LayerはAPI、JSON、Message Queueなどの通信方式を担当する。

Knowledge Reference LayerはKnowledge IDやRepository IDを指定する。

Semantic Context LayerはOntology、Domain、Relationshipを指定する。

Agent Task Layerは実行すべきタスクを定義する。

Executive Intent Layerは最終的な意思決定目的を表す。

これにより、通信方式と知識意味論を分離する。

---

## 10.3 Agent Message

PMOSのAgent Messageは、少なくとも以下の情報を持つ。

```text
Message ID
Task ID
Sender Agent
Receiver Agent
Knowledge References
Semantic Context
Requested Operation
Expected Output
Version
Timestamp
Trace ID
```

Knowledge ReferencesにはKnowledge IDを指定する。

Agentはファイル名やURLだけを通信識別子として利用しない。

---

## 10.4 Knowledge IDによる通信

例えばAGRIX AgentがM3 Agentへ情報を要求する場合、自然言語だけで

「土壌と作物の代謝関係を教えてください」

と送信するのではなく、対象となるKnowledge AssetとSemantic Contextを指定する。

```text
Sender:
AGRIX-Agent

Receiver:
M3-Core-Agent

Intent:
METABOLIC_RELATION_QUERY

Domain:
Agriculture

Knowledge:
[AGRIX-KA-...]

Context:
Soil → Crop

Expected:
Metabolic Relationship Model
```

これにより、Agentは同じKnowledge Assetを共有しながら協調できる。

---

## 10.5 Agent Task Model

各Agent Taskは以下の構造を持つ。

```text
Task ID
Parent Task ID
Objective
Domain
Knowledge Scope
Required Agents
Expected Output
Validation Rule
Status
```

PMOS Director AgentはExecutive Requestを受け取ると、必要なAgent Taskへ分解する。

例えば、

```text
Executive Request
        │
        ▼
PMOS Director
        │
        ├── AGRIX Task
        ├── HealthBook Task
        ├── M3 Task
        └── PBPE Task
```

各Agentは担当Taskだけを処理する。

---

## 10.6 Agent Context

Agentが受け取るContextは無制限ではない。

Semantic Retrieval AgentがKnowledge GraphとPineconeから必要なKnowledge Assetを取得し、Agent Contextを構成する。

```text
User Intent

↓

Knowledge Graph

↓

Relevant Assets

↓

Semantic Retrieval

↓

Context Package

↓

Domain Agent
```

この方式により、Agentが不要なRepositoryや古いKnowledge Assetを参照することを防ぐ。

---

## 10.7 Agent-to-Agent Collaboration

複数Agentが協調する場合、PMOS Director AgentがCoordinatorとして機能する。

```text
                PMOS Director
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     AGRIX       HealthBook       M3
        │            │            │
        └────────────┼────────────┘
                     ▼
                   PBPE
                     │
                     ▼
                 Dashboard
```

各Domain Agentは独立して推論し、Director Agentが結果を統合する。

Agent同士が無秩序に直接通信するMesh構造は採用しない。

---

## 10.8 Metabolic Intelligence Code

PMOSでは、ドメイン間通信を標準化するため、Metabolic Intelligence Code（MIC）を導入する。

MICは自然言語そのものではなく、代謝・資源・生物学的関係を表現する意味コードとして利用する。

概念的には以下の構造を持つ。

```text
MIC

├── Domain
├── Entity
├── Process
├── Transformation
├── Direction
├── Impact
└── Confidence
```

例えば、

```text
SOIL
   ↓
MICROBIAL_PROCESS
   ↓
NUTRIENT_TRANSFORMATION
   ↓
CROP
```

のような関係を構造化してAgent間で共有する。

MICはPMOS固有の知識交換規約として発展させる。

---

## 10.9 Communication Validation

Agent Messageは送信前にValidationされる。

最低限、以下を確認する。

- Sender Agentが登録されている
    
- Receiver Agentが登録されている
    
- Knowledge IDが存在する
    
- Versionが一致している
    
- Domainが定義されている
    
- Task IDが存在する
    
- Expected Outputが定義されている
    

Validationに失敗したMessageは下流Agentへ送信しない。

---

## 10.10 Traceability

すべてのAgent TaskにはTrace IDを付与する。

Trace IDによって、

```text
Executive Request
      ↓
Director Agent
      ↓
Agent Task
      ↓
Knowledge Asset
      ↓
Knowledge Graph
      ↓
Domain Agent
      ↓
Integrated Result
      ↓
Dashboard
```

という一連の処理を追跡できる。

この仕組みはExplainable AIと監査可能性の基盤となる。

---

## 10.11 Agent Memory

PMOSではAgentごとに独立した長期記憶を持たせることを基本としない。

長期的に保持すべき知識はKnowledge AssetとしてGitHubへ保存する。

Agent Memoryは以下に限定する。

- Session Context
    
- Task State
    
- Temporary Reasoning Context
    
- Execution Metadata
    

永続的な知識はRepositoryへ戻す。

これにより、AIモデルを交換してもPMOSの知識体系を維持できる。

---

## 10.12 Communication Lifecycle

```text
Request

↓

Intent Parsing

↓

Task Creation

↓

Knowledge Resolution

↓

Semantic Context Construction

↓

Agent Execution

↓

Validation

↓

Integration

↓

Trace Recording

↓

Executive Output
```

通信は単なるメッセージ交換ではなく、Knowledge Assetを基準とした実行ライフサイクルとして管理する。

---

## 10.13 アーキテクチャ上の新規性

PMOSのAgent Communication Architectureは、LLM同士を直接会話させる方式ではない。

中心に存在するのはAgentではなくKnowledge Architectureである。

```text
        AI Agent
           │
           ▼
   Semantic Communication
           │
           ▼
     Knowledge Graph
           │
           ▼
   Knowledge Registry
           │
           ▼
    GitHub Knowledge
```

これにより、異なるLLM、異なるAIベンダー、異なるドメインAgentを同一の知識基盤へ接続できる。

PMOSにおけるAI協調の本質は、**「AI同士を会話させること」ではなく、「共通の意味体系を介してAIを協調させること」**にある。