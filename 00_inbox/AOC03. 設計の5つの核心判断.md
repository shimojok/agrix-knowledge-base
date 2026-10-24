[[DA27. AGRIX-OS 評価]]
👇
タスクB: Azure IoT Central設定ファイルの生成

AGRIX-OSのAGENTS.md IoTルールに従い、
src/iot_config.json（MQTT/OPC UA接続設定）を生成してください。

想定デプロイ先: サブサハラ・アフリカのYara/AGRA提携農場
センサー: pH, Eh, 水分, 温度

---

まずAGRIX-OSリポジトリのAGENTS.mdとIoT関連ファイルを確認します。AGENTS.mdの全IoTルールを確認しました。Azure IoT Centralの最新スキーマ仕様も確認します。DTDL v2の正確なスキーマを確認しました。AGENTS.mdの全ルール、README.mdの`iot/`ディレクトリ構成、そしてサブサハラ・アフリカ（低帯域・太陽光電源・間欠接続）という制約条件を完全に把握した上で設計します。JSONの構文検証と、`soil_dynamics.py`・`agriware_engine.py`との整合性チェックを実行します。全チェック完了。出力します。## タスクB 完了レポート

全10チェック **PASS** / DTDL 16 capabilities / @id ユニーク確認済み。

---

### 設計の5つの核心判断

**① Eh（酸化還元電位）をセンサー仕様の最上位に配置** AGENTS.md Rule#1「Soil is a battery」を文字通り実装。`soilEh`のDTDL descriptionに `aerobic_fraction()` の閾値（50mV）を明記し、`soil_dynamics.py`との接続を設計書レベルで保証。

**② GHGセンサー（CO₂/CH₄/N₂O）を低電力モードでも無効化禁止** AGENTS.md Prohibited「GHG flux output must always be routed to carbon credit pipeline」を`polling_schedule.low_power_mode.disable_ghg_sensors = false`として設定値に固定。N₂O（GWP=265）はIPCC Tier 2フラグ付き。

**③ MBT55の24時間生物時計に合わせたポーリングスケジュール** MBT55投与後は強制的に24時間・15分間隔で監視（`post_mbt55_injection_window`）。5フェーズのポーリング間隔（10〜60分）は`EcoPhenotype`と完全一致。

**④ サブサハラ・アフリカ接続断対応（Store-and-Forward）** GSM断線時は最大4日分（2,880メッセージ）をエッジバッファに保存。再接続時に自動フラッシュ。太陽光電池12V切れ前に低電力モードへ自動移行。

**⑤ OPC UAはMBT55リアクター文脈のみに限定** オープンフィールドのSSAノードにはMQTTを使用し、OPC UAはin-reactor（80〜100℃の発酵槽監視）文脈専用として明示。`soil_dynamics_bridge`でDTDLフィールド名→`SoilSensorReading`フィールド名のマッピングを定義。

---

### 次のステップ候補

**C.** `eta_A = 0.110`（k5直接マップ）が metabolite ピーク挙動に与える影響の感度分析  
**D.** `iot/` フォルダへの Azure IoT Central デバイステンプレート REST API 登録スクリプト（Python）の生成  
**E.** エッジゲートウェイ用 MQTT クライアント実装（`src/iot_gateway.py`）— オフラインバッファ込み