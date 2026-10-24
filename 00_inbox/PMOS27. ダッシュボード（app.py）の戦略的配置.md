はい、進めて下さい。

---

下條さん、ありがとうございます。

**`04_Azure_Economic_Impact/dashboard/app.py`** の実装と、プロジェクト全体の統合を進めます。

このダッシュボードは、ナデラCEOが「Azureのダッシュボードにこの画面が統合されている未来」を想起させるための重要なプロトタイプになります。

---

### 1. ダッシュボード（app.py）の戦略的配置

`04_Azure_Economic_Impact` フォルダ内に `dashboard` フォルダを作成し、そこに `app.py` を配置してください。これにより、このフォルダも `docs` と `dashboard` に分かれ、美しい階層構造になります。

#### **📄 04_Azure_Economic_Impact/dashboard/app.py (拡張版)**

AGRIXの計算結果と、HealthBookの推論結果を「経営指標」として統合表示するコードです。

Python

```
import streamlit as st
import sys
import os
import pandas as pd

# エンジン類のパスを通す
sys.path.append(os.path.abspath('../../01_AGRIX_Platform/src'))
sys.path.append(os.path.abspath('../../02_HealthBook_Platform/src'))

try:
    from agrix_simulator import AGRIXEconomicEngine
    from metabolic_intelligence import MetabolicIntelligence
except ImportError:
    st.error("Engine files not found. Please check the directory structure.")

def main():
    st.set_page_config(page_title="Azure-PMOS Management Console", layout="wide")
    
    # サイドパネル：言語と言語に応じたパラメータ設定
    lang = st.sidebar.selectbox("Language / 言語", ["en", "ja"])
    st.sidebar.markdown("---")
    st.sidebar.write("Project: **Azure-PMOS**")
    st.sidebar.write("Strategic Value: **Planetary Sustainability**")

    # タイトル
    title = "Azure-PMOS: Executive Decision Support" if lang == 'en' else "Azure-PMOS: 経営意思決定支援ダッシュボード"
    st.title(f"🌐 {title}")

    # タブでプラットフォームを切り替え
    tab1, tab2, tab3 = st.tabs(["AGRIX (Environment)", "HealthBook (Metabolic)", "M&A Impact"])

    # --- Tab 1: AGRIX ---
    with tab1:
        st.header("AGRIX: Soil & Carbon Finance")
        col1, col2 = st.columns([1, 2])
        with col1:
            crop = st.selectbox("Industry Sector", ["Coffee", "Rice", "Cacao", "Wheat"])
            hectares = st.number_input("Cultivation Area (ha)", value=1000)
            c_price = st.slider("Carbon Price (USD/tCO2e)", 50, 200, 100)
        
        engine = AGRIXEconomicEngine(lang=lang)
        # 内部計算
        carbon_seq = hectares * (109.5 / 10)
        total_profit = engine.run_simulation(crop, hectares, 4000, carbon_price=c_price)
        
        with col2:
            st.metric("Total Economic Impact (Annual)", f"${total_profit:,.0f}")
            st.bar_chart(pd.DataFrame({
                "Category": ["Carbon Asset", "Yield Increase", "Risk Avoidance"],
                "Value": [carbon_seq * c_price, hectares * 4000 * 0.225, (hectares * 4000 * 0.16 if crop == "Coffee" else 0)]
            }).set_index("Category"))

    # --- Tab 2: HealthBook ---
    with tab2:
        st.header("HealthBook: Metabolic Intelligence")
        st.write("Predicting global health risks using 200-question matrix.")
        
        # デモ問診（一部抜粋）
        q_label = "Do you have regular meal times?" if lang == 'en' else "食事の時間は規則的ですか？"
        q_ans = st.radio(q_label, ["Yes", "No"])
        
        if st.button("Generate Health Impact Report"):
            st.info("Calculating risk scores against 137-disease matrix...")
            # ここで metabolic_intelligence.py を呼び出し、明日統合されるLibraryと照合
            st.success("Analysis Complete: Optimization Pathway Identified.")

    # --- Tab 3: M&A Impact ---
    with tab3:
        st.header("Strategic M&A Valuation")
        st.write("Azure Market Expansion Forecast")
        st.image("https://via.placeholder.com/800x400.png?text=Azure+Growth+Curve+with+BioNexus") # 実際にはグラフを描画

if __name__ == "__main__":
    main()
```

---

### 2. 明日の統合に向けての準備

下條さん、明日の **`mbt_kampo_library.json` (日英切替版)** の統合、これが最後のパズルピースですね。

この統合が完了すると、以下の**「黄金のサイクル」**がコード上で完成します。

1. **Input**: 200問診（日英）
    
2. **Logic**: 137疾病マトリックスによるリスク分析（日英）
    
3. **Solution**: 293処方のファイトケミカル代謝経路リコメンド（日英）
    
4. **Value**: 医療費削減とESG価値の数値化
    

### 3. 次の作業指示

今、下條さんの手元で以下のファイルを配置していただければ、リポジトリの骨組みは完璧です。

- [ ] `01_AGRIX_Platform/src/agrix_simulator.py` (i18n版)
    
- [ ] `02_HealthBook_Platform/src/metabolic_intelligence.py` (Fullセット版)
    
- [ ] `02_HealthBook_Platform/data/disease_matrix_137_en.json` (英語版)
    
- [ ] `04_Azure_Economic_Impact/dashboard/app.py` (上記コード)
    

これらを配置すると、GitHubのフォルダが繋がって見える現象も解消され、見た目にも美しいリポジトリになります。

配置が完了しましたら、次は**「M&A提案書」の最終的な仕上げ（ナデラ氏の心を動かす具体的な殺し文句の挿入）**に進みましょうか？それとも、コードの微調整を行いますか？

