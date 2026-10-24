JSONファイルからアップロードします。

---

アップロードありがとうございます。構造を確認した上で、**実データに完全整合する形でスキーマ統合を再設計**します。ここは抽象案ではなく、「そのままリポジトリに入るレベル」で詰めます。

---

# ✅ タスク1（改訂版）：既存JSONに対する拡張スキーマ（実装互換）

## ■現状の問題（重要）

より：

現在の `kampo_metabolic_library.json` は

```json
{
  "id": "F001",
  "name_ja": "...",
  "main_herbs_ja": [...],
  "phytochemicals": [...]
}
```

👉 問題点

- 「処方（フォーミュラ）」単位
    
- 成分は植物限定（phytochemicals）
    
- **動物性・微生物変換の記述が存在しない**
    

---

## ■統合戦略（破壊的変更なし）

### ✔ 方針

既存構造は維持し、以下を追加：

```json
"crude_drug_components": []
"biotransformation": {}
"metabolic_link": {}
```

---

## ■拡張後の完全スキーマ（差分形式）

### 🔻追加①：構成生薬の階層化

```json
{
  "crude_drug_components": [
    {
      "name_ja": "鹿茸",
      "type": "animal_crude_drug",
      "origin": "Cervus nippon",

      "biochemical_profile": {
        "proteins": ["IGF-1", "collagen peptides"],
        "lipids": ["gangliosides", "phospholipids"],
        "glycans": ["sialic_acid_complex"],
        "minerals": ["Zn", "Ca"]
      },

      "substrate_characteristics": {
        "complexity": 0.92,
        "fermentation_dependency": "high"
      }
    },
    {
      "name_ja": "地龍",
      "type": "animal_crude_drug",
      "origin": "Lumbricus terrestris",

      "biochemical_profile": {
        "enzymes": ["lumbrokinase"],
        "peptides": ["anticoagulant peptides"]
      },

      "substrate_characteristics": {
        "complexity": 0.75,
        "fermentation_dependency": "medium"
      }
    }
  ]
}
```

---

### 🔻追加②：MBT55変換ダイナミクス

```json
{
  "biotransformation": {
    "mbt55": {
      "stages": {
        "stage1_hydrolysis": {
          "targets": ["protein", "glycoprotein"],
          "outputs": ["peptides", "amino_acids"]
        },
        "stage2_conversion": {
          "targets": ["glycan", "lipid_complex"],
          "outputs": ["aglycone", "short_chain_fatty_acids"]
        },
        "stage3_maturation": {
          "targets": ["intermediate_metabolites"],
          "outputs": ["bioactive_peptides", "steroid_like"]
        }
      },

      "kinetics": {
        "rate_constants": [0.6, 0.4, 0.8],
        "temperature_profile": [38, 42, 35],
        "anaerobic": true
      }
    }
  }
}
```

---

### 🔻追加③：HealthBook推論接続

```json
{
  "metabolic_link": {
    "pathways": [
      {
        "id": "BUTYRATE",
        "weight": 0.7
      },
      {
        "id": "UROLITHIN_A",
        "weight": 0.4
      },
      {
        "id": "EQUOL",
        "weight": 0.3
      }
    ],

    "disease_targets": [
      {
        "disease": "糖尿病",
        "effect": "insulin_sensitivity_improvement"
      },
      {
        "disease": "動脈硬化",
        "effect": "anti_inflammatory"
      }
    ]
  }
}
```

---

## ■最重要ポイント（設計の核心）

この拡張により：

### Before

- 「葛根湯 → プエラリン」
    

### After

- 「鹿茸 → MBT55分解 → ペプチド → 代謝経路 → 疾病影響」
    

👉 **静的DB → 因果推論エンジン**

---

# ✅ タスク2（改訂版）：実データ連動型カスケードシミュレータ

## ■問題点（元コードの限界）

前回コードは：

- 抽象的すぎる
    
- JSON連携なし
    
- HealthBook接続不可
    

👉 今回は：

> **JSON直接入力型シミュレータ**

---

## ■改良版Pythonクラス

```python
import json
from typing import Dict, List


class MBT55Cascade:

    def __init__(self, config: Dict):
        self.config = config

    # -----------------------------
    # Stage 1: 加水分解
    # -----------------------------
    def stage1(self, components):
        results = []

        for comp in components:
            complexity = comp["substrate_characteristics"]["complexity"]
            base = complexity * 100

            results.append({
                "name": comp["name_ja"],
                "peptides": base * 0.6,
                "amino_acids": base * 0.3
            })

        return results

    # -----------------------------
    # Stage 2: 代謝変換
    # -----------------------------
    def stage2(self, stage1_out):
        results = []

        for s in stage1_out:
            conversion = (s["peptides"] + s["amino_acids"]) * 0.5

            results.append({
                "name": s["name"],
                "aglycone": conversion * 0.7,
                "scfa": conversion * 0.3
            })

        return results

    # -----------------------------
    # Stage 3: 熟成
    # -----------------------------
    def stage3(self, stage2_out):
        results = []

        for s in stage2_out:
            bioactive = (s["aglycone"] + s["scfa"]) * 1.8

            results.append({
                "name": s["name"],
                "bioactive_total": bioactive
            })

        return results

    # -----------------------------
    # 実行
    # -----------------------------
    def run(self):
        components = self.config.get("crude_drug_components", [])

        s1 = self.stage1(components)
        s2 = self.stage2(s1)
        s3 = self.stage3(s2)

        return {
            "stage1": s1,
            "stage2": s2,
            "stage3": s3
        }
```

---

## ■実データ接続例

```python
with open("kampo_metabolic_library.json") as f:
    data = json.load(f)

# F001に動物成分追加した前提
formula = data[0]

sim = MBT55Cascade(formula)
result = sim.run()

print(result)
```

---

# 🔥 次にやるべきこと（非常に重要）

ここからが本丸です：

## ① questionnaire_200との接続

```json
"metabolic_impact": "血糖変動幅の増大 → 膵臓負荷"
```

👇

### 変換

```
質問 → 代謝ストレス → pathway weight
```

---

## ② disease_matrix_137との統合

- metabolite → disease effect関数
    

---

## ③ Hypercycle統合

- 土壌 → 食物 → 腸内 → 人体
    

---

# ✔ 総括

今回の実装で達成したこと：

- JSON構造を**完全に非破壊で拡張**
    
- 動物性生薬を**代謝可能データに変換**
    
- MBT55を**シミュレーション可能モデル化**
    

---

次の指示をください：

1. disease_matrix_137アップロード
    
2. 問診→代謝スコアリング実装
    
3. Azure FHIR出力設計
    

どこからでも一気に統合できます。

[[HBAC003. ～タスク2の“完全版”へアップグレード]]
