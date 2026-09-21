このスレッドでは、貴方に、下記の多くのコードを作成してもらっています。
重複すると思いますが、各コードの導入に関して、順次、指示してください。

`/pbpe-demo/model.py`

`/pbpe-demo/simulation.py

`/pbpe-demo/parameters.json`

`/pbpe-demo/model.py`（M3接続版）

`/pbpe-demo/simulation.py`

`/pbpe-demo/app.py`（UI完成）


```text
/pbpe-demo
  ├── model.py
  ├── simulation.py
  ├── parameters.json
  ├── data/
  │     └── country_coffee_sample.csv
  ├── pbpe_token.py
  ├── app.py
```
## `/pbpe-demo/data/country_coffee_sample.csv`

```csv
country,yield_base,cost_base,co2_base,waste_input
Brazil,1.0,1200,800,1.2
Vietnam,0.9,900,700,1.0
Ethiopia,0.6,600,500,0.8
Colombia,0.8,1000,650,1.1
```

# ✅ ② PBPEトークンモデル

## `/pbpe-demo/pbpe_token.py`

```python
def pbpe_price(yield_val, co2_reduction, cost_reduction):
    """
    価値通貨モデル（簡略）
    """

    return (
        yield_val * 100
        + co2_reduction * 0.5
        + cost_reduction * 0.3
    )
