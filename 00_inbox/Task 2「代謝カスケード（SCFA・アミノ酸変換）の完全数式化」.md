進めてください。

---

## ① 概要（1–2行）  
基質→中間代謝物→最終産物（SCFA・アミノ酸代謝）を酵素反応速度論（Monod/Michaelis-Menten）とクロスフィーディングを含むODE系として定式化する。

---

## ② 数式（Metabolic Cascade Model）

### (1) 基質 → 中間代謝物

$$  
\frac{dS_a}{dt} = - \sum_{i=1}^{N} V_{i,a} \cdot \frac{S_a}{K_{m,i,a} + S_a} \cdot M_i  
$$

$$  
\frac{dI_b}{dt} = \sum_{i=1}^{N} Y_{i,a \rightarrow b} \cdot V_{i,a} \cdot \frac{S_a}{K_{m,i,a} + S_a} \cdot M_i - \sum_{j=1}^{N} V_{j,b} \cdot \frac{I_b}{K_{m,j,b} + I_b} \cdot M_j  
$$

---

### (2) 中間代謝物 → SCFA（酢酸・酪酸・プロピオン酸）

$$  
\frac{dSCFA_k}{dt} =  
\sum_{i=1}^{N} Y_{i,b \rightarrow k} \cdot V_{i,b} \cdot \frac{I_b}{K_{m,i,b} + I_b} \cdot M_i

- \lambda_k SCFA_k  
    $$
    

---

### (3) アミノ酸代謝（脱アミノ・発酵）

$$  
\frac{dAA_c}{dt} =

- \sum_{i=1}^{N} V_{i,c} \cdot \frac{AA_c}{K_{m,i,c} + AA_c} \cdot M_i  
    $$
    

$$  
\frac{dNH_3}{dt} =  
\sum_{i=1}^{N} Y_{i,c \rightarrow NH3} \cdot V_{i,c} \cdot \frac{AA_c}{K_{m,i,c} + AA_c} \cdot M_i  
$$

---

### (4) クロスフィーディング（相互利用）

$$  
\frac{dI_b}{dt} += \sum_{i \neq j} \theta_{ij} \cdot M_i \cdot SCFA_j  
$$

---

### (5) エネルギー収支（ATP生成）

$$  
ATP_i = \sum_k \epsilon_{i,k} \cdot SCFA_k  
$$

$$  
\frac{dM_i}{dt} = M_i \left( \mu_i \cdot \frac{ATP_i}{K_{ATP,i} + ATP_i} - d_i \right)  
$$

---

## ③ 変数定義（Variables & Units）

|変数|意味|単位|範囲|
|---|---|---|---|
|(S_a)|炭水化物/脂質/タンパク質基質|g/L|0–100|
|(I_b)|中間代謝物（乳酸など）|mmol/L|0–50|
|(SCFA_k)|短鎖脂肪酸|mmol/L|0–150|
|(AA_c)|アミノ酸|mmol/L|0–50|
|(NH_3)|アンモニア|mmol/L|0–20|
|(M_i)|微生物群|cells/mL|10⁵–10¹²|

---

**パラメータ**

|パラメータ|意味|範囲|
|---|---|---|
|(V_{i,x})|最大反応速度|0.01–5 mmol/L/hr|
|(K_{m,i,x})|半飽和定数|0.1–10 mmol/L|
|(Y)|収率係数|0–1|
|(\lambda_k)|消費率|0.01–1 hr⁻¹|
|(\theta_{ij})|クロスフィード係数|0–0.5|
|(\epsilon_{i,k})|ATP変換効率|0–10|

---

## ④ Python実装（Executable）

```python
import numpy as np
from scipy.integrate import solve_ivp

N = 3  # 微生物数

# 初期値
S = 50
I = 10
SCFA = np.array([5, 5, 5])  # acetate, propionate, butyrate
AA = 10
NH3 = 1
M = np.array([1e6, 1e6, 1e6])

y0 = [S, I] + list(SCFA) + [AA, NH3] + list(M)

# パラメータ
V = np.array([1.0, 1.2, 0.8])
Km = np.array([2.0, 2.5, 1.5])
mu = np.array([0.5, 0.6, 0.4])
d = np.array([0.1, 0.1, 0.1])

def model(t, y):
    S = y[0]
    I = y[1]
    SCFA = np.array(y[2:5])
    AA = y[5]
    NH3 = y[6]
    M = np.array(y[7:])

    # 基質分解
    dSdt = -np.sum(V * S/(Km + S) * M)

    # 中間代謝物
    dIdt = np.sum(0.5 * V * S/(Km + S) * M) - np.sum(V * I/(Km + I) * M)

    # SCFA生成
    dSCFAdt = 0.3 * V * I/(Km + I) * M - 0.1 * SCFA

    # アミノ酸代謝
    dAAdt = -np.sum(V * AA/(Km + AA) * M)
    dNH3dt = np.sum(0.2 * V * AA/(Km + AA) * M)

    # ATP
    ATP = np.sum(0.5 * SCFA)

    dMdt = M * (mu * ATP/(1 + ATP) - d)

    return [dSdt, dIdt] + list(dSCFAdt) + [dAAdt, dNH3dt] + list(dMdt)

sol = solve_ivp(model, (0, 100), y0, t_eval=np.linspace(0,100,200))

print(sol.y)
```

---

## ⑤ 検証方法（Validation）

### 1. 数学的整合性（Math Agent）

- 非負性制約：すべての濃度 ≥ 0
    
- 保存則：炭素フラックスの収支確認
    

---

### 2. 因果検証（Causality Agent）

- S増加 → I増加 → SCFA増加 → ATP増加 → M増加
    
- クロスフィード経路が閉じているか確認
    

---

### 3. トレース検証（Trace Agent）

- 初期条件変更（S, AA）に対するSCFA応答曲線
    
- 感度分析（Sobol / 局所微分）
    

---

### 4. 生物学的妥当性

- SCFA比率（酢酸:プロピオン酸:酪酸 ≈ 60:20:20）への収束確認
    
- NH3過剰生成時のpH低下との整合性
    

---

次ステップ：  
▶ Task 3「腸内細菌 → 代謝産物 → フェノタイプ → 疾病リスク」の因果モデル構築に進むべき段階です

[[現在の保持状況（事実）]]
