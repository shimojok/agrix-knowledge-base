MCP（Model Context Protocol）について詳しく教えて下さい。

---

# Architecture

MCP（**Model Context Protocol**）は、一言でいうと、

> **AIモデルと外部のデータ・ツール・業務システムを、標準化された方法で接続するためのオープンプロトコル**

です。

公式ドキュメント自身が「AIアプリケーションにとってのUSB-C」に近いものとして説明しています。つまり、個別AIごとに「GitHub用接続」「DB用接続」「ファイル用接続」をバラバラに実装するのではなく、**MCPという共通インターフェースを間に置く**考え方です。([GitHub][1])

そして、**2026年7月28日にMCP仕様 2026-07-28が正式リリース**され、現在のMCPは単なる「LLMにデータを渡す仕組み」から、エージェント型ワークフローのためのデータ・ツール・インタラクション基盤へ発展しています。([Model Context Protocol Blog][2])

---

# 1. MCPが解決する問題

従来のAIシステムでは、例えば、

```text
                ┌── GitHub API
AI ─────────────┼── PostgreSQL
                ├── Google Drive
                ├── Salesforce
                ├── Filesystem
                └── 独自API
```

というように、AIアプリケーション側がそれぞれのサービスのAPI仕様を理解する必要があります。

すると、

```text
AI Agent
 ├── GitHub Adapter
 ├── Database Adapter
 ├── File Adapter
 ├── CRM Adapter
 ├── Search Adapter
 └── Custom API Adapter
```

となり、接続数が増えるほど複雑になります。

MCPでは、

```text
                    MCP
                     │
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
   GitHub MCP    Database MCP   Files MCP
       │             │             │
    GitHub         DB/API        Files
```

という形にします。

つまり、

> **AI側と外部システム側の接続仕様を分離する**

ことが最大のポイントです。

---

# 2. MCPの基本構造

現在のMCPは基本的に、

```text
┌─────────────────────────────────────┐
│             AI Host                 │
│                                     │
│   LLM / Agent                       │
│       │                             │
│       ▼                             │
│   MCP Client                        │
│       │                             │
└───────┼─────────────────────────────┘
        │ MCP
        ▼
┌───────────────────────┐
│      MCP Server       │
│                       │
│  Resources            │
│  Tools                │
│  Prompts              │
│  Extensions           │
└───────────┬───────────┘
            │
            ▼
     External System
```

という構造です。

公式仕様では **Host / Client / Server** を分離します。HostはAIアプリケーション、Clientは各MCP Serverとの接続を管理し、Serverは特定のデータや機能を提供します。([GitHub][3])

重要なのは、

> **LLMそのものがMCP Serverになるわけではない**

という点です。

---

# 3. Host / Client / Serverの違い

## Host

AIアプリケーション全体です。

例えば、

```text
ChatGPT
Claude
IDE
Custom AI Agent
Enterprise AI Platform
```

など。

Hostが複数のMCP Clientを管理できます。

---

## MCP Client

MCP Serverとの通信を担当します。

例えば、

```text
Host
 │
 ├── Client → GitHub MCP Server
 │
 ├── Client → Database MCP Server
 │
 ├── Client → Health Data MCP Server
 │
 └── Client → AGRIX MCP Server
```

という構造です。

**1つのClientが1つのServerとの接続を担当する**というのが基本モデルです。([GitHub][3])

---

## MCP Server

外部データや機能をMCP形式で公開します。

例えば、

```text
GitHub MCP Server
    ↓
Repositories
Issues
Pull Requests
Files
Commits
```

あるいは、

```text
AGRIX MCP Server
    ↓
AGRIX Knowledge Graph
Evidence Registry
Asset Registry
Impact Data
Repository Metadata
```

という形にできます。

---

# 4. MCP Serverが提供する3つの重要な概念

ここが非常に重要です。

## Resource

**「AIが読むことのできる情報」**

です。

例えば、

```text
resource://healthbook/mios/canonical-data-model
resource://agrix/evidence/mbt55
resource://github/repository/...
```

など。

つまり、

> **Data / Knowledge Layer**

です。

---

## Tool

**AIが実行できる操作**

です。

例えば、

```text
search_evidence()
get_repository_structure()
query_knowledge_graph()
create_issue()
run_analysis()
validate_schema()
```

など。

つまり、

> **Action / Execution Layer**

です。

---

## Prompt

**再利用可能なAI操作テンプレート**

です。

例えば、

