Tier 1 の「MBT55 55クラス定義」と「分解速度・pH/温度カーブ」のドラフトを、一緒に数式レベルまで切り出して下さい。

---

### ドキュメント案：MBT55 Tier 1 パラメータドラフト

**対象：MBT55 55クラス定義＋分解速度・pH/温度カーブ（数式レベル）**

---

## 1. MBT55 クラス定義ドラフト（機能クラスベース）

**方針：**

- 実在菌種ベースではなく、**機能クラス（functional guild）ベースの55クラス**として定義
    
- 各クラスは以下の属性を持つ：
    
- **`id`**: MBTクラスID（1〜55）
    
- **`name`**: 機能クラス名
    
- **`substrates`**: 主な基質（starch, protein, lipid, cellulose, mucin, lactate, etc.）
    
- **`products`**: 主な代謝産物（acetate, propionate, butyrate, lactate, gas, etc.）
    
- **`oxygen_type`**: `"obligate_anaerobe" | "facultative" | "microaerophilic" | "aerobe"`
    
- **`role`**: `"primary_degrader" | "secondary_fermenter" | "cross_feeder" | "terminal_electron_acceptor_user"`
    
- **`notes`**: 想定する代表菌群（例：butyrate producers, mucin degraders など）
    

#### 1.1 クラス一覧（例：55クラス）

**A. 炭水化物分解・発酵系（C1–C15）**

1. **C1**: Starch primary degraders（アミラーゼ高活性、主に acetate＋lactate）
2. **C2**: Resistant starch degraders（butyrate 産生寄与大）
3. **C3**: Simple sugar fermenters（glucose, fructose → lactate＋acetate）
4. **C4**: Oligosaccharide degraders（FOS, GOS → acetate＋propionate）
5. **C5**: Cellulose degraders（セルラーゼ活性、acetate 主体）
6. **C6**: Hemicellulose degraders
7. **C7**: Pectin degraders
8. **C8**: Mucin-associated carbohydrate degraders
9. **C9**: Lactate producers（糖 → lactate 主体）
10. **C10**: Lactate utilizers（lactate → propionate / butyrate）
11. **C11**: Gas-producing fermenters（H₂, CO₂ 多産生）
12. **C12**: Ethanol-producing fermenters
13. **C13**: Succinate-producing fermenters
14. **C14**: Succinate-utilizing propionate producers
15. **C15**: Mixed SCFA generalists（acetate＋propionate＋butyrate）

**B. タンパク質・アミノ酸分解系（P16–P25）**

16. **P16**: Protein primary degraders（protease 高活性）
17. **P17**: Peptidase-rich peptide degraders
18. **P18**: Amino acid fermenters（branched-chain SCFA 生成）
19. **P19**: Putrefactive proteolytic bacteria（アンモニア・硫化水素生成）
20. **P20**: Urease-positive bacteria（尿素 → アンモニア）
21. **P21**: Tryptophan metabolizers（インドール・キヌレニン経路）
22. **P22**: Tyrosine metabolizers（p-cresol など）
23. **P23**: Histidine metabolizers（ヒスタミン生成）
24. **P24**: Polyamine producers（スペルミン・スペルミジン）
25. **P25**: Proteolytic butyrate producers

**C. 脂質・胆汁酸関連（L26–L32）**

26. **L26**: Lipid primary degraders（リパーゼ活性）
27. **L27**: Bile salt hydrolase-positive bacteria（BSH）
28. **L28**: Secondary bile acid producers
29. **L29**: Medium-chain fatty acid producers
30. **L30**: Long-chain fatty acid β-oxidizers（腸内）
31. **L31**: Phospholipid degraders
32. **L32**: Sphingolipid-associated bacteria

**D. 粘膜・バリア関連（M33–M38）**

33. **M33**: Mucin primary degraders（例：A. muciniphila 機能クラス）
34. **M34**: Mucin cross-feeders（mucin 分解産物利用）
35. **M35**: Epithelial-associated butyrate producers（バリア保護）
36. **M36**: IgA-coated commensals（免疫調整）
37. **M37**: Biofilm-forming commensals
38. **M38**: Opportunistic pathobionts（炎症誘発）

**E. 電子受容体・ガス関連（E39–E45）**

