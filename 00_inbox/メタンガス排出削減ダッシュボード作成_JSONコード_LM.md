8月24日月曜日

メタンガス排出削減ダッシュボード作成に関する指示書を２つ送ります。

from pydantic import BaseModel, Field from typing import List, Optional

class MethaneReductionScene(BaseModel): """ 単一の削減シーン（発酵飼料、水田、食品廃棄物、流木災害など）ごとの メタン排出削減シミュレーション結果。 """ scene_id: str = Field(..., description="シーンの一意なID（例: 'livestock_feed', 'rice_paddy', 'food_waste', 'driftwood_disaster'）") scene_name: str = Field(..., description="シーン名（日本語）") description: str = Field(..., description="NotebookLMから抽出した、シーンの詳細説明") baseline_emission_ton_ch4_per_year: float = Field(..., description="MBT導入前の年間メタン排出量 [ton-CH4/year]") mbt_reduction_ton_ch4_per_year: float = Field(..., description="MBT発酵肥料・飼料導入後の年間メタン削減量 [ton-CH4/year]") reduction_rate_percent: float = Field(..., description="削減率 [%] = mbt_reduction / baseline_emission * 100") key_parameters: List[str] = Field(..., description="削減量算出に使った主要パラメータ（NotebookLMからの出典を含む）") data_source_notes: str = Field(..., description="NotebookLM内のどのドキュメント・セクションから抽出したかのメモ")

class MethaneReductionSummary(BaseModel): """ 全シーンを統合した、MBT55によるメタン削減シミュレーションの集計結果。 """ total_baseline_emission_ton_ch4_per_year: float = Field(..., description="全シーン合計のMBT導入前年間メタン排出量 [ton-CH4/year]") total_mbt_reduction_ton_ch4_per_year: float = Field(..., description="全シーン合計のMBT導入後年間メタン削減量 [ton-CH4/year]") total_reduction_rate_percent: float = Field(..., description="全体削減率 [%]") scenes: List[MethaneReductionScene] = Field(..., description="各シーンの詳細結果リスト") notes: Optional[str] = Field(None, description="前提条件・不確実性・補足説明など")

次がPromptです。

あなたは、NotebookLMに格納されたBioNexus / AGRIX / MBT55関連ドキュメントを横断的に解析し、 MBT発酵肥料・発酵飼料・MBT廃棄物処理によるメタンガス排出削減シミュレーションを、 Contract-Firstの型定義に従って構造化して出力する専門家です。

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

--- Python 型定義（参考用。構造だけを厳守してください） --- from pydantic import BaseModel, Field from typing import List, Optional

class MethaneReductionScene(BaseModel): scene_id: str scene_name: str description: str baseline_emission_ton_ch4_per_year: float mbt_reduction_ton_ch4_per_year: float reduction_rate_percent: float key_parameters: List[str] data_source_notes: str

class MethaneReductionSummary(BaseModel): total_baseline_emission_ton_ch4_per_year: float total_mbt_reduction_ton_ch4_per_year: float total_reduction_rate_percent: float scenes: List[MethaneReductionScene] notes: Optional[str]

【最終出力】

- 上記 MethaneReductionSummary に対応する JSON を1つだけ出力してください。
- 数値が不確実な場合は、最も信頼できるレンジの中央値を採用し、 不確実性は `notes` に記載してください。

---

