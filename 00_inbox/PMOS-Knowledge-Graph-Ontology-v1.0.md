# PMOS Knowledge Graph / Ontology Specification v1.0

**Repository:** `02-BioNexus-Core/knowledge-graph`
**Status:** Draft — 実装可能レベルの初版
**Depends on:** PMOS Architecture Book, Repository Atlas

---

## 1. 設計原則

1. **Property Graph モデル**を採用する（ノード＋型付きエッジ＋プロパティ）。GraphQLやNeo4j、あるいはJSON-LDへの変換を前提に設計する。
2. AGRIX / HealthBook / PBPE の各ドメイン固有ノードは、すべて共通の抽象ノード `MetabolicEntity` を継承する。これにより「農業の窒素循環」と「人体の代謝経路」と「資本の循環」を、**同じグラフ構造の上で横断的に比較・推論できる**ことがPMOSの新規性の核になる。
3. **1ノード＝1ファイル**の原則。GitHub上の実ファイルとナレッジグラフのノードは1対1で対応させ、グラフはGitHubを正典（Single Source of Truth）とする導出物として扱う。
4. Pineconeにはノードのテキスト表現のみをベクトル化して格納し、構造（型・エッジ）はグラフ側が保持する。Pineconeは意味検索の索引にすぎない。

---

## 2. コアノード型（Core Node Types）

### 2.1 `MetabolicEntity`（抽象基底型）

すべてのノードが継承する共通フィールド。

```json
{
  "$id": "MetabolicEntity",
  "type": "object",
  "required": ["id", "type", "domain", "name", "created_at", "source_repository", "source_path"],
  "properties": {
    "id": { "type": "string", "pattern": "^[a-z]+:[a-z0-9-]+$", "description": "例: agrix:nitrogen-cycle-001" },
    "type": { "type": "string", "enum": ["KnowledgeAsset","Concept","MetabolicPathway","Indicator","Agent","DataContract","ADR","Repository","Dashboard","DemoScenario"] },
    "domain": { "type": "string", "enum": ["Agriculture","Health","Impact","Biosecurity","Climate","Governance"] },
    "name": { "type": "string" },
    "description": { "type": "string" },
    "unit_system": { "type": "string", "enum": ["SI","Index","Currency","Composite"], "default": "Index" },
    "status": { "type": "string", "enum": ["draft","review","approved","published","deprecated"] },
    "created_at": { "type": "string", "format": "date-time" },
    "updated_at": { "type": "string", "format": "date-time" },
    "source_repository": { "type": "string" },
    "source_path": { "type": "string" }
  }
}
```

### 2.2 `MetabolicPathway`（PMOS独自の中核ノード）

ドメイン横断の「流れ」を表すノード。AGRIXの窒素循環、HealthBookの糖代謝経路、PBPEの資本循環は、すべてこの型のインスタンスとして表現される。

```json
{
  "$id": "MetabolicPathway",
  "allOf": [{ "$ref": "MetabolicEntity" }],
  "type": "object",
  "required": ["input_flows", "output_flows", "efficiency_metric"],
  "properties": {
    "input_flows": {
      "type": "array",
      "items": { "type": "object", "properties": {
        "flow_name": { "type": "string" },
        "unit": { "type": "string" },
        "source_entity_id": { "type": "string" }
      }}
    },
    "output_flows": {
      "type": "array",
      "items": { "type": "object", "properties": {
        "flow_name": { "type": "string" },
        "unit": { "type": "string" },
        "target_entity_id": { "type": "string" }
      }}
    },
    "efficiency_metric": { "type": "string", "description": "この経路のIndicatorノードへの参照ID" },
    "state": { "type": "string", "enum": ["IMPROVING","STABLE","DEGRADING","CRITICAL","RECOVERING"] }
  }
}
```

**例（AGRIX側インスタンス）**

