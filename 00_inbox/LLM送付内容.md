NotebookLM に送るのは **Python（Pydantic）モデル＋NotebookLM向けPrompt**  
Claude に送るのは **TypeScript Protocol＋Claude向けPrompt＋NotebookLMのJSON**
貴方の指示通り、上記を送付しました。間違いないのではないですか？

ではまず、LLMへの送付内容を送ります。

### 1. Contract-First 型定義（Python / TypeScript）

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

#### TypeScript Protocol（Docstring付き）

```ts
/**
 * 単一の削減シーン（発酵飼料、水田、食品廃棄物、流木災害など）ごとの
 * メタン排出削減シミュレーション結果。
 */
export interface MethaneReductionScene {
  /** シーンの一意なID（例: 'livestock_feed', 'rice_paddy', 'food_waste', 'driftwood_disaster'） */
  scene_id: string;
  /** シーン名（日本語） */
  scene_name: string;
  /** NotebookLMから抽出した、シーンの詳細説明 */
  description: string;
  /** MBT導入前の年間メタン排出量 [ton-CH4/year] */
  baseline_emission_ton_ch4_per_year: number;
  /** MBT発酵肥料・飼料導入後の年間メタン削減量 [ton-CH4/year] */
  mbt_reduction_ton_ch4_per_year: number;
  /** 削減率 [%] = mbt_reduction / baseline_emission * 100 */
  reduction_rate_percent: number;
  /** 削減量算出に使った主要パラメータ（NotebookLMからの出典を含む） */
  key_parameters: string[];
  /** NotebookLM内のどのドキュメント・セクションから抽出したかのメモ */
  data_source_notes: string;
}

/**
 * 全シーンを統合した、MBT55によるメタン削減シミュレーションの集計結果。
 */
export interface MethaneReductionSummary {
  /** 全シーン合計のMBT導入前年間メタン排出量 [ton-CH4/year] */
  total_baseline_emission_ton_ch4_per_year: number;
  /** 全シーン合計のMBT導入後年間メタン削減量 [ton-CH4/year] */
  total_mbt_reduction_ton_ch4_per_year: number;
  /** 全体削減率 [%] */
  total_reduction_rate_percent: number;
  /** 各シーンの詳細結果リスト */
  scenes: MethaneReductionScene[];
  /** 前提条件・不確実性・補足説明など */
  notes?: string;
}
```

---
