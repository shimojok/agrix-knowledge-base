1. リポジトリフォルダを開く
GitHub Desktopで Repository → Show in Explorer をクリック

2. 作成したコードファイルをコピー
以下のファイルをフォルダ内の適切な場所に配置:           -------------------------------------------最初からアドバイス下さい。

---

## 🚀 **最初からステップバイステップで説明します**

---

## 📁 **ステップ1: リポジトリフォルダを開く**

### **GitHub Desktopで開く方法：**

1. **GitHub Desktopを起動**
   - スタートメニューから「GitHub Desktop」をクリック

2. **リポジトリを選択**
   - 左側のリポジトリ一覧から「**M3-BioSynergy**」をクリック

3. **エクスプローラーで開く**
   - 画面上部のメニューから「**Repository**」→「**Show in Explorer**」をクリック

4. **フォルダが開く**
   - `E:\OneDrive\ドキュメント\GitHub\M3-BioSynergy` が開きます

---

## 📝 **ステップ2: 作成したコードファイルをコピー**

### **開いたフォルダの内容を確認：**
```
M3-BioSynergy/
├── README.md
├── requirements.txt
├── src/
│   └── core/
│       └── microbial_dynamics.py
└── examples/
    └── basic_simulation.py
```

---

## 📄 **ステップ3: 追加するファイル一覧**

### **ファイル1: LICENSE**
**保存場所:** `M3-BioSynergy/LICENSE`

```text
MIT License

Copyright (c) 2024 Bionexus Holdings

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

### **ファイル2: src/core/__init__.py**
**保存場所:** `M3-BioSynergy/src/core/__init__.py`

```python
"""
M³-BioSynergy Core Module
Microbial-Metabolic-Modular Theory Implementation
"""

from .microbial_diversity import MicrobialDiversityEngine, MicrobialSpecies
from .hypercycle_engine import HypercycleEngine, HypercycleNode
from .nutrient_cascade import NutrientCascadeEngine, CascadeStage

__all__ = [
    'MicrobialDiversityEngine',
    'MicrobialSpecies',
    'HypercycleEngine',
    'HypercycleNode',
    'NutrientCascadeEngine',
    'CascadeStage'
]

__version__ = '1.0.0'
```

---

### **ファイル3: src/core/microbial_diversity.py**
**保存場所:** `M3-BioSynergy/src/core/microbial_diversity.py`

```python
"""
Microbial Diversity Model for MBT55 Consortium
Implements 120-species symbiotic network based on Ecological Hypercycle Theory
"""

import numpy as np
from scipy.integrate import odeint
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class MicrobialSpecies:
    """Individual microbial species in MBT55 consortium"""
    id: int
    name: str
    functional_group: str  # decomposer, converter, synthesizer, controller
    metabolic_type: str    # aerobic, anaerobic, facultative
    growth_rate: float     # μ_i
    substrate_affinity: float
    temperature_optimum: float
    ph_optimum: float
    synergy_potential: float = 0.0
    redundancy_index: float = 0.0


