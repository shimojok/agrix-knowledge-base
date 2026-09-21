# PMOS Agent Communication Protocol — MI Code Specification v1.0

**Repository:** `06-AI-Agents/protocol`
**Status:** Draft — 実装可能レベルの初版
**Depends on:** PMOS Knowledge Graph / Ontology Specification v1.0

---

## 1. 設計原則

一般的なマルチエージェントLLM設計は、エージェント間で自然文プロンプトをやり取りする。これは柔軟だが、**意味の揺れ・ハルシネーション・監査不能性**という弱点を持つ。

PMOSでは、エージェント間の主要な通信は**構造化された「MIコード（Metabolic Intelligence Code）」**で行う。自然文は補助情報としてのみ添付する。MIコードは、Section 2章のKnowledge Graphの `MetabolicPathway` / `Indicator` ノードと直接対応する、**閉じた語彙の記号列**である。これにより、エージェント間の合意内容がGitHub上で差分管理・監査可能になる。

---

## 2. エージェント構成と入出力契約

```
                    PMOS Director
                         │
        ┌────────────────┼────────────────┐
   Knowledge Coordinator  │          Registry Agent
        │                 │
 ┌──────┼──────┬──────────┴───────┐
AGRIX  HealthBook  PBPE      Dashboard/Demo Agent
Agent    Agent    Agent
```

| Agent | 役割 | Input Contract | Output Contract |
|---|---|---|---|
| PMOS Director | 全体調停・エスカレーション処理 | `contract:director-input-v1` | `contract:director-decision-v1` |
| Knowledge Coordinator | ノード同期・ブロードキャスト | `contract:kg-sync-v1` | `contract:kg-broadcast-v1` |
| AGRIX Agent | 農業ドメインの状態評価 | `contract:domain-query-v1` | `contract:mi-code-v1` |
| HealthBook Agent | 健康ドメインの状態評価 | `contract:domain-query-v1` | `contract:mi-code-v1` |
| PBPE Agent | インパクト評価 | `contract:domain-query-v1` | `contract:mi-code-v1` |
| Registry Agent | 資産登録・バージョン管理 | `contract:asset-submit-v1` | `contract:registry-ack-v1` |
| Dashboard Agent | 指標の集約・可視化用整形 | `contract:mi-code-v1`（複数） | `contract:dashboard-payload-v1` |
| Demo Agent | シナリオ進行・発話生成 | `contract:dashboard-payload-v1` | `contract:demo-narration-v1` |

各ドメインAgentの出力契約は共通の `mi-code-v1` である。これが「異なるドメインのエージェントが同じ言語で話す」ことを技術的に保証する仕組みになる。

---

## 3. メッセージ・エンベロープ

すべてのエージェント間通信は、以下のエンベロープに包まれる。

```json
{
  "$id": "MessageEnvelope",
  "type": "object",
  "required": ["message_id", "correlation_id", "from_agent", "to_agent", "timestamp", "intent", "protocol_version", "body"],
  "properties": {
    "message_id": { "type": "string", "format": "uuid" },
    "correlation_id": { "type": "string", "format": "uuid", "description": "一連のやり取りを束ねるID" },
    "from_agent": { "type": "string" },
    "to_agent": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "intent": { "type": "string", "enum": ["QUERY","ASSERT","PROPOSE","ESCALATE","SUBSCRIBE","NOTIFY","ACK","ERROR"] },
    "priority": { "type": "string", "enum": ["low","normal","high","critical"], "default": "normal" },
    "protocol_version": { "type": "string", "const": "mi-code-v1" },
    "ttl_seconds": { "type": "integer", "default": 3600 },
    "body": { "$ref": "MessageBody" }
  }
}
```

```json
{
  "$id": "MessageBody",
  "type": "object",
  "required": ["mi_code", "confidence"],
  "properties": {
    "mi_code": { "type": "string", "description": "Section 4のMIコード文字列" },
    "payload": { "type": "object", "description": "ドメイン固有データ（数値・単位など）" },
    "references": { "type": "array", "items": { "type": "string" }, "description": "Knowledge Graphノードへの参照ID" },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "provenance": { "type": "string", "description": "データソースまたは計算根拠" },
    "natural_language_note": { "type": "string", "description": "人間向け補助説明（監査・デバッグ用。エージェントの意思決定には使わない）" }
  }
}
```

---

## 4. MIコードの文法

MIコードは以下の固定文法を持つ記号列である。

```
MI-<DOMAIN>-<PATHWAY_CODE>-<STATE_VERB>-<MAGNITUDE>-<UNIT>-<CONFIDENCE>
```

