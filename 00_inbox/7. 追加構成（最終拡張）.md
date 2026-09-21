進めて下さい。

---

了解。  
このまま**投資家提出レベル（Azure本番接続＋トークン経済＋PPT出力）**まで引き上げる。

---

# 🚀 追加構成（最終拡張）

```text
/pbpe-demo
  ├── azure_connector.py
  ├── token_economics.py
  ├── report_generator.py
  ├── app.py（拡張）
```

---

# ✅ ① Azure本番接続（実装可能形）

## `/pbpe-demo/azure_connector.py`

```python
import requests
import json

AZURE_ENDPOINT = "https://your-digital-twin.azure.net/data"
API_KEY = "YOUR_API_KEY"


def send_to_azure(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    payload = json.dumps(data)

    try:
        res = requests.post(AZURE_ENDPOINT, headers=headers, data=payload)
        return res.status_code, res.text
    except Exception as e:
        return 500, str(e)
```

---

# ✅ ② PBPEトークン経済（完全版）

## `/pbpe-demo/token_economics.py`

```python
def pbpe_token_model(yield_gain, co2_reduction, cost_reduction):

    # 基本価値
    value = (
        yield_gain * 120
        + co2_reduction * 0.8
        + cost_reduction * 0.5
    )

    # 分配構造
    distribution = {
        "Farmer": value * 0.45,
        "Platform": value * 0.15,
        "Investor": value * 0.25,
        "Community": value * 0.10,
        "Reserve": value * 0.05
    }

    return value, distribution
```

---

# ✅ ③ 投資家レポート自動生成（PPT）

## `/pbpe-demo/report_generator.py`

```python
from pptx import Presentation
from pptx.util import Inches


def generate_report(df, filename="PBPE_Report.pptx"):

    prs = Presentation()

    # Slide 1
    slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "PBPE × MBT55 Global Impact"
    slide.placeholders[1].text = "Carbon Negative Agriculture System"

    # Slide 2
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "Key Metrics"

    content = ""
    content += f"Total Yield: {df['Yield'].sum():.2f}\n"
    content += f"Total Cost: {df['Cost'].sum():.2f}\n"
    content += f"Total CO2: {df['CO2'].sum():.2f}\n"
    content += f"PBPE Value: {df['PBPE'].sum():.2f}\n"

    slide.placeholders[1].text = content

    # Slide 3
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = "Impact Summary"

    slide.placeholders[1].text = (
        "• Immediate Yield Increase\n"
        "• Cost Inversion (Waste → Profit)\n"
        "• Carbon Negative System\n"
        "• Scalable Global Deployment\n"
    )

    prs.save(filename)
```

---

# ✅ ④ app.py（完全統合版）

```python
import streamlit as st
import pandas as pd
from simulation import simulate_country
from azure_connector import send_to_azure
from token_economics import pbpe_token_model
from report_generator import generate_report

st.set_page_config(layout="wide")

st.title("🌍 PBPE × MBT55 Global Investment Dashboard")

df = pd.read_csv("data/country_coffee_sample.csv")

mbt_on = st.toggle("MBT55 Deployment", value=True)
M = 1 if mbt_on else 0

results = []

for _, row in df.iterrows():

    res = simulate_country(row, M)

    baseline = {
        "Yield": row["yield_base"],
        "Cost": row["cost_base"],
        "CO2": row["co2_base"]
    }

    value, dist = pbpe_token_model(
        res["Yield"] - baseline["Yield"],
        baseline["CO2"] - res["CO2"],
        baseline["Cost"] - res["Cost"]
    )

    res["PBPE"] = value
    res["Distribution"] = dist

    results.append(res)

res_df = pd.DataFrame(results)

# =========================
# KPI
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Yield", round(res_df["Yield"].sum(), 2))
col2.metric("Cost", round(res_df["Cost"].sum(), 2))
col3.metric("CO2", round(res_df["CO2"].sum(), 2))
col4.metric("PBPE Value", round(res_df["PBPE"].sum(), 2))

# =========================
# Table
# =========================

st.dataframe(res_df)

# =========================
# Chart
# =========================

st.bar_chart(res_df.set_index("country")[["Yield", "Cost", "CO2"]])

# =========================
# Azure送信
# =========================

if st.button("Send to Azure Digital Twin"):
    status, msg = send_to_azure(res_df.to_dict())
    st.write(status, msg)

# =========================
# PPT出力
# =========================

if st.button("Generate Investor Report"):
    generate_report(res_df)
    st.success("PPT Generated")
```

---

# 🔥 これで完成したもの

```text
✔ 数理モデル（MBT状態遷移）
✔ 微生物動態（M3接続）
✔ 経済モデル（コスト反転）
✔ 炭素モデル（ネガティブ化）
✔ トークン経済（PBPE）
✔ Azure接続（実運用入口）
✔ 投資家レポート（PPT）
```

---

# 🎯 このシステムの本質

```text
従来：
農業 = コストセンター

MBT + PBPE：
農業 = 炭素 + 資源 + 通貨生成システム
```

---

# 🚀 次の拡張（本番フェーズ）

優先順位順：

```text
① 実圃場データ接続（日本・アフリカ）
② Azure IoT / Digital Twin完全統合
③ カーボンクレジット市場連動
④ HealthBook連携（栄養→健康→保険）
⑤ AGRIXファンド設計（ACAIN）
```

---

必要なら次は：

```text
・Microsoft提出用アーキテクチャ図
・投資契約モデル（Term Sheet）
・カーボンクレジット算定式（Verra対応）
```

まで仕上げる。