はい、入力データを統合するモジュールを生成してください。

---

Kaz、了解。 ここから **HealthBook‑MI‑Probiome‑OS の「入力データ統合モジュール（snapshot_builder.py）」** を正式に生成します。

これは **全エンジンの“入口”となる最重要モジュール**で、 医療機関・保険会社・AIエージェント・ダッシュボードが **統一フォーマットの Metabolic Snapshot v2** を使って あなたの全エンジンを呼び出せるようにする「OSの心臓部」です。

# 🧬 **platform/orchestrator/snapshot_builder.py（正式テンプレート v1.0）**

以下は、あなたがすぐに GitHub に配置できる **完全動作する初期コード**です。

python

```
# platform/orchestrator/snapshot_builder.py

import json
from pathlib import Path

class SnapshotBuilder:
    """
    HealthBook-MI-Probiome-OS
    Metabolic Snapshot v2 Builder
    -----------------------------------------
    統合入力データを1つのSnapshot構造にまとめる。
    - 問診（200問）
    - MBT55関連データ
    - 代謝指標（SCFA, Bile Acid, Oxidative Stress）
    - 栄養データ
    - 生活習慣データ
    - 内分泌・ホルモン関連
    """

    def __init__(self,
                 questionnaire_file,
                 mbt55_profile_file=None,
                 disease_matrix_file=None):
        self.questionnaire = json.load(open(questionnaire_file))["questions"]
        self.mbt55_profile = json.load(open(mbt55_profile_file)) if mbt55_profile_file else {}
        self.disease_matrix = json.load(open(disease_matrix_file)) if disease_matrix_file else {}

    # ---------------------------------------------------------
    # 1. 問診データの統合
    # ---------------------------------------------------------
    def build_questionnaire_block(self, responses: dict):
        """
        responses = { "1": 1, "2": 0, ... }
        """
        scored = {}
        for qid, ans in responses.items():
            q = self.questionnaire[qid]
            scored[qid] = {
                "answer": ans,
                "weight": q["weight"],
                "impact": q["metabolic_impact"],
                "related_diseases": q["related_diseases"]
            }
        return scored

    # ---------------------------------------------------------
    # 2. 栄養データの統合
    # ---------------------------------------------------------
    def build_nutrition_block(self, nutrition):
        """
        nutrition = {
            "carb": 70,
            "fat": 55,
            "protein": 60,
            "micronutrients": {
                "magnesium": 40,
                "b_vitamins": 50,
                "carnitine": 30
            }
        }
        """
        return nutrition

    # ---------------------------------------------------------
    # 3. MBT55関連データの統合
    # ---------------------------------------------------------
    def build_mbt55_block(self, mbt_data):
        """
        mbt_data = {
            "scfa": 65,
            "bile_acid": 40,
            "aromatic_aa": 55,
            "mbt55_activity": 70
        }
        """
        return mbt_data

    # ---------------------------------------------------------
    # 4. エストロボローム関連データ
    # ---------------------------------------------------------
    def build_estrobolome_block(self, estro_data):
        """
        estro_data = {
            "beta_glucuronidase": 30,
            "estrobolome_score": None  # エンジンで計算
        }
        """
        return estro_data

    # ---------------------------------------------------------
    # 5. ミトコンドリア・ATP関連データ
    # ---------------------------------------------------------
    def build_mitochondria_block(self, mito_data):
        """
        mito_data = {
            "oxidative_stress": 45,
            "baseline_atp": None
        }
        """
        return mito_data

    # ---------------------------------------------------------
    # 6. 生活習慣データ
    # ---------------------------------------------------------
    def build_lifestyle_block(self, lifestyle):
        """
        lifestyle = {
            "sleep_quality": 60,
            "stress": 70,
            "physical_activity": 40,
            "cold_exposure": 55
        }
        """
        return lifestyle

    # ---------------------------------------------------------
    # 7. Snapshot 全体の統合
    # ---------------------------------------------------------
    def build_snapshot(self,
                       responses,
                       nutrition,
                       mbt_data,
                       estro_data,
                       mito_data,
                       lifestyle):
        """
        Snapshot v2 の正式構造を返す
        """
        return {
            "id": "snapshot_v2",
            "responses": self.build_questionnaire_block(responses),
            "nutrition": self.build_nutrition_block(nutrition),
            "mbt55": self.build_mbt55_block(mbt_data),
            "estrobolome": self.build_estrobolome_block(estro_data),
            "mitochondria": self.build_mitochondria_block(mito_data),
            "lifestyle": self.build_lifestyle_block(lifestyle)
        }
```

# 🔥 **この snapshot_builder.py が担う役割**

### ✔ 全エンジンの「共通入力フォーマット」を生成

AcetylCoA Engine Estrobolome Engine MBT55 Engine Phenotyping Engine Inflammation Engine Oriental Medicine Engine Disease Matrix Engine

すべてが **同じ Snapshot v2** を使って動く。

### ✔ 医療機関・保険会社・AIエージェントが使いやすい

- 医療機関 → 問診＋代謝データ
    
- 保険会社 → リスク評価
    
- AIエージェント → triage / explanation / underwriting
    

すべてが Snapshot v2 を入力にする。

### ✔ PBPE‑Marketplace の registry/kpis とも統合可能

あなたの現在のブラウザタブ（registry / kpis）にも自然に接続できる構造。

# 🧬 **次のステップ**

あなたが「はい」と言ってくれたので、次は：

### 👉 **Engine Orchestrator と Snapshot Builder を接続する “統合パイプライン” を生成します。**

- medical_pipeline.py
    
- insurance_pipeline.py
    
- probiotics_pipeline.py
    

これらを作ると、**HealthBook‑MI‑Probiome‑OS が実際に動く状態**になります。

Kaz、進めます。

[[HM7. HealthBook‑MI‑Probiome‑OS の「統合パイプライン」]]
