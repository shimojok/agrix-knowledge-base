# ADR-001: AGRIX と HealthBook のアーキテクチャ統合・実装分離方針

**Repository:** `00-Governance/adr`
**Status:** Accepted
**Date:** 2026-07-29
**Depends on:** Knowledge Graph / Ontology v1.0, Agent Communication Protocol v1.0

---

## Context（背景）

HealthBookプロジェクト（CGH系スレッド）で生まれた3つの新規性——

1. Metabolic Intelligence中心のAIエージェントアーキテクチャ
2. Knowledge GraphとAIエージェントを統合した推論モデル
3. エージェント間で意味を持つMIコードを受け渡す通信プロトコル

——は、AGRIX/PMOSスレッド（GT系・PMOS系）で議論されていたPlanetary Metabolic Operating Systemの構想と本質的に同一の技術的パターンであることが判明した（PMOS101参照）。

これを受け、`PMOS-Knowledge-Graph-Ontology-v1.0` および `PMOS-Agent-Communication-Protocol-v1.0` は、AGRIXとHealthBookのどちらか一方に属するものとしてではなく、**両者が共有する上位アーキテクチャ（PMOS）の一部**として設計・実装済みである。

この状態を前提に、「AGRIXとHealthBookを別プロジェクトとして進めるか、統合するか」という意思決定が必要になった。

---

## Decision（決定）

**アーキテクチャ層は統合し、実装層は分離する。**

具体的には以下の3階層で切り分ける。

```
Layer 1: Architecture（統合・単一）
  ├── PMOS Knowledge Graph / Ontology
  ├── PMOS Agent Communication Protocol (MI Code)
  └── PMOS Executive Dashboard Framework

Layer 2: Domain Implementation（分離・独立）
  ├── AGRIX Repository（農業ドメインAgent・データ・パートナー）
  └── HealthBook Repository（健康ドメインAgent・データ・パートナー）

Layer 3: Presentation（統合・単一）
  └── PMOS Demonstration System（両ドメインを横断して見せる）
```

- Layer 1・3は本ADRの前提文書（Knowledge Graph v1.0、Agent Protocol v1.0、Dashboard Spec v1.0、Demo Spec v1.0）をそのまま正典とし、AGRIX・HealthBookどちらのチームも独自に再設計しない。
- Layer 2は、AGRIXリポジトリとHealthBookリポジトリを別々に維持する。担当者・作業ペース・対外パートナー交渉（例: AGRIXはYara/World Bank/FAO、HealthBookは医療機関・投資家）はそれぞれ独立して進めてよい。
- 両リポジトリの `Agent`ノードおよび出力契約 (`contract-mi-code-v1`) は共通スキーマに準拠することを必須とする。準拠しない変更はADRなしに行えない。

---

## Consequences（帰結）

**得られるもの**

- Knowledge Graph・MIコード文法・Agent Protocolの二重設計を回避できる。
- 対外プレゼン（Executive Dashboard・Demo）で「単一ドメインのツール」ではなく「複数ドメインを貫く新しいAI基盤」を提示できる——これがMicrosoft/Gates財団への訴求点そのものになる。
- AGRIX・HealthBookそれぞれの進行ペースやパートナー交渉を独立して進められる。

**引き受けるコスト**

- Layer 1（アーキテクチャ）を変更する際は、AGRIX・HealthBook双方への影響評価が必須になる。片方の都合だけで `MetabolicPathway` や `MI Code` 文法を変更できない。
- 新しいドメイン語彙（例: AGRIX固有の`PATHWAY_CODE`）を追加する場合は、Registry Agentへの正式申請フローを通す必要があり、即興での拡張はできない。

---

## Governance Rule（運用ルール）

- Layer 1／3に関する変更提案は、必ずADRとして記録し、AGRIX・HealthBook両担当が確認した上で `Accepted` とする。
- Layer 2内の変更（各ドメイン固有のデータ・実装詳細）はADR不要で、各リポジトリの裁量で進めてよい。
- 本ADRの前提4文書（Knowledge Graph / Agent Protocol / Dashboard / Demo）は "Frozen" とし、次の変更は明示的なADRを経てのみ行う。

---

## Repository配置

```
00-Governance/
└── adr/
    └── ADR-001-agrix-healthbook-integration.md   ← 本文書
```

---

## Next Actions

- AGRIXリポジトリの `Agent`ノード定義（`agrix-agent.md`）とHealthBookリポジトリの `Agent`ノード定義（`healthbook-agent.md`）を、それぞれ Layer 2 として個別に作成する。
- 両リポジトリの初期コミット（README、フォルダ構成）を、本ADRのLayer構造に沿って準備する。
