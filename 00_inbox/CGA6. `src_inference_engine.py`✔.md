現在のHealthBook-AIプロジェクトに、以下の重要な設計変更を適用します。
[[DA19. 必須ファイル（最初の5つ）]]
## 変更1: 推論エンジンの実装
添付の「HealthBook Platform v5.0.md」の runEngine() ロジックを参照し、
以下の5ステップをPythonで再実装してください：
1. 回答からアクティブなリスク因子を収集（重み付き）
2. 疾病リスクスコア算出（マッチ率 × 重み）
3. MBT55 5経路の介入優先度を算出
4. 漢方処方マッチング（上位疾患から重複排除）
5. 予防スコア算出（上位10疾患の平均リスクから逆算）

## 変更2: データ構造の統合
- 200項目問診（添付のquestionnaire JSON）
- 137疾病マトリックス（添付のdisease_matrix JSON）
- 漢方代謝ライブラリー（添付のkampo_metabolic_library JSON）
- 5経路（PATH_01〜05）をMBT55の3段階カスケードと接続

## 変更3: Game 3は破棄
Game 3の10項目問診・3疾病モデルは要件を満たさないため、
推論コアとしては採用しません。UI構造のみ参考にしてください。

## 出力
- src/inference_engine.py（runEngineのPython移植版）
- 既存のMetaboliteDiseaseMapper、GutMetabolismConnector、FHIRClinicalDecisionSupportとの統合インターフェース

---

了解しました。設計変更に基づき、**runEngine()のPython移植 + 統合インターフェース**を、HealthBookの因果推論構造（リスク因子 → 疾病 → 経路 → 介入）に忠実に再構築します。

以下はそのまま `src/inference_engine.py` として実装可能な形です。

---

# ✅ `src/inference_engine.py`

```python
import json
from collections import defaultdict
from typing import Dict, List, Any


class HealthBookInferenceEngine:

    def __init__(self, questionnaire_path, disease_matrix_path, kampo_library_path):
        self.Q = self._load_json(questionnaire_path)["questions"]
        self.DM = self._load_json(disease_matrix_path)["disease_matrix"]
        self.KL = self._load_json(kampo_library_path)

        # インデックス構築
        self.disease_rf_map = self._build_disease_rf_map()
        self.kampo_dict = {k["id"]: k for k in self.KL}

    def _load_json(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _build_disease_rf_map(self):
        """
        disease_name → risk_factor list
        """
        rf_map = {}
        for d in self.DM:
            rf_map[d["disease_id"]] = {
                "name": d["disease_name_ja"],
                "rf": d.get("risk_factors", []),  # 拡張対応
                "kampo": d.get("recommended_kampo", [])
            }
        return rf_map

    # -----------------------------
    # ① アクティブリスク因子抽出
    # -----------------------------
    def extract_active_risk_factors(self, answers: Dict[int, int]):
        """
        answers: {question_id: 0/1/2} (No / Sometimes / Often)
        """
        rf_scores = defaultdict(float)

        for qid, ans in answers.items():
            if ans == 0:
                continue

            q = self.Q[str(qid)]
            weight = q["weight"]

            # スコア係数
            multiplier = 1.0 if ans == 2 else 0.5

            for rf in q["risk_factors"]:
                rf_scores[rf] += weight * multiplier

        return dict(rf_scores)

    # -----------------------------
    # ② 疾病リスクスコア算出
    # -----------------------------
    def calculate_disease_risk(self, rf_scores):
        disease_scores = []

        for d in self.DM:
            disease_id = d["disease_id"]
            disease_name = d["disease_name_ja"]

            disease_rf = d.get("risk_factors", [])

            if not disease_rf:
                continue

            match_score = 0
            total_weight = 0

            for rf in disease_rf:
                total_weight += 1
                if rf in rf_scores:
                    match_score += rf_scores[rf]

            if total_weight == 0:
                continue

            score = match_score / total_weight

            disease_scores.append({
                "disease_id": disease_id,
                "disease_name": disease_name,
                "score": score
            })

        return sorted(disease_scores, key=lambda x: x["score"], reverse=True)

    # -----------------------------
    # ③ MBT55 経路優先度
    # -----------------------------
    def calculate_mbt55_pathways(self, top_diseases):
        """
        仮実装: disease → pathway マッピング必要
        """
        pathway_scores = defaultdict(float)

        # 仮: disease_id のプレフィックスで分岐
        for d in top_diseases[:10]:
            did = d["disease_id"]
            score = d["score"]

            if did.startswith("D00"):
                pathway_scores["PATH_01"] += score
            elif did.startswith("D01"):
                pathway_scores["PATH_02"] += score
            elif did.startswith("D02"):
                pathway_scores["PATH_03"] += score
            elif did.startswith("D03"):
                pathway_scores["PATH_04"] += score
            else:
                pathway_scores["PATH_05"] += score

        return dict(sorted(pathway_scores.items(), key=lambda x: x[1], reverse=True))

    # -----------------------------
    # ④ 漢方マッチング
    # -----------------------------
    def match_kampo(self, top_diseases):
        kampo_set = []
        seen = set()

        for d in top_diseases[:10]:
            for kid in d.get("recommended_kampo", []):
                if kid not in seen and kid in self.kampo_dict:
                    kampo_set.append(self.kampo_dict[kid])
                    seen.add(kid)

        return kampo_set

    # -----------------------------
    # ⑤ 予防スコア
    # -----------------------------
    def calculate_prevention_score(self, top_diseases):
        if not top_diseases:
            return 100

        top10 = top_diseases[:10]
        avg_risk = sum(d["score"] for d in top10) / len(top10)

        return round(100 * (1 - avg_risk), 2)

    # -----------------------------
    # 🚀 runEngine
    # -----------------------------
    def run_engine(self, answers: Dict[int, int]):

        # ① リスク因子
        rf_scores = self.extract_active_risk_factors(answers)

        # ② 疾病スコア
        disease_scores = self.calculate_disease_risk(rf_scores)

        # ③ 経路優先度
        pathway_scores = self.calculate_mbt55_pathways(disease_scores)

        # ④ 漢方
        kampo = self.match_kampo(disease_scores)

        # ⑤ 予防スコア
        prevention_score = self.calculate_prevention_score(disease_scores)

        return {
            "risk_factors": rf_scores,
            "disease_ranking": disease_scores[:20],
            "mbt55_pathways": pathway_scores,
            "kampo_recommendations": kampo,
            "prevention_score": prevention_score
        }
```

