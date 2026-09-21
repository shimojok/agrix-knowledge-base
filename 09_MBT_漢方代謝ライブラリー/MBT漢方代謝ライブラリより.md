このスレッド全ての成果物を、新しくマルチAIエージェントに移管するために、AIが利用できる最適なフォーマット（JSONコード、データベースなど）として出力してください。

---

### 全体方針

このスレッドで作ってきたものは、だいたい以下の「概念」に整理できます。

- **生薬（Herb）**
    
- **方剤（Formula）**
    
- **MBT55代謝経路（MicrobePathway）**
    
- **代謝物クラスター（MetaboliteCluster）**
    
- **証（Sho）**
    
- **症状（Symptom）**
    
- **ネットワーク図（NetworkMap / Mermaid）**
    
- **PBPE統合モデル（PBPEModel）**
    
- **HealthBook UI案（HealthBookUI）**
    

マルチAIエージェントが扱いやすい形として、 **1つの大きな JSON オブジェクト**に、これらをすべて「構造化データ」としてまとめるのが最適です。

以下は **スキーマ＋実データの例** です。 このまま `.json` として保存すれば、どのエージェントからも扱えます。

### マスタースキーマ＋データ（抜粋版）

json

```
{
  "meta": {
    "version": "1.0",
    "description": "MBT漢方代謝ライブラリー統合データ（Kaz用）"
  },

  "herbs": [
    {
      "id": "herb_ninjin",
      "name_ja": "人参",
      "name_en": "Ginseng",
      "mbt55_paths": ["poly_degraders"],
      "metabolite_clusters": ["SCFA", "mucosal_repair"],
      "sho": ["補気"],
      "symptoms": ["疲労", "胃腸障害", "母子健康"],
      "formulas": ["formula_shikunshito", "formula_rikkunshito", "formula_hochuekkito"],
      "notes_md": "# 生薬：人参\n..."
    },
    {
      "id": "herb_kakkon",
      "name_ja": "葛根",
      "name_en": "Kakkon",
      "mbt55_paths": ["poly_degraders", "aromatic_degraders"],
      "metabolite_clusters": ["metabolic_activation", "warm_yang", "SCFA"],
      "sho": ["補気", "温陽"],
      "symptoms": ["疲労", "冷え", "頭痛"],
      "formulas": ["formula_kakkonto"],
      "notes_md": "# 生薬：葛根（かっこん）\n..."
    }
    /* 他の生薬も同様に追加 */
  ],

  "formulas": [
    {
      "id": "formula_maoto",
      "name_ja": "麻黄湯",
      "category": "Core12",
      "herbs": ["herb_maou", "herb_keishi", "herb_kanzo", "herb_kyonin"],
      "mbt55_paths": ["aromatic_degraders", "lactic_acid_bacteria"],
      "metabolite_clusters": ["anti_inflammatory_flavonoids", "anti_allergy", "warm_yang", "mucosal_repair"],
      "sho": ["清熱", "温陽"],
      "symptoms": ["感染症", "咳", "喘息", "花粉症", "咽頭痛"],
      "network_map_id": "map_maoto",
      "notes_md": "# 麻黄湯_ネットワーク図\n```mermaid\n...```"
    },
    {
      "id": "formula_shikunshito",
      "name_ja": "四君子湯",
      "category": "Core12",
      "herbs": ["herb_ninjin", "herb_byakujutsu", "herb_bukuryo", "herb_kanzo"],
      "mbt55_paths": ["poly_degraders", "lactic_acid_bacteria"],
      "metabolite_clusters": ["SCFA", "mucosal_repair"],
      "sho": ["補気", "和解"],
      "symptoms": ["疲労", "胃腸障害", "母子健康"],
      "network_map_id": "map_shikunshito",
      "notes_md": "# 四君子湯（Shikunshito）ネットワーク図\n```mermaid\n...```"
    }
    /* 他の方剤も同様に追加 */
  ],

  "mbt55_paths": [
    {
      "id": "aromatic_degraders",
      "name_ja": "芳香族分解菌",
      "metabolite_clusters": [
        "anti_inflammatory_flavonoids",
        "vasodilators",
        "anti_allergy",
        "anti_viral"
      ],
      "herbs": [
        "herb_maou",
        "herb_keishi",
        "herb_keihi",
        "herb_saiko",
        "herb_ougon",
        "herb_oren",
        "herb_renkyo",
        "herb_botanpi",
        "herb_senkyu",
        "herb_tounin",
        "herb_kouka"
      ],
      "sho": ["清熱", "活血"],
      "symptoms": ["感染症", "アレルギー", "冷え", "月経痛"],
      "notes_md": "# MBT55代謝経路：芳香族分解菌\n..."
    },
    {
      "id": "poly_degraders",
      "name_ja": "多糖分解菌",
      "metabolite_clusters": ["SCFA", "mucosal_repair", "diuretic"],
      "herbs": ["herb_ninjin", "herb_byakujutsu", "herb_bukuryo", "herb_taiso", "herb_makimondo", "herb_hange", "herb_takusha", "herb_chorei"],
      "sho": ["補気", "利水", "和解"],
      "symptoms": ["疲労", "胃腸障害", "むくみ"],
      "notes_md": "# MBT55代謝経路：多糖分解菌\n..."
    }
    /* 他のMBT55 5経路も同様に追加 */
  ],

  "metabolite_clusters": [
    {
      "id": "SCFA",
      "name_ja": "短鎖脂肪酸",
      "mbt55_paths": ["poly_degraders", "lactic_acid_bacteria"],
      "herbs": ["herb_ninjin", "herb_byakujutsu", "herb_bukuryo", "herb_taiso", "herb_hange"],
      "sho": ["補気"],
      "symptoms": ["疲労", "胃腸障害", "母子健康", "生活習慣病"],
      "formulas": ["formula_shikunshito", "formula_rikkunshito", "formula_hochuekkito", "formula_ninjinto"],
      "notes_md": "# 代謝物クラスター：SCFA\n..."
    },
    {
      "id": "anti_inflammatory_flavonoids",
      "name_ja": "抗炎症フラボノイド",
      "mbt55_paths": ["aromatic_degraders", "actinomycetes"],
      "herbs": ["herb_maou", "herb_ougon", "herb_oren", "herb_renkyo", "herb_botanpi", "herb_saiko"],
      "sho": ["清熱"],
      "symptoms": ["感染症", "アレルギー", "生活習慣病", "咽頭痛"],
      "formulas": ["formula_maoto", "formula_shosaikoto", "formula_hangeshashinto", "formula_byakkoto"],
      "notes_md": "# 代謝物クラスター：抗炎症フラボノイド\n..."
    }
    /* 他の代謝物クラスターも追加 */
  ],

  "sho": [
    {
      "id": "sho_hoki",
      "name_ja": "補気",
      "metabolite_clusters": ["SCFA", "metabolic_activation"],
      "mbt55_paths": ["poly_degraders", "lactic_acid_bacteria"],
      "symptoms": ["疲労", "胃腸障害", "母子健康", "生活習慣病"],
      "herbs": ["herb_ninjin", "herb_byakujutsu", "herb_bukuryo", "herb_taiso", "herb_kanzo"],
      "formulas": ["formula_shikunshito", "formula_rikkunshito", "formula_hochuekkito", "formula_ninjinto"],
      "notes_md": "# 証：補気\n..."
    },
    {
      "id": "sho_seinetu",
      "name_ja": "清熱",
      "metabolite_clusters": ["anti_inflammatory_flavonoids", "anti_viral", "anti_allergy"],
      "mbt55_paths": ["aromatic_degraders", "actinomycetes"],
      "symptoms": ["感染症", "アレルギー", "咽頭痛", "生活習慣病"],
      "herbs": ["herb_maou", "herb_ougon", "herb_oren", "herb_renkyo", "herb_botanpi"],
      "formulas": ["formula_maoto", "formula_shosaikoto", "formula_hangeshashinto", "formula_byakkoto"],
      "notes_md": "# 証：清熱\n..."
    }
    /* 他の証も追加（活血・利水・補血・温陽・和解） */
  ],

  "symptoms": [
    {
      "id": "symptom_fatigue",
      "name_ja": "疲労",
      "sho": ["補気", "温陽"],
      "metabolite_clusters": ["SCFA", "metabolic_activation"],
      "mbt55_paths": ["poly_degraders", "lactic_acid_bacteria"],
      "herbs": ["herb_ninjin", "herb_byakujutsu", "herb_bukuryo"],
      "formulas": ["formula_shikunshito", "formula_rikkunshito", "formula_hochuekkito", "formula_ninjinto"],
      "notes_md": "# 症状：疲労\n..."
    },
    {
      "id": "symptom_cold",
      "name_ja": "冷え",
      "sho": ["温陽", "活血"],
      "metabolite_clusters": ["warm_yang", "vasodilators"],
      "mbt55_paths": ["aromatic_degraders", "sulfur_metabolism", "fungi"],
      "herbs": ["herb_kankyo", "herb_keihi", "herb_keishi", "herb_maou"],
      "formulas": ["formula_keishito", "formula_shokenchuto", "formula_ninjinto", "formula_keishibukuryogan"],
      "notes_md": "# 症状：冷え\n..."
    }
    /* 他の症状も追加（感染症・アレルギー・胃腸障害・咳・喘息・むくみ・腎・泌尿器・自律神経不安定・月経痛・生活習慣病・不安・不眠・母子健康・咽頭痛・花粉症・頭痛） */
  ],

  "network_maps": [
    {
      "id": "map_maoto",
      "type": "mermaid",
      "formula_id": "formula_maoto",
      "content_md": "# 麻黄湯（Maoto）ネットワーク図\n```mermaid\n...```"
    },
    {
      "id": "map_shosaikoto",
      "type": "mermaid",
      "formula_id": "formula_shosaikoto",
      "content_md": "# 小柴胡湯（Shosaikoto）ネットワーク図\n```mermaid\n...```"
    }
    /* 他の方剤ネットワーク図、三次元マップなど */
  ],

  "pbpe_model": {
    "id": "pbpe_v1",
    "mapping": [
      {
        "pbpe_phenotype": "エネルギー不足",
        "sho": "補気",
        "metabolite_clusters": ["SCFA"],
        "mbt55_paths": ["poly_degraders"]
      },
      {
        "pbpe_phenotype": "水分停滞",
        "sho": "利水",
        "metabolite_clusters": ["diuretic"],
        "mbt55_paths": ["poly_degraders", "mineral_metabolism"]
      },
      {
        "pbpe_phenotype": "血流停滞",
        "sho": "活血",
        "metabolite_clusters": ["vasodilators"],
        "mbt55_paths": ["aromatic_degraders", "fungi"]
      },
      {
        "pbpe_phenotype": "慢性炎症",
        "sho": "清熱",
        "metabolite_clusters": ["anti_inflammatory_flavonoids"],
        "mbt55_paths": ["aromatic_degraders", "actinomycetes"]
      },
      {
        "pbpe_phenotype": "冷え",
        "sho": "温陽",
        "metabolite_clusters": ["warm_yang"],
        "mbt55_paths": ["sulfur_metabolism", "aromatic_degraders"]
      },
      {
        "pbpe_phenotype": "女性健康",
        "sho": "補血",
        "metabolite_clusters": ["anti_spasm"],
        "mbt55_paths": ["lactic_acid_bacteria", "aromatic_degraders"]
      }
    ],
    "notes_md": "# PBPE統合（Version 1.0）\n..."
  },

  "healthbook_ui": {
    "id": "healthbook_v1",
    "layers": [
      "症状入力",
      "証推定",
      "代謝物クラスター推定",
      "MBT55プロファイル",
      "方剤・生薬レコメンド",
      "PBPE地域フェノタイプ"
    ],
    "home_screen": {
      "sho_radar": ["補気", "活血", "清熱", "利水", "補血", "温陽"],
      "symptom_scores": ["疲労", "冷え", "胃腸障害", "アレルギー"],
      "recommended_actions": ["方剤", "食事", "運動", "生薬食材"]
    },
    "notes_md": "# HealthBook UI案（Version 1.0）\n..."
  }
}
```

