
### 1. NotebookLM向けContract-First 型定義（Python / TypeScript）

#### Python（Pydantic）モデル

```python
from pydantic import BaseModel, Field
from typing import List, Optional

class MethaneReductionScene(BaseModel):
    """
    単一の削減シーン（発酵飼料、水田、食品廃棄物、流木災害など）ごとの
    メタン排出削減シミュレーション結果。
    """
    scene_id: str = Field(..., description="シーンの一意なID（例: 'livestock_feed', 'rice_paddy', 'food_waste', 'driftwood_disaster'）")
    scene_name: str = Field(..., description="シーン名（日本語）")
    description: str = Field(..., description="NotebookLMから抽出した、シーンの詳細説明")
    baseline_emission_ton_ch4_per_year: float = Field(..., description="MBT導入前の年間メタン排出量 [ton-CH4/year]")
    mbt_reduction_ton_ch4_per_year: float = Field(..., description="MBT発酵肥料・飼料導入後の年間メタン削減量 [ton-CH4/year]")
    reduction_rate_percent: float = Field(..., description="削減率 [%] = mbt_reduction / baseline_emission * 100")
    key_parameters: List[str] = Field(..., description="削減量算出に使った主要パラメータ（NotebookLMからの出典を含む）")
    data_source_notes: str = Field(..., description="NotebookLM内のどのドキュメント・セクションから抽出したかのメモ")

class MethaneReductionSummary(BaseModel):
    """
    全シーンを統合した、MBT55によるメタン削減シミュレーションの集計結果。
    """
    total_baseline_emission_ton_ch4_per_year: float = Field(..., description="全シーン合計のMBT導入前年間メタン排出量 [ton-CH4/year]")
    total_mbt_reduction_ton_ch4_per_year: float = Field(..., description="全シーン合計のMBT導入後年間メタン削減量 [ton-CH4/year]")
    total_reduction_rate_percent: float = Field(..., description="全体削減率 [%]")
    scenes: List[MethaneReductionScene] = Field(..., description="各シーンの詳細結果リスト")
    notes: Optional[str] = Field(None, description="前提条件・不確実性・補足説明など")
```

---
### 2. NotebookLM向けメタ検索プロンプト（日本語）

NotebookLM に投げるときの「指示役プロンプト」を、**検索範囲・深度・出力形式**まで含めて書きます。

```text
あなたは、NotebookLMに格納されたBioNexus / AGRIX / MBT55関連ドキュメントを横断的に解析し、
MBT発酵肥料・発酵飼料・MBT廃棄物処理によるメタンガス排出削減シミュレーションを、
Contract-Firstの型定義に従って構造化して出力する専門家です。

【検索対象（メタ検索指示）】
- 17リポジトリ全体から、以下のキーワードを含むドキュメントを優先的に検索してください：
  - "MBT55", "MBT発酵肥料", "発酵飼料", "メタン", "CH4", "家畜", "水田", "食品廃棄物", "災害廃棄物", "流木"
- 特に、以下のシーンに関連する技術仕様・数値・ロジックを深く参照してください：
  1. 家畜への発酵飼料投与によるメタン排出削減
  2. 水田・農地へのMBT発酵肥料施用によるメタン排出削減
  3. 加工食品廃棄物・生ごみのMBT処理によるメタン排出削減
  4. 流木・災害廃棄物のMBT処理によるメタン排出削減
  5. その他、NotebookLM内で定義されているMBT関連削減シーン

【検索深度・分割指定】
- 各シーンについて、以下を必ず抽出してください：
  - MBT導入前のベースライン排出量の推定ロジックと代表値
  - MBT導入後の削減量の算出ロジックと代表値
  - 削減率 [%] の計算式と前提条件
  - 使用した主要パラメータ（例：家畜頭数、飼料投入量、水田面積、廃棄物量など）
- ドキュメントが複数に分散している場合は、
  - 「どのドキュメントのどのセクションから引用したか」を `data_source_notes` に明記してください。

【出力フォーマット】
- 出力は、以下の Python Pydantic モデルに完全準拠した JSON 形式としてください。
- 余計な説明文は書かず、JSONオブジェクトのみを返してください。

--- Python 型定義（参考用。構造だけを厳守してください） ---
from pydantic import BaseModel, Field
from typing import List, Optional

class MethaneReductionScene(BaseModel):
    scene_id: str
    scene_name: str
    description: str
    baseline_emission_ton_ch4_per_year: float
    mbt_reduction_ton_ch4_per_year: float
    reduction_rate_percent: float
    key_parameters: List[str]
    data_source_notes: str

class MethaneReductionSummary(BaseModel):
    total_baseline_emission_ton_ch4_per_year: float
    total_mbt_reduction_ton_ch4_per_year: float
    total_reduction_rate_percent: float
    scenes: List[MethaneReductionScene]
    notes: Optional[str]

【最終出力】
- 上記 MethaneReductionSummary に対応する JSON を1つだけ出力してください。
- 数値が不確実な場合は、最も信頼できるレンジの中央値を採用し、
  不確実性は `notes` に記載してください。
```

