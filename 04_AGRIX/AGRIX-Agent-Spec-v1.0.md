---
tag: AgriWare
---
# AGRIX Agent Specification v1.0

**Repository:** `03-AGRIX/agent`
**Layer:** 2（Domain Implementation — ADR-001準拠）
**Conforms to:** Agent Communication Protocol v1.0（`contract-domain-query-v1` / `contract-mi-code-v1`）

---

## 1. Agentノード定義

```json
{
  "id": "agent:agrix",
  "type": "Agent",
  "domain": "Agriculture",
  "name": "AGRIX Agent",
  "agent_role": "DomainAgent",
  "responsibilities": [
    "圃場レベルの代謝経路（窒素・水・炭素循環）の状態評価",
    "IoTセンサー・衛星データ・投入記録からのIndicator算出",
    "Knowledge CoordinatorからのQUERYへのASSERT応答",
    "安全閾値超過時のPMOS Directorへの強制エスカレーション"
  ],
  "input_contract_ref": "contract:domain-query-v1",
  "output_contract_ref": "contract:mi-code-v1",
  "communication_endpoints": ["knowledge-coordinator", "pmos-director", "dashboard-agent"]
}
```

---

## 2. ドメイン語彙（PATHWAY_CODE レジストリ登録）

Agent Communication Protocol v1.0 Section 4の `PATHWAY_CODE` に対し、AGRIX Agentが管理する語彙は以下の通り。新規追加はRegistry Agentへの申請を要する（Protocol Section 8, `E-VOCAB-002`参照）。

| PATHWAY_CODE | 対象 | 単位系 |
|---|---|---|
| `NITROGEN_CYCLE` | 窒素循環（施肥→流出） | INDEX |
| `WATER_CYCLE` | 灌漑・土壌水分循環 | INDEX |
| `CARBON_SEQUESTRATION` | 土壌炭素貯留 | RATE |
| `PEST_PRESSURE` | 病害虫リスク | INDEX |
| `SOIL_HEALTH_INDEX` | 土壌総合健全度 | INDEX |

---

## 3. データソース

| ソース | 提供データ | 更新頻度 |
|---|---|---|
| 土壌IoTセンサー | pH, 水分率, EC値 | 15分毎 |
| 衛星NDVI | 植生指数 | 週次 |
| 投入記録（施肥・農薬） | 種類, 量, 日時 | イベント毎 |
| 土壌検査ラボ | 窒素・リン・カリウム含有量 | 四半期 |

---

## 4. `contract-domain-query-v1` ペイロード拡張（AGRIX固有）

```json
{
  "$id": "agrix-payload-extension-v1",
  "type": "object",
  "properties": {
    "field_block_id": { "type": "string" },
    "ph": { "type": "number" },
    "soil_moisture_pct": { "type": "number" },
    "ndvi": { "type": "number", "minimum": -1, "maximum": 1 },
    "runoff_kg_per_ha": { "type": "number" },
    "pesticide_residue_ppm": { "type": "number" }
  }
}
```

---

## 5. 既知のMetabolicPathwayインスタンス

**`agrix:nitrogen-cycle-001`**（Knowledge Graph Spec v1.0で定義済み）

```
state: DEGRADING (0.23)  confidence: 0.87
出力: MI-AGRIX-NITROGEN_CYCLE-DEGRADING-0.23-INDEX-0.87
```

**`agrix:carbon-sequestration-A12`**（新規追加）

```json
{
  "id": "agrix:carbon-sequestration-A12",
  "type": "MetabolicPathway",
  "domain": "Agriculture",
  "name": "Carbon Sequestration — Field Block A12",
  "input_flows": [
    { "flow_name": "cover_crop_biomass", "unit": "t/ha", "source_entity_id": "agrix:planting-log-A12" }
  ],
  "output_flows": [
    { "flow_name": "soil_organic_carbon_delta", "unit": "t/ha/yr", "target_entity_id": "agrix:indicator-soc-A12" }
  ],
  "efficiency_metric": "agrix:indicator-soc-A12",
  "state": "IMPROVING",
  "source_repository": "AGRIX",
  "source_path": "knowledge/pathways/carbon-sequestration-A12.md"
}
```

MIコード出力例: `MI-AGRIX-CARBON_SEQUESTRATION-IMPROVING-0.11-RATE-0.79`

---

## 6. エスカレーションルール（AGRIX固有の追加条件）

Agent Protocol Section 5.3の一般ルール（confidence<0.5、他ドメインとの矛盾）に加え、AGRIX Agentは以下の場合、confidenceに関わらず**強制的に`ESCALATE`（priority=critical）**を発行する。

- `pesticide_residue_ppm` が規制基準値を超過した場合
- `NDVI` が7日間で0.15以上急落した場合（作物ストレスの急性シグナル）

これは食品安全・環境規制に関わるため、通常のconfidence閾値ロジックより優先される。

---

## 7. ファイル配置規約

```
03-AGRIX/
├── agent/
│   └── agrix-agent-spec.md          ← 本文書
├── knowledge/
│   └── pathways/
│       ├── nitrogen-cycle-001.md
│       └── carbon-sequestration-A12.md
└── data-sources/
    └── iot-integration.md
```

---

## 8. 次に必要な作業

- 実際のIoTセンサーAPI仕様（プロトコル・認証方式）の確定
- `pesticide_residue_ppm` の規制基準値テーブル（国・作物別）の整備