### どう使うか（マルチAIエージェント視点）

- **知識エージェント**
    
    - `herbs`, `formulas`, `mbt55_paths`, `metabolite_clusters`, `sho`, `symptoms` を参照して推論・説明。
        
- **レコメンドエージェント**
    
    - `symptoms` → `sho` → `metabolite_clusters` → `mbt55_paths` → `formulas` のチェーンで方剤提案。
        
- **UIエージェント**
    
    - `healthbook_ui` を元に画面構成・API設計。
        
- **PBPEエージェント**
    
    - `pbpe_model` を使って地域フェノタイプから証・方剤へマッピング。
        

もし「全部のノート本文を JSON に完全格納したフル版」が欲しければ、 このスキーマに沿って **notes_md に全Markdownを流し込むだけ**で完成します。

次のステップとして：

- この JSON をどのエージェントにどう渡すか（API設計）
    
- あるいは、これを **PostgreSQL / Neo4j** にマッピングする ER 図
    

まで一緒に詰めてもいい。

---

「全部のノート本文を JSON に完全格納したフル版」が欲しいです。

---


正直に言うと、**このスレッド全体のノート本文をすべて 1つの JSON に完全格納すると、現実的な文字数を超えます**。 なので、ここでは：

- **実運用に耐える「フル版のための正規スキーマ」**
    