```
{
  "total_baseline_emission_ton_ch4_per_year": 14014336.92,
  "total_mbt_reduction_ton_ch4_per_year": 8243727.6,
  "total_reduction_rate_percent": 58.82,
  "scenes": [
    {
      "scene_id": "livestock_feed",
      "scene_name": "家畜への発酵飼料投与によるメタン排出削減",
      "description": "MBT55を家畜飼料に添加することで、腸内環境を短鎖脂肪酸（SCFA）生成へシフトさせ、メタン生成の基質となる水素の分圧を低下（dH2/dt ≈ 0）させる。反芻動物の消化効率を改善し、呼気由来のメタンを抑制する。",
      "baseline_emission_ton_ch4_per_year": 5973715.56,
      "mbt_reduction_ton_ch4_per_year": 1075268.8,
      "reduction_rate_percent": 18.0,
      "key_parameters": [
        "家畜数（アフリカ全土：牛3.5億頭、羊・ヤギ8億頭）",
        "腸内メタン削減係数: 0.012 kg CH4/kg MBT55/日",
        "GWP (CH4): 27.9"
      ],
      "data_source_notes": "BioNexus-Enterprise.txt [Section 02_Evidence/ja/05_livestock], M3-Core-Engine.txt [dashboard/app.py]"
    },
    {
      "scene_id": "rice_paddy",
      "scene_name": "水田へのMBT発酵肥料施用によるメタン排出削減",
      "description": "MBT55発酵肥料の施用により、土壌の好気性画分を55%に高め、メタン酸化菌（Methanotrophs）を活性化する。嫌気的なメタン生成古細菌の活動を抑制し、水田からのメタンフラックスを削減する。",
      "baseline_emission_ton_ch4_per_year": 1592990.89,
      "mbt_reduction_ton_ch4_per_year": 716845.9,
      "reduction_rate_percent": 45.0,
      "key_parameters": [
        "水田削減率レンジ: 30-60%",
        "土壌 Eh（酸化還元電位）固定範囲: -100 to +200 mV",
        "メタン酸化菌（Methylococcus capsulatus等）の含有"
      ],
      "data_source_notes": "M3-BioSynergy-Core.txt [4_Applications/AGRIX.md], MBT-Biosecurity-Engine.txt [06_Soil_Climate_Engine/Methane_Suppression_Engine.md]"
    },
    {
      "scene_id": "waste_management",
      "scene_name": "有機廃棄物（生ごみ等）のMBT処理によるメタン削減",
      "description": "食品廃棄物や加工残渣を24時間で完全腐植化することで、埋立処分時に発生する嫌気性分解由来のメタンを未然に回避（Avoidance）する。焼却処理に比べエネルギー効率が高く、メタンのリーケージを最小化する。",
      "baseline_emission_ton_ch4_per_year": 6451612.9,
      "mbt_reduction_ton_ch4_per_year": 6451612.9,
      "reduction_rate_percent": 100.0,
      "key_parameters": [
        "廃棄物メタン回避貢献度: GHG削減全体の35%",
        "24時間高速分解・完全腐植化ロジック",
        "焼却排出（600 kgCO2e/t）の回避"
      ],
      "data_source_notes": "M3-Core-Engine.txt [dashboard/app.py], PBPE-Marketplace.txt [backend/routers/dashboard.py]"
    },
    {
      "scene_id": "disaster_sludge",
      "scene_name": "流木・災害廃棄物のMBT処理によるメタン削減",
      "description": "震災汚泥や洪水後の有機廃棄物を数日で分解し、発酵肥料へ転換。嫌気的な泥中での有機物分解によるメタン発生を、MBT55の酸素マイクロニッチ供給機能により抑制する。",
      "baseline_emission_ton_ch4_per_year": 1.0,
      "mbt_reduction_ton_ch4_per_year": 0.0,
      "reduction_rate_percent": 0.0,
      "key_parameters": [
        "津波堆積物（海底汚泥）の数日内分解実績",
        "無臭化（水素分圧ゼロ dH2/dt ≈ 0）の物理的制約",
        "塩害土壌修復による副次的炭素固定"
      ],
      "data_source_notes": "BioNexus-Enterprise.txt [02_Evidence/ja/02_iwanuma_sludge], PBPE-Marketplace.txt [docs/evidence/MBT55_Biosecurity_Cases.md]"
    }
  ],
  "notes": "年間のメタン削減量は、総GHG削減目標5.1億トン（510 Mt-CO2e）に対し、GWP=27.9（IPCC AR6）を用いて逆算。災害廃棄物シーンは個別の削減統計値が不足しているため、ベースラインに代表値を仮置き。モデルの確実性は、dH2/dt ≈ 0（水素蓄積ゼロ）の物理拘束条件の遵守に基づいている。"
}
```