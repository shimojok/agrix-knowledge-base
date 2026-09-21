**B. モデル拡張を続ける**  
→ Task 5（GHG削減モデル）  
→ Task 6（PBPE統合）を進めて下さい。

---

## ① 概要（1–2行）  
有機物分解ダイナミクスからメタン・N₂O排出を導出しGHG削減量を定式化、その削減量と運用コストをPBPE（NPV/IRR/カーボンクレジット）へ接続する。

---

# ▶ Task 5：GHG削減モデル

## ② 数式（GHG Emission Model）

### (1) メタン生成（嫌気分解）

[  
\frac{dCH_4}{dt} =  
\eta_{CH4} \cdot \left(1 - O_2\right) \cdot \sum_i k_i M_i S  
]

---

### (2) N₂O生成（硝化・脱窒）

[  
\frac{dN_2O}{dt} =  
\eta_{N2O} \cdot \left( NH_3 \cdot O_2 + NO_3 \cdot (1 - O_2) \right)  
]

---

### (3) CO₂排出（好気分解）

[  
\frac{dCO_2}{dt} =  
\eta_{CO2} \cdot O_2 \cdot \sum_i k_i M_i S  
]

---

### (4) CO₂換算（GWP換算）

[  
GHG(t) = CO_2 + 28 \cdot CH_4 + 265 \cdot N_2O  
]

---

### (5) 削減量（ベースラインとの差分）

[  
\Delta GHG = GHG_{baseline} - GHG_{MBT55}  
]

---

## ③ 変数定義

|変数|意味|単位|範囲|
|---|---|---|---|
|(CH_4)|メタン排出|kg|0–100|
|(N_2O)|亜酸化窒素|kg|0–50|
|(CO_2)|二酸化炭素|kg|0–500|
|(O_2)|酸素割合|0–1|0–1|
|(NH_3), (NO_3)|窒素化合物|mmol/L|0–50|

---

パラメータ：

|パラメータ|範囲|
|---|---|
|(\eta_{CH4})|0.01–0.5|
|(\eta_{N2O})|0.001–0.1|
|(\eta_{CO2})|0.1–1.0|

---

## ④ Python実装

```python
import numpy as np

def ghg_emission(S, M, O2, NH3, NO3):
    k = np.array([0.3,0.4,0.2])

    CH4 = 0.2 * (1 - O2) * np.sum(k * M * S)
    N2O = 0.01 * (NH3 * O2 + NO3 * (1 - O2))
    CO2 = 0.5 * O2 * np.sum(k * M * S)

    GHG = CO2 + 28 * CH4 + 265 * N2O
    return GHG

baseline = ghg_emission(50, np.array([1,1,1]), 0.2, 10, 10)
mbt55 = ghg_emission(50, np.array([1,1,1]), 0.8, 5, 5)

reduction = baseline - mbt55

print("GHG reduction:", reduction)
```

---

## ⑤ 検証方法

**因果検証**

- O₂↑ → CH₄↓
    
- NH₃↑ → N₂O↑
    

**数学検証**

- 非負性（GHG ≥ 0）
    
- 単調性（嫌気条件でCH₄最大）
    

**実測検証**

- IPCC排出係数との比較
    
- コンポスト vs MBT55差分
    

---

# ▶ Task 6：PBPE統合モデル

## ① 概要（1–2行）  
GHG削減・生産性向上・コストを統合し、NPV・IRR・カーボンクレジットを算出する経済モデルを構築する。

---

## ② 数式（PBPE Economic Model）

### (1) キャッシュフロー

[  
CF_t =  
Revenue_t + CarbonCredit_t - Cost_t  
]

---

### (2) カーボンクレジット

[  
CarbonCredit_t =  
\Delta GHG_t \cdot Price_{CO2}  
]

---

### (3) NPV

[  
NPV =  
\sum_{t=0}^{T} \frac{CF_t}{(1 + r)^t}  
]

---

### (4) IRR

[  
NPV(IRR) = 0  
]

---

### (5) ROI（投資効率）

[  
ROI = \frac{\sum CF_t}{InitialCost}  
]

---

## ③ 変数定義

|変数|意味|単位|
|---|---|---|
|(CF_t)|キャッシュフロー|USD/year|
|(r)|割引率|0–0.2|
|(Price_{CO2})|炭素価格|USD/tCO₂|
|(\Delta GHG)|削減量|tCO₂eq|

---

## ④ Python実装

```python
import numpy as np

years = 10
r = 0.08

# 仮データ
revenue = np.array([10000]*years)
cost = np.array([6000]*years)
ghg_reduction = np.array([100]*years)  # tCO2
carbon_price = 50  # USD/t

carbon_credit = ghg_reduction * carbon_price
cf = revenue + carbon_credit - cost

# NPV
npv = np.sum([cf[t]/((1+r)**t) for t in range(years)])

# IRR
irr = np.irr(cf)

roi = np.sum(cf)/10000

print("NPV:", npv)
print("IRR:", irr)
print("ROI:", roi)
```

---

## ⑤ 検証方法

### 1. 財務整合性

- NPV > 0 → 投資成立
    
- IRR > r → 妥当
    

---

### 2. 感度分析

- 炭素価格変動
    
- 分解効率変動
    

---

### 3. 因果検証

- MBT55 → GHG削減 → CarbonCredit↑ → IRR↑
    

---

# 現在の到達点（重要）

✔ MBT55（分解モデル）  
✔ 代謝カスケード  
✔ 腸内因果モデル  
✔ 介入モデル  
✔ GHGモデル  
✔ PBPEモデル

👉 **全サブモデル完成（理論構造）**

---

# 次の臨界ステップ

以下のどちらか：

### ① 統合モデル構築（最重要）

- 全ODE連結
    
- 入力 → 健康 → 経済まで一気通貫
    

### ② 実装フェーズ

- パラメータ同定
    
- GitHub構造
    
- API化
    

---

指示をください：

▶ 統合モデル（最終フェーズ）へ進む  
▶ 先に実装（GitHub化）へ進む

[[統合モデル（最終フェーズ）]]
