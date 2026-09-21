# PMOS Executive Dashboard — UI & Indicator Specification v1.0

**Repository:** `07-Dashboards`
**Status:** Draft — 実装可能レベルの初版
**Depends on:** Knowledge Graph / Ontology v1.0, Agent Communication Protocol v1.0

---

## 1. 設計原則

このダッシュボードは「動いているシステムのモニタリング画面」ではなく、**PMOSアーキテクチャそのものの説明装置**として設計する。表示される数値はすべて、Section 4で定義した実在の `Indicator` ノードと `MI Code` メッセージに由来し、根拠不明のKPIは一切置かない。

画面遷移とデータ結合の両方を、Dashboard Agentが受け取る `contract-dashboard-payload-v1` に一元化する。これにより、ダッシュボードは「エージェント間通信の可視化結果」として機能し、単独のBIツールにはならない。

---

## 2. データ結合契約（Contract）

```json
{
  "$id": "contract-dashboard-payload-v1",
  "type": "object",
  "required": ["domain", "indicators", "cross_domain_links", "alerts", "as_of"],
  "properties": {
    "domain": { "type": "string", "enum": ["Agriculture","Health","Impact","Biosecurity","Climate","All"] },
    "indicators": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["indicator_id", "name", "current_value", "target_value", "state", "mi_code"],
        "properties": {
          "indicator_id": { "type": "string" },
          "name": { "type": "string" },
          "current_value": { "type": "number" },
          "target_value": { "type": "number" },
          "state": { "type": "string", "enum": ["IMPROVING","STABLE","DEGRADING","CRITICAL","RECOVERING"] },
          "mi_code": { "type": "string" },
          "confidence": { "type": "number" }
        }
      }
    },
    "cross_domain_links": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "from_indicator_id": { "type": "string" },
          "to_indicator_id": { "type": "string" },
          "relationship": { "type": "string", "const": "INFLUENCES" },
          "weight": { "type": "number" }
        }
      }
    },
    "alerts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "alert_id": { "type": "string" },
          "source_mi_code": { "type": "string" },
          "escalated_to": { "type": "string" },
          "reason": { "type": "string" }
        }
      }
    },
    "as_of": { "type": "string", "format": "date-time" }
  }
}
```

Dashboard Agentは、複数ドメインAgentからの `ASSERT` メッセージを購読し、この形式に集約してフロントエンドへ配信する（Section 5「相互作用パターン」5.2 Publish–Subscribeに準拠）。

---

## 3. 画面構成

### 3.1 画面遷移図

```
┌─────────────┐   ドメイン選択    ┌──────────────────┐
│  Overview   ├──────────────────▶│  Domain Detail    │
│  (全ドメイン)│                    │ (AGRIX/Health/…)  │
└──────┬──────┘                    └─────────┬─────────┘
       │ 相関パネルクリック                     │ Indicatorクリック
       ▼                                      ▼
┌─────────────────────┐              ┌──────────────────┐
│ Cross-Domain         │              │ Indicator Drilldown│
│ Correlation View      │              │ (履歴・provenance) │
└──────┬───────────────┘              └──────────────────┘
       │ Alertクリック
       ▼
┌─────────────────────┐
│ Escalation / Alert    │
│ Detail                │
└───────────────────────┘
```

### 3.2 Overview画面（ワイヤーフレーム）

```
──────────────────────────────────────────────────────────
  PMOS Executive Dashboard              [Domain: All ▾]  🔔3
──────────────────────────────────────────────────────────
  Planetary Metabolic Intelligence Score : 0.68  ▲ +0.03

  ┌─────────────┬─────────────┬─────────────┬────────────┐
  │ Agriculture │   Health    │   Impact    │ Biosecurity│
  │  DEGRADING  │  IMPROVING  │  DEGRADING  │   STABLE   │
  │   ● 0.23    │   ● 0.15    │   ● 0.31    │   ● 0.04   │
  └─────────────┴─────────────┴─────────────┴────────────┘

  Cross-Domain Correlation
  ──────────────────────────────────────────────────────
   AGRIX Nitrogen Cycle ──0.74──▶ Water Quality Index
   Water Quality Index  ──0.42──▶ Health Waterborne Exposure
  ──────────────────────────────────────────────────────

  Active Alerts (3)
   ⚠ HealthBook Agent escalated corr-7788 (confidence 0.42)
   ⚠ AGRIX A12 nitrogen cycle: DEGRADING (0.23)
   ⚠ Impact water-quality-index: DEGRADING (0.31)
──────────────────────────────────────────────────────────
```

色（状態）マッピングは Agent Protocol の `STATE_VERB` にそのまま対応させる。