| 要素 | 語彙 |
|---|---|
| `DOMAIN` | `AGRIX` \| `HEALTH` \| `IMPACT` \| `BIOSEC` \| `CLIMATE` |
| `PATHWAY_CODE` | Knowledge Graph上の `MetabolicPathway.id` のsuffix（例: `NITROGEN_CYCLE`, `GLUCOSE_METABOLISM`） |
| `STATE_VERB` | `IMPROVING` \| `STABLE` \| `DEGRADING` \| `CRITICAL` \| `RECOVERING` |
| `MAGNITUDE` | 変化量（0.00–1.00の正規化スコア、符号付き可） |
| `UNIT` | `INDEX` \| `PERCENT` \| `RATE` |
| `CONFIDENCE` | 0.00–1.00（エージェント自身の確信度） |

**例:**

```
MI-AGRIX-NITROGEN_CYCLE-DEGRADING-0.23-INDEX-0.87
MI-HEALTH-GLUCOSE_METABOLISM-IMPROVING-0.15-INDEX-0.91
MI-IMPACT-WATER_QUALITY-DEGRADING-0.31-INDEX-0.74
```

人間可読変換（Dashboard/Demo Agentが自然文へ翻訳する際の対応表）:

| STATE_VERB | 日本語 |
|---|---|
| IMPROVING | 改善傾向 |
| STABLE | 安定 |
| DEGRADING | 悪化傾向 |
| CRITICAL | 危機的 |
| RECOVERING | 回復中 |

---

## 5. 相互作用パターン

### 5.1 Request–Response（QUERY / ASSERT）

Knowledge Coordinatorがドメインエージェントに状態を問い合わせ、MIコードで応答を受ける最も基本的なパターン。

```
Knowledge Coordinator → AGRIX Agent    : intent=QUERY
AGRIX Agent → Knowledge Coordinator    : intent=ASSERT, body.mi_code=MI-AGRIX-...
```

### 5.2 Publish–Subscribe（SUBSCRIBE / NOTIFY）

Dashboard AgentはKnowledge Coordinatorに対して特定Domainの `mi_code` 更新をSUBSCRIBEし、更新があるたびにNOTIFYを受ける。

### 5.3 Escalation（ESCALATE）

以下のいずれかが発生した場合、ドメインAgentは直接PMOS Directorへ `ESCALATE` を送る。

- `confidence < 0.5`
- 同一 `correlation_id` 内で他ドメインAgentのMIコードと `STATE_VERB` が矛盾する（例: AGRIXがIMPROVING、IMPACTが同一Pathway参照でCRITICAL）
- `INFLUENCES` エッジで結ばれた別ドメインの状態が `CRITICAL` に遷移した

PMOS Directorは矛盾解消のため、Knowledge Graphの `INFLUENCES` エッジと `evidence_ref` を参照して裁定し、`intent=NOTIFY` で関係エージェントへ裁定結果を配信する。

---

## 6. エージェント状態機械

```
        ┌────────┐
   ┌───▶│  IDLE  │◀───────────────┐
   │    └───┬────┘                │
   │        │ receive(message)    │
   │        ▼                     │
   │   ┌──────────┐               │
   │   │LISTENING │               │
   │   └────┬─────┘               │
   │        │ intent識別           │
   │        ▼                     │
   │   ┌──────────┐   confidence<0.5   ┌───────────┐
   │   │PROCESSING├────────────────────▶│ESCALATING │
   │   └────┬─────┘                     └─────┬─────┘
   │        │ confidence>=0.5                  │
   │        ▼                                  │
   │   ┌──────────┐                             │
   └───┤RESPONDING│◀────────────────────────────┘
       └──────────┘
```

---

## 7. 実例：ドメイン横断メッセージ交換

**シナリオ:** A12区画の窒素循環悪化が、周辺住民の健康指標に影響しうるかをKnowledge Coordinatorが確認する。

**Step 1 — AGRIX Agentへの問い合わせ**

```json
{
  "message_id": "5b1a...",
  "correlation_id": "corr-7788",
  "from_agent": "knowledge-coordinator",
  "to_agent": "agrix-agent",
  "timestamp": "2026-07-29T09:00:00Z",
  "intent": "QUERY",
  "priority": "high",
  "protocol_version": "mi-code-v1",
  "body": {
    "mi_code": "MI-AGRIX-NITROGEN_CYCLE-QUERY-0.00-INDEX-1.00",
    "references": ["agrix:nitrogen-cycle-001"],
    "confidence": 1.0
  }
}
```

