
import streamlit as st

import pandas as pd

  

from simulation import simulate, simulate_country

from pbpe_token import pbpe_value

from fund_model import irr_proxy

from carbon_credit import carbon_value

from models.irr import calculate_irr

from models.ranking import country_score

from models.lcoa import calculate_lcoa

from models.irr import compare_irr_lcoa

  

lcoa = calculate_lcoa(capex, opex, yield_series, discount_rate)

comparison = compare_irr_lcoa(irr, lcoa)

  

st.metric("LCOA", round(lcoa, 2))

st.metric("IRR/LCOA Efficiency", round(comparison["Efficiency Score"], 4))

  

st.set_page_config(layout="wide")

  

st.title("🌍 PBPE × MBT55 Investment Dashboard")

  

# =========================

# ON/OFF（サイドバー）

# =========================

with st.sidebar:

    st.header("⚙️ Control Panel")

  

    M = 1 if st.toggle("MBT55 ON/OFF", True) else 0

  

# =========================

# Simulation

# =========================

on = simulate(1)

off = simulate(0)

res = simulate(M)

  

yield_gain = on["Yield"] - off["Yield"]

cost_reduction = off["Cost"] - on["Cost"]

co2_reduction = off["CO2"] - on["CO2"]

  

# =========================

# Economics

# =========================

pbpe = pbpe_value(yield_gain, co2_reduction, cost_reduction)

carbon = carbon_value(co2_reduction)

  

annual_profit = cost_reduction + carbon/1000 + yield_gain * 50

cashflows = [-200] + [annual_profit] * 10

irr = calculate_irr(cashflows) * 100

  

# ON/OFFそれぞれのIRRを計算

annual_profit_on = (

    cost_reduction +

    carbon/1000 +

    yield_gain * 50

)

  

cashflows_on = [-200] + [annual_profit_on] * 10

  

irr_on = calculate_irr(cashflows_on) * 100

  

annual_profit_off = (

    off["Cost"] * -1 +

    carbon_value(off["CO2"]) / 1000 +

    off["Yield"] * 50

)

  

cashflows_off = [-200] + [annual_profit_off] * 10

irr_off = 0

  

# 差分

delta_irr = irr_on - irr_off  # = irr_on

  

# =========================

# Investment Decision

# =========================

st.markdown("## 🚀 Investment Decision")

  

col1, col2, col3 = st.columns(3)

  

col1.metric("💰 Profit Impact", round(cost_reduction if M else 0, 2))

col2.metric("🌱 Carbon Impact", round(co2_reduction if M else 0, 2))

col3.metric("📈 Yield Growth", round(yield_gain if M else 0, 2))

  

# =========================

# PBPE

# =========================

st.markdown("## 💠 PBPE Value Engine")

st.metric("PBPE Token", round(pbpe if M else 0, 2))

  

# =========================

# Green Premium

# =========================

st.markdown("## ♻️ Negative Green Premium")

st.metric("Cost Advantage", round(cost_reduction if M else 0, 2))

  

# =========================

# Carbon

# =========================

st.markdown("## 🌍 Carbon Value")

st.metric("Carbon Revenue ($)", round(carbon if M else 0, 2))

  

# =========================

# Investment Metrics

# =========================

st.markdown("## 💼 Investment Metrics")

  

col4, col5 = st.columns(2)

  

col4.metric(

    "IRR (%)",

    round(irr_on if M else 0, 2),

    delta=round(delta_irr, 2)

)

  

investment = 200

payback = investment / max(1, (cost_reduction + carbon/1000 + yield_gain * 50))

  

col5.metric("Payback (years)", round(payback if M else 0, 2))

  

# =========================

# Signal

# =========================

st.markdown("## 🟢 Investment Signal")

  

if M and cost_reduction > 0 and co2_reduction > 0:

    st.success("STRONG BUY")

else:

    st.warning("OFF or REVIEW")

  

# =========================

# Core Metrics

# =========================

st.markdown("## 📊 Core Metrics")

  

col6, col7, col8 = st.columns(3)

  

st.markdown("## 📈 ON vs OFF")

  

