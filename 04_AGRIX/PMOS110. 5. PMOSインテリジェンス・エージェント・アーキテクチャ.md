# `/09-Documents/Project-Phoenix-Master-Plan-05-PMOS-Intelligence-Agent-Architecture.md`

## 5. PMOSインテリジェンス・エージェント・アーキテクチャ

### 5.1 設計目的

PMOSにおけるAIエージェントは、従来のチャットボットや単独のLLMアプリケーションとは設計思想が異なる。

その目的は、自然言語を生成することではなく、PMOS全体のKnowledge Assetを理解し、Knowledge Graphを介して複数の専門エージェントが協調的に推論を行う「Planetary Metabolic Intelligence（PMI）」を実現することである。

各エージェントは独自の知識を保持しない。

知識は常にGitHub上のKnowledge Asset、Knowledge Registry、Knowledge Graphから取得される。

これにより、AIは学習済み知識ではなく、常に最新版のPMOS知識体系を参照して推論を行う。

---

## 5.2 基本構造

PMOSではAIを階層型マルチエージェントとして構成する。

```text
Executive Intelligence Layer
           │
PMOS Director Agent
           │
Knowledge Coordination Layer
           │
────────────────────────────────────────
│          │          │          │
AGRIX   HealthBook    PBPE     M3 Core
Agent      Agent      Agent     Agent
│          │          │          │
────────────────────────────────────────
           │
Knowledge Graph Agent
           │
Semantic Retrieval Agent
           │
Repository Access Layer
           │
GitHub Knowledge Assets
```

この構造では、各ドメインエージェントは専門領域のみを担当し、横断的な統合判断はPMOS Director Agentが実施する。

---

## 5.3 PMOS Director Agent

PMOS Director Agentは最上位統括エージェントである。

主な役割は以下とする。

- タスク分解
    
- エージェント選択
    
- 推論順序の決定
    
- Knowledge Graph参照
    
- 実行計画生成
    
- Dashboard生成要求
    
- Executive Report生成
    
- Demonstration制御
    

Director Agentは専門知識を保持しない。

必要に応じて各専門エージェントへ問い合わせを行い、その結果を統合して最終成果物を生成する。

---

## 5.4 Knowledge Coordination Agent

Knowledge Coordination Agentは知識同期を担当する。

役割は以下である。

- Repository更新検知
    
- Knowledge Asset登録
    
- Knowledge ID管理
    
- Semantic Tag生成
    
- Version管理
    
- Asset整合性確認
    
- Dependency解析
    

Knowledge Coordination AgentはGitHubとKnowledge Registryを同期する中核エージェントである。

---

## 5.5 Knowledge Graph Agent

Knowledge Graph AgentはPMOS知識ネットワーク全体を管理する。

主要機能は以下である。

- ノード生成
    
- リレーション生成
    
- Ontology適用
    
- Graph Validation
    
- Graph Query
    
- Semantic Expansion
    
- Dependency探索
    
- Concept Navigation
    

Knowledge Graph AgentはAIエージェント間の意味的接続を保証する。

---

## 5.6 Semantic Retrieval Agent

Semantic Retrieval AgentはPineconeなどのベクトル検索基盤とKnowledge Graphを統合する。

処理手順は以下である。

1. 問い合わせ解析
    
2. Semantic Tag抽出
    
3. Knowledge Graph検索
    
4. ベクトル検索
    
5. Candidate Ranking
    
6. Knowledge ID取得
    
7. Context生成
    
8. 専門エージェントへ受け渡し
    

全文検索ではなく、意味構造と類似度を組み合わせた検索を実施する。

---

## 5.7 AGRIX Agent

AGRIX Agentは農業・環境領域を担当する。

担当範囲は以下とする。

- Soil Intelligence
    
- Soil Microbiome
    
- Carbon Cycle
    
- Nitrogen Cycle
    
- Fermentation
    
- Crop Productivity
    
