良い状態です。  
**JSON読込・実行環境は完全に正常**。ここから一気にコアを接続します。

---

# 🚀 次のステップ（即実装）

```text
model.py → simulation.py接続 → ON/OFF差分確認
```

---

# 🧠 STEP 1：`model.py`（M3統合・完成版）

👉 `/pbpe-demo/model.py` をこの内容に置き換え

```python
import math

def run_step(state, microbial, M, params):

    # -----------------------------
    # 微生物ダイナミクス（M3）
    # -----------------------------
    X, S = microbial

    mu = params["microbial_growth"]
    decay = params["microbial_decay"]

    dX = mu * X * S - decay * X
    X_new = max(0.01, X + dX)

    S_new = max(0.01, S - params["substrate_utilization"] * X)

    # -----------------------------
    # 土壌制御（MBT効果）
    # -----------------------------
    nutrient = state["nutrient"] + M * params["nutrient_boost"] * X_new
    toxicity = state["toxic"] * (1 - M * params["toxicity_reduction"])
    salinity = state["salinity"] * (1 - M * params["salinity_reset"])

    # -----------------------------
    # 病害
    # -----------------------------
    D = state["D0"] * math.exp(-params["beta"] * M * X_new)

    # -----------------------------
    # 収量
    # -----------------------------
    Y = params["Y0"] * nutrient * (1 - toxicity) * (1 - salinity) * (1 - D)

    # -----------------------------
    # コスト
    # -----------------------------
    cost = (
        params["fertilizer_price"] * (1 - M)
        + params["process_cost_per_ton"] * M
        - params["waste_disposal_cost"] * M
    )

    # -----------------------------
    # CO2
    # -----------------------------
    CO2 = (
        params["incineration_emission"] * (1 - M)
        + params["process_emission"] * M
        - params["carbon_sequestration"] * M
    )

    new_state = {
        "nutrient": nutrient,
        "toxic": toxicity,
        "salinity": salinity,
        "D0": D,
        "waste_input": state["waste_input"]
    }

    return new_state, (X_new, S_new), {
        "Yield": Y,
        "Cost": cost,
        "CO2": CO2
    }
```

---

# 🔁 STEP 2：`simulation.py`（モデル接続）

👉 上書きしてください

```python
import json
from model import run_step

with open("parameters.json") as f:
    PARAMS = json.load(f)


def simulate(M=1, steps=5):

    state = {
        "waste_input": 1.0,
        "toxic": 0.6,
        "salinity": 0.5,
        "nutrient": 0.3,
        "D0": 0.5
    }

    microbial = (1.0, 1.0)

    history = []

    for t in range(steps):
        state, microbial, result = run_step(
            state, microbial, M, PARAMS
        )
        history.append(result)

    return history[-1]


if __name__ == "__main__":

    on = simulate(M=1)
    off = simulate(M=0)

    print("MBT ON :", on)
    print("MBT OFF:", off)
```

---

# ▶ 実行

```powershell
python simulation.py
```

---

# 🎯 正常出力（期待）

```text
MBT ON :  {'Yield': 高い, 'Cost': 低い or マイナス, 'CO2': マイナス}
MBT OFF: {'Yield': 低い, 'Cost': 高い, 'CO2': 正}
```

---

# 🔥 ここで起きていること

```text
ON：
・微生物増殖 → 栄養増加
・毒性低下
・病害抑制
・CO2負転

OFF：
・従来農業状態
```

---

# 🚀 次ステップ（ここまで来たら即）

```text
Streamlit UI接続
```

---

# 🖥 STEP 3：最小UI（すぐ動く）

👉 `/pbpe-demo/app.py`

```python
import streamlit as st
from simulation import simulate

st.title("PBPE × MBT55 Demo")

M = 1 if st.toggle("MBT55 ON", True) else 0

result = simulate(M)

st.metric("Yield", round(result["Yield"], 2))
st.metric("Cost", round(result["Cost"], 2))
st.metric("CO2", round(result["CO2"], 2))
```

---

## ▶ 起動

```powershell
streamlit run app.py
```

---

# 🎯 ここまでで達成

```text
✔ 数理モデル動作
✔ ON/OFF差分確認
✔ UI表示
```

---

# 🚀 次にやるべきこと

```text
① 国別データ接続
② PBPEトークン追加
③ 投資家UI化
```

---

必要なら次は：

👉 **「エラーゼロの完成UI（投資家版）」**  
一気に仕上げます。

---

