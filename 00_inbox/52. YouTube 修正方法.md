下條さん、ご確認ありがとうございます。Streamlit上の動画プレイヤーで発生している「エラー 153」は、YouTube側が**「外部サイト（この場合はStreamlitのデモ画面）での埋め込み再生」を制限している**場合に出る特有のエラーです。

ナデラCEOに見せる際に「動画が映らない」のは避けるべきですので、**「埋め込み許可済みのURL形式」への修正**、および万が一再生できない場合の**「バックアップ・リンク」**を配置する修正を行いましょう。

### 🛠️ 修正方法

`final_demo.py` の一番下にある `with tab4:` のブロック（YouTubeを表示している部分）を、以下のコードに書き換えてください。

Python


    # --- Tab 4: Iwanuma Evidence (Video Fix) ---
    with tab4:
        st.header(t["iw_h"])
        
        # 埋め込み形式のURLに修正
        video_url = "https://www.youtube.com/embed/urH8fNTZQ2Q"
        
        # コンテナを使って表示を安定させる
        st.video(video_url)
        
        st.markdown("---")
        st.write("#### 🔗 Direct Evidence Links")
        st.info("If the player does not load, please view the evidence directly on YouTube:")
        st.markdown(f"[▶️ Watch: Iwanuma Project Evidence (2011)]({video_url.replace('embed/', 'watch?v=')})")
        
        st.write("Result: 1-week transformation of toxic sludge into bio-fertilizer." if lang=="en" else "実績：震災汚泥を1週間で無害化・肥料化。")


---

### 💡 なぜこれで直るのか？

1. **URL形式の変更**: 通常の `watch?v=...` 形式ではなく、`/embed/...` という埋め込み専用のパスを明示することで、プレイヤーの競合を回避します。
    
2. **バックアップ・リンク**: YouTubeのポリシー変更等でプレイヤーがブロックされた場合でも、すぐに別タブで開けるよう「直接リンク」を配置しました。エグゼクティブ向けのデモでは、こうした**「不測の事態への備え」**自体がシステムの信頼性として評価されます。
    

### 🚀 反映手順

1. GitHubで `final_demo.py` を開き、一番下の `with tab4:` 部分を上記に書き換えて保存。
    
2. ブラウザのデモ画面をリロードしてください。
    

これで動画がスムーズに再生されるはずです。試してみてください！