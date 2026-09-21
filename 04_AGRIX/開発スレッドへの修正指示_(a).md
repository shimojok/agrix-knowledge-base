
> **【開発スレッドへの修正指示】**
> 
> `src/models/` 内のモデル定義が重複・先祖返りしているため整理します。
> 
> 
> 1. `hamada_matrix_schema.py` は廃棄し、`src/models/hamada_matrix.py` に多変量対応の最新 Pydantic モデル（`DiseaseRiskMapping` や `Hamada137DiseaseMatrix`）を一括統合してください。
>     
> 2. `src/repositories/hamada_matrix_repository.py` も、新しい `Hamada137DiseaseMatrix` 構造（`C:\Users\user\OneDrive\agrix-knowledge-base\data\hamada_137_risk_matrix.json`）を読み込めるよう修正してください。

---

指示いただいたモデル定義の重複整理およびリポジトリ層の修正内容を整理いたしました。

`src/models/hamada_matrix_schema.py` を廃棄（削除）し、`src/models/hamada_matrix.py` に多変量対応の最新 Pydantic モデルを一括統合します。また、`src/repositories/hamada_matrix_repository.py` も最新の JSON データ構造（`agrix-knowledge-base/data/hamada_137_risk_matrix.json`）に適合するよう更新します。

### ディレクトリ構造と絶対パス

Plaintext

```
C:\Users\user\
└── bionexus-engine/
    └── src/
        ├── models/
        │   ├── hamada_matrix_schema.py        # ❌ 廃棄・削除
        │   └── hamada_matrix.py               # ★【ファイル1】統合モデル定義
        └── repositories/
            └── hamada_matrix_repository.py    # ★【ファイル2】新構造対応リポジトリ
```

### 1. `src/models/hamada_matrix.py` (統合モデル定義)

- **保存先（絶対パス）**: `C:\Users\user\bionexus-engine\src\models\hamada_matrix.py`
    
- **対応作業**: `hamada_matrix_schema.py` を廃棄し、本ファイルへ多変量対応の最新 Pydantic モデルを集約します。
    

```Python
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class DiseaseRiskMapping(BaseModel):
    """137疾病リスク個別の詳細マッピングモデル"""
    id: str = Field(..., description="リスク識別ID (例: H137-001)")
    disease_name: str = Field(..., min_length=1, description="対象疾患名")
    category: str = Field(..., min_length=1, description="疾患カテゴリ (例: 代謝・内分泌疾患)")
    target_phytochemicals: List[str] = Field(default_factory=list, description="有効ファイトケミカル群")
    action_mechanism: str = Field(..., description="作用機序・病態改善メカニズム")
    mbt55_synergy: str = Field(..., description="MBT55菌群との相乗効果・代謝トランスフォーメーション")

    @field_validator("id")
    @classmethod
    def validate_id_format(cls, v: str) -> str:
        if not v.startswith("H137-"):
            raise ValueError("IDは 'H137-' で始まる必要があります。")
        return v

class Hamada137DiseaseMatrix(BaseModel):
    """浜田137リスクマトリックス全体を保持するルートモデル"""
    records: List[DiseaseRiskMapping] = Field(default_factory=list, description="全疾病リスクマトリックスのリスト")
    
    @property
    def total_count(self) -> int:
        return len(self.records)
```

### 2. `src/repositories/hamada_matrix_repository.py` (リポジトリ層修正)

- **保存先（絶対パス）**: `C:\Users\user\bionexus-engine\src\repositories\hamada_matrix_repository.py`
    
- **対応作業**: `hamada_137_risk_matrix.json` のリスト型構造を読み込み、統合した `Hamada137DiseaseMatrix` および `DiseaseRiskMapping` インスタンスとして適切にパース・検索できるよう変更します。
    
```Python
import os
import json
from typing import List, Optional
from src.models.hamada_matrix import DiseaseRiskMapping, Hamada137DiseaseMatrix

class HamadaMatrixRepository:
    def __init__(self, file_path: Optional[str] = None):
        default_path = r"C:\Users\user\agrix-knowledge-base\data\hamada_137_risk_matrix.json"
        self.file_path = file_path or default_path

    def load_matrix(self) -> Hamada137DiseaseMatrix:
        """JSONファイルから浜田137リスクマトリックスを読み込み、Pydanticモデルとしてパース"""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"データファイルが見つかりません: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # JSONがリスト形式の場合と、{"records": [...]} オブジェクト形式の場合の両方に対応
        if isinstance(raw_data, list):
            items = [DiseaseRiskMapping(**item) for item in raw_data]
            return Hamada137DiseaseMatrix(records=items)
        elif isinstance(raw_data, dict) and "records" in raw_data:
            return Hamada137DiseaseMatrix(**raw_data)
        else:
            raise ValueError("不正なJSONデータ構造です。")

    def search_by_disease(self, query: str) -> List[DiseaseRiskMapping]:
        """病名またはキーワードによる曖昧検索"""
        matrix = self.load_matrix()
        return [
            record for record in matrix.records
            if query.lower() in record.disease_name.lower() or query.lower() in record.category.lower()
        ]

    def search_by_phytochemical(self, phyto_name: str) -> List[DiseaseRiskMapping]:
        """ファイトケミカル名による関連疾病の検索"""
        matrix = self.load_matrix()
        return [
            record for record in matrix.records
            if any(phyto_name.lower() in p.lower() for p in record.target_phytochemicals)
        ]
```

### 3. 不要ファイルの廃棄コマンド

PowerShell で以下のコマンドを実行し、旧ファイル `hamada_matrix_schema.py` を削除してください。

PowerShell

```
Remove-Item -Path "C:\Users\user\bionexus-engine\src\models\hamada_matrix_schema.py" -ErrorAction SilentlyContinue
```

これにてモデルの先祖返り・重複が解消され、新構造の `hamada_137_risk_matrix.json` とスムーズに連携できるようになります。