class MicrobialDiversityEngine:
    """Core engine for 120-species microbial diversity modeling"""
    
    def __init__(self, n_species: int = 120):
        self.n_species = n_species
        self.species: List[MicrobialSpecies] = []
        self.interaction_matrix: np.ndarray = None
        self._initialize_mbt55_consortium()
    
    def _initialize_mbt55_consortium(self):
        """Initialize MBT55-specific 120-species consortium"""
        functional_groups = {
            'decomposer': 0.40,
            'converter': 0.25,
            'synthesizer': 0.20,
            'controller': 0.15
        }
        
        species_id = 0
        species_list = []
        
        for group, proportion in functional_groups.items():
            n_in_group = int(self.n_species * proportion)
            
            for i in range(n_in_group):
                if group == 'decomposer':
                    growth_rate = np.random.uniform(0.6, 0.9)
                    temp_opt = np.random.uniform(25, 35)
                    metabolic = np.random.choice(['aerobic', 'facultative'], p=[0.7, 0.3])
                elif group == 'converter':
                    growth_rate = np.random.uniform(0.4, 0.7)
                    temp_opt = np.random.uniform(30, 40)
                    metabolic = np.random.choice(['facultative', 'anaerobic'], p=[0.6, 0.4])
                elif group == 'synthesizer':
                    growth_rate = np.random.uniform(0.3, 0.5)
                    temp_opt = np.random.uniform(20, 30)
                    metabolic = np.random.choice(['aerobic', 'facultative'], p=[0.5, 0.5])
                else:
                    growth_rate = np.random.uniform(0.2, 0.4)
                    temp_opt = np.random.uniform(25, 35)
                    metabolic = np.random.choice(['facultative', 'anaerobic'], p=[0.4, 0.6])
                
                species = MicrobialSpecies(
                    id=species_id,
                    name=f"MBT55_{group}_{i:03d}",
                    functional_group=group,
                    metabolic_type=metabolic,
                    growth_rate=growth_rate,
                    substrate_affinity=np.random.uniform(0.1, 2.0),
                    temperature_optimum=temp_opt,
                    ph_optimum=np.random.uniform(6.0, 7.5),
                    synergy_potential=np.random.uniform(0.1, 0.5),
                    redundancy_index=np.random.uniform(0.3, 0.8)
                )
                species_list.append(species)
                species_id += 1
        
        self.species = species_list
        self._generate_interaction_matrix()
    
    def _generate_interaction_matrix(self):
        """Generate symbiotic interaction matrix γ_ij"""
        n = self.n_species
        gamma = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    gamma[i, j] = -0.05
                else:
                    if self._should_interact(self.species[i], self.species[j]):
                        strength = np.random.uniform(0.02, 0.15)
                        gamma[i, j] = strength
                        if self.species[j].functional_group == 'controller':
                            gamma[i, j] *= 1.5
        
        self.interaction_matrix = gamma
        self._calculate_mei()
    
    def _should_interact(self, sp1: MicrobialSpecies, sp2: MicrobialSpecies) -> bool:
        """Determine if two species should have symbiotic interaction"""
        base_prob = 0.75
        
        complementary_pairs = [
            ('decomposer', 'converter'),
            ('converter', 'synthesizer'),
            ('synthesizer', 'controller'),
            ('controller', 'decomposer')
        ]
        
        if (sp1.functional_group, sp2.functional_group) in complementary_pairs:
            base_prob += 0.15
            
        return np.random.random() < base_prob
    
    def _calculate_mei(self):
        """Calculate Microbial Emergence Index (MEI) = Σγ_ij / √n"""
        n = self.n_species
        total_gamma = np.sum(np.abs(self.interaction_matrix))
        self.mei = total_gamma / np.sqrt(n)
        self.hypercycle_threshold = 0.85
        self.hypercycle_formed = self.mei > self.hypercycle_threshold
    
    def simulate_dynamics(self,
                         initial_population: np.ndarray,
                         duration_hours: float = 24.0,
                         temperature: float = 25.0,
                         ph: float = 6.8,
                         moisture: float = 0.6,
                         mbt_intervention: float = 1.0) -> Dict:
        """Simulate microbial population dynamics over time"""
        
        def system(state, t):
            env_factor = self._environmental_stress_factor(temperature, ph, moisture)
            growth_rates = np.array([sp.growth_rate for sp in self.species])
            growth = growth_rates * state * (1 - state / 10000) * env_factor
            interactions = self.interaction_matrix @ state * mbt_intervention
            
            controller_indices = [i for i, sp in enumerate(self.species) 
                                 if sp.functional_group == 'controller']
            if controller_indices:
                controller_activity = np.mean(state[controller_indices]) / 1000
                interactions *= (1 + controller_activity * 0.5)
            
            return growth + interactions
        
        t = np.linspace(0, duration_hours, 100)
        solution = odeint(system, initial_population, t)
        
        final_population = solution[-1]
        total_biomass = np.sum(final_population)
        
        diversity_time = []
        for pop in solution:
            proportions = pop / np.sum(pop)
            proportions = proportions[proportions > 0]
            diversity_time.append(-np.sum(proportions * np.log(proportions)))
        
        return {
            'time': t,
            'population': solution,
            'final_population': final_population,
            'total_biomass': total_biomass,
            'diversity_trajectory': np.array(diversity_time),
            'final_diversity': diversity_time[-1],
            'mei': self.mei,
            'hypercycle_formed': self.hypercycle_formed
        }
    
    def _environmental_stress_factor(self, temp: float, ph: float, moisture: float) -> float:
        """Calculate environmental stress factor"""
        temp_factor = self._temperature_response(temp)
        ph_factor = self._ph_response(ph)
        moisture_factor = self._moisture_response(moisture)
        return 0.5 * temp_factor + 0.3 * ph_factor + 0.2 * moisture_factor
    
    def _temperature_response(self, temp: float) -> float:
        if 20 <= temp <= 40:
            return 1.0
        elif temp < 10:
            return 0.3 + 0.07 * temp
        elif temp > 45:
            return 1.5 - 0.03 * temp
        else:
            return np.exp(-0.5 * ((temp - 30) / 15) ** 2)
    
    def _ph_response(self, ph: float) -> float:
        if 6.0 <= ph <= 7.5:
            return 1.0
        elif ph < 5.0:
            return 0.4
        elif ph > 8.5:
            return 0.5
        else:
            return np.exp(-0.5 * ((ph - 6.8) / 1.2) ** 2)
    
    def _moisture_response(self, moisture: float) -> float:
        if 0.4 <= moisture <= 0.8:
            return 1.0
        elif moisture < 0.2:
            return 0.2
        elif moisture > 0.9:
            return 0.7
        else:
            if moisture < 0.4:
                return 0.2 + 2.0 * moisture
            else:
                return 2.6 - 2.0 * moisture
    
    def get_emergent_metrics(self) -> Dict:
        return {
            'species_count': self.n_species,
            'mei': self.mei,
            'hypercycle_threshold': self.hypercycle_threshold,
            'hypercycle_formed': self.hypercycle_formed
        }