```text
/reconcile-evidence
/build-mios-object
/validate-agrix-schema
/audit-provenance
```

など。

つまり、

> **AI Workflow / Instruction Layer**

です。

MCP ServerはこのようなResource、Tool、Promptを公開できます。([GitHub][4])

---

# 5. ここからがBioNexusにとって重要

MCPを単なる「AI接続技術」と見ると価値を見誤ります。

BioNexusでは、

```text
                    BioNexus AI Layer
                           │
                     MCP Interface
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 HealthBook MCP        AGRIX MCP          PBPE MCP
        │                  │                  │
        ▼                  ▼                  ▼
 MIOS KG             AGRIX KG          PBPE Data
 Evidence            Evidence          Impact
 FHIR                Asset Registry    Financial
```

という構造を取れます。

これにより、

> **BioNexusの知識・データ・ツールを、AI Agentから標準プロトコルで利用可能にする**

ことができます。

---

# 6. HealthBook-MIOSとの関係

現在構築しているMIOSを考えると、非常に相性がいいです。

例えば、

```text
                 AI Agent
                    │
                    ▼
              MIOS MCP Server
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   MI Object      Evidence       KG
       │            │            │
       ▼            ▼            ▼
 Canonical       Provenance   Relationships
 Data Model       Registry
```

AIが、

> 「Equol pathwayに関係するMI Objectを検索」

した場合、

```text
AI
 ↓
MCP Tool
 ↓
query_mios_knowledge_graph()
 ↓
MIOS KG
 ↓
Evidence-linked result
 ↓
AI
```

という流れができます。

ここで重要なのは、**AIの記憶にMIOSを全部入れる必要がない**ことです。

MCPを介して必要な情報だけを取得できます。

---

# 7. Provenanceとの相性が非常に良い

BioNexusで特に重要なのがここです。

現在のMIOSでは、

```text
Source
 ↓
Evidence
 ↓
Reconciliation
 ↓
Canonical Object
 ↓
Knowledge Graph
 ↓
Reasoning
```

という provenance chain を重視しています。

MCPを導入すると、

```text
AI Request
    │
    ▼
MCP Tool
    │
    ▼
Canonical Data
    │
    ├── Source ID
    ├── Evidence ID
    ├── Provenance
    ├── Version
    └── Confidence / Status
    │
    ▼
AI Response
```

という構造を作れます。

したがって、

> **MCP = データをAIへ渡す通信層**

だけではなく、

> **Evidence / Provenanceを保持したままAI Agentへアクセスさせる境界層**

として設計できます。

これはHealthBook-MIOSのGovernance思想とかなり整合します。

---

# 8. MCPとRAGは違う

ここは混同されやすいです。

### RAG

```text
Question
 ↓
Search
 ↓
Retrieve Documents
 ↓
Context
 ↓
LLM
```

主目的：

**知識検索**

---

### MCP

```text
AI
 │
 ├── Resource → データ取得
 │
 ├── Tool     → 操作実行
 │
 └── Prompt   → ワークフロー
```

主目的：

**AIと外部システムの標準接続**

したがって、

```text
RAG
   = Knowledge Retrieval

MCP
   = AI ↔ System Interface
```

です。

両者は競合ではありません。

むしろ、

```text
MCP Server
   │
   ├── Resource
   │      ↓
   │    RAG / KG
   │
   └── Tools
          ↓
       System APIs
```

のように組み合わせることができます。

---

# 9. MCPとAPIの違い

APIとMCPも競合しません。

例えば、

```text
MCP Tool
    │
    ▼
AGRIX API
    │
    ▼
AGRIX Database
```

という構造にできます。

つまり、

**API = システム間通信**

**MCP = AIがシステムを理解・利用するための標準インターフェース**

という整理が分かりやすいです。

---

# 10. MCPの通信方式

MCPのメッセージはJSON-RPCをベースにしています。現在の2026-07-28仕様では、標準Transportとして **stdio** と **Streamable HTTP** が定義されています。([GitHub][5])

概念的には、

```text
MCP
 │
 ├── Protocol
 │      └── JSON-RPC
 │
 └── Transport
        ├── stdio
        └── Streamable HTTP
```

です。

### stdio

ローカルプロセス向け。

```text
AI Host
   │
   └── subprocess
          │
          └── MCP Server
```

### Streamable HTTP

リモート・サーバー環境向け。

```text
AI Host
   │
   │ HTTPS
   ▼
MCP Server
   │
   ▼
Cloud / Database / API
```