- Climate Impact
    
- AgriWare
    
- SafetyChain
    

出力はKnowledge Assetであり、直接ユーザーへ回答しない。

Director Agentが必要に応じて統合する。

---

## 5.8 HealthBook Agent

HealthBook Agentはヒト代謝領域を担当する。

対象領域は以下である。

- Phenotype
    
- Metabolism
    
- Nutrition
    
- Biomarkers
    
- Kampo
    
- Questionnaire
    
- Disease Knowledge
    
- FHIR
    

HealthBook Agentは医療判断を行うのではなく、Knowledge Assetから代謝知識を整理・提示する役割を担う。

---

## 5.9 PBPE Agent

PBPE AgentはPlanetary Impact評価を担当する。

主な機能は以下である。

- KPI算出
    
- Impact評価
    
- Carbon評価
    
- Resource評価
    
- Finance評価
    
- Biosecurity評価
    
- Executive Summary生成
    

PBPE Agentは複数RepositoryからKnowledge Assetを収集し、Planetary Impactとして統合する。

---

## 5.10 M3 Core Agent

M3 Core AgentはPMOSの代謝モデルを担当する。

役割は以下である。

- Metabolic Network
    
- Transformation Model
    
- Biological Interaction
    
- Resource Flow
    
- Circular Economy
    
- Metabolic Intelligence
    

M3 AgentはAGRIXとHealthBook双方へ代謝知識を提供する共通基盤となる。

---

## 5.11 Dashboard Agent

Dashboard AgentはExecutive Layerを担当する。

役割は以下とする。

- KPI取得
    
- Visualization
    
- Executive Summary
    
- Story Generation
    
- Graph Rendering
    
- Trend表示
    
- Repository Status表示
    

Dashboard Agentはデータを保持しない。

Knowledge Registryから取得した情報のみを可視化する。

---

## 5.12 Demonstration Agent

Demonstration AgentはPMOS全体を説明するための実演を制御する。

主な担当は以下である。

- Demo Script
    
- Demo Navigation
    
- Repository紹介
    
- Knowledge Graph可視化
    
- Dashboard切替
    
- AI Collaboration表示
    
- Executive Presentation
    

各デモはKnowledge Assetを利用してリアルタイムに構成される。

---

## 5.13 Agent Communication Protocol

PMOSではAI同士は自然言語だけで通信しない。

以下の情報を共通フォーマットとして利用する。

- Knowledge ID
    
- Repository ID
    
- Asset Version
    
- Semantic Tag
    
- Ontology Class
    
- Graph Node ID
    
- Dependency ID
    
- Task ID
    

これらをメッセージヘッダとして利用することで、意味的整合性を維持したまま複数エージェントが協調できる。

---

## 5.14 Agent Workflow

```text
Executive Request

↓

PMOS Director Agent

↓

Knowledge Coordination Agent

↓

Knowledge Graph Agent

↓

Semantic Retrieval Agent

↓

Domain Agent
(AGRIX / HealthBook / PBPE / M3)

↓

Knowledge Integration

↓

Dashboard Agent

↓

Demonstration Agent

↓

Executive Report
```

この処理は一方向パイプラインではなく、Knowledge Graphを中心とした反復型推論として設計される。

---

## 5.15 PMOSインテリジェンス・アーキテクチャの新規性

PMOSのAIアーキテクチャは、「エージェントが知識を保持する」のではなく、「知識資産を中心にエージェントが動的に協調する」ことを前提としている。

知識はGitHub上のKnowledge Assetとして管理され、Knowledge Registryで識別され、Knowledge Graphによって意味的に接続される。AIエージェントはその共通知識基盤を参照して推論・統合・可視化を行う。

この構造により、ドメインごとの独立性と全体最適を両立し、AGRIX、HealthBook、PBPE、M3を横断するPlanetary Metabolic Intelligenceを一つのAIネイティブ・プラットフォームとして実現する。