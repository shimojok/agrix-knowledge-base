はい、お願いします。

---

Kaz、了解しました。  
**2_Models（コード雛形）と 3_Data（CSVテンプレート）を、英語版・日本語版ともに “同時に” 進めます。**  
説明は省き、必要なファイル内容だけを一気に提示します。

---

# ✅ **2_Models（コード雛形）**

以下をそのまま各ファイルとして追加してください。

---

## 📁 **2_Models/microbial_dynamics.py**

```python
"""
Microbial Dynamics Model
MBT55 population growth and interaction dynamics
"""

import numpy as np

def microbial_growth(N, r, K):
    """
    Logistic growth model
    N : population
    r : growth rate
    K : carrying capacity
    """
    return r * N * (1 - N / K)

def update_population(N, r, K, dt=0.1):
    return N + microbial_growth(N, r, K) * dt

if __name__ == "__main__":
    N = 0.1
    for t in range(50):
        N = update_population(N, r=0.5, K=1.0)
        print(t, N)
```

---

## 📁 **2_Models/enzyme_cascade.py**

```python
"""
Enzyme Cascade Model
Simulates multi-step enzymatic reactions
"""

import numpy as np

def cascade_step(S, k):
    """
    S : substrate concentration
    k : reaction rate
    """
    return -k * S

def run_cascade(S0, k_list, dt=0.1):
    S = S0
    for k in k_list:
        S += cascade_step(S, k) * dt
    return S

if __name__ == "__main__":
    S = run_cascade(1.0, [0.2, 0.1, 0.05])
    print("Final substrate:", S)
```

---

## 📁 **2_Models/carbon_flux.py**

```python
"""
Carbon Flux Acceleration Model
"""

def carbon_flux(C, alpha):
    return alpha * C

def update_carbon(C, alpha, dt=0.1):
    return C + carbon_flux(C, alpha) * dt
```

---

## 📁 **2_Models/nitrogen_flux.py**

```python
"""
Nitrogen Flux Model
"""

def nitrogen_flux(N, beta):
    return beta * N

def update_nitrogen(N, beta, dt=0.1):
    return N + nitrogen_flux(N, beta) * dt
```

---

## 📁 **2_Models/ghg_model.py**

```python
"""
GHG Reduction Model
"""

def ghg_reduction(CH4, CO2, rate):
    CH4_new = CH4 * (1 - rate)
    CO2_new = CO2 * (1 - rate * 0.5)
    return CH4_new, CO2_new
```

---

## 📁 **2_Models/hypercycle.py**

```python
"""
Hypercycle Integration Model
Combines microbial, enzyme, and flux models
"""

from microbial_dynamics import update_population
from enzyme_cascade import run_cascade
from carbon_flux import update_carbon
from nitrogen_flux import update_nitrogen

def hypercycle_step(N, S, C, N2):
    N = update_population(N, r=0.4, K=1.0)
    S = run_cascade(S, [0.2, 0.1])
    C = update_carbon(C, alpha=0.3)
    N2 = update_nitrogen(N2, beta=0.25)
    return N, S, C, N2
```

---

## 📁 **2_Models/run_demo.py**

```python
"""
Unified Demo Script for M3-BioSynergy Core
"""

from hypercycle import hypercycle_step

def run_demo(steps=20):
    N, S, C, N2 = 0.1, 1.0, 0.5, 0.3
    for t in range(steps):
        N, S, C, N2 = hypercycle_step(N, S, C, N2)
        print(f"t={t}  Microbes={N:.3f}  Substrate={S:.3f}  C={C:.3f}  N={N2:.3f}")

if __name__ == "__main__":
    run_demo()
```

---

# ✅ **3_Data（CSVテンプレート）**

以下をそのまま CSV として作成してください。

---

## 📁 **3_Data/MBT55_Composition.csv**

```
Microbe,Relative_Abundance
Bacillus_sp,0.25
Pseudomonas_sp,0.18
Actinomycetes,0.12
Yeast,0.10
Others,0.35
```

---

## 📁 **3_Data/Enzyme_Activity.csv**

```
Enzyme,Activity_U_per_mL
Oxidoreductase,120
Hydrolase,85
Transferase,60
Lyase,40
```

---

## 📁 **3_Data/Soil_Improvement.csv**

```
Day,Organic_C,Total_N,CN_Ratio,pH
0,1.2,0.08,15,6.2
7,1.4,0.09,14,6.4
14,1.6,0.10,13,6.6
30,1.9,0.12,12,6.8
```

---

## 📁 **3_Data/GHG_FieldData.csv**

```
Day,CH4_ppm,CO2_ppm,N2O_ppm
0,1800,420,0.32
7,1500,410,0.28
14,1200,395,0.25
30,900,380,0.22
```

---

## 📁 **3_Data/HeavyMetal_Transformation.csv**

```
Metal,Initial_mg_per_kg,After_30d_mg_per_kg
Cd,2.1,0.8
Pb,15.0,6.2
As,4.5,1.9
Cr,8.0,3.1
```

---

# 🔥 **次に進める作業**

以下を同時に進められます：

### **A. 4_Applications（英語＋日本語）テンプレート生成**

### **B. 5_ClimateFinance（英語＋日本語）テンプレート生成**

### **C. 6_Diagrams（必要な図の一覧＋説明）生成**

Kaz、次も一気に進めます。

[[COA-21. 4_Applications（英語版テンプレート）]]
