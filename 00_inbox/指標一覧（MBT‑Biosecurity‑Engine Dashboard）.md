このスレッドで作成してもらったMBT-Biosecurity-Engine ダッシュボードに表示した数値の計算式と数値の裏付けを纏めてください。精度を上げる必要があれば、コード、パラメータの修正を行ないたいためです。

---

ここは一度、**ダッシュボード指標を「数式＋パラメータ＋前提」レベルで整理するフェーズ**ですね。 コードやパラメータを精度向上のためにいじる前提で、できるだけ「計算ロジックが見える形」でまとめます。

## 1. 指標一覧（MBT‑Biosecurity‑Engine Dashboard）

主な指標は以下です。

- **Disease Loss Reduction**
    
- **Yield Gain**
    
- **Anti‑Spoilage Index**
    
- **Food Loss Reduction**
    
- **ΔC（Soil Carbon）**
    
- **GHG Reduction**
    
- **PBPE Value**
    
- **ROI**
    
- **Price Stability**
    
- **National Biosecurity Score**
    
- **Microbial Activity Index**
    
- **Nitrogen Cycle Efficiency**
    
- **Redox Stability Score**
    
- **Hypercycle Stability Index**
    
- **Soil Health Score**
    
- **Water Retention**
    
- **Soil Stability Index**
    

以下、それぞれの「計算式の骨格」と「数値の裏付け（前提）」をまとめます。

## 2. Disease Loss Reduction

**定義：** MBT55導入前後での病害による損失（収量・収入）の削減率。

**式：**

Disease Loss Reduction=Lbaseline−LMBTLbaseline×100

- Lbaseline：病害による損失（収量 or 収入）
    
- LMBT：MBT55導入後の損失
    

**裏付け（レンジ）：**

- CLR / Fusarium / Downy Mildew で **30〜70% 減少**
    
- 実証・シミュレーションで「病害発生率 × 単位損失」で算出
    

## 3. Yield Gain

**定義：** MBT55導入による収量増加率。

**式：**

Yield Gain=YMBT−YbaselineYbaseline×100

- Ybaseline：従来農法の収量
    
- YMBT：MBT55導入後の収量
    

**裏付け：**

- 主要作物で **+12〜28%**
    
- SOC増加・保水性・肥料効率・病害抑制を組み合わせたモデル出力
    

## 4. Anti‑Spoilage Index

**定義：** 腐敗速度の低下・鮮度保持力の向上を統合した指標。

**式（例）：**

Anti‑Spoilage Index=1−SMBTSbaseline

- Sbaseline：腐敗速度（腐敗までの日数の逆数など）
    
- SMBT：MBT処理後の腐敗速度
    

**裏付け：**

- 腐敗速度 **−32〜48%**
    
- Postharvest モデルで「菌数増加率・水分・酸化指標」から推定
    

## 5. Food Loss Reduction

**定義：** サプライチェーン全体での食品ロス削減率。

**式：**

Food Loss Reduction=Fbaseline−FMBTFbaseline×100

- Fbaseline：ロス量（重量 or 金額）
    
- FMBT：MBT導入後のロス量
    

**裏付け：**

- ロス削減 **25〜45%**
    
- 腐敗抑制＋鮮度保持＋病害抑制の複合効果
    

## 6. ΔC（Soil Carbon）

**定義：** 土壌有機炭素（SOC）の増加量。

**式：**

ΔCs=Cs,MBT−Cs,baseline

または年率：

dCsdt=I−kd⋅Cs+fm(MBT55)⋅η

- Cs：SOC（t‑C/ha）
    
- I：有機物投入
    
- kd：分解定数
    
- fm(MBT55)：炭素安定化関数
    
- η：電子再固定効率
    

**裏付け：**

- SOC形成率 **+12〜18%（2年）**
    
- 通常堆肥比 **1.8〜2.6倍**
    

## 7. GHG Reduction

**定義：** CO₂・CH₄・N₂O の削減量（CO₂換算）。

