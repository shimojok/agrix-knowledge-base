# HealthBook Agent Specification v1.0

**Repository:** `04-HealthBook/agent`
**Layer:** 2（Domain Implementation — ADR-001準拠）
**Conforms to:** Agent Communication Protocol v1.0（`contract-domain-query-v1` / `contract-mi-code-v1`）

---

## 1. Agentノード定義

```json
{
  "id": "agent:healthbook",
  "type": "Agent",
  "domain": "Health",
  "name": "HealthBook Agent",
  "agent_role": "DomainAgent",
  "responsibilities": [
    "患者／コホートレベルの代謝経路（糖代謝・脂質代謝・環境曝露リスク）の状態評価",
    "ウェアラブル・臨床検査データからのIndicator算出",
    "Knowledge CoordinatorからのQUERYへのASSERT応答",
    "臨床的安全閾値超過時の人間レビュー必須エスカレーション"
  ],
  "input_contract_ref": "contract:domain-query-v1",
  "output_contract_ref": "contract:mi-code-v1",
  "communication_endpoints": ["knowledge-coordinator", "pmos-director", "dashboard-agent"]
}
```

---

## 2. ドメイン語彙（PATHWAY_CODE レジストリ登録）

| PATHWAY_CODE | 対象 | 単位系 |
|---|---|---|
| `GLUCOSE_METABOLISM` | 糖代謝効率 | INDEX |
| `LIPID_METABOLISM` | 脂質代謝 | INDEX |
| `WATERBORNE_EXPOSURE` | 水系環境曝露リスク（AGRIX由来データと連携） | INDEX |
| `RENAL_FUNCTION` | 腎機能 | INDEX |
| `CARDIOVASCULAR_LOAD` | 心血管負荷 | INDEX |

`WATERBORNE_EXPOSURE` は、AGRIX Agentの `impact:water-quality-index` を `INFLUENCES` エッジ経由で参照するドメイン横断語彙である（Agent Protocol Section 7 実例参照）。

---

## 3. データソースとプライバシー要件

| ソース | 提供データ | 更新頻度 |
|---|---|---|
| ウェアラブルデバイス | 血糖値連続測定, 心拍 | リアルタイム〜日次 |
| 臨床検査ラボ | HbA1c, LDL, eGFR | 月次〜四半期 |
| 患者摂取ログ | 炭水化物摂取量 | 日次 |
| 環境曝露データ（AGRIX/Impact連携） | 水質指標 | AGRIX側の更新頻度に準拠 |

**プライバシー原則（HealthBook固有・必須）**

- すべてのpayloadは患者個人を直接特定できない**コホート単位またはde-identified ID**で扱う（例: `p3391` はコホート内の匿名参照IDであり、実PHI（Protected Health Information）はGitHub/Pineconeに一切格納しない）。
- 実PHIは院内システムにとどめ、HealthBook AgentはIndicator値（集約・匿名化済み）のみを送受信する。
- この制約により、`natural_language_note` フィールドに患者を特定しうる記述を含めることを禁止する（Agent Protocol Section 3参照）。

---

## 4. `contract-domain-query-v1` ペイロード拡張（HealthBook固有）

```json
{
  "$id": "healthbook-payload-extension-v1",
  "type": "object",
  "properties": {
    "cohort_id": { "type": "string" },
    "hba1c_pct": { "type": "number" },
    "ldl_mg_dl": { "type": "number" },
    "egfr_ml_min": { "type": "number" },
    "carb_intake_g_day": { "type": "number" },
    "environmental_exposure_ref": { "type": "string", "description": "AGRIX/ImpactドメインのIndicator IDへの参照" }
  }
}
```

---

## 5. 既知のMetabolicPathwayインスタンス

**`healthbook:glucose-metabolism-p3391`**（Knowledge Graph Spec v1.0で定義済み）

```
state: IMPROVING (0.15)
出力: MI-HEALTH-GLUCOSE_METABOLISM-IMPROVING-0.15-INDEX-0.91
```

**`healthbook:renal-function-p3391`**（新規追加）

```json
{
  "id": "healthbook:renal-function-p3391",
  "type": "MetabolicPathway",
  "domain": "Health",
  "name": "Renal Function — Cohort P3391",
  "input_flows": [
    { "flow_name": "sodium_intake_mg_day", "unit": "mg/day", "source_entity_id": "healthbook:intake-log-p3391" }
  ],
  "output_flows": [
    { "flow_name": "egfr_trend", "unit": "ml/min/1.73m2", "target_entity_id": "healthbook:indicator-egfr-p3391" }
  ],
  "efficiency_metric": "healthbook:indicator-renal-efficiency-p3391",
  "state": "STABLE",
  "source_repository": "HealthBook",
  "source_path": "knowledge/pathways/renal-function-p3391.md"
}
```

MIコード出力例: `MI-HEALTH-RENAL_FUNCTION-STABLE-0.02-INDEX-0.68`

---

## 6. エスカレーションルール（HealthBook固有の追加条件）

Agent Protocol Section 5.3の一般ルールに加え、HealthBook Agentは以下の場合、confidenceに関わらず**強制的に`ESCALATE`（priority=critical）＋人間の臨床レビュー必須フラグ**を発行する。

- `hba1c_pct` が臨床的危険閾値（例: 9.0%）を超過した場合
- `egfr_ml_min` が急性腎機能低下を示す閾値を下回った場合
- Agent Protocol Section 7実例のように、`confidence < 0.5` で環境曝露リスクとの相関が疑われる場合（Waterborne Exposureの例）

健康ドメインでは、AGRIXと異なり**自動応答のみでダッシュボードに反映することを禁止**し、`CRITICAL`状態は必ず人間の確認を経てから `Dashboard Agent` へ配信する（`pmos-director`が裁定するまで `Alert Panel` には "Pending Clinical Review" 状態で表示）。

---

## 7. ファイル配置規約

```
04-HealthBook/
├── agent/
│   └── healthbook-agent-spec.md     ← 本文書
├── knowledge/
│   └── pathways/
│       ├── glucose-metabolism-p3391.md
│       └── renal-function-p3391.md
└── data-sources/
    └── privacy-deidentification-policy.md
```

---

## 8. 次に必要な作業

- 匿名化・de-identification方式の技術仕様（k-匿名性の基準値など）の確定
- 臨床的危険閾値テーブル（疾患・年齢層別）の医療監修による整備
- AGRIX側 `impact:water-quality-index` との `INFLUENCES` エッジの重み算出ロジックの確定