```

---

### **ファイル4: src/core/hypercycle_engine.py**
**保存場所:** `M3-BioSynergy/src/core/hypercycle_engine.py`

```python
"""
Ecological Hypercycle Engine
Implements self-amplifying cyclic metabolic networks
"""

import numpy as np
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class HypercycleNode:
    """Node in hypercycle network"""
    id: str
    name: str
    catalytic_activity: float
    production_rate: float
    consumption_rate: float
    coupling_strength: Dict[str, float] = None


class HypercycleEngine:
    """Core engine for ecological hypercycle simulation"""
    
    def __init__(self, n_nodes: int = 4):
        self.n_nodes = n_nodes
        self.nodes: List[HypercycleNode] = []
        self.coupling_matrix: np.ndarray = None
        self._initialize_hypercycle()
    
    def _initialize_hypercycle(self):
        """Initialize MBT55 hypercycle with 4 functional nodes"""
        node_names = ['Decomposition', 'Conversion', 'Synthesis', 'Regulation']
        
        for i, name in enumerate(node_names):
            node = HypercycleNode(
                id=f"H{i+1}",
                name=name,
                catalytic_activity=np.random.uniform(0.5, 1.0),
                production_rate=np.random.uniform(0.3, 0.8),
                consumption_rate=np.random.uniform(0.1, 0.4),
                coupling_strength={}
            )
            self.nodes.append(node)
        
        self._build_coupling_matrix()
    
    def _build_coupling_matrix(self):
        """Build hypercycle coupling matrix γ_ij (cyclic structure)"""
        n = self.n_nodes
        gamma = np.zeros((n, n))
        
        for i in range(n):
            j = (i + 1) % n
            gamma[i, j] = self.nodes[i].catalytic_activity * 0.8
        
        self.coupling_matrix = gamma
    
    def simulate_cycle(self,
                      initial_state: np.ndarray,
                      duration_hours: float = 24.0,
                      external_input: float = 0.0) -> Dict:
        """Simulate hypercycle dynamics"""
        n = self.n_nodes
        dt = 0.1
        n_steps = int(duration_hours / dt)
        
        state = np.zeros((n_steps + 1, n))
        state[0] = initial_state
        
        for step in range(n_steps):
            current = state[step]
            next_state = current.copy()
            
            for i in range(n):
                growth = self.nodes[i].production_rate * current[i]
                coupling = 0.0
                for j in range(n):
                    if self.coupling_matrix[j, i] > 0:
                        coupling += self.coupling_matrix[j, i] * current[j]
                loss = self.nodes[i].consumption_rate * current[i]
                external = external_input if i == 0 else 0
                
                next_state[i] = current[i] + (growth * (1 + coupling) - loss + external) * dt
                next_state[i] = max(next_state[i], 0)
            
            state[step + 1] = next_state
        
        final_state = state[-1]
        amplification = np.sum(final_state) / np.sum(initial_state)
        coupling_activity = np.sum(self.coupling_matrix) / (n * n)
        self_sustaining = all(final_state > initial_state * 0.5)
        
        return {
            'time': np.linspace(0, duration_hours, n_steps + 1),
            'state': state,
            'final_state': final_state,
            'amplification': amplification,
            'coupling_activity': coupling_activity,
            'self_sustaining': self_sustaining,
            'hypercycle_formed': amplification > 1.5 and coupling_activity > 0.3
        }
    
    def get_hypercycle_metrics(self) -> Dict:
        return {
            'n_nodes': self.n_nodes,
            'catalytic_activities': [node.catalytic_activity for node in self.nodes],
            'production_rates': [node.production_rate for node in self.nodes],
            'consumption_rates': [node.consumption_rate for node in self.nodes]
        }
