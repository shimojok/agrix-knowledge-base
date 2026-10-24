#claude #2026-09-27 

既存の資産棚卸しから始めます。今回の資料と`repo-consolidation.md`の内容を合わせると、実態が見えてきました。

## 現状把握：9つの独立ダッシュボード＋4種のHTMLモックアップ

GitHub側で既にライブ稼働しているダッシュボードだけで9個あります（M3-Core-Engine、MBT-Biosecurity-Engine、PBPE-Marketplace、PBPE-Finance、PBPE-Dashboard、pbpe-mbt55-investment-engine、Azure-PMOS、HealthBook-AI、HealthBook-MBT55-Unified）。加えて今回のHTML添付4種を確認しました。

|ファイル|内容|
|---|---|
|`index.html`|言語選択ゲートウェイ（英語/日本語）。7つの課題領域、Yield+30%・医療費-2.3兆ドル・GHG-22%・気候金融TAM 790億ドル+|
|`index_1.html`|**「PMOS — Planetary Metabolism OS」**。入力コントロールパネル、SOC10年累積推移、ha当たりコスト構造、陸海一体型インパクト|
|`agrix_architecture_dashboard.html`（×2、同一内容）|「AGRIX Platform OS — Architecture Dashboard」|
|`pbpe-dashboard-v2-en.html`|ACIB（農地炭素担保型インフラ債）、ARS（農業収益スワップ）、HALI（健康連動保険）の3金融商品＋Export/Pitch Deck機能|

**これは「足りない」状況ではなく「バラバラに存在しすぎている」状況です。** そして、以前分野別仕訳けで確立した6プロジェクト分類（PROJECT 01 HealthBook / 02 AGRIX / 03 MBT55 / 04 PBPE / **05 PMOS** / 06 BioNexus Integration）と、この`index_1.html`の「PMOS」という名称が偶然ではなく完全に一致しています。つまりKazさんの頭の中の構造と、既に作られたダッシュボードの構造は、実はもう揃っているんです。整理されていないだけです。

## 問題の所在

9つのStreamlitアプリ＋複数のHTMLモックアップが、**それぞれ独立して数字を持っている**可能性が高いという点が一番のリスクです。PBPE-FinanceとPBPE-Dashboardとpbpe-mbt55-investment-engineは、おそらく似た数字（ROI、NPV、GHG削減量）を別々に計算・表示しています。ゲイツ財団やMicrosoftの担当者が2つのダッシュボードを開いて数字が食い違っていたら、それだけで信頼性が崩れます。前回話した「独立検証済みデータの公開」という戦略とも真っ向から矛盾します。

## 提案する構築手法：4層アーキテクチャ

新しく作るのではなく、**既存の9+4資産を4層に再配置する**方法を提案します。

```
Layer 0: Single Source of Truth
  agrix-knowledge-base（kb017/kb018で設計中の意味論抽出エンジン経由）
  ＋ agrix-platform-kb.json / pbpe-platform-kb.json
        │
Layer 1: 計算コア（唯一の真実源）
  mbt_hypercycle/（kb017 Phase 2）
  pbpe/npv_engine.py, pbpe/carbon_engine.py 等
  ← ここでしか数字を計算しない。ACIB/ARS/HALIの利回りも、GHG削減量も、ここが唯一の出所
        │
Layer 2: データAPI層
  既存9リポジトリが共通で叩く1つのAPI（またはjson出力）
  ← 各Streamlitアプリはこの層からのみ数字を取得し、独自計算を持たない
        │
Layer 3: プレゼンテーション層（複数存在してよい）
  PMOS Dashboard（index_1.html）＝統合ハブ・全体像
  AGRIX Architecture Dashboard＝技術者・専門家向け
  PBPE Dashboard v2＝投資家・金融機関向け（ACIB/ARS/HALI）
  各Streamlitアプリ＝詳細ドリルダウン用
```

**Layer 3は今のまま9個+αあってよい**、というのが要点です。問題は乱立ではなく、Layer 1（計算コア）が存在せず、Layer 3の各アプリが自前で数字を持っていることです。Layer 1〜2を作れば、既存資産はほぼ捨てずに再利用できます。

## トラックA/Bとの接続

以前話したトラックA（ゲイツ財団・Microsoft向けピッチ）にとって必要なのは、Layer 3の中で**1つだけ**を「これが公式版」と決めることです。`pbpe-dashboard-v2-en.html`はACIB/ARS/HALIという金融商品構造を持ち、Export/Pitch Deck機能まで既にある——これが一番トラックAに近い完成度だと思います。これを軸に、Layer 1の実データ（BPK002の実測値、下水汚泥試験の性能指標）を接続すれば、独立検証済みの数字で武装したピッチ資料になります。

`index_1.html`（PMOS）は、トラックB（社内エンジン・全体統合）の入口として位置づけるのが自然です。

## 次の一手

Layer 1（計算コア）は、kb017 Phase 2で既に設計に入っています。ここに実データ（BPK002の廃棄物単価、下水汚泥試験の処理速度、今回の特許文書の性能指標）を接続する作業と、`pbpe-dashboard-v2-en.html`をトラックAの「公式版」として磨く作業は、並行させず順番にやるべきだと思います（work-preferencesの通り）。

どちらを先にやりますか。個人的には、ピッチの緊急性を考えると、**まず`pbpe-dashboard-v2-en.html`に実データを1つずつ差し込んでいく**（Layer 1を本格構築する前に、手作業でこのダッシュボードだけ実データ化する）方が、Layer 1〜2の設計を待つより早く「見せられるもの」ができると思います。