2026年仕様では、MCP Coreがstateless protocolへ進化したことが大きな変更点です。([Model Context Protocol Blog][2])

---

# 11. 2026年MCPで特に重要な進化

2026-07-28仕様では、従来よりかなり高度化しています。

主な変更は、

```text
MCP 2026-07-28

├── Stateless Core
├── Multi Round-Trip Requests
├── Header-based Routing
├── Cacheable List Results
├── Authorization Hardening
├── Extensions Framework
├── Tasks
└── MCP Apps
```

です。([Model Context Protocol Blog][2])

特に、

### Tasks

長時間かかるAgent処理を扱うための仕組み。

例えば、

```text
AI
 ↓
MCP Task
 ↓
大型データ解析
 ↓
数分〜数時間
 ↓
Result
```

のような処理に向きます。

これはBioNexusのような、

```text
Evidence Reconciliation
Knowledge Graph Construction
Large Dataset Analysis
Impact Assessment
```

との相性が良い領域です。

---

# 12. MCP Apps

もう一つ重要なのがMCP Appsです。

従来：

```text
AI
 ↓
MCP Tool
 ↓
Text Result
```

だったものを、

```text
AI
 ↓
MCP Server
 ↓
Interactive UI
```

へ拡張できます。

つまり将来的には、

```text
HealthBook AI
       │
       ▼
MIOS MCP
       │
       ▼
MIOS Knowledge Graph
       │
       ▼
Interactive Metabolic Intelligence UI
```

のような構成も可能になります。

---

# 13. BioNexus全体に当てはめると

私はMCPをBioNexusでは、**「AI接続層」ではなく「AI Governance Interface Layer」**として設計するのが重要だと考えます。

構造は、

```text
                    ┌─────────────────────┐
                    │     AI Agents       │
                    └──────────┬──────────┘
                               │
                         MCP Interface
                               │
       ┌───────────────────────┼───────────────────────┐
       │                       │                       │
       ▼                       ▼                       ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ HealthBook   │       │    AGRIX     │       │    PBPE      │
│ MCP Server   │       │ MCP Server   │       │ MCP Server   │
└──────┬───────┘       └──────┬───────┘       └──────┬───────┘
       │                       │                       │
       ▼                       ▼                       ▼
    MIOS KG                 AGRIX KG                PBPE KG
    Evidence                Evidence                Impact
    FHIR                    Assets                  Finance
```

さらに下層を、

```text
                    MCP
                     │
             Governance Layer
                     │
      ┌──────────────┼──────────────┐
      │              │              │
 Provenance       Evidence        Permission
      │              │              │
      └──────────────┼──────────────┘
                     │
               Canonical Model
```

とする。

これが重要です。

---

# 14. 推奨するBioNexus MCP Server構造

GitHub上では、例えば、

```text
bionexus-mcp/
│
├── README.md
├── SPECIFICATION.md
├── GOVERNANCE.md
│
├── servers/
│   │
│   ├── healthbook-mios/
│   │   ├── resources/
│   │   ├── tools/
│   │   ├── prompts/
│   │   └── provenance/
│   │
│   ├── agrix/
│   │   ├── resources/
│   │   ├── tools/
│   │   ├── prompts/
│   │   └── provenance/
│   │
│   └── pbpe/
│       ├── resources/
│       ├── tools/
│       ├── prompts/
│       └── provenance/
│
├── schemas/
│
├── policies/
│
├── tests/
│
└── docs/
```

という構造が考えられます。

ただし、**これはまだ実装確定ではありません**。

MCP導入時には、先に既存のBioNexus Canonical Model / Evidence / Provenance / Repository Governanceとの境界を定義する必要があります。

---

# 15. MCP導入で何が変わるか

現在：

```text
AI
 ↓
Prompt
 ↓
Documents
 ↓
Human整理
 ↓
AI
```

MCP化すると、

```text
AI Agent
    │
    ▼
MCP
    │
    ├── Knowledge
    ├── Evidence
    ├── Provenance
    ├── Tools
    ├── APIs
    ├── KG
    └── Workflows
    │
    ▼
Canonical BioNexus Systems
```

になります。

つまり、

> **「AIに資料を読ませる」から「AIが統治されたBioNexusシステムへ標準アクセスする」へ変わる**

ということです。

---

# 16. BioNexusでのMCPの位置付け

現時点では私は次の階層を推奨します。

