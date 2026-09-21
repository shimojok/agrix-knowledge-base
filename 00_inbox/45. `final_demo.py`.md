下條さん、再三にわたる不具合、誠に申し訳ございません。

「全く変わらない」ということは、**「上書き保存したはずの最新コードが、Streamlitの実行環境に反映されていない（古いキャッシュや別ファイルを読み続けている）」**可能性が極めて高いです。

GitHub Codespaces特有の「保存の遅延」や「実行パスの固定化」を打破し、**今この瞬間に、下條さんの画面にダッシュボードを表示させるための「最後の手順」**を提案します。

一度、既存のファイル構成を忘れ、**「今いる場所に、新しい名前で、全てが完結したファイル」**を作って実行しましょう。

---

### 🛠 解決手順：新しいファイルで強制起動

1. ターミナル（一番下の黒い画面）で、以下のコマンドをコピーして貼り付け、Enterを押してください。
    
    - これによって、現在のフォルダに直接 `final_demo.py` という新しいファイルが作成されます。
        

Bash

```
cat << 'EOF' > final_demo.py
import streamlit as st
import pandas as pd

# 下條さんのロジックを統合した単一ファイル
def main():
    st.set_page_config(page_title="Azure-PMOS Executive", layout="wide")
    st.sidebar.title("🌐 Azure-PMOS")
    lang = st.sidebar.selectbox("Language / 言語", ["ja", "en"])
    
    title = "Azure-PMOS: 経営意思決定支援" if lang == 'ja' else "Azure-PMOS: Executive Decision Support"
    st.title(title)
    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs(["AGRIX", "HealthBook", "Strategic Impact", "Iwanuma Evidence"])

    with tab1:
        st.header("AGRIX: 土壌生態制御 (Soil Ecological Control)")
        col1, col2 = st.columns([1, 2])
        with col1:
            ha = st.number_input("面積 / Area (ha)", value=1000)
            mbt = st.toggle("MBT55 (5x Yield Boost)", value=True)
            yield_val = 5.0 if mbt else 1.0
        with col2:
            impact = ha * 4000 * yield_val
            st.metric("経済インパクト / Economic Impact", f"${impact:,.0f}")
            st.success("✅ Negative Green Premium Achieved" if mbt else "Traditional")

    with tab2:
        st.header("HealthBook: 代謝インテリジェンス")
        st.write("200問診 × 137疾病マトリックス × 293漢方ライブラリ")
        if st.button("分析デモ実行 / Run Analysis"):
            st.json({"Status": "Optimal", "Target": "Mitochondrial Activation"})

    with tab3:
        st.header("M&A Strategy / 時価総額予測")
        df = pd.DataFrame({
            "Entity": ["Microsoft", "Yara International"],
            "Value": ["+$300B - $400B", "5.5x Growth"],
            "Logic": ["Ecological Data Monopoly", "Waste-to-Asset"]
        })
        st.table(df)

    with tab4:
        st.header("Proven Results: 岩沼の実績")
        st.video("https://www.youtube.com/watch?v=urH8fNTZQ2Q")

if __name__ == "__main__":
    main()
EOF
```

2. 次に、この新しく作ったファイルを**直接**実行します。
    

Bash

```
streamlit run final_demo.py
```

---

### 💡 なぜこれで動くのか

- **ファイル読み込みの失敗を回避**: `app.py` ではなく `final_demo.py` という新しい名前で実行することで、古いキャッシュを強制的に破棄します。
    
- **パス問題を解消**: 外部ファイルのインポートを一切行わず、一つのファイルに全てのロジックを詰め込んだため、`NameError` が出る余地がありません。
    

これで画面が開かなければ、Codespaces自体の接続エラーですので、ブラウザをリロード（再読み込み）してください。

下條さん、この「新ファイル作成 ➔ 実行」で、ようやくダッシュボードが動き出すはずです。信じて試してみてください。