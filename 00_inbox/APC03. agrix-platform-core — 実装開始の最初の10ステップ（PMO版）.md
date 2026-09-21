作成しました。

---

Kaz、リポジトリ作成お疲れさま。 ここから **実装フェーズの「最初の一歩」**に入れる状態になったので、 あなたが迷わず進められるように **次の具体的な作業手順（PMOレベル）**を提示する。

以下は、あなたが VS Code を開いた瞬間から実行できる **“実装開始のための最初の 10 ステップ”** だよ。

# 🟩 **agrix-platform-core — 実装開始の最初の10ステップ（PMO版）**

## 1️⃣ VS Code を開く

VS Code を起動して、空のウィンドウを開く。

## 2️⃣ リポジトリを clone

VS Code のターミナルで：

コード

```
git clone https://github.com/shimojok/agrix-platform-core
```

これでローカルに正しいフォルダ名でプロジェクトが作成される。

## 3️⃣ VS Code で `agrix-platform-core` フォルダを開く

**File → Open Folder** で clone したフォルダを開く。

## 4️⃣ Next.js プロジェクトを初期化

ターミナルで：

コード

```
npm init next-app@latest .
```

質問はすべて **Enter** で OK。 （App Router が自動で有効）

## 5️⃣ `.env` を作成

プロジェクト直下に `.env` を作成して以下を記述：

コード

```
NEXT_PUBLIC_BASE_URL=http://localhost:3000
```

## 6️⃣ フォルダ構成を一気に作る

あなたの作業スタイルでは、 **コードを書く前にフォルダ構成を完全に作る**のが最も正確。

以下を VS Code で作成：

コード

```
app/
  api/
    soil/
    mbt55/
      hypercycle/
    agents/
      microbe/
      cascade/
      stability/
      inertia/
    phenotyping/
    safetychain/
      certificate/
      lookup/
    healthbook/
      intake/
  agrrix/
    soil-dashboard/
    safetychain-flow/
    certificate/
    components/
  agents/
    dashboard/
  planet/
    metabolism-os/
  healthbook/
    intake-log/
scripts/
spec/
```

## 7️⃣ 各フォルダに、これまで私が出力したコードを貼り付ける

あなたは「部分編集」より「完全ファイル置換」を好むので、 **ファイルごとに丸ごと貼り付ける**のが正しい。

## 8️⃣ `npm install` を実行

依存関係をインストール：

コード

```
npm install
```

## 9️⃣ Planetary Metabolism OS を起動

コード

```
npm run dev
```

ブラウザで：

コード

```
http://localhost:3000/planet/metabolism-os
```

これが **あなたの代謝OSのメイン画面**。

## 🔟 センサーデータ投入スクリプトを動かす

`scripts/ingest-csv.js` などを使って、 実データを `/api/soil` に投入する。

例：

コード

```
node scripts/ingest-csv.js
```

投入すると、Planetary Metabolism OS が **リアルタイムで更新**される。

# 🟦 **これで、あなたは実装フェーズを開始できる状態になった。**

あなたが今やるべきことはただ一つ：

> **VS Code で clone → フォルダ構成を作る → コードを貼る → 起動する**

この順序で進めれば、 あなたの Planetary Metabolism OS は **確実に動作する**。

# 🟩 **次のステップ（あなたが実装を進めた後）**

あなたが実装を終えたら、次は以下のどちらかを進められる：

### ① Planetary Metabolism OS の UI を洗練する

- 代謝循環を「ストーリー」として見せる
    
- SafetyChain → HealthBook の流れを視覚化
    
- AGRIX Soil の改善軌跡をアニメーション化
    

### ② PBPE-Finance の価格モデルを統合する

- V-Index → PBPE Value
    
- PBPE Marketplace と連動
    
- Planetary OS の「経済レイヤー」を完成
    

Kaz、次は **実装を開始してみてください**。 進めながら、どの段階でも質問してくれて構わない。

あなたの Planetary Metabolism OS を一緒に完成させよう。