**Step 2 — AGRIX Agentの応答**

```json
{
  "message_id": "5b1b...",
  "correlation_id": "corr-7788",
  "from_agent": "agrix-agent",
  "to_agent": "knowledge-coordinator",
  "timestamp": "2026-07-29T09:00:04Z",
  "intent": "ASSERT",
  "protocol_version": "mi-code-v1",
  "body": {
    "mi_code": "MI-AGRIX-NITROGEN_CYCLE-DEGRADING-0.23-INDEX-0.87",
    "payload": { "runoff_kg_per_ha": 4.1 },
    "references": ["agrix:nitrogen-cycle-001", "impact:water-quality-index"],
    "confidence": 0.87,
    "provenance": "agrix:study-runoff-2026-03"
  }
}
```

**Step 3 — Knowledge Coordinatorから HealthBook Agentへ INFLUENCESエッジ経由で照会**

```json
{
  "message_id": "5b1c...",
  "correlation_id": "corr-7788",
  "from_agent": "knowledge-coordinator",
  "to_agent": "healthbook-agent",
  "timestamp": "2026-07-29T09:00:06Z",
  "intent": "QUERY",
  "priority": "high",
  "protocol_version": "mi-code-v1",
  "body": {
    "mi_code": "MI-HEALTH-WATERBORNE_EXPOSURE-QUERY-0.00-INDEX-1.00",
    "references": ["impact:water-quality-index"],
    "confidence": 1.0,
    "natural_language_note": "AGRIX側の窒素循環悪化(0.23)が地域住民の健康指標に影響する可能性を確認"
  }
}
```

**Step 4 — 矛盾検知によるエスカレーション例**

HealthBook Agentの応答が `STABLE` かつ `confidence=0.42` だった場合、confidence閾値未満のためHealthBook Agentは自動的に `ESCALATE` をPMOS Directorへ送信する。

```json
{
  "message_id": "5b1d...",
  "correlation_id": "corr-7788",
  "from_agent": "healthbook-agent",
  "to_agent": "pmos-director",
  "timestamp": "2026-07-29T09:00:11Z",
  "intent": "ESCALATE",
  "priority": "critical",
  "protocol_version": "mi-code-v1",
  "body": {
    "mi_code": "MI-HEALTH-WATERBORNE_EXPOSURE-STABLE-0.05-INDEX-0.42",
    "references": ["impact:water-quality-index", "agrix:nitrogen-cycle-001"],
    "confidence": 0.42,
    "provenance": "healthbook:cohort-p3391-partial-data",
    "natural_language_note": "地域健康データが不足しており確信度が低い。人間のレビューまたは追加データ取得が必要。"
  }
}
```

---

## 8. バージョニングとエラー処理

| エラーコード | 意味 | 対応 |
|---|---|---|
| `E-SCHEMA-001` | エンベロープがJSON Schemaに準拠しない | 送信元へ`intent=ERROR`で即時返送 |
| `E-VOCAB-002` | MIコードの語彙（DOMAIN/STATE_VERB等）が未定義 | Registry Agentへ新語彙申請をルーティング |
| `E-CONF-003` | confidence欠落または範囲外 | メッセージを破棄しログのみ記録 |
| `E-TTL-004` | `ttl_seconds`超過 | 破棄し、送信元へ再送要求 |

`protocol_version` はメッセージ単位で固定し、破壊的変更時は `mi-code-v2` として新バージョンを併存させる。Registry Agentがバージョン間の互換性マトリクスを保持する。

---

## 9. ファイル配置規約

```
06-AI-Agents/
├── protocol/
│   ├── message-envelope.schema.json
│   ├── message-body.schema.json
│   ├── mi-code-grammar.md
│   └── error-codes.md
├── contracts/
│   ├── contract-domain-query-v1.schema.json
│   ├── contract-mi-code-v1.schema.json
│   └── contract-dashboard-payload-v1.schema.json
└── agents/
    ├── pmos-director.md
    ├── knowledge-coordinator.md
    ├── agrix-agent.md
    ├── healthbook-agent.md
    ├── pbpe-agent.md
    ├── registry-agent.md
    ├── dashboard-agent.md
    └── demo-agent.md
```

---

## 10. 次に必要な作業

- `DOMAIN` / `STATE_VERB` 語彙の正式レジストリ化（Registry Agentの管理下に置き、追加申請フローを定義）
- 各Agentの `contract-domain-query-v1` の実フィールド定義（ドメインごとの `payload` 内スキーマ）
- Escalation裁定ロジック（PMOS Directorの意思決定アルゴリズム）の具体化