---

# ⚠️ 重要な構造ギャップ（必須修正）

現在の `disease_matrix_137.json` には：

```json
"risk_factors": []
```

が存在しません（致命的）。

👉 runEngine成立には以下が必須です：

```json
{
  "disease_id": "D006",
  "risk_factors": ["不規則型", "間食多い", "糖質過多"]
}
```

これは「病気と食生活の関係シート」の本体です。  
この列がないと **マッチ率計算が成立しません**。

---

# ✅ インターフェース統合

## 1. MetaboliteDiseaseMapper

```python
class MetaboliteDiseaseMapper:

    def map(self, disease_ranking, kampo_list):
        return [
            {
                "disease": d["disease_name"],
                "metabolites": self._extract_metabolites(kampo_list)
            }
            for d in disease_ranking[:10]
        ]

    def _extract_metabolites(self, kampo_list):
        mets = []
        for k in kampo_list:
            for p in k.get("phytochemicals", []):
                mets.append(p["name_en"])
        return list(set(mets))
```

---

## 2. GutMetabolismConnector

```python
class GutMetabolismConnector:

    def connect(self, pathways, kampo_list):
        result = []

        for k in kampo_list:
            result.append({
                "kampo": k["name_en"],
                "mbt55_strains": k["mbt55_optimization"]["recommended_strains"],
                "pathways": list(set([
                    p["pathway"] for p in k.get("phytochemicals", [])
                ]))
            })

        return result
```

---

## 3. FHIRClinicalDecisionSupport

```python
class FHIRClinicalDecisionSupport:

    def build(self, inference_result):
        return {
            "resourceType": "ClinicalImpression",
            "status": "completed",
            "summary": "HealthBook AI Inference",
            "finding": [
                {
                    "itemCodeableConcept": {
                        "text": d["disease_name"]
                    },
                    "basis": f"Risk Score: {d['score']:.2f}"
                }
                for d in inference_result["disease_ranking"][:10]
            ],
            "prognosisCodeableConcept": {
                "text": f"Prevention Score: {inference_result['prevention_score']}"
            }
        }
```

---

# 🔬 次のクリティカルタスク

このままでは「構造は完成・意味は未完成」です。  
優先順位は明確です：

### ① Disease × RiskFactor 完全復元（最重要）

- 浜田式マトリックスの再構築
    
- 137疾病 × 約100RF
    

### ② Disease → Pathway（D2P）マッピング

- PATH_01：炎症・免疫
    
- PATH_02：解毒・肝代謝
    
- PATH_03：循環・ミトコンドリア
    
- PATH_04：腸・神経
    
- PATH_05：内分泌
    

### ③ MBT55カスケード統合

- Stage1: 分解（糖鎖・タンパク）
    
- Stage2: 変換（アグリコン化）
    
- Stage3: 再合成（シグナル分子）
    

---

必要なら次は：

- D2Pマッピングの完全設計
    
- RF→代謝ベクトル（15経路）変換
    
- 因果推論グラフ（SCFA・エクオール・ウロリチンA）
    

まで一気に統合できます。

[[CGA7. 修正版 `src_inference_engine.py`]]

