☛現在のGitHubリポジトリです。

mbt55-climate-overview （MBT55 気候変動）
M3-BioSynergy-JP （MBT55日本語版）
M3-BioSynergy （MBT55英語版）
以上の３つは、コンパクトにまとめてあります。


planetary-metabolism-os-workspace 
Planetary-Metabolism-OS 
この２つが、GeminiやClaudeが途中まで進めたものです。

BioNexus_vault （Private）
ほとんで、バックアップです。

HealthBook_MI_Core 
（Private）
これは、HealthBook、MBT漢方代謝ライブラリーを構築途中でした。

mbt55-climate-overview （MBT55 気候変動）
M3-BioSynergy-JP （MBT55日本語版）
M3-BioSynergy （MBT55英語版）
の3つ以外の中途半端なものを再利用したいと思いますが、いかがでしょうか？

---

## 🔍 **現状分析**

### **完了・統合済み（高品質）**
| リポジトリ | 状態 | 評価 |
|------------|------|------|
| **mbt55-climate-overview** | ✅ 完成 | 理論・数式・英語対応済み |
| **M3-BioSynergy** | ✅ 完成 | 英語版、国際向け |
| **M3-BioSynergy-JP** | ✅ 完成 | 日本語版、国内向け |

### **中途半端（再利用可能）**
| リポジトリ | 状態 | 再利用価値 |
|------------|------|------------|
| **planetary-metabolism-os-workspace** | ⚠️ 途中 | 低（Gemini/Claudeの試行錯誤） |
| **Planetary-Metabolism-OS** | ⚠️ 途中 | 低（同上） |
| **BioNexus_vault** | 📦 バックアップ | 中（資料として参照可） |
| **HealthBook_MI_Core** | 🔧 構築中 | **高（HealthBook核となる資産）** |

---

## 🎯 **再利用戦略**

### **フェーズ1: HealthBook_MI_Coreの統合（最優先）**

**このリポジトリには価値が高い：**
- HealthBook推論エンジン
- MBT漢方代謝ライブラリー（293処方）
- 200項目問診JSON
- 疾病リスク予測ロジック

**統合先：** `M3-BioSynergy` の `healthbook/` サブディレクトリとして組み込み

```
M3-BioSynergy/
├── src/core/           # 既存の微生物動態モデル
├── src/agrix/          # 新規：AGRIX炭素モデル
├── src/healthbook/     # 新規：HealthBook_MI_Coreから移行
│   ├── inference_engine.py
│   ├── kampo_library.py
│   ├── questionnaire.py
│   └── risk_predictor.py
├── data/
│   ├── mbt_kampo_library_final_array.json
│   └── questionnaire_full.json
└── examples/
    └── healthbook_demo.py
```

### **フェーズ2: Planetary-Metabolism-OS系はアーカイブ**

これらのリポジトリは：
- 内容が重複
- 品質が未完成
- 試行錯誤の産物

→ **アーカイブ化（読取専用）して参照用に残す**

```bash
# GitHub上でアーカイブ設定
gh repo archive planetary-metabolism-os-workspace --yes
gh repo archive Planetary-Metabolism-OS --yes
```

### **フェーズ3: BioNexus_vaultは資料庫として保持**

- 4,800以上のノート
- 理論的裏付け資料
- 実証データ

→ **Privateのまま参照用に維持**

---

## 🚀 **具体的な統合作業**

### **ステップ1: HealthBook_MI_Coreの内容を確認**

現在の `HealthBook_MI_Core` に含まれるもの：
- [ ] `game3_api.py` - FastAPIベースの推論エンジン
- [ ] `mbt_kampo_library_final_array.json` - 293処方データ
- [ ] `questionnaire_full.json` - 200項目問診データ
- [ ] `healthbook_inference.py` - 推論ロジック（あれば）

### **ステップ2: M3-BioSynergyに統合**

```bash
# クローン
git clone https://github.com/shimojok/M3-BioSynergy.git
cd M3-BioSynergy

# HealthBookモジュール用ディレクトリ作成
mkdir -p src/healthbook data

# HealthBook_MI_Coreから必要なファイルをコピー
cp ../HealthBook_MI_Core/game3_api.py src/healthbook/inference_engine.py
cp ../HealthBook_MI_Core/mbt_kampo_library_final_array.json data/
cp ../HealthBook_MI_Core/questionnaire_full.json data/

# AGRIXモジュール追加
mkdir -p src/agrix
# 先日のAGRIXコアエンジンをコピー
cp ../agrix-core/src/agrix/*.py src/agrix/
```

### **ステップ3: 統合README作成**

```markdown
# M³-BioSynergy

## Modules

### 1. Microbial Core
120-species MBT55 consortium dynamics

### 2. AGRIX (Carbon & Agriculture)
- Carbon cycle simulation
- Negative Green Premium calculation
- Market integration with Yara

### 3. HealthBook (Global Health)
- 200-item questionnaire (30k+ patient data)
- 293 kampo formulas with MBT55 pathways
- Disease risk prediction
- Phytochemical recommendations
```

---

## 📋 **整理後のリポジトリ構成（理想）**

```
GitHub: shimojok/
├── M3-BioSynergy           # メイン（Public, 完成）
│   ├── src/
│   │   ├── core/          # 微生物動態
│   │   ├── agrix/         # 農業・炭素
│   │   └── healthbook/    # 健康診断
│   ├── data/
│   └── examples/
│
├── M3-BioSynergy-JP        # 日本語版（Public）
│
├── BioNexus_vault          # 資料庫（Private, 参照用）
│
├── HealthBook_MI_Core      # アーカイブ（Read-only）
└── planetary-*             # アーカイブ（Read-only）
```

---

## 🎯 **今すぐのアクション**

1. **HealthBook_MI_Coreの内容を確認**
   - どのファイルが有用か特定
   - 重複や不要ファイルの洗い出し

2. **M3-BioSynergyに統合**
   - AGRIXモジュール追加
   - HealthBookモジュール追加
   - データファイル配置

3. **不要リポジトリのアーカイブ化**
   - `planetary-metabolism-os-workspace`
   - `Planetary-Metabolism-OS`

---

**まず HealthBook_MI_Core の内容を確認したいのですが、中身をここに貼り付けていただけますか？**

特に以下のファイルがあるか教えてください：
- `game3_api.py`（FastAPIエンジン）
- `healthbook_inference.py`（推論ロジック）
- `mbt_kampo_library_final_array.json`（漢方データ）
- `questionnaire_full.json`（問診データ）

[[DSH9. 現状分析：完成している資産と中途半端な資産]]