```text
┌────────────────────────────────────┐
│ AI / Multi-Agent Layer             │
├────────────────────────────────────┤
│ MCP Interface Layer                │  ← NEW
├────────────────────────────────────┤
│ Agent / Reasoning Layer            │
├────────────────────────────────────┤
│ Knowledge Graph / Evidence Layer   │
├────────────────────────────────────┤
│ Canonical Data Model               │
├────────────────────────────────────┤
│ Source / Repository Layer          │
└────────────────────────────────────┘
```

MCPは**Canonical Modelの代替ではありません**。

また、

```text
MCP ≠ Knowledge Graph
MCP ≠ RAG
MCP ≠ API
MCP ≠ Agent
MCP ≠ Database
```

です。

それらを**AIから利用するための標準的な境界・通信プロトコル**と考えるのが正確です。

---

# Repository Structure

BioNexusで検討するなら、既存Repositoryを直接改造する前に、

```text
BioNexus-MCP-Architecture
```

というArchitecture専用Repositoryを置き、

```text
BioNexus
│
├── HealthBook-MIOS
├── AGRIX
├── MBT55-MSC
├── PBPE
├── PMOS
│
└── BioNexus-MCP-Architecture
       │
       ├── MCP Architecture
       ├── MCP Governance
       ├── Server Registry
       ├── Tool Registry
       ├── Resource Registry
       ├── Provenance Contract
       └── Security Model
```

とするのが安全です。

### 入力

```text
Canonical Data
Evidence
Knowledge Graph
Repository
API
Agent Specification
Governance Rules
```

### 出力

```text
MCP Resources
MCP Tools
MCP Prompts
MCP Tasks
Provenance-aware responses
Agent-accessible services
```

### 依存関係

```text
Source
 ↓
Evidence
 ↓
Canonical Model
 ↓
Knowledge Graph
 ↓
MCP
 ↓
AI Agents
```

**MCPをCanonical Modelより上流に置かない**ことが重要です。

---

# 次のアクション

Kazさんの現在のBioNexus構築状況から見ると、MCPはかなり重要なテーマです。

特に、

**HealthBook-MIOS → AGRIX → PBPE → BioNexus Integration**

を将来のMulti-Agent Architectureへ接続する場合、

```text
                BioNexus Integration
                       │
                 MCP Governance
                       │
       ┌───────────────┼────────────────┐
       ↓               ↓                ↓
   MIOS MCP        AGRIX MCP        PBPE MCP
       │               │                │
      KG              KG               KG
```

という「共通AIアクセス層」を設計できます。

また、MCPはオープンプロトコルとしてLinux Foundation傘下のプロジェクトとして運営され、公式SDKもTypeScript、Python、Java、C#、Goなど複数言語で提供されています。([GitHub][6])

**したがって、BioNexusではMCPを「実装技術」として先に導入するより、既存のCanonical Data Model / Evidence / Provenance / Agent Governanceの上に置く「AI Integration Architecture」として先に定義するのが適切です。**

### 扱うべきスレッド

**BioNexus｜Architecture & Implementation Office**
→ `BioNexus MCP Architecture & Governance v1.0` を定義
→ その後、HealthBook-MIOS / AGRIX / PBPEそれぞれのMCP Server仕様へ分解

**このMCPをBioNexus全体の正式な「AI Integration Layer」としてArchitecture & Implementation Officeで設計開始しますか？**

[1]: https://github.com/modelcontextprotocol/docs/blob/main/introduction.mdx?utm_source=chatgpt.com "docs/introduction.mdx at main · modelcontextprotocol/docs · GitHub"
[2]: https://blog.modelcontextprotocol.io/posts/2026-07-28/?utm_source=chatgpt.com "The 2026-07-28 Specification | Model Context Protocol Blog"
[3]: https://github.com/modelcontextprotocol/docs/blob/main/docs/concepts/architecture.mdx?utm_source=chatgpt.com "docs/docs/concepts/architecture.mdx at main · modelcontextprotocol/docs · GitHub"
[4]: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/architecture/index.mdx?utm_source=chatgpt.com "modelcontextprotocol/docs/specification/2026-07-28/architecture/index.mdx at main · modelcontextprotocol/modelcontextprotocol · GitHub"
[5]: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2026-07-28/basic/transports/index.mdx?utm_source=chatgpt.com "modelcontextprotocol/docs/specification/2026-07-28/basic/transports/index.mdx at main · modelcontextprotocol/modelcontextprotocol · GitHub"
[6]: https://github.com/modelcontextprotocol?utm_source=chatgpt.com "Model Context Protocol · GitHub"