39. **E39**: Methanogens（メタン生成）
40. **E40**: Sulfate-reducing bacteria（H₂S 生成）
41. **E41**: Nitrate-reducing bacteria
42. **E42**: Acetogens（H₂＋CO₂ → acetate）
43. **E43**: Hydrogen-scavenging bacteria
44. **E44**: Oxygen-tolerant anaerobes（microaerophilic）
45. **E45**: Facultative anaerobes（O₂存在下での糖代謝）

**F. 免疫・炎症・代謝調整（I46–I55）**

46. **I46**: Anti-inflammatory SCFA producers（regulatory T cell 誘導）
47. **I47**: Pro-inflammatory LPS-high producers
48. **I48**: Tryptophan–AhR axis modulators
49. **I49**: BCAA metabolism modulators（インスリン抵抗性関連）
50. **I50**: Choline–TMA/TMAO producers
51. **I51**: Uric acid metabolism modulators
52. **I52**: Oxalate degraders
53. **I53**: Phenolic compound metabolizers（ポリフェノール代謝）
54. **I54**: Vitamin-producing bacteria（B群, K など）
55. **I55**: Keystone commensals（ネットワーク安定性に寄与）

---

## 2. 分解速度モデル（基質×MBTクラス）

### 2.1 基本形：Michaelis–Menten＋環境補正

基質 ( j )（例：starch, protein, lipid, cellulose）に対する  
MBTクラス ( i ) の分解速度 ( v_{ij} ) を：

[ v_{ij} = V_{\max,ij} \cdot \frac{[S_j]}{K_{m,ij} + [S_j]} \cdot f_{\mathrm{O_2},i}(\mathrm{O_2}) \cdot f_{\mathrm{pH},i}(\mathrm{pH}) \cdot f_{T,i}(T) ]

- **( V_{\max,ij} )**: クラス ( i ) が基質 ( j ) を分解する最大速度
- **( K_{m,ij} )**: 基質 ( j ) に対する半飽和定数
- **([S_j])**: 基質濃度
- **( f_{\mathrm{O_2},i} )**: 酸素条件による補正
- **( f_{\mathrm{pH},i} )**: pH による補正
- **( f_{T,i} )**: 温度による補正

### 2.2 酸素補正関数 ( f_{\mathrm{O_2},i} )

クラスごとに「好気/嫌気プロファイル」を持たせる：

- **嫌気性（obligate_anaerobe）クラス：**

[ f_{\mathrm{O_2},i}(\mathrm{O_2}) = \exp\left(-\alpha_i \cdot \mathrm{O_2}\right) ]

- **通性嫌気性（facultative）クラス：**

[ f_{\mathrm{O_2},i}(\mathrm{O_2}) = 1 - \beta_i \cdot \max(0, \mathrm{O_2} - \mathrm{O_2}^{\ast}_i) ]

- **好気性（aerobe）クラス：**

[ f_{\mathrm{O_2},i}(\mathrm{O_2}) = \frac{\mathrm{O_2}}{K_{\mathrm{O_2},i} + \mathrm{O_2}} ]

ここで：

- (\mathrm{O_2}): 局所酸素分圧（相対値でも可）
- (\alpha_i, \beta_i, \mathrm{O_2}^{\ast}_i, K_{\mathrm{O_2},i}): クラス固有パラメータ

### 2.3 pH 応答カーブ ( f_{\mathrm{pH},i} )

**ガウス型（最適 pH 付近で最大活性）：**

[ f_{\mathrm{pH},i}(\mathrm{pH}) = \exp\left( -\frac{(\mathrm{pH} - \mathrm{pH}^{\mathrm{opt}}_i)^2}{2\sigma_{\mathrm{pH},i}^2} \right) ]

- (\mathrm{pH}^{\mathrm{opt}}_i): クラス ( i ) の最適 pH
- (\sigma_{\mathrm{pH},i}): 許容幅（pH 変動に対する感度）

### 2.4 温度応答カーブ ( f_{T,i} )

**Q10 モデル＋最適温度カットオフのハイブリッド案：**

[ f_{T,i}(T) = Q_{10,i}^{\frac{T - T_{\mathrm{ref}}}{10}} \cdot g_{T,i}(T) ]

