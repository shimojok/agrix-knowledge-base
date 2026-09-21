添付ノート、
[[W003-2_a3. Phase 2 のコア実装]]
にある、
”浜田137リスクマトリックス対応 Pydanticモデル (`models/hamada_matrix.py`)”
が、同じホルダーに存在しますが、全く機能が異なるファイルですか？重複していませんか？

---

結論から申し上げますと、**機能的に大きく重複しており、役割がバッティング（競合）しています。そのまま放置するとエラーや混乱の原因になりますので、一本化（整理）が必要です。**

### 何が起きているのか（分析）

1. **先ほどの `hamada_matrix_schema.py`**
    
    先ほどの依頼ノート（W004_c2）でコンテキスト最適化スレッドから提供した、**多変量（＋／−）相関や詳細な問診項目に対応した新しい設計**です。
    
1. **W003-2_a3 内の `hamada_matrix.py`**
    
    開発スレッド側で「受け取ったデータを使って Phase 2 のコードを書いた」として出力されたファイルですが、設計が以前の簡易版（`disease_id` や `risk_correlation_score` などのフラットな構成）に基づいて作られています。
    
つまり、**開発スレッド側が提案の新しいスキーマ構造（`hamada_matrix_schema.py`）を完全に反映しきれず、旧来の構成で `hamada_matrix.py` を再出力してしまっている状態**です。

### 解決策（一本化の手順）

混同を避けるため、ファイル名を **`src/models/hamada_matrix.py` に統一**し、先ほど定義した最新のスキーマ（`hamada_matrix_schema.py` の内容）で上書きします。


#### 【確定版】`C:\Users\user\bionexus-engine\src\models\hamada_matrix.py`

（`hamada_matrix_schema.py` を削除し、このファイル1つに集約します）


```Python
from typing import List, Dict, Optional
from enum import Enum
from pydantic import BaseModel, Field

class FactorImpact(str, Enum):
    POSITIVE_RISK = "POSITIVE_RISK"  # リスクを高める(+)要因
    NEGATIVE_RISK = "NEGATIVE_RISK"  # リスクを低減する(-)要因
    NEUTRAL = "NEUTRAL"

class DietaryFactor(BaseModel):
    factor_id: str = Field(..., description="生活習慣・問診項目ID")
    factor_name: str = Field(..., description="問診質問・習慣名称")
    impact: FactorImpact = Field(..., description="該当疾患に対する影響")
    weight: float = Field(default=1.0, ge=0.0, le=5.0, description="臨床的影響度・重み")

class MetabolicPathLink(BaseModel):
    target_pathway: str = Field(..., description="関与する代謝系 (例: PDH_COMPLEX, SCFA_PRODUCTION)")
    key_nutrients: List[str] = Field(default_factory=list, description="関与する補酵素・栄養素")

class DiseaseRiskMapping(BaseModel):
    disease_id: str = Field(..., description="137疾病コード")
    disease_name: str = Field(..., description="疾病名称")
    category: str = Field(..., description="疾患カテゴリ")
    dietary_factors: List[DietaryFactor] = Field(..., description="正負相関をもつ生活習慣・問診因子リスト")
    phytochemical_targets: List[str] = Field(default_factory=list, description="有効なファイトケミカル分類")
    metabolic_links: List[MetabolicPathLink] = Field(default_factory=list, description="関連する代謝メカニズム")
    mbt55_probiotics_target: bool = Field(default=True, description="MBT Probioticsによる改善対象か否か")

class Hamada137DiseaseMatrix(BaseModel):
    version: str = "3.0"
    description: str = "浜田プロトコル 臨床137疾病リスク x 生活習慣正負相関 x 代謝軸マトリクス"
    diseases: Dict[str, DiseaseRiskMapping]
```

### 今後の開発スレッドへの指示プロンプト

重複をなくし、最新のモデルで統一させるため、開発スレッドへ以下のプロンプトを送ってください。

  

> **【開発スレッドへの修正指示】**
> 
> `src/models/` 内のモデル定義が重複・先祖返りしているため整理します。
> 
> 
> 1. `hamada_matrix_schema.py` は廃棄し、`src/models/hamada_matrix.py` に多変量対応の最新 Pydantic モデル（`DiseaseRiskMapping` や `Hamada137DiseaseMatrix`）を一括統合してください。
>     
> 2. `src/repositories/hamada_matrix_repository.py` も、新しい `Hamada137DiseaseMatrix` 構造（`C:\Users\user\OneDrive\agrix-knowledge-base\data\hamada_137_risk_matrix.json`）を読み込めるよう修正してください。
>