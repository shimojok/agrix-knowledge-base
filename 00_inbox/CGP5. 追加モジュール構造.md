PBPE-Financeのdashboard/app.pyに、SafetyChain™動的価格決定モデルを統合してください。

## 追加機能
1. **4レイヤー価格シミュレーター**
   - P_total = P_market + V + L + m + C
   - スライダーで各レイヤーの係数を調整可能
   - MBT55処理 vs 慣行農業の価格差を表示

2. **医療費削減価値（m-ROI）計算**
   - 特定代謝産物（SCFA前駆体）の含有量 → 疾患予防価値に変換
   - 糖尿病・高血圧・大腸がんの予防貢献額を試算

3. **炭素クレジット小口決済シミュレーター**
   - 消費者1回の購入で発生する炭素クレジット量
   - 年間累積インパクトの表示

## 参照ドキュメント
添付の □2-11, ■GAI-4, SafetyChain™定義 を参照してください。

---

以下に **`dashboard/app.py`へ直接統合可能な実装コード**を提示します。  
既存PBPEダッシュボードに“SafetyChain™価値レイヤー”を追加する構成です。

---

# 🔧 追加モジュール構造

```python
# app.py 追記

import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
```

---

# ① SafetyChain™ 4レイヤー価格モデル

## 数式

```
P_total = P_market + V + L + m + C
```

- V：栄養価プレミアム（Functional Value）
    
- L：ロス削減価値
    
- m：医療費削減価値（m-ROI）
    
- C：カーボンクレジット価値
    

---

## UI + 計算

```python
st.header("🔗 SafetyChain™ Dynamic Pricing Model")

col1, col2 = st.columns(2)

with col1:
    P_market = st.slider("市場価格 (¥/kg)", 100, 2000, 500)
    V = st.slider("栄養価プレミアム V", 0, 500, 100)
    L = st.slider("ロス削減価値 L", 0, 300, 50)

with col2:
    m = st.slider("医療費削減価値 m", 0, 500, 120)
    C = st.slider("炭素価値 C", 0, 300, 80)

P_total = P_market + V + L + m + C

# 慣行農業比較
P_conventional = P_market
delta_price = P_total - P_conventional

st.metric("MBT55価格", f"¥{P_total}")
st.metric("従来価格", f"¥{P_conventional}")
st.metric("プレミアム差分", f"¥{delta_price}")
```

---

## 可視化（価格分解）

```python
fig = go.Figure()

components = ["Market", "Nutrition", "Loss", "Health", "Carbon"]
values = [P_market, V, L, m, C]

fig.add_trace(go.Bar(x=components, y=values))

fig.update_layout(title="価格構成分解（SafetyChain™）")

st.plotly_chart(fig)
```

---

# ② m-ROI（医療費削減価値）モデル

## ロジック（簡略化モデル）

SCFA前駆体 → 疾患リスク低減 → 医療費回避

```python
st.header("🧬 m-ROI Health Value Engine")

scfa = st.slider("SCFA前駆体含有量 (mg/100g)", 0, 1000, 300)

# 疾患別削減係数（仮定：HealthBook連携前提）
diabetes_factor = 0.15
hypertension_factor = 0.12
colon_cancer_factor = 0.10

# 年間医療費（平均）
cost_diabetes = 300000
cost_hypertension = 200000
cost_cancer = 800000

# 効果計算
m_diabetes = scfa * diabetes_factor * cost_diabetes / 1000
m_hypertension = scfa * hypertension_factor * cost_hypertension / 1000
m_cancer = scfa * colon_cancer_factor * cost_cancer / 1000

m_total = m_diabetes + m_hypertension + m_cancer

df_mroi = pd.DataFrame({
    "Disease": ["Diabetes", "Hypertension", "Colon Cancer"],
    "Value (¥)": [m_diabetes, m_hypertension, m_cancer]
})

st.dataframe(df_mroi)
st.metric("総医療費削減価値 (m-ROI)", f"¥{int(m_total)}")
```

---

## 可視化

```python
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=df_mroi["Disease"], y=df_mroi["Value (¥)"]))
fig2.update_layout(title="疾患別 医療費削減インパクト")

st.plotly_chart(fig2)
```

---

# ③ カーボンクレジット小口決済モデル

## ロジック

- 1購入あたりCO2削減量
    
- 年間消費 → 累積インパクト
    

```python
st.header("🌍 Carbon Micro-Transaction Simulator")

co2_per_purchase = st.slider("1回購入あたりCO2削減 (kg)", 0.1, 5.0, 1.0)
purchases_per_year = st.slider("年間購入回数", 1, 500, 100)
carbon_price = st.slider("炭素価格 ($/ton)", 10, 100, 30)

annual_co2 = co2_per_purchase * purchases_per_year
annual_value = (annual_co2 / 1000) * carbon_price

st.metric("年間CO2削減量", f"{annual_co2:.2f} kg")
st.metric("炭素価値 ($)", f"${annual_value:.2f}")
```

---

## 可視化（累積インパクト）

```python
years = np.arange(1, 11)
cumulative_co2 = annual_co2 * years

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=years, y=cumulative_co2, mode='lines+markers'))

fig3.update_layout(
    title="累積CO2削減（10年）",
    xaxis_title="Year",
    yaxis_title="kg-CO2"
)

st.plotly_chart(fig3)
```

---

# 📊 統合出力（投資家向け）

```python
df_summary = pd.DataFrame({
    "Metric": [
        "Total Price",
        "Premium",
        "Health Value",
        "Annual CO2",
        "Carbon Value"
    ],
    "Value": [
        P_total,
        delta_price,
        m_total,
        annual_co2,
        annual_value
    ]
})

df_summary.to_csv("safetychain_summary.csv", index=False)
st.dataframe(df_summary)
```

---

# 🚀 実装効果（投資モデル視点）

この統合により：

### 1. **価格 = 生態系価値**

→ 単なるコモディティから脱却

### 2. **m-ROIの可視化**

→ HealthBook連携で

- 医療費削減 = キャッシュフロー化
    

### 3. **消費者 = カーボン投資家**

→ Scope3削減の分散化

---

# 次ステップ（重要）

以下を統合すると「機関投資家モデル」になります：

- Monte Carlo（価格・炭素ボラティリティ）
    
- IRR / NPV連動
    
- PBPE Token価格リンク
    
- 保険料低減（リスクプレミアム）
    

---

必要なら、**IRRに直結する完全版（Streamlit + MonteCarlo + Token連動）**まで一気に拡張します。