- **代表的なノートを実際に埋め込んだ“具体例”**
    
- **残りを機械的に埋めるためのルール**
    

を出します。これをそのままベースにして、Vault 全体を JSON 化できます。

### 1. 正規スキーマ（この形で 1ファイルにまとめる）

json

```
{
  "meta": {
    "version": "1.0",
    "description": "MBT漢方代謝ライブラリー統合データ（Kaz用・フル版）"
  },

  "notes": [
    {
      "id": "note_shoyaku_ichiran",
      "file_name": "生薬一覧.md",
      "title": "生薬一覧",
      "category": "index",
      "folder": "0_体系図",
      "content_md": "..."
    },
    {
      "id": "note_formula_maoto_network",
      "file_name": "麻黄湯_ネットワーク図.md",
      "title": "麻黄湯（Maoto）ネットワーク図",
      "category": "network_map",
      "folder": "7_図式化（Mermaid）",
      "content_md": "..."
    }
    /* ここに Vault 内の全 .md を 1件ずつ入れていく */
  ]
}
```

### 2. 実際の「content_md」埋め込み例

ここからは、**実際のノート本文を JSON に入れた形**を見せます。 このパターンで、残りを機械的に変換すれば「フル版」が完成します。

#### 例1：`生薬一覧.md`

json

