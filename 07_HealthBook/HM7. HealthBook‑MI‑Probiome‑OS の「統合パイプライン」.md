Engine Orchestrator と Snapshot Builder を接続する “統合パイプライン” を生成してください。

---

Kaz、ここから **HealthBook‑MI‑Probiome‑OS の「統合パイプライン」**を正式に生成します。 これは **Snapshot Builder → Engine Orchestrator → 各エンジン** を一気に接続し、 医療機関・保険会社・MBT55プロバイオティクス解析・AIエージェントが **1つの API / 1つの関数呼び出しで全エンジンを動かせる**ようにする “OS の動脈” です。

あなたのリポジトリの中核になるコードです。

# 🧬 **platform/pipelines/medical_pipeline.py（医療機関向け）**

python

```
# platform/pipelines/medical_pipeline.py

class MedicalPipeline:
    """
    医療機関向け統合パイプライン
    SnapshotBuilder → EngineOrchestrator → 医療レポート
    """

    def __init__(self, snapshot_builder, orchestrator):
        self.snapshot_builder = snapshot_builder
        self.orchestrator = orchestrator

    def run(self, responses, nutrition, mbt_data, estro_data, mito_data, lifestyle):
        # Snapshot v2 を構築
        snapshot = self.snapshot_builder.build_snapshot(
            responses, nutrition, mbt_data, estro_data, mito_data, lifestyle
        )

        # 全エンジンを実行
        results = self.orchestrator.run_all(snapshot)

        # 医療機関向けレポート形式に整形
        return {
            "snapshot": snapshot,
            "phenotype": results["phenotype"],
            "estrobolome": results["estrobolome"],
            "acetylcoa": results["acetylcoa"],
            "inflammation": results["inflammation"],
            "clinical_summary": self._clinical_summary(results)
        }

    def _clinical_summary(self, results):
        return {
            "metabolic_risk": results["phenotype"]["phenotype"],
            "hormone_status": results["estrobolome"]["hormone_balance_pattern"],
            "energy_status": results["acetylcoa"]["mi_acetylcoa_index"],
            "inflammation_load": results["inflammation"]["inflammation_load"]
        }
```

# 🧬 **platform/pipelines/insurance_pipeline.py（生命保険会社向け）**

python

```
# platform/pipelines/insurance_pipeline.py

class InsurancePipeline:
    """
    生命保険会社向け統合パイプライン
    SnapshotBuilder → EngineOrchestrator → 引受判断モデル
    """

    def __init__(self, snapshot_builder, orchestrator, underwriting_rules):
        self.snapshot_builder = snapshot_builder
        self.orchestrator = orchestrator
        self.rules = underwriting_rules

    def run(self, responses, nutrition, mbt_data, estro_data, mito_data, lifestyle):
        snapshot = self.snapshot_builder.build_snapshot(
            responses, nutrition, mbt_data, estro_data, mito_data, lifestyle
        )

        results = self.orchestrator.run_all(snapshot)

        underwriting = self._underwriting_decision(results)

        return {
            "snapshot": snapshot,
            "risk_profile": results,
            "underwriting_decision": underwriting
        }

    def _underwriting_decision(self, results):
        score = results["phenotype"]["total_score"]
        inflammation = results["inflammation"]["inflammation_load"]
        hormone = results["estrobolome"]["estrobolome_score"]

        if score > 120 or inflammation > 70:
            return {"decision": "Decline", "reason": "High metabolic risk"}
        elif hormone < 30:
            return {"decision": "Postpone", "reason": "Hormonal instability"}
        else:
            return {"decision": "Accept", "reason": "Risk acceptable"}
```

# 🧬 **platform/pipelines/probiotics_pipeline.py（MBT55プロバイオティクス解析）**

python

```
# platform/pipelines/probiotics_pipeline.py

class ProbioticsPipeline:
    """
    MBT55 × 生薬 × 代謝経路 × 疾病パスウェイ
    Probiotics Screening Engine を中心にした統合パイプライン
    """

    def __init__(self, snapshot_builder, orchestrator, probiotics_engine):
        self.snapshot_builder = snapshot_builder
        self.orchestrator = orchestrator
        self.probiotics_engine = probiotics_engine

    def run(self, responses, nutrition, mbt_data, estro_data, mito_data, lifestyle, substrate):
        snapshot = self.snapshot_builder.build_snapshot(
            responses, nutrition, mbt_data, estro_data, mito_data, lifestyle
        )

        results = self.orchestrator.run_all(snapshot)

        # PATHスコアを生成（簡易版）
        path_scores = {
            "PATH_01": nutrition["carb"],
            "PATH_02": mbt_data["bile_acid"],
            "PATH_03": results["acetylcoa"]["mi_acetylcoa_index"],
            "PATH_04": mito_data["oxidative_stress"],
            "PATH_05": results["estrobolome"]["estrobolome_score"]
        }

        probiotics = self.probiotics_engine.run(substrate, path_scores)

        return {
            "snapshot": snapshot,
            "engine_results": results,
            "probiotics_recommendation": probiotics
        }
```

# 🧬 **これで HealthBook‑MI‑Probiome‑OS の “OSパイプライン” が完成しました**

あなたのプラットフォームは、以下のように動作します：

コード

```
SnapshotBuilder → EngineOrchestrator → Pipeline → 医療/保険/MBT55解析
```

医療機関向け 生命保険会社向け MBT55プロバイオティクス解析 AIエージェント向け

すべてが **同じ Snapshot v2 を使い、同じ Orchestrator を通り、同じエンジン群を動かす** 完全統合型の代謝OSになりました。

# 🔥 次のステップ

次は **AIエージェント（triage / explainer / underwriting / clinical）** を このパイプラインに接続するための：

### 👉 ai_agents/triage_agent.py

### 👉 ai_agents/risk_explainer.py

### 👉 ai_agents/underwriting_agent.py

### 👉 ai_agents/clinical_agent.py

を生成します。

Kaz、進めます。

[[HM8. AI Agent モジュール]]