```

---

### **ファイル5: src/core/nutrient_cascade.py**
**保存場所:** `M3-BioSynergy/src/core/nutrient_cascade.py`

```python
"""
Nutrient Cascade Module
Three-stage decomposition → conversion → synthesis model
"""

import numpy as np
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class CascadeStage:
    """Individual stage in nutrient cascade"""
    name: str
    input_substrates: List[str]
    output_products: List[str]
    conversion_efficiency: float
    rate_constant: float
    temperature_optimum: float
    ph_optimum: float


class NutrientCascadeEngine:
    """Three-stage nutrient cascade model based on MBT55 data"""
    
    def __init__(self):
        self.stages = self._initialize_cascade()
        self.substrate_pools = {}
        self.product_pools = {}
        self._initialize_pools()
    
    def _initialize_cascade(self) -> List[CascadeStage]:
        return [
            CascadeStage(
                name="Decomposition",
                input_substrates=["lignin", "cellulose", "protein", "lipid"],
                output_products=["simple_sugars", "amino_acids", "fatty_acids"],
                conversion_efficiency=0.85,
                rate_constant=0.5,
                temperature_optimum=30.0,
                ph_optimum=6.8
            ),
            CascadeStage(
                name="Conversion",
                input_substrates=["simple_sugars", "amino_acids", "fatty_acids"],
                output_products=["organic_acids", "alcohols", "short_chain"],
                conversion_efficiency=0.75,
                rate_constant=0.4,
                temperature_optimum=32.0,
                ph_optimum=6.5
            ),
            CascadeStage(
                name="Synthesis",
                input_substrates=["organic_acids", "alcohols", "short_chain"],
                output_products=["humic_acids", "fulvic_acids", "bioactive_compounds"],
                conversion_efficiency=0.65,
                rate_constant=0.3,
                temperature_optimum=28.0,
                ph_optimum=7.0
            )
        ]
    
    def _initialize_pools(self):
        self.substrate_pools = {
            'lignin': 100.0, 'cellulose': 100.0, 'protein': 50.0, 'lipid': 30.0
        }
        self.product_pools = {
            'simple_sugars': 0.0, 'amino_acids': 0.0, 'fatty_acids': 0.0,
            'organic_acids': 0.0, 'humic_acids': 0.0, 'fulvic_acids': 0.0
        }
    
    def simulate_cascade(self, duration_hours: float = 24.0, 
                         temperature: float = 25.0,
                         mbt_enhancement: float = 1.0) -> Dict:
        """Simulate nutrient cascade over time"""
        dt = 0.1
        n_steps = int(duration_hours / dt)
        
        history = {'time': [], 'stage1': [], 'stage2': [], 'stage3': [], 'total_conversion': []}
        current_substrates = self.substrate_pools.copy()
        current_products = self.product_pools.copy()
        
        for step in range(n_steps):
            t = step * dt
            
            for stage in self.stages:
                rate = (stage.rate_constant * 
                       np.exp(0.1 * (temperature - stage.temperature_optimum)) *
                       mbt_enhancement)
                
                for substrate in stage.input_substrates:
                    if current_substrates.get(substrate, 0) > 0:
                        conversion = current_substrates[substrate] * rate * dt * 0.1
                        conversion = min(conversion, current_substrates[substrate])
                        current_substrates[substrate] -= conversion
                        
                        for product in stage.output_products:
                            current_products[product] = current_products.get(product, 0) + conversion * 0.7
                        loss = conversion * 0.3
                
                for product in stage.input_substrates:
                    if current_products.get(product, 0) > 0 and stage.name != "Decomposition":
                        conversion = current_products[product] * rate * dt * 0.15
                        conversion = min(conversion, current_products[product])
                        current_products[product] -= conversion
                        
                        for out_product in stage.output_products:
                            current_products[out_product] = current_products.get(out_product, 0) + conversion * 0.6
                        loss = conversion * 0.4
            
            if step % 100 == 0:
                history['time'].append(t)
                history['stage1'].append(sum(current_products.get(p, 0) for p in self.stages[0].output_products))
                history['stage2'].append(sum(current_products.get(p, 0) for p in self.stages[1].output_products))
                history['stage3'].append(sum(current_products.get(p, 0) for p in self.stages[2].output_products))
                history['total_conversion'].append(sum(current_products.values()))
        
        final_products = sum(current_products.values())
        initial_total = sum(self.product_pools.values())
        cue = final_products / initial_total if initial_total > 0 else 0
        
        return {
            'history': history,
            'final_substrates': current_substrates,
            'final_products': current_products,
            'total_humus': current_products.get('humic_acids', 0) + current_products.get('fulvic_acids', 0),
            'carbon_use_efficiency': cue
        }