```
{
  "id": "note_shoyaku_ichiran",
  "file_name": "生薬一覧.md",
  "title": "生薬一覧",
  "category": "index",
  "folder": "0_体系図",
  "content_md": "# 生薬一覧\n\n- 麻黄\n- 桂枝\n- 葛根\n- 人参\n- 白朮\n- 茯苓\n- 大棗\n- 甘草\n- 黄芩\n- 黄連\n- 連翹\n- 牡丹皮\n- 川芎\n- 桃仁\n- 紅花\n- 当帰\n- 芍薬\n- 白芍\n- 沢瀉\n- 猪苓\n- 竜骨\n- 牡蛎\n- 石膏\n- 知母\n- 生姜\n- 乾姜\n- 半夏\n- 麦門冬\n- 杏仁\n- 五味子\n- 陳皮\n- 柴胡\n- 桂皮\n- 膠飴\n..."
}
```

#### 例2：`MBT55代謝経路：芳香族分解菌.md`

json

```
{
  "id": "note_mbt55_aromatic",
  "file_name": "芳香族分解菌.md",
  "title": "MBT55代謝経路：芳香族分解菌（Aromatic Degraders）",
  "category": "mbt55_pathway",
  "folder": "4_MBT55代謝経路",
  "content_md": "# MBT55代謝経路：芳香族分解菌（Aromatic Degraders）\n\n## 概要\n芳香族化合物（フラボノイド・精油・リグナンなど）を分解し、\n抗炎症・血流改善・抗アレルギーなどの代謝物を生成する中心的な菌群。\n\n## 主な生成代謝物\n- [[抗炎症フラボノイド]]\n- [[血管拡張代謝物]]\n- [[抗アレルギー代謝物]]\n- [[抗ウイルス代謝物]]\n\n## 関連する生薬\n- [[麻黄]]\n- [[桂枝]]\n- [[桂皮]]\n- [[柴胡]]\n- [[黄芩]]\n- [[黄連]]\n- [[連翹]]\n- [[牡丹皮]]\n- [[川芎]]\n- [[桃仁]]\n- [[紅花]]\n\n## 対応する証\n- [[清熱]]\n- [[活血]]\n\n## 関連症状\n- [[感染症]]\n- [[アレルギー]]\n- [[冷え]]\n- [[月経痛]]\n\n## 関連方剤\n- [[麻黄湯]]\n- [[葛根湯]]\n- [[小柴胡湯]]\n- [[桂枝茯苓丸]]\n- [[桃核承気湯]]\n\n## Mermaid（ミニマップ）\n```mermaid\ngraph LR\n    Aro[芳香族分解菌]\n    AntiInf[抗炎症代謝物]\n    Vaso[血管拡張代謝物]\n    Seinetu[清熱]\n    Kakketsu[活血]\n\n    Aro --> AntiInf\n    Aro --> Vaso\n    AntiInf --> Seinetu\n    Vaso --> Kakketsu\n```\n"
}
```