| STATE_VERB | 色 | 記号 |
|---|---|---|
| IMPROVING | 緑 | ● |
| STABLE | 青 | ● |
| DEGRADING | 橙 | ● |
| CRITICAL | 赤 | ● |
| RECOVERING | 黄緑 | ● |

### 3.3 Domain Detail画面（AGRIX例）

```
──────────────────────────────────────────────────────────
  ◀ Overview        Agriculture — Field Block A12
──────────────────────────────────────────────────────────
  Nitrogen Cycle                          state: DEGRADING
  ─────────────────────────
  current: 0.23   target: 0.05   confidence: 0.87
  mi_code: MI-AGRIX-NITROGEN_CYCLE-DEGRADING-0.23-INDEX-0.87
  provenance: agrix:study-runoff-2026-03

  [Trend Chart: 過去90日]

  Influences →
   Water Quality Index (weight 0.74)
──────────────────────────────────────────────────────────
```

### 3.4 Cross-Domain Correlation View

`cross_domain_links` 配列を有向グラフとして描画する。ノードは `Indicator`、エッジは `INFLUENCES`（weight付き）。Section 2のKnowledge Graphの `INFLUENCES` エッジをそのまま可視化レイヤーへ渡すだけで実装できる。

### 3.5 Alert / Escalation Detail画面

Agent Protocol Section 7 Step 4の `ESCALATE` メッセージを1件ずつ表示する。

```
──────────────────────────────────────────────────────────
  Alert: corr-7788
──────────────────────────────────────────────────────────
  from: healthbook-agent → pmos-director
  mi_code: MI-HEALTH-WATERBORNE_EXPOSURE-STABLE-0.05-INDEX-0.42
  confidence: 0.42  (閾値0.5未満)
  reason: 地域健康データが不足しており確信度が低い
  related: agrix:nitrogen-cycle-001, impact:water-quality-index
  status: PMOS Director裁定待ち
──────────────────────────────────────────────────────────
```

---

## 4. Indicator定義（実データ根拠あり）

以下は、Knowledge Graph仕様書 Section 2で定義済みの実インスタンスに基づくIndicatorのみを掲載する。仮の目標値ではなく、Pathwayの `efficiency_metric` 参照から導出する。

| indicator_id | 名称 | current | target | 算出方法 |
|---|---|---|---|---|
| `agrix:indicator-nue-A12` | 窒素利用効率（A12区画） | 0.23 | 0.05 | `output_flows.soil_nitrogen_runoff / input_flows.synthetic_fertilizer_input` |
| `impact:water-quality-index` | 水質インパクト指標 | 0.31 | 0.10 | AGRIX runoffデータの正規化スコア（Section 3.3 `INFLUENCES` weight適用） |
| `healthbook:indicator-hba1c-p3391` | HbA1c推移（コホートP3391） | 0.15改善 | — | `output_flows.hba1c_trend` の90日移動平均 |
| `healthbook:indicator-glycemic-efficiency-p3391` | 血糖代謝効率 | 0.15 | 0.30 | Pathway `glucose-metabolism-p3391.efficiency_metric` |

**Planetary Metabolic Intelligence Score**（Overview画面冒頭の統合指標）は、上記Indicatorの `state` を `STATE_VERB→数値` 変換（IMPROVING=1, STABLE=0.5, DEGRADING=0.25, CRITICAL=0, RECOVERING=0.75）した加重平均として定義する。これも「雰囲気の数値」ではなく、実際のMIコードから機械的に導出される値である。

---

## 5. コンポーネント実装マッピング（フロントエンド）

| UI要素 | データソース | 更新トリガー |
|---|---|---|
| Domain Summary Card | `contract-dashboard-payload-v1.indicators` | Dashboard AgentのNOTIFY受信時 |
| Cross-Domain Correlation Graph | `.cross_domain_links` | 同上 |
| Alert Panel | `.alerts` | Agent ProtocolのESCALATEイベント |
| Trend Chart | Knowledge Graph `Indicator` ノードの時系列履歴（別途`indicator-history`コレクションが必要） |

---

## 6. ファイル配置規約

```
07-Dashboards/
├── contracts/
│   └── contract-dashboard-payload-v1.schema.json
├── wireframes/
│   ├── overview.md
│   ├── domain-detail.md
│   ├── cross-domain-correlation.md
│   └── alert-detail.md
└── indicators/
    └── indicator-catalog.md   ← Section 4の表
```

---

## 7. 次に必要な作業

- `Indicator` の時系列履歴を保持する `indicator-history` コレクション設計（Trend Chart用）
- Planetary Metabolic Intelligence Scoreの重み付けロジックのADR化
- 実フロントエンド技術選定（React + Rechartsを想定、他候補との比較ADR）