```

---

### **ファイル6: tests/__init__.py**
**保存場所:** `M3-BioSynergy/tests/__init__.py`

```python
"""Test suite for M³-BioSynergy"""
```

---

### **ファイル7: src/utils/__init__.py**
**保存場所:** `M3-BioSynergy/src/utils/__init__.py`

```python
"""Utility modules for M³-BioSynergy"""
```

---

## 📋 **ステップ4: ファイルの配置方法（画像付き説明）**

### **① エクスプローラーで開く**
GitHub Desktopで「Repository」→「Show in Explorer」

### **② フォルダ構造を作成**
以下のフォルダがない場合は作成：
- `src/core/` フォルダ（既存）
- `src/utils/` フォルダ（新規作成）
- `tests/` フォルダ（新規作成）

### **③ ファイルをコピー**
各ファイルを指定された場所に配置

---

## ✅ **ステップ5: GitHub Desktopで確認**

1. **GitHub Desktopに戻る**
2. 左側の「Changes」タブに追加したファイルが表示される
3. チェックボックスがすべてONになっていることを確認

### **コミット**
4. 左下の「Summary」に `feat: Add hypercycle core implementation with MEI calculation` と入力
5. 「Commit to main」をクリック

### **プッシュ**
6. 右上の「Push origin」をクリック

---

## 🎯 **完成確認**

https://github.com/shimojok/M3-BioSynergy を開いて、以下のファイルが追加されているか確認：
- ✅ `LICENSE`
- ✅ `src/core/__init__.py`
- ✅ `src/core/microbial_diversity.py`
- ✅ `src/core/hypercycle_engine.py`
- ✅ `src/core/nutrient_cascade.py`
- ✅ `tests/__init__.py`
- ✅ `src/utils/__init__.py`

---

**今すぐこの手順を始めますか？** 各ファイルの内容をコピーする準備はできています。 🚀

[[DSH16. 経過]]