#### 例3：`麻黄湯_ネットワーク図.md`

json

```
{
  "id": "note_formula_maoto_network",
  "file_name": "麻黄湯_ネットワーク図.md",
  "title": "麻黄湯（Maoto）ネットワーク図",
  "category": "network_map",
  "folder": "7_図式化（Mermaid）",
  "content_md": "# 麻黄湯（Maoto）ネットワーク図\n\n```mermaid\ngraph LR\n    Maou[麻黄]\n    Keishi[桂枝]\n    Kyouin[杏仁]\n    Kanzo[甘草]\n\n    Aro[芳香族分解菌]\n    Lacto[乳酸菌群]\n\n    AntiInf[抗炎症代謝物]\n    AntiAllergy[抗アレルギー代謝物]\n    WarmM[温陽代謝物]\n    Mucosa[粘膜修復代謝物]\n\n    Seinetu[清熱]\n    Onyo[温陽]\n    Wakai[和解]\n\n    Infection[感染症]\n    Cough[咳]\n    Asthma[喘息]\n\n    Maou --> Aro\n    Keishi --> Aro\n    Kyouin --> Lacto\n    Kanzo --> Lacto\n\n    Aro --> AntiInf\n    Aro --> AntiAllergy\n    Aro --> WarmM\n    Lacto --> Mucosa\n\n    AntiInf --> Seinetu\n    AntiAllergy --> Seinetu\n    WarmM --> Onyo\n    Mucosa --> Wakai\n\n    Seinetu --> Infection\n    Seinetu --> Cough\n    Wakai --> Cough\n    Onyo --> Asthma\n```\n"
}
```

### 3. 残りを機械的に埋めるためのルール

1. **Vault 内の全** `.md` **を列挙**
    
    - `find` や PowerShell でファイル一覧を取得。
        
2. **各ファイルごとに JSON の 1要素を作る**
    
    - `file_name`: 実際のファイル名
        
    - `title`: 先頭行の `# 見出し`
        
    - `folder`: パスから抽出（例：`4_MBT55代謝経路`）
        
    - `category`: フォルダ＋タイトルから分類（例：`mbt55_pathway`, `symptom`, `sho`, `herb`, `formula`, `network_map`, `index`）
        
    - `content_md`: ファイル全文
        
3. **それを** `notes` **配列に全部詰める** → これで「全部のノート本文を JSON に完全格納したフル版」が完成。
    

### 4. もしスクリプトを書くなら（イメージ）

例えば Python なら、こんな感じで一括変換できます。

python

```
import json
from pathlib import Path

vault = Path("/path/to/ObsidianVault")

notes = []

for md in vault.rglob("*.md"):
    content = md.read_text(encoding="utf-8")
    lines = content.splitlines()
    title = lines[0].lstrip("# ").strip() if lines and lines[0].startswith("#") else md.stem

    notes.append({
        "id": f"note_{md.stem}",
        "file_name": md.name,
        "title": title,
        "folder": str(md.parent.relative_to(vault)),
        "category": "auto",  # 後で手で or スクリプトで分類
        "content_md": content
    })

data = {
    "meta": {
        "version": "1.0",
        "description": "MBT漢方代謝ライブラリー統合データ（Kaz用・フル版）"
    },
    "notes": notes
}

Path("mbt_library_full.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
```

### 5. 率直なところ

この場で「全ノート本文を完全に JSON に埋めたフル版」を手作業で書き切るのは、 あなたの Vault の規模的に現実的じゃない。

でも、**構造・スキーマ・変換ロジックはもう固まっている**ので、 上の Python 1本で「本当に全部入りの JSON」を自動生成できます。

もしよければ、次は：

- この JSON をどう API に載せるか
    
- どのエージェントがどのフィールドを見るか
    

まで一緒に設計しよう。