```json
{
  "id": "agrix:nitrogen-cycle-001",
  "type": "MetabolicPathway",
  "domain": "Agriculture",
  "name": "Nitrogen Cycle — Field Block A12",
  "input_flows": [
    { "flow_name": "synthetic_fertilizer_input", "unit": "kg/ha", "source_entity_id": "agrix:input-log-A12" }
  ],
  "output_flows": [
    { "flow_name": "soil_nitrogen_runoff", "unit": "kg/ha", "target_entity_id": "impact:water-quality-index" }
  ],
  "efficiency_metric": "agrix:indicator-nue-A12",
  "state": "DEGRADING",
  "source_repository": "AGRIX",
  "source_path": "knowledge/pathways/nitrogen-cycle-001.md",
  "created_at": "2026-07-01T00:00:00Z"
}
```

**例（HealthBook側インスタンス — 同じ型を使う）**

```json
{
  "id": "healthbook:glucose-metabolism-p3391",
  "type": "MetabolicPathway",
  "domain": "Health",
  "name": "Glucose Metabolism — Patient Cohort P3391",
  "input_flows": [
    { "flow_name": "dietary_carbohydrate_intake", "unit": "g/day", "source_entity_id": "healthbook:intake-log-p3391" }
  ],
  "output_flows": [
    { "flow_name": "hba1c_trend", "unit": "%", "target_entity_id": "healthbook:indicator-hba1c-p3391" }
  ],
  "efficiency_metric": "healthbook:indicator-glycemic-efficiency-p3391",
  "state": "IMPROVING"
}
```

同じ `MetabolicPathway` 型を使うことで、後述のエージェント間通信でも「農業の窒素循環の悪化」と「患者の血糖効率の改善」を**同一の意味構造で比較・相関分析できる**。これがPMOSの「Planetary Metabolic Intelligence」の技術的な実体になる。

### 2.3 `Indicator`

```json
{
  "$id": "Indicator",
  "allOf": [{ "$ref": "MetabolicEntity" }],
  "required": ["value_type", "computation_method"],
  "properties": {
    "value_type": { "type": "string", "enum": ["numeric","categorical","index_0_1"] },
    "computation_method": { "type": "string" },
    "current_value": { "type": "number" },
    "target_value": { "type": "number" },
    "data_source": { "type": "string" },
    "last_computed_at": { "type": "string", "format": "date-time" }
  }
}
```

### 2.4 `Agent`

```json
{
  "$id": "Agent",
  "allOf": [{ "$ref": "MetabolicEntity" }],
  "required": ["agent_role", "input_contract_ref", "output_contract_ref"],
  "properties": {
    "agent_role": { "type": "string", "enum": ["Director","KnowledgeCoordinator","DomainAgent","RegistryAgent","DashboardAgent","DemoAgent"] },
    "responsibilities": { "type": "array", "items": { "type": "string" } },
    "input_contract_ref": { "type": "string", "description": "DataContractノードのID" },
    "output_contract_ref": { "type": "string" },
    "communication_endpoints": { "type": "array", "items": { "type": "string" } }
  }
}
```

### 2.5 その他のノード型（簡略定義）

| 型 | 用途 | 主要プロパティ |
|---|---|---|
| `KnowledgeAsset` | ドキュメント／データセット／モデルの管理単位 | asset_type, format, version, authors |
| `Concept` | 用語・定義（Glossary） | definition, related_concepts[] |
| `DataContract` | エージェント間・リポジトリ間のスキーマ契約 | schema_ref, produced_by, consumed_by[], version |
| `ADR` | 設計決定記録 | decision_id, status, context, decision, consequences |
| `Repository` | GitHubリポジトリのメタ表現 | repo_name, url, contains[] |
| `Dashboard` | ダッシュボード定義 | kpis[], target_audience[] |
| `DemoScenario` | デモ台本 | steps[], target_audience[] |

---

## 3. エッジ型（Edge Types）