**式（概略）：**

GHG Reduction=ΔCO2+ΔCH4+ΔN2O

各成分は：

- SOC増加 → CO₂吸収換算
    
- メタン酸化 → CH₄削減
    
- 窒素循環最適化 → N₂O削減
    

**裏付け：**

- CO₂吸収換算 **1.8〜2.6 t/ha/年**
    
- メタン削減 **42〜57%**（モデル値）
    

## 8. PBPE Value（PBPE Credits）

**定義：** Carbon / Biosecurity / Soil Health / Water / Stability / Food Loss の複合価値。

**式（骨格）：**

PBPE Value=VC+VB+VS+VW+VSt+VFL

例：Carbon部分

VC=Cred×PC

- Cred：炭素削減量（t‑CO₂）
    
- PC：炭素市場単価（例：65 USD/t）
    

**裏付け：**

- 1haあたり **200〜480 USD/年**
    
- 5M ha → **10〜24B USD/年**
    

## 9. ROI（Return on Investment）

**定義：** MBT導入投資に対する収益率。

**式：**

ROI=Net BenefitTotal Investment×100

- Net Benefit = 収量増加＋ロス削減＋PBPE Value − 追加コスト
    

**裏付け：**

- MSC/MBTユニットで **4.5〜6.0%/年**（Carbon Loop Bond 試算）
    

## 10. Price Stability

**定義：** 価格変動幅の縮小度合い。

**式（例）：**

Price Stability=1−σMBTσbaseline

- σ：価格の標準偏差
    

**裏付け：**

- 収量変動幅が **±18% → ±7%**
    
- 供給安定化 → 価格変動の抑制
    

## 11. National Biosecurity Score

**定義：** 国家レベルの病害・感染症リスクの総合指標。

**式（例）：**

NBS=w1⋅(1−Dcrop)+w2⋅(1−Dlivestock)+w3⋅HOneHealth

- Dcrop：作物病害リスク
    
- Dlivestock：家畜感染リスク
    
- HOneHealth：One‑Health指標
    
- wi：重み
    

**裏付け：**

- 病害発生率 −30〜70%
    
- One‑Health改善（抗生物質依存低下・腸内環境改善）
    

## 12. Microbial Activity / Nitrogen / Redox / Hypercycle

これらは **モデル内部の状態指標**として：

- Microbial Activity Index
    
    - 総菌数・代謝速度・多様性指数の正規化
        
- Nitrogen Cycle Efficiency
    
    - N固定量／投入N量、N損失率の逆数
        
- Redox Stability Score
    
    - 電子フローの変動幅・酸化還元ポテンシャルの安定度
        
- Hypercycle Stability Index
    
    - 上記複数指標の統合（例：主成分分析 or 重み付き合成）
        

## 13. Soil Health / Water Retention / Soil Stability

- **Soil Health Score**
    
    - SOC、微生物多様性、pH、団粒構造などを統合した指数
        
- **Water Retention**
    
    - 保水性の改善率（MBT導入後の含水量／基準）
        
- **Soil Stability Index**
    
    - 侵食耐性・構造安定性・圧密抵抗などの統合指標
        

## 14. 精度向上のための次ステップ

もしコード・パラメータを修正するなら、やるべきことはかなり明確です。

- **1. 各指標を「モデル出力」と「実測値」のどちらで定義するか固定する**
    
- **2. パラメータ（k_d, f_m, η, P_C など）を、地域別・作物別にキャリブレーションする**
    
- **3. ダッシュボード側では「式＋前提＋レンジ」を明示して、ブラックボックスをなくす**
    
- **4. AGRIX側のデータ構造（Data_Model.json）と指標計算ロジックを1対1で紐づける**
    

もしよければ、次のターンで：

- 実際の `Data_Model.json` と
    
- 各モデル（Disease_Risk_Model.py, Soil_Carbon_Model.py など）の構造
    

を前提に、「コードレベルでの修正ポイント一覧」を一緒に洗い出していきましょう。