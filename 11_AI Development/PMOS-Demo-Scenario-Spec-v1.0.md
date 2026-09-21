# PMOS Interactive Demonstration — Scenario & Screen Flow Specification v1.0

**Repository:** `08-Demonstrations`
**Status:** Draft — 実装可能レベルの初版
**Depends on:** Knowledge Graph v1.0, Agent Communication Protocol v1.0, Executive Dashboard Spec v1.0

---

## 1. 設計原則

このデモは「全機能が実際に動く」ことを証明するものではない。目的は、**Microsoft / Gates財団クラスの評価者が15分以内に「このアーキテクチャは新しいプラットフォームになり得る」と判断できること**である（PMOS101で確定した目的定義に準拠）。

そのため台本は、Section 7で定義済みの実メッセージ交換（AGRIX窒素循環悪化 → HealthBook健康影響照会 → confidence不足によるエスカレーション）を、そのまま**単一の一貫したストーリー**としてなぞる構成にする。新しいデータ例を持ち出さず、既存の2文書と完全に一致させることで、質問されても矛盾が生じない。

---

## 2. デモ実行契約（Contract）

```json
{
  "$id": "contract-demo-narration-v1",
  "type": "object",
  "required": ["scenario_id", "steps"],
  "properties": {
    "scenario_id": { "type": "string" },
    "target_audience": { "type": "array", "items": { "type": "string" } },
    "steps": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["step_id", "screen", "trigger", "narration", "system_action"],
        "properties": {
          "step_id": { "type": "string" },
          "screen": { "type": "string" },
          "trigger": { "type": "string", "enum": ["presenter_click","auto_advance","live_agent_event"] },
          "narration": { "type": "string" },
          "system_action": { "type": "string" },
          "data_mode": { "type": "string", "enum": ["live","canned"], "default": "canned" },
          "duration_seconds": { "type": "integer" }
        }
      }
    }
  }
}
```

`data_mode` を明示的に持たせているのが実務上の要点。ライブデモ中にエージェント応答が遅延・失敗した場合、`canned`（事前記録済みのMIコード応答）へ即座にフォールバックできるようにする。これにより「ライブデモが壊れる」リスクを設計段階で潰す。

---

## 3. 台本（Demo Scenario: `demo:cross-domain-alert-001`）

**総尺: 約12分　対象: Microsoft / Gates財団 / Rockefeller Foundation**

| step_id | 画面 | トリガー | ナレーション（要約） | システム動作 | data_mode | 秒 |
|---|---|---|---|---|---|---|
| S1 | Welcome | auto_advance | 「PMOSは、農業・健康・インパクトを一つの意味構造で扱う、初めてのAIネイティブ・プラットフォームです」 | ロゴ表示のみ | canned | 30 |
| S2 | Overview Dashboard | presenter_click | 「4ドメインの状態が同時に見えます。今、農業と環境インパクトが悪化傾向です」 | `contract-dashboard-payload-v1` をロードしOverview描画 | canned | 60 |
| S3 | Domain Detail (AGRIX) | presenter_click | 「A12区画で窒素循環が悪化しています。これは単発の数値ではなく、実際にAGRIXエージェントがMIコードとして発信したものです」 | `MI-AGRIX-NITROGEN_CYCLE-DEGRADING-0.23-INDEX-0.87` を表示、生JSONメッセージも展開表示 | canned | 90 |
| S4 | Cross-Domain Correlation View | presenter_click | 「このAGRIXの悪化は、Knowledge Graphの`INFLUENCES`エッジを通じて水質指標、さらに人の健康リスクへ伝播しうると、PMOSは構造的に把握しています」 | `INFLUENCES`グラフを描画、AGRIX→Water Quality→Healthのパスをハイライト | canned | 90 |
| S5 | Agent Protocol Live View | presenter_click / live_agent_event | 「実際に、Knowledge CoordinatorがHealthBookエージェントに照会するところをご覧ください」 | ライブでAgent間メッセージ（Section 7 Step 3相当）を発火し、JSON生ログをストリーム表示 | **live**（失敗時はStep7の`corr-7788`ログにフォールバック） | 120 |
| S6 | Alert / Escalation Detail | auto_advance | 「HealthBook側はデータ不足で確信度0.42となり、閾値0.5未満のため自動的にPMOS Directorへエスカレーションされました。これは単なるエラーではなく、"人間の判断が必要"という誠実なシグナルです」 | Alert Detail画面（Executive Dashboard仕様 Section 3.5）を表示 | canned | 90 |
| S7 | Knowledge Graph Explorer | presenter_click | 「この一連の判断はすべて、GitHub上のノード・エッジとして残ります。ブラックボックスではありません」 | `agrix:nitrogen-cycle-001` から `impact:water-quality-index` への経路をグラフDB風に可視化 | canned | 90 |
| S8 | Roadmap / Partnership | auto_advance | 「これが、AGRIX・HealthBook・PBPEを貫く単一のアーキテクチャです。次の段階は、実データでのパイロット運用です」 | ロードマップ画面表示 | canned | 60 |

**合計: 630秒（約10.5分）+ Q&Aバッファ90秒 = 12分**

---

## 4. ライブ実行部分（S5）の技術要件

S5のみを `live` にする理由は、**デモ全体をライブにするリスクを避けつつ、「本当に動く」ことを1箇所だけ証明する**ため。

- 実行対象: Knowledge Coordinator → HealthBook Agentの `QUERY`/`ASSERT` 往復（Agent Protocol Section 7 Step 3-4と同一のcorrelation_idシナリオを再現）
- タイムアウト: `ttl_seconds` を通常より短い15秒に設定し、応答がなければ即座に `canned` ログ（Step 7の実例JSON）へ切替
- 表示: 生のMessageEnvelope JSONを画面右側にストリーム表示し、「装飾されたデモではなく実際のプロトコル」であることを示す

---

## 5. プレゼンター操作ガイド（抜粋）

```
S4 → S5 遷移時の実際の操作:
  1. 画面右下の "Trigger Live Query" ボタンをクリック
  2. system は knowledge-coordinator → healthbook-agent へ QUERY送信
  3. 15秒以内に ASSERT または ESCALATE を受信すればライブ表示を継続
  4. 受信なしの場合、自動的に "Recorded Session — corr-7788" ラベル付きでcannedログを表示
     （観客への説明: "本番同等の記録済みセッションです"）
```

---

## 6. ファイル配置規約

```
08-Demonstrations/
├── contracts/
│   └── contract-demo-narration-v1.schema.json
├── scenarios/
│   └── demo-cross-domain-alert-001.json   ← Section 3の表をJSON化したもの
├── canned-sessions/
│   └── corr-7788.jsonl                    ← Agent Protocol実例をそのまま格納
└── presenter-guide.md
```

---

## 7. 次に必要な作業

- Section 3の台本を `contract-demo-narration-v1` 準拠のJSONへ変換し `scenarios/` へ配置
- S5のライブクエリを実行するための最小Agent実装（Knowledge Coordinator・HealthBook Agentのモックサーバ）
- 12分尺のプレゼンター用リハーサル台本（実際の発話全文、現在は要約のみ）