| エッジ | 方向 | 意味 | 重み |
|---|---|---|---|
| `PART_OF` | A→B | AはBの構成要素 | なし |
| `DERIVED_FROM` | A→B | AはBから派生（来歴） | なし |
| `MEASURED_BY` | MetabolicPathway→Indicator | この経路はこの指標で測定される | なし |
| `INFLUENCES` | MetabolicPathway→MetabolicPathway | ドメイン横断の因果・相関 | 0.0–1.0（相関強度） |
| `DEPENDS_ON` | KnowledgeAsset→KnowledgeAsset | 依存関係 | なし |
| `VALIDATED_BY` | KnowledgeAsset→ADR | この資産の正当性を裏付けるADR | なし |
| `COMMUNICATES_WITH` | Agent→Agent | 実際に通信するエージェント間関係 | 通信頻度（回/日） |
| `GOVERNED_BY` | Repository→ADR | このリポジトリを規定するADR | なし |
| `VISUALIZES` | Dashboard→Indicator | このダッシュボードが表示する指標 | なし |
| `DEMONSTRATES` | DemoScenario→KnowledgeAsset | このデモが提示する資産 | なし |

**ドメイン横断の実例:**

```json
{
  "edge": "INFLUENCES",
  "from": "agrix:nitrogen-cycle-001",
  "to": "impact:water-quality-index",
  "weight": 0.74,
  "evidence_ref": "agrix:study-runoff-2026-03"
}
```

これにより「A12区画の窒素循環悪化 → 水質指標の悪化 → PBPEの環境インパクトスコア低下」という**説明可能な因果チェーン**がグラフ上で追跡できる。これは単なるダッシュボードの飾りではなく、実際にエージェントが推論に使う構造である。

---

## 4. ファイル配置規約（GitHubマッピング）

```
02-BioNexus-Core/
└── knowledge-graph/
    ├── nodes/
    │   ├── metabolic-pathway/
    │   │   └── agrix-nitrogen-cycle-001.md   ← YAML frontmatter + 本文
    │   ├── indicator/
    │   ├── agent/
    │   └── data-contract/
    ├── edges/
    │   └── edges.jsonl                        ← 1行1エッジ（上記JSON形式）
    └── schema/
        ├── metabolic-entity.schema.json
        ├── metabolic-pathway.schema.json
        ├── indicator.schema.json
        └── agent.schema.json
```

各ノードファイルは、YAML frontmatterにスキーマ準拠のプロパティを書き、本文（Markdown）に人間可読な説明を書く。これによりGitHub上でそのまま読め、かつ機械可読でもある。

```markdown
---
id: agrix:nitrogen-cycle-001
type: MetabolicPathway
domain: Agriculture
state: DEGRADING
efficiency_metric: agrix:indicator-nue-A12
---

# Nitrogen Cycle — Field Block A12

A12区画における窒素循環の現状と、水質指標への影響について記述する。
```

---

## 5. Pinecone連携（メタデータマッピング）

| Pineconeフィールド | 由来 |
|---|---|
| `vector` | ノード本文（description + 本文Markdown）の埋め込み |
| `metadata.node_id` | `id` |
| `metadata.node_type` | `type` |
| `metadata.domain` | `domain` |
| `metadata.repository` | `source_repository` |

検索結果はまずPineconeで候補ノードIDを取得し、その後グラフ側で `edges.jsonl` を辿って関連ノード（`INFLUENCES`, `MEASURED_BY` 等）を展開する、という2段構成にする。これにより「意味的に近い」だけでなく「構造的に関連する」ノードもエージェントに渡せる。

---

## 6. 次に必要な作業

- 各ドメイン（AGRIX / HealthBook / PBPE）ごとの `MetabolicPathway` インスタンスの実データ棚卸し（最低10件ずつ）
- `edges.jsonl` の初期データ投入（ドメイン横断エッジを最低5本）
- スキーマのJSON Schema Draft 2020-12への正式変換とCI検証（GitHub Actions）