df_compare = pd.DataFrame({

    "State": ["OFF", "ON"],

    "Yield": [off["Yield"], on["Yield"]],

    "Cost": [off["Cost"], on["Cost"]],

    "CO2": [off["CO2"], on["CO2"]]

})

  

st.bar_chart(df_compare.set_index("State"))

  

# =========================

# Country Data（最初に定義）

# =========================

df = pd.read_csv("data/country_coffee_sample.csv")

  

# =========================

# Simulation + IRR（ここで全部作る）

# =========================

results = []

  

for _, row in df.iterrows():

    sim = simulate_country(row, M)

  

    # IRR計算

    annual_profit = (

        -sim["Cost"] +

        sim["CO2"] * -0.1 +

        sim["Yield"] * 50

    )

  

from models.mrv import calculate_verified_credits, calculate_carbon_revenue

  

verified_co2 = calculate_verified_credits(

    baseline_emission,

    project_emission,

    leakage_rate,

    buffer_rate

)

  

carbon_revenue = calculate_carbon_revenue(

    verified_co2,

    carbon_price

)

  

    if annual_profit > 0:

        cashflows = [-200] + [annual_profit] * 10

        irr_country = calculate_irr(cashflows) * 100

    else:

        irr_country = 0

  

    sim["IRR"] = irr_country

  

    results.append(sim)

  

# --- MRV Inputs ---

baseline_emission = st.number_input("Baseline Emission (tCO2)", value=1000.0)

project_emission = st.number_input("Project Emission (tCO2)", value=600.0)

carbon_price = st.number_input("Carbon Price ($/t)", value=30.0)

leakage_rate = st.slider("Leakage Rate", 0.0, 0.5, 0.1)

buffer_rate = st.slider("Buffer Rate", 0.0, 0.5, 0.2)

  

# =========================

# DataFrame生成

# =========================

  

res_df = pd.DataFrame(results)

  

res_df["Score"] = res_df.apply(country_score, axis=1)

res_df = res_df.sort_values("Score", ascending=False)

  

# =========================

# 💰 Capital Allocation（ここ）

# =========================

total_capital = 1_000_000

  

res_df["Weight"] = res_df["Score"] / res_df["Score"].sum()

res_df["Investment"] = res_df["Weight"] * total_capital

  

st.markdown("## 💰 Capital Allocation")

  

for _, row in res_df.iterrows():

    st.write(f"{row['country']} → ${round(row['Investment'], 0)}")

  

# =========================

# 💠 PBPE Market Model

# =========================

  

demand = res_df["Score"].sum() * 1_000_000 * M

supply = 1_000_000

  

token_price = demand / supply

  

st.markdown("## 💠 PBPE Market")

st.metric("Token Market Price", round(token_price, 4))

  

# =========================

# 🌐 Global Expansion（復活）

# =========================

st.markdown("## 🌐 Global Expansion")

  

st.dataframe(res_df)

st.bar_chart(res_df.set_index("country")[["Yield", "Cost", "CO2"]])

  

# =========================

# 🌍 Country Ranking

# =========================

st.markdown("## 🌍 Country Ranking")

  

for _, row in res_df.iterrows():

    st.write(f"{row['country']} — Score: {round(row['Score'], 3)}")

  

# =========================

# Market

# =========================

st.markdown("## 🌍 Market Scale")

  

global_market = 100_000_000_000

impact_ratio = min(1.0, yield_gain / 3.0)

tam = global_market * impact_ratio

  

st.metric("Addressable Market ($)", f"{int(tam):,}")

  

col1, col2 = st.columns(2)

  

with col1:

    st.metric("Verified CO2 (t)", round(verified_co2, 2))

  

with col2:

    st.metric("Carbon Revenue", round(carbon_revenue, 2))

  

# =========================

# Insight

# =========================

st.markdown("## 🧠 Executive Insight")

  

st.success(

    f"MBT55 enables {round(cost_reduction,0)} cost reduction, "

    f"{round(co2_reduction,0)} CO2 reduction, "

    f"and {round(yield_gain,1)} yield increase."

)