ここで：

- (Q_{10,i}): 温度10℃上昇あたりの活性増加倍率
- (T_{\mathrm{ref}}): 基準温度（例：37℃）
- (g_{T,i}(T)): 極端温度での活性低下を表すカットオフ関数

**カットオフ関数の例（ガウス型）：**

[ g_{T,i}(T) = \exp\left( -\frac{(T - T^{\mathrm{opt}}_i)^2}{2\sigma_{T,i}^2} \right) ]

- (T^{\mathrm{opt}}_i): クラス ( i ) の最適温度
- (\sigma_{T,i}): 許容温度幅

---

## 3. パラメータ構造（実装用ドラフト）

### 3.1 MBT55 クラス定義 JSON スキーマ案

```json
{
  "class_id": "C1",
  "name": "Starch primary degraders",
  "oxygen_type": "obligate_anaerobe",
  "role": "primary_degrader",
  "substrates": ["starch"],
  "products": ["acetate", "lactate"],
  "representative_functions": ["amylase_high", "fast_growth_on_starch"],
  "env_optima": {
    "pH_opt": 6.5,
    "pH_sigma": 0.5,
    "T_opt": 37.0,
    "T_sigma": 3.0,
    "Q10": 2.0,
    "O2_sensitivity": {
      "type": "anaerobe",
      "alpha": 5.0
    }
  }
}
```

### 3.2 分解速度パラメータ JSON スキーマ案

```json
{
  "class_id": "C1",
  "substrate": "starch",
  "kinetics": {
    "model": "michaelis_menten",
    "Vmax": 1.2,
    "Km": 0.8,
    "units": {
      "Vmax": "mmol_substrate/(L·h)",
      "Km": "mmol_substrate/L"
    }
  }
}
```

### 3.3 統合的な速度計算の疑似コード

```python
def v_ij(class_params, kinetics_params, S, O2, pH, T):
    Vmax = kinetics_params["Vmax"]
    Km = kinetics_params["Km"]

    # 基本MM
    v_base = Vmax * S / (Km + S)

    # O2補正
    o2_type = class_params["env_optima"]["O2_sensitivity"]["type"]
    if o2_type == "anaerobe":
        alpha = class_params["env_optima"]["O2_sensitivity"]["alpha"]
        f_O2 = math.exp(-alpha * O2)
    elif o2_type == "facultative":
        # 例：簡略版
        f_O2 = 1.0
    else:
        f_O2 = 1.0  # 必要に応じて拡張

    # pH補正
    pH_opt = class_params["env_optima"]["pH_opt"]
    pH_sigma = class_params["env_optima"]["pH_sigma"]
    f_pH = math.exp(-((pH - pH_opt) ** 2) / (2 * pH_sigma ** 2))

    # 温度補正
    T_opt = class_params["env_optima"]["T_opt"]
    T_sigma = class_params["env_optima"]["T_sigma"]
    Q10 = class_params["env_optima"]["Q10"]
    T_ref = 37.0

    f_Q10 = Q10 ** ((T - T_ref) / 10.0)
    f_T_gauss = math.exp(-((T - T_opt) ** 2) / (2 * T_sigma ** 2))
    f_T = f_Q10 * f_T_gauss

    return v_base * f_O2 * f_pH * f_T
```

---

## 4. 次のステップ候補

1. **この55クラス案をベースに、実際に使いたいクラス名・役割を微調整**
2. **Tier 1 用の実ファイル構造を決める**
    - `MBT55_classes_v1.json`
    - `MBT55_kinetics_v1.json`
3. その後、
    - 特に **C1–C5（炭水化物）＋P16–P20（タンパク）＋M33（mucin）＋I46/I47（炎症）**  
        あたりから、優先的に「仮パラメータ」を埋めていくと、  
        HealthBook 側の SCFA・炎症・エネルギー軸とすぐ接続できます。

---

このドラフトをそのまま **仕様書（`HB_MBT55_Tier1_spec_v1.md`）** として起こしてもいいし、  
まずは「55クラスの中身」と「速度式の形」で修正したいところがあれば、そこから一緒に詰めていこう。

どこを一番最初に「実数値を入れる対象」にしたい？（炭水化物系か、mucin系か、炎症系か。）