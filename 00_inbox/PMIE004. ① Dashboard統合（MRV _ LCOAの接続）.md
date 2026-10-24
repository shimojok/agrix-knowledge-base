コードの追加など完了しました。

以下の内容の作業方法を説明ください。

■ Dashboard統合
■ 重要（監査対応ログ）
■ モデル選択：GBM拡張（需要ドリブン）
■ Dashboard追加
■ 動的化（時間依存）

---

実装自体は完了しているので、ここからは**「壊さずに統合するための手順」**にフォーカスします。ポイントはすべて**ブロック単位で差し込む**ことです。

---

# ■ ① Dashboard統合（MRV / LCOAの接続）

## ■ 手順（app.py）

### ① 入力セクションの整理（既存の近くに追加）

```python
# --- MRV Inputs ---
baseline_emission = st.number_input("Baseline Emission (tCO2)", value=1000.0)
project_emission = st.number_input("Project Emission (tCO2)", value=600.0)
carbon_price = st.number_input("Carbon Price ($/t)", value=30.0)
leakage_rate = st.slider("Leakage Rate", 0.0, 0.5, 0.1)
buffer_rate = st.slider("Buffer Rate", 0.0, 0.5, 0.2)
```

---

### ② 計算ブロック（IRR計算の直後に追加）

```python
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
```

---

### ③ 表示ブロック（metricsエリア）

```python
col1, col2 = st.columns(2)

with col1:
    st.metric("Verified CO2 (t)", round(verified_co2, 2))

with col2:
    st.metric("Carbon Revenue", round(carbon_revenue, 2))
```

---

# ■ ② 監査対応ログ（最重要）

## ■ 方針

- **再現性**
    
- **トレーサビリティ**
    
- **外部監査対応（Verra想定）**
    

---

## ■ 実装（必ず独立ブロック）

```python
import json
from datetime import datetime

mrv_log = {
    "timestamp": datetime.utcnow().isoformat(),
    "baseline": baseline_emission,
    "project": project_emission,
    "leakage_rate": leakage_rate,
    "buffer_rate": buffer_rate,
    "verified_co2": verified_co2,
    "carbon_price": carbon_price,
    "carbon_revenue": carbon_revenue
}
```

---

## ■ 保存処理

```python
with open("mrv_log.json", "a") as f:
    f.write(json.dumps(mrv_log) + "\n")
```

---

## ■ UI追加（監査ログ可視化）

```python
if st.checkbox("Show MRV Log"):
    st.json(mrv_log)
```

---

# ■ ③ GBM拡張モデル（需要ドリブン）

## ■ Dashboard入力追加

```python
# --- Token Market Inputs ---
demand = st.slider("Demand", 0.0, 100.0, 50.0)
supply = st.slider("Supply", 0.0, 100.0, 40.0)
volatility = st.slider("Volatility (σ)", 0.0, 1.0, 0.2)
alpha = st.slider("Market Sensitivity (α)", 0.0, 0.1, 0.01)
```

---

## ■ 呼び出し

```python
from models.token_model import simulate_token_price

prices = simulate_token_price(
    P0=token_price,
    demand=demand,
    supply=supply,
    alpha=alpha,
    sigma=volatility
)
```

---

# ■ ④ Dashboard追加（Token可視化）

## ■ グラフ

```python
st.subheader("Token Price Simulation")
st.line_chart(prices)
```

---

## ■ 最終価格

```python
st.metric("Final Token Price", round(prices[-1], 2))
```

---

# ■ ⑤ 動的化（時間依存モデル）

ここが**最も重要な進化ポイント**です。

---

## ■ 基本構造

```python
T = 10  # years
soil = [1.0]  # 初期SOC
yield_series = []

for t in range(T):
    # Soil更新
    delta_soc = 0.05  # MBT55効果
    soil.append(soil[-1] + delta_soc)
    
    # YieldはSoil依存
    y = 3.0 + 0.5 * soil[-1]
    yield_series.append(y)
```

---

## ■ LCOAへの接続

```python
lcoa = calculate_lcoa(capex, opex, yield_series, discount_rate)
```

---

## ■ MRVへの接続（時間対応）

```python
baseline_series = [baseline_emission] * T
project_series = [project_emission - 10*t for t in range(T)]

verified_total = sum([
    calculate_verified_credits(baseline_series[t], project_series[t])
    for t in range(T)
])
```

---

## ■ 可視化

```python
st.subheader("Soil Evolution")
st.line_chart(soil)

st.subheader("Yield Evolution")
st.line_chart(yield_series)
```

---

# ■ 統合の最重要ルール

```text
① Input
② Compute（モデル）
③ Output（UI）
④ Log（監査）
```

👉 この順序を崩さない

---

# ■ 完成状態（あなたのシステム）

```text
Static Model → Dynamic System
↓
Finance → Verified Finance
↓
Simulation → Market Engine
```

---

# ■ 次の一手（強く推奨）

この段階に来たので：

```text
・LCOA × MRV → 投資商品の裏付け
・Token → 流動性
```

👉 次はこれ：

```text
SPV（ファンド構造）モデル化
```

---

必要なら次は：

- Azure Digital Twin接続コード（IoT連携）
    
- 国別リスクσ導入（VaR）
    
- トークンとカーボンクレジットの裁定モデル
    

まで一気に進められます。
