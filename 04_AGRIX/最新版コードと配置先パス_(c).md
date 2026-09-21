[[W007_ab4. bionexus_sim_engine.py`（シミュレーションエンジン）の骨格実装]]
`bionexus_sim_engine.py`
`analyzer/repo_dependency_analyzer.py`
[[W008_ab5. エグゼクティブ・問合せインターフェース]]
`ask_executive.py`
 `streamlit run app.py`
[[W009_ab6. 推奨ディレクトリ構造]]
`requirements.txt`

次は、上記の実装に進みます。いずれも開発スレッドが作成したものです。確認後、最新版コードの出力とパスを示してください。

---

**間違い**（一部ディレクトリ構造および依存モジュールに非互換が生じています）。

開発スレッドで作成されたコード群（`W007` 〜 `W009`）は初期プロトタイプ段階のものであり、先ほど一本化した **`src/agrix_kb/` パッケージ構造**（`AGRIX Knowledge Base` 統合環境）および **`agrix_knowledge_base.json`** のキー構造と不整合を起こしています。

  
具体的には、旧コードが参照していた `models.hamada_matrix` や `repositories.hamada_matrix_repository` は、現在 `src.agrix_kb` 配下の統合モデル・統合リポジトリへ集約されているため、そのまま配置すると `ModuleNotFoundError` や `KeyError` が発生します。


### 修正点

1. **データモデル・参照先の統合**
    
      
    - 旧 `HamadaDiseaseRiskModel` を `src.agrix_kb.models.dietary` (`DiseaseDietaryRisk`) へ差し替え。
        
    - 旧 `HamadaMatrixRepository` を `src.agrix_kb.repository.kb_repository` (`AgrixKnowledgeBaseRepository`) へ統合。
        
2. **ディレクトリの統一**
    
    - プロジェクトルート `C:\Users\user\bionexus-engine` 直下に集約し、独自モジュールは `src/` 配下からインポートする構成に修正。
        
### 最新版コードと配置先パス

以下のスクリプトを PowerShell で丸ごと実行することで、修正版コードが指定の絶対パスへ一括配置されます。

  

#### 1. 一括配置スクリプト（PowerShell実行用）

PowerShell

```
# ルートへ移動および必要フォルダ作成
cd C:\Users\user\bionexus-engine
New-Item -ItemType Directory -Force -Path "analyzer" | Out-Null

# ① bionexus_sim_engine.py
@'
from typing import List, Dict
from pydantic import BaseModel, Field
from src.agrix_kb.models.dietary import DiseaseDietaryRisk

class UserBiomarkerInput(BaseModel):
    user_id: str
    target_disease_ids: List[str] = Field(..., description="評価対象の疾患IDリスト")
    phytochemical_intake: Dict[str, float] = Field(..., description="ファイトケミカル摂取量 (mg/日)")

class SimulationResult(BaseModel):
    disease_id: str
    disease_name: str
    baseline_risk_score: float
    adjusted_risk_score: float
    mitigation_percentage: float
    matched_risk_factors: List[str]

class BioNexusSimEngine:
    def __init__(self, disease_risks: List[DiseaseDietaryRisk]):
        self.disease_map = {item.disease_id: item for item in disease_risks}

    def run_simulation(self, user_input: UserBiomarkerInput) -> List[SimulationResult]:
        results = []
        for disease_id in user_input.target_disease_ids:
            disease_data = self.disease_map.get(disease_id)
            if not disease_data:
                continue

            base_score = 1.0
            mitigation_factor = 0.0

            for phyto_name, amount in user_input.phytochemical_intake.items():
                mitigation_factor += min(amount / 100.0, 0.3)

            adjusted_score = max(base_score * (1.0 - mitigation_factor), 0.05)
            mitigation_pct = round((1.0 - (adjusted_score / base_score)) * 100, 2)

            results.append(SimulationResult(
                disease_id=disease_id,
                disease_name=disease_data.disease_name,
                baseline_risk_score=base_score,
                adjusted_risk_score=round(adjusted_score, 3),
                mitigation_percentage=mitigation_pct,
                matched_risk_factors=disease_data.dietary_risk_factors
            ))

        return results
'@ | Out-File -Encoding utf8 "bionexus_sim_engine.py"

# ② analyzer/repo_dependency_analyzer.py
@'
import json
from typing import Dict, List, Set
from pydantic import BaseModel

class ClassSignature(BaseModel):
    name: str
    methods: List[str]

class RepoSkeletonData(BaseModel):
    repo_name: str
    file_path: str
    imports: List[str]
    classes: List[ClassSignature]

class RepoDependencyAnalyzer:
    def __init__(self, skeleton_json_path: str):
        with open(skeleton_json_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        self.skeletons: List[RepoSkeletonData] = [RepoSkeletonData(**item) for item in raw_data]

    def build_dependency_graph(self) -> Dict[str, List[str]]:
        graph: Dict[str, Set[str]] = {}
        for item in self.skeletons:
            repo = item.repo_name
            if repo not in graph:
                graph[repo] = set()
            for imp in item.imports:
                for target_item in self.skeletons:
                    if target_item.repo_name != repo and target_item.repo_name in imp:
                        graph[repo].add(target_item.repo_name)
        return {k: list(v) for k, v in graph.items()}

    def get_orphaned_modules(self) -> List[str]:
        graph = self.build_dependency_graph()
        all_referenced = set(dep for deps in graph.values() for dep in deps)
        return [repo for repo in graph.keys() if repo not in all_referenced]
'@ | Out-File -Encoding utf8 "analyzer\repo_dependency_analyzer.py"

# ③ ask_executive.py
@'
from typing import Dict, Any
from src.agrix_kb.repository.kb_repository import AgrixKnowledgeBaseRepository
from bionexus_sim_engine import BioNexusSimEngine, UserBiomarkerInput

class ExecutiveQueryHandler:
    def __init__(self, kb_path: str = None):
        self.repo = AgrixKnowledgeBaseRepository(kb_path)
        self.engine = BioNexusSimEngine(self.repo.disease_risks)

    def ask(self, query_text: str, target_diseases: list, phyto_intake: Dict[str, float]) -> Dict[str, Any]:
        sim_input = UserBiomarkerInput(
            user_id="exec-user-001",
            target_disease_ids=target_diseases,
            phytochemical_intake=phyto_intake
        )
        results = self.engine.run_simulation(sim_input)
        
        summary = {
            "query": query_text,
            "evaluated_diseases_count": len(results),
            "top_recommendations": [],
            "detailed_results": [r.model_dump() for r in results]
        }
        for res in results:
            if res.mitigation_percentage > 0:
                summary["top_recommendations"].append(
                    f"疾患 [{res.disease_name}] のリスクが {res.mitigation_percentage}% 低減されました。"
                )
        return summary

if __name__ == "__main__":
    handler = ExecutiveQueryHandler()
    demo_res = handler.ask(
        query_text="主要疾患に対するファイトケミカル介入効果",
        target_diseases=["DIS_001"],
        phyto_intake={"リコピン": 20.0, "ケルセチン": 15.0}
    )
    print("=== Executive Response ===")
    print(demo_res)
'@ | Out-File -Encoding utf8 "ask_executive.py"

# ④ app.py
@'
import streamlit as st
from src.agrix_kb.repository.kb_repository import AgrixKnowledgeBaseRepository
from bionexus_sim_engine import BioNexusSimEngine, UserBiomarkerInput

st.set_page_config(page_title="BioNexus Executive Dashboard", layout="wide")
st.title("🌱 BioNexus Executive Engine Dashboard")

st.sidebar.header("📊 介入パラメータ設定")
lycopene = st.sidebar.slider("リコピン摂取量 (mg)", 0.0, 50.0, 15.0)
quercetin = st.sidebar.slider("ケルセチン摂取量 (mg)", 0.0, 50.0, 10.0)

@st.cache_resource
def get_repository():
    return AgrixKnowledgeBaseRepository()

repo = get_repository()
engine = BioNexusSimEngine(repo.disease_risks)

disease_options = {d.disease_id: d.disease_name for d in repo.disease_risks}
selected_disease_id = st.selectbox(
    "評価対象の疾患を選択",
    options=list(disease_options.keys()),
    format_func=lambda x: f"{x}: {disease_options[x]}"
) if disease_options else None

if selected_disease_id:
    sim_input = UserBiomarkerInput(
        user_id="dashboard-user",
        target_disease_ids=[selected_disease_id],
        phytochemical_intake={"リコピン": lycopene, "ケルセチン": quercetin}
    )
    results = engine.run_simulation(sim_input)

    col1, col2, col3 = st.columns(3)
    if results:
        res = results[0]
        col1.metric("対象疾患", res.disease_name)
        col2.metric("ベースラインリスク", res.baseline_risk_score)
        col3.metric("調整後リスク", res.adjusted_risk_score, delta=f"-{res.mitigation_percentage}%")

    st.divider()
    st.subheader("詳細シミュレーション結果")
    st.json([r.model_dump() for r in results])
'@ | Out-File -Encoding utf8 "app.py"

# ⑤ requirements.txt
@'
pydantic>=2.0.0
streamlit>=1.28.0
pandas>=2.0.0
openpyxl>=3.1.0
python-dotenv>=1.0.0
'@ | Out-File -Encoding utf8 "requirements.txt"
```

#### 2. 最新の配置パス一覧

- `C:\Users\user\bionexus-engine\bionexus_sim_engine.py`
    
- `C:\Users\user\bionexus-engine\analyzer\repo_dependency_analyzer.py`
    
- `C:\Users\user\bionexus-engine\ask_executive.py`
    
- `C:\Users\user\bionexus-engine\app.py`
    
- `C:\Users\user\bionexus-engine\requirements.txt`

---

PowerShellの仕様上、**文末に全角スペース（ ）が含まれていたため、コマンドの確定（改行）として認識されずに停止していました。**


キーボードの **`Enter` キー** を押していただくか、以下のコードをそのままターミナルに貼り付けて実行してください。

### 解消用コマンド（全角スペース除去版）

PowerShell

```
# 1. 残りの設定を一括実行
@'
pydantic>=2.0.0
streamlit>=1.28.0
pandas>=2.0.0
openpyxl>=3.1.0
python-dotenv>=1.0.0
'@ | Out-File -Encoding utf8 "requirements.txt"

# 2. 必要なライブラリの一括インストール
pip install -r requirements.txt
```

### 実行後の動作確認

インストール完了後、以下のコマンドでダッシュボードを立ち上げることができます。

PowerShell

```
streamlit run app.py
```