混乱し、必要なファイルを間違えて削除したかもしれません。

---

ご安心ください。必要なファイルを一括で完全復元・再生成するための「単一の自動修復・生成スクリプト」を用意いたしました。

これ一つを実行するだけで、①〜④のすべてのソースコードとデータファイル（`agrix_knowledge_base.json`）が正しいパスに自動で作成・配置されます。

### 一括復元・生成スクリプトの実行手順

PowerShell（ターミナル）を開き、以下のコード枠を**丸ごとコピーして貼り付け、Enterキー**を押してください。

PowerShell

```
# 1. ディレクトリの準備
cd C:\Users\user\bionexus-engine
New-Item -ItemType Directory -Force -Path "src\agrix_kb\models", "src\agrix_kb\repository" | Out-Null

# 2. ① src/agrix_kb/models/phytochemical.py の作成
@'
from pydantic import BaseModel, Field, field_validator
from typing import List

class PhytochemicalCompound(BaseModel):
    phytochemical_id: str = Field(..., description="ファイトケミカルID (例: PHY_001)")
    group: str = Field(..., description="大分類 (例: ポリフェノール群)")
    subgroup: str = Field(..., description="系統 (例: フラボノイド系)")
    category: str = Field(..., description="グループ・成分分類")
    compound_name: str = Field(..., description="成分名 (例: ルテオリン)")
    source_foods: List[str] = Field(default_factory=list, description="主な含有食品")

    @field_validator("phytochemical_id")
    @classmethod
    def validate_id_format(cls, v: str) -> str:
        if not v.startswith("PHY_"):
            raise ValueError("IDは 'PHY_' で始まる必要があります。")
        return v
'@ | Out-File -Encoding utf8 "src\agrix_kb\models\phytochemical.py"

# 3. ② src/agrix_kb/models/dietary.py の作成
@'
from pydantic import BaseModel, Field
from typing import List

class DiseaseDietaryRisk(BaseModel):
    disease_id: str = Field(..., description="疾患ID")
    disease_name: str = Field(..., description="疾患名称")
    dietary_risk_factors: List[str] = Field(default_factory=list, description="関連する食生活・生活習慣リスク因子")
'@ | Out-File -Encoding utf8 "src\agrix_kb\models\dietary.py"

# 4. ③ src/agrix_kb/repository/kb_repository.py の作成
@'
import os
import json
from typing import List
from dotenv import load_dotenv
from src.agrix_kb.models.phytochemical import PhytochemicalCompound
from src.agrix_kb.models.dietary import DiseaseDietaryRisk

load_dotenv()

class AgrixKnowledgeBaseRepository:
    def __init__(self, kb_path: str = None):
        if kb_path is None:
            data_dir = os.getenv("DATA_DIR", r"C:\Users\user\OneDrive\agrix-knowledge-base\data")
            kb_path = os.path.join(data_dir, "agrix_knowledge_base.json")
        self.kb_path = kb_path
        self.phytochemicals: List[PhytochemicalCompound] = []
        self.disease_risks: List[DiseaseDietaryRisk] = []
        self._load_kb()

    def _load_kb(self):
        if not os.path.exists(self.kb_path):
            raise FileNotFoundError(f"Knowledge Base file not found: {self.kb_path}")
        
        with open(self.kb_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        self.phytochemicals = [
            PhytochemicalCompound(**item) for item in data.get("phytochemical_library", [])
        ]
        self.disease_risks = [
            DiseaseDietaryRisk(**item) for item in data.get("disease_diet_matrix", [])
        ]

    def get_all_phytochemicals(self) -> List[PhytochemicalCompound]:
        return self.phytochemicals

    def search_phytochemical_by_food(self, food_name: str) -> List[PhytochemicalCompound]:
        return [
            item for item in self.phytochemicals 
            if any(food_name in food for food in item.source_foods)
        ]

    def search_phytochemical_by_name(self, name: str) -> List[PhytochemicalCompound]:
        return [item for item in self.phytochemicals if name in item.compound_name]
'@ | Out-File -Encoding utf8 "src\agrix_kb\repository\kb_repository.py"

# 5. ④ generate_agrix_kb.py の作成
@'
import os
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

search_dirs = [r"C:\Users\user\bionexus-engine", r"C:\Users\user\OneDrive\agrix-knowledge-base"]

def find_excel_file(keywords):
    for d in search_dirs:
        if os.path.exists(d):
            for root, _, files in os.walk(d):
                for f in files:
                    if any(k in f for k in keywords) and f.endswith((".xlsx", ".xls")):
                        return os.path.join(root, f)
    return None

phy_excel = find_excel_file(["ファイトケミカル"])
diet_excel = find_excel_file(["生活習慣チェック", "病気と食生活"])

if not phy_excel or not diet_excel:
    raise FileNotFoundError("元データのExcelファイルが見つかりません。")

df_phy = pd.read_excel(phy_excel, sheet_name='分類')
phytochemical_entries = []
current_group = ""
current_subgroup = ""

for idx in range(1, len(df_phy)):
    row = df_phy.iloc[idx]
    c_group = str(row.iloc[0]).strip() if pd.notna(row.iloc[0]) else ""
    c_subgroup = str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else ""
    c_category = str(row.iloc[2]).strip() if pd.notna(row.iloc[2]) else ""
    c_name = str(row.iloc[3]).strip() if pd.notna(row.iloc[3]) else ""
    c_foods = str(row.iloc[5]).strip() if pd.notna(row.iloc[5]) else ""

    if c_group:
        current_group = c_group.split("（")[0].strip()
    if c_subgroup:
        current_subgroup = c_subgroup.split("（")[0].strip()

    if c_name and c_name != "nan":
        foods_list = [f.strip() for f in c_foods.replace("、", ",").split(",") if f.strip() and f.strip() != "nan"]
        phytochemical_entries.append({
            "phytochemical_id": f"PHY_{len(phytochemical_entries)+1:03d}",
            "group": current_group,
            "subgroup": current_subgroup,
            "category": c_category,
            "compound_name": c_name,
            "source_foods": foods_list
        })

df_diet = pd.read_excel(diet_excel, sheet_name='Sheet1')
headers = df_diet.iloc[0].values
disease_data = []

for idx in range(1, len(df_diet)):
    row = df_diet.iloc[idx]
    disease_name = str(row.iloc[0]).strip()
    if not disease_name or disease_name == 'nan':
        continue
    
    risk_factors = []
    for col_idx in range(1, len(headers)-1):
        val = row.iloc[col_idx]
        if str(val).strip() in ['●', '○', '1', 'true', 'True']:
            factor_name = str(headers[col_idx]).strip()
            if factor_name and factor_name != 'nan':
                risk_factors.append(factor_name)
    
    disease_data.append({
        "disease_id": f"DIS_{len(disease_data)+1:03d}",
        "disease_name": disease_name,
        "dietary_risk_factors": risk_factors
    })

output_dir = os.getenv("DATA_DIR", r"C:\Users\user\OneDrive\agrix-knowledge-base\data")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "agrix_knowledge_base.json")

kb_agrix = {
    "metadata": {
        "title": "AGRIX Knowledge Base",
        "version": "1.0.0",
        "description": "ファイトケミカル分類および137疾患×食生活リスク統合ナレッジベース"
    },
    "phytochemical_library": phytochemical_entries,
    "disease_diet_matrix": disease_data
}

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(kb_agrix, f, ensure_ascii=False, indent=2)

print("--------------------------------------------------")
print("成功: すべてのモジュールおよび統合JSONデータの復元完了")
print("--------------------------------------------------")
'@ | Out-File -Encoding utf8 "generate_agrix_kb.py"

# 6. 自動実行してJSONファイルを生成
python generate_agrix_kb.py
```

実行後、`成功: すべてのモジュールおよび統合JSONデータの復元完了` と表示されれば、コードファイルもデータファイルもすべて正常な状態で完全に復元されます。