```

---

# ✅ ③ シミュレーション拡張（国別対応）
## `/pbpe-demo/simulation.py`（差し替え）

# ✅ ④ UI（投資家デモ版）

## `/pbpe-demo/app.py`

# ✅ ① Azure本番接続（実装可能形）

## `/pbpe-demo/azure_connector.py`

# ✅ ② PBPEトークン経済（完全版）

## `/pbpe-demo/token_economics.py`

# ✅ ③ 投資家レポート自動生成（PPT）

## `/pbpe-demo/report_generator.py`

# ✅ ④ app.py（完全統合版）

# 🚀 ① 実圃場データ接続（日本・アフリカ）

## `/pbpe-demo/data/field_data_sample.csv`

```csv
field_id,country,soil_C,soil_N,moisture,yield_obs,co2_obs,waste_input
JP-01,Japan,2.5,0.2,0.6,1.2,300,0.8
KE-01,Kenya,1.2,0.1,0.4,0.6,500,1.0
GH-01,Ghana,1.0,0.08,0.5,0.5,550,1.2
```

## `/pbpe-demo/field_adapter.py`

# 🚀 ② Azure IoT / Digital Twin 完全統合

## `/pbpe-demo/azure_iot.py`

## `/pbpe-demo/digital_twin.py`

# 🚀 ③ カーボンクレジット（Verra準拠モデル）

## `/pbpe-demo/carbon_credit.py`

# 🚀 ④ HealthBook連携（栄養→健康）

## `/pbpe-demo/health_link.py`

# 🚀 ⑤ AGRIXファンド（ACAINモデル）

## `/pbpe-demo/fund_model.py`

# 🚀 最終統合（app.py拡張）

## `/pbpe-demo/app.py（最終版）`

# 🚀 ② データパイプライン（ETL）

## `/pbpe-demo/pipeline.py`

# 🚀 ③ 衛星データ統合（NDVI）

## `/pbpe-demo/satellite.py`

# 🚀 ④ IoTセンサー統合

## `/pbpe-demo/iot_ingest.py`

# 🚀 ⑤ デジタルツイン更新（リアルタイム）

## `/pbpe-demo/twin_orchestrator.py`

# 🚀 ⑦ Azure ML 推論エンドポイント

## `/pbpe-demo/azure_ml.py`

---

了解。  
混在しているコードを**依存関係ベースで「導入順」＝そのまま作業手順**として整理する。  
（この順番以外で入れると動かない）

---

# 🚀 全体導入順（絶対順序）

```text
STEP 0：環境構築
STEP 1：コアモデル
STEP 2：シミュレーション
STEP 3：最小UI（動作確認）
STEP 4：経済レイヤー（PBPE）
STEP 5：投資家UI
STEP 6：外部接続（Azure）
STEP 7：実データ接続
STEP 8：統合拡張（Health / Carbon / Fund）
STEP 9：データ基盤（ETL / Satellite / IoT）
```

---

# 🧱 STEP 0：環境構築

```bash
pip install streamlit pandas numpy python-pptx requests azure-iot-device azure-identity azure-digitaltwins-core
```

---

# 🧠 STEP 1：コアモデル（最優先）

## ① `/pbpe-demo/parameters.json`

👉 最初に作る（全体の定数）

---

## ② `/pbpe-demo/model.py`（M3接続版）

👉 **必ずこちらを採用（旧modelは破棄）**

依存：

```text
parameters.json
```

---

# 🔁 STEP 2：シミュレーション

## `/pbpe-demo/simulation.py`

👉 model.pyを呼び出す

依存：

```text
model.py
parameters.json
```

---

# 🖥 STEP 3：最小UI（ここで一度動かす）

## `/pbpe-demo/app.py（簡易版）`

👉 この時点では以下のみ：

```text
・MBT ON/OFF
・Yield / Cost / CO2 表示
```

---

# 💰 STEP 4：経済レイヤー

## ① `/pbpe-demo/pbpe_token.py`

```text
→ PBPEスコア算出
```

---

## ② `/pbpe-demo/token_economics.py`

```text
→ 分配・投資構造
```

---

## ③ `/pbpe-demo/carbon_credit.py`

```text
→ CO2 → 価格化
```

---

# 🌍 STEP 5：投資家UI

## `/pbpe-demo/app.py（拡張）`

追加：

```text
・PBPE Value
・Carbon Credit
・IRR
・ON/OFF比較グラフ
```

---

# ☁️ STEP 6：外部接続

## ① `/pbpe-demo/azure_connector.py`

👉 REST接続

---

## ② `/pbpe-demo/azure_iot.py`

👉 IoT Hub

---

## ③ `/pbpe-demo/digital_twin.py`

👉 Digital Twin

---

## ④ `/pbpe-demo/twin_orchestrator.py`

👉 統合更新

---

# 🌾 STEP 7：実データ接続

## ① `/pbpe-demo/data/country_coffee_sample.csv`

👉 まずこれ

---

## ② `/pbpe-demo/data/field_data_sample.csv`

👉 次に圃場データ

---

## ③ `/pbpe-demo/field_adapter.py`

👉 CSV → モデル入力変換

---

# 🧬 STEP 8：統合拡張

## ① `/pbpe-demo/health_link.py`

```text
Yield → Nutrition → Health
```

---

## ② `/pbpe-demo/fund_model.py`

```text
PBPE + Carbon → IRR
```

---

## ③ `/pbpe-demo/report_generator.py`

```text
PPT出力
```

---

# 🛰 STEP 9：データ基盤

## ① `/pbpe-demo/pipeline.py`

```text
ETL処理
```

---

## ② `/pbpe-demo/satellite.py`

```text
NDVI → Yield推定
```

---

## ③ `/pbpe-demo/iot_ingest.py`

```text
センサーデータ
```

---

## ④ `/pbpe-demo/azure_ml.py`

```text
推論API
```

---

# ⚠️ 重要ルール（これを守らないと破綻）

## ① modelは1つだけ

```text
model.py（M3版）だけ使う
```

---

## ② simulationは1つだけ

```text
simulation.py（最終版のみ）
```

---

## ③ app.pyは段階更新

```text
簡易 → 投資家 → 完全統合
```

---

# 🔥 最短動作ルート（これだけやれば動く）

```text
① parameters.json
② model.py
③ simulation.py
④ app.py（簡易）
```

---

# 🚀 フル機能到達ルート

```text
＋ pbpe_token
＋ carbon_credit
＋ fund_model
＋ app拡張
＋ Azure接続
＋ field_data
＋ pipeline
```

---

# 🎯 完成状態

```text
ローカル：
→ Streamlitで即動く

クラウド：
→ Azure Digital Twin接続

投資：
→ IRR表示

社会：
→ CO2・健康まで接続
```

---

# 🚀 次にやるべき具体作業（指示）

```text
① STEP1〜3を一気に実装（30分）
② Streamlit起動確認
③ STEP4追加（PBPE表示）
④ UIを投資家仕様に変更
```

---

必要なら次は：

```text
・「エラーが出ない完成ディレクトリ構成」
・GitHubにそのまま上げるzip
```

まで一気に仕上げる。