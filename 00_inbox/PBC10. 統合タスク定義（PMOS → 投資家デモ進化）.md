前のスレッドでの作業を完了しました。下記のプロンプトの内容と、このスレッドの内容をまとめた作業内容を指示してください。ーーーーーーーーーーーーーーーーーーーープロジェクト「🗃️Planetary Metabolic Operating System」の新スレッドとして開始します。

現在、PBPE-CoffeeのStreamlitデモにおいて以下を達成済みです：

・MBT55 ON/OFFによる数理モデル実装
・肥料削減、収量増加、コスト低減、CO2/N2O削減の可視化
・グラフ表示（Comparison）
・Impact Summary（%表示）

この状態をベースに、次のフェーズとして：

① 投資家（Bill Gates、Howard Schultz、Rockefeller Foundation等）に刺さるUI設計
② 「ネガティブ・グリーンプレミアム」の直感的表現
③ PBPE（価格安定化）との統合ストーリー
④ Azure Digital Twinとの接続設計（SoilDigitalTwinとの統合）
⑤ GitHub上での「体験型デモ」構築

を進めたい。

単なるUI改善ではなく、
「科学 → 数理 → 経済 → 社会インパクト」
が一体として理解されるプロダクト設計を行ってください。

まずは：
・現在のStreamlit構造を投資家向けUIに再設計
・トップ画面の構成案（1画面で理解できる設計）
から開始してください。

---

了解。  
これまでの両スレッドを統合し、**次フェーズの作業指示（実装ベース）**を定義する。

---

# 🚀 統合タスク定義（PMOS → 投資家デモ進化）

## 🎯 ゴール（再定義）

```text
「触れば理解できる」
→「見た瞬間に投資判断できる」
```

---

# 🔴 フェーズ構造（必須順序）

```text
PHASE 1：UI再設計（投資家用）
PHASE 2：ネガティブ・グリーンプレミアム可視化
PHASE 3：PBPE統合（価格安定）
PHASE 4：Azure Digital Twin接続設計
PHASE 5：GitHub体験型デモ化
```

---

# 🚀 PHASE 1：トップ画面（最重要）

## 🎯 要件

```text
1画面・5秒で理解
```

---

## ✅ UI構造（そのまま実装）

```python
# /pbpe-demo/app.py（トップ再設計）
```

---

## 🧠 画面構成（完全定義）

```text
┌──────────────────────────────┐
│ 🌍 PBPE × MBT55 Global System │
├──────────────────────────────┤
│ [MBT ON/OFF トグル]          │
├──────────────────────────────┤
│ KPI（4つ）                   │
│ ・Yield ↑                    │
│ ・Cost ↓                     │
│ ・CO2 ↓                      │
│ ・PBPE Value ↑               │
├──────────────────────────────┤
│ 🔥 KEY INSIGHT              │
│ 「Cost → Profit」           │
│ 「CO2 → Negative」          │
├──────────────────────────────┤
│ グラフ（ON vs OFF）          │
├──────────────────────────────┤
│ 🌐 Global Impact（国別）     │
├──────────────────────────────┤
│ 💰 Investment Return         │
│ IRR / Carbon / Token         │
└──────────────────────────────┘
```

---

## ✅ Streamlitコード（トップUI）

```python
import streamlit as st
import pandas as pd
from simulation import simulate_country

st.set_page_config(layout="wide")

st.title("🌍 PBPE × MBT55 Investment Dashboard")

# =========================
# トグル
# =========================

M = 1 if st.toggle("MBT55 ON", True) else 0

# =========================
# データ
# =========================

df = pd.read_csv("data/country_coffee_sample.csv")

results = [simulate_country(row, M) for _, row in df.iterrows()]
res_df = pd.DataFrame(results)

# =========================
# KPI（最重要）
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Yield ↑", round(res_df["Yield"].sum(), 2))
col2.metric("Cost ↓", round(res_df["Cost"].sum(), 2))
col3.metric("CO2 ↓", round(res_df["CO2"].sum(), 2))
col4.metric("PBPE Value ↑", round(res_df["PBPE"].sum(), 2))

# =========================
# KEY INSIGHT
# =========================

st.markdown("""
## 🔥 System Transformation
- Cost → Profit
- CO2 → Carbon Negative
- Waste → Resource
""")

# =========================
# 比較グラフ
# =========================

on_df = pd.DataFrame([simulate_country(r, 1) for _, r in df.iterrows()])
off_df = pd.DataFrame([simulate_country(r, 0) for _, r in df.iterrows()])

compare = pd.DataFrame({
    "Yield_ON": on_df["Yield"],
    "Yield_OFF": off_df["Yield"],
    "Cost_ON": on_df["Cost"],
    "Cost_OFF": off_df["Cost"],
    "CO2_ON": on_df["CO2"],
    "CO2_OFF": off_df["CO2"]
})

st.line_chart(compare)

# =========================
# 国別
# =========================

st.subheader("🌐 Global Impact")

st.bar_chart(res_df.set_index("country")[["Yield", "Cost", "CO2"]])
```

---

# 🚀 PHASE 2：ネガティブ・グリーンプレミアム

## 🎯 定義（数式）

```text
GreenPremium = Cost_conventional - Cost_MBT
```

```python
def green_premium(cost_conv, cost_mbt):
    return cost_conv - cost_mbt
```

---

## UI追加

```python
st.metric("Negative Green Premium", round(gp_total, 2))
```

👉 **「コストが下がる」ではなく**

```text
「使うほど儲かる」
```

---

# 🚀 PHASE 3：PBPE（価格安定）

## モデル

```python
def price_stability(supply, demand):

    return demand / (supply + 1e-6)
```

MBT ON：

```text
供給安定 → 価格変動低下
```

---

## UI

```python
st.line_chart(price_series)
```

---

# 🚀 PHASE 4：Azure Digital Twin設計

## 🎯 統合対象

```text
SoilDigitalTwin
＋
PBPE Engine
```

---

## Twinモデル

```json
{
  "field_id": "JP-01",
  "SoilMetabolism": 0.8,
  "Yield": 1.2,
  "CO2": -200,
  "PBPE": 500
}
```

---

## 接続

```python
update_twin(field_id, metrics)
```

---

# 🚀 PHASE 5：GitHub体験型デモ

## 必須構成

```text
README.md
↓
1クリックで起動
↓
Streamlit UI
↓
ON/OFF体験
```

---

## README（構造）

```text
# PBPE × MBT55 Demo

## What happens if you click ON?

→ Yield increases
→ Cost becomes negative
→ CO2 becomes negative

## Run

streamlit run app.py
```

---

# 🔥 最重要設計思想

```text
説明を排除する

↓
操作で理解させる
```

---

# 🚀 次の即実行タスク

```text
① トップUIをこの構造に差し替え
② Green Premium表示追加
③ PBPE価格グラフ追加
④ Azure送信ボタン接続
⑤ README作成
```

---

# 🎯 完成状態

```text
投資家が5秒で理解し
30秒で確信し
その場で判断できるUI
```

---

次に進むなら：

```text
・Microsoft提出用スライド（完成版）
・Bill Gates向け1枚資料
```

まで仕上げる。