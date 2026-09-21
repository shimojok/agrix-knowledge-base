最初にLCOAモデルをPythonで実装し、既存IRRと比較可能な形で統合してください。
その後、LCOAの即実装コード、MRVのVerra準拠ロジック（監査対応）、Tokenの確率微分方程式モデル
まで一気に進めて下さい。

---

了解しました。依存関係を踏まえ、**①LCOA統合 → ②MRV → ③Token SDE**の順で、一貫したモジュール構造と即実装コードを提示します。すべて既存の `IRR / Dashboard` にそのまま接続可能な形にしています。

---

# ■ ① LCOAモデル実装（IRR統合）

## ■ 設計思想

- IRR：投資効率（金融）
    
- LCOA：単位生産コスト（実体経済）
    

👉 両者を並列評価可能にする

---

## ■ `models/lcoa.py`

```python
import numpy as np

def calculate_lcoa(capex, opex, yield_series, discount_rate):
    """
    LCOA = (CAPEX + Σ OPEX_t / (1+r)^t) / Σ Yield_t / (1+r)^t
    """
    years = len(opex)
    
    discounted_opex = sum(
        opex[t] / ((1 + discount_rate) ** (t + 1))
        for t in range(years)
    )
    
    discounted_yield = sum(
        yield_series[t] / ((1 + discount_rate) ** (t + 1))
        for t in range(years)
    )
    
    lcoa = (capex + discounted_opex) / discounted_yield
    
    return lcoa
```

---

## ■ IRR統合（`models/irr.py`に追加）

```python
def compare_irr_lcoa(irr, lcoa):
    """
    投資評価の2軸比較
    """
    return {
        "IRR": irr,
        "LCOA": lcoa,
        "Efficiency Score": irr / lcoa  # 新指標
    }
```

---

## ■ Streamlit追加（app.py）

```python
from models.lcoa import calculate_lcoa
from models.irr import compare_irr_lcoa

lcoa = calculate_lcoa(capex, opex, yield_series, discount_rate)
comparison = compare_irr_lcoa(irr, lcoa)

st.metric("LCOA", round(lcoa, 2))
st.metric("IRR/LCOA Efficiency", round(comparison["Efficiency Score"], 4))
```

---

# ■ ② MRV（Verra準拠ロジック）

## ■ 設計要点（監査対応）

Verraの本質：

```text
追加性（Additionality）
ベースライン設定（Baseline）
リーケージ考慮（Leakage）
永続性（Permanence）
```

---

## ■ `models/mrv.py`

```python
def calculate_co2e_reduction(baseline_emission, project_emission):
    return baseline_emission - project_emission


def apply_leakage(co2_reduction, leakage_rate=0.1):
    return co2_reduction * (1 - leakage_rate)


def apply_permanence_buffer(co2_reduction, buffer_rate=0.2):
    return co2_reduction * (1 - buffer_rate)


def calculate_verified_credits(
    baseline,
    project,
    leakage_rate=0.1,
    buffer_rate=0.2
):
    reduction = calculate_co2e_reduction(baseline, project)
    net_reduction = apply_leakage(reduction, leakage_rate)
    verified = apply_permanence_buffer(net_reduction, buffer_rate)
    
    return verified


def calculate_carbon_revenue(verified_credits, carbon_price):
    return verified_credits * carbon_price
```

---

## ■ Dashboard統合

```python
from models.mrv import calculate_verified_credits, calculate_carbon_revenue

verified_co2 = calculate_verified_credits(
    baseline_emission,
    project_emission
)

carbon_revenue = calculate_carbon_revenue(
    verified_co2,
    carbon_price
)

st.metric("Verified CO2 (t)", round(verified_co2, 2))
st.metric("Carbon Revenue", round(carbon_revenue, 2))
```

---

## ■ 重要（監査対応ログ）

```python
mrv_log = {
    "baseline": baseline_emission,
    "project": project_emission,
    "leakage_rate": leakage_rate,
    "buffer_rate": buffer_rate,
    "verified_co2": verified_co2
}
```

👉 JSON保存で監査対応可能

---

# ■ ③ Token価格モデル（確率微分方程式）

## ■ モデル選択：GBM拡張（需要ドリブン）

```text
dP = α(D - S)P dt + σP dW
```

---

## ■ `models/token_model.py`

```python
import numpy as np

def simulate_token_price(
    P0,
    demand,
    supply,
    alpha=0.01,
    sigma=0.2,
    T=1,
    dt=0.01
):
    """
    確率微分方程式による価格シミュレーション
    """
    N = int(T / dt)
    prices = np.zeros(N)
    prices[0] = P0
    
    for t in range(1, N):
        dW = np.random.normal(0, np.sqrt(dt))
        
        drift = alpha * (demand - supply) * prices[t-1] * dt
        diffusion = sigma * prices[t-1] * dW
        
        prices[t] = prices[t-1] + drift + diffusion
    
    return prices
```

---

## ■ Dashboard追加

```python
from models.token_model import simulate_token_price

prices = simulate_token_price(
    P0=token_price,
    demand=demand,
    supply=supply
)

st.line_chart(prices)
```

---

# ■ 統合構造（完成形）

```text
MBT55
↓
Yield / Cost / CO2
↓
LCOA + IRR（並列評価）
↓
MRV（Verified Carbon）
↓
Carbon Revenue
↓
Capital Allocation
↓
Token Price（SDE）
```

---

# ■ 追加（次にやるべき最重要1点）

## ■ 動的化（時間依存）

次に必ず入れるべき：

```python
soil[t+1] = soil[t] + delta_soc
yield[t] = f(soil[t])
```

👉 これで：

- LCOAが変化
    
- MRVが変化
    
- Tokenが変化
    

＝完全な「生態系経済モデル」

---

# ■ 結論

```text
① LCOA → 投資の実体化
② MRV → 信頼性（監査）
③ Token SDE → 市場化

＝「金融商品として成立」
```

---

必要なら次は：

- Azure Digital Twin 接続コード
    
- リスク（国別σ）統合
    
- ファンド組成モデル（SPV構造）
    

まで一気に進めます。