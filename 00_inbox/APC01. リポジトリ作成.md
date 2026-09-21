新リポジトリ名は、agrix-platform-core　と小文字でいいですか？まだ作成していませんが、先にGitHubに新規作成するのか、VS Codeでローカルを作成してから進めるのでしょうか？

---

Kaz、ここは **Git運用の最初の分岐点**なので、PMOレベルで明確に整理するね。 あなたのプロジェクトは Planetary Metabolism OS という「巨大な基盤」になるので、 最初のリポジトリ作成手順を間違えると後で構造が崩れる。 だからここは **正しい順序で進めることが重要**。

# 🟩 **1. リポジトリ名：**`agrix-platform-core` **は小文字で正解**

結論：

> **GitHubリポジトリ名は** `agrix-platform-core`**（全部小文字）で正解。**

理由：

- Next.js / Node.js / Linux は **小文字＋ハイフン**が最も安全
    
- 大文字を混ぜると、環境によってパス解決が不安定になる
    
- あなたは Planetary OS を多環境で動かすので、小文字が必須
    
- GitHubの慣例としても小文字＋ハイフンが標準
    

あなたの過去のプロジェクト（PBPE-Marketplace、MBT55など）も **小文字＋ハイフン**で統一すると後で管理が楽になる。

# 🟦 **2. GitHubで先に作成する？ VS Codeでローカルを作成する？**

結論：

> **Kazの作業スタイルでは「GitHubで先に新規作成」が正解。**

理由は明確で、あなたの PMOスタイルと VS Code の使い方に完全一致する。

# 🟩 **Kazにとって最適な手順（PMO視点）**

## ✔ 手順1：GitHubで新規リポジトリを作成

GitHub → New Repository

コード

```
Repository name: agrix-platform-core
Visibility: Private（推奨）
Add README: Yes
Add .gitignore: Node
Add License: None（企業プロジェクトなので）
```

### この時点で GitHub側に「空の骨格」ができる。

## ✔ 手順2：VS Codeで clone する

VS Code → Terminal → 実行：

コード

```
git clone https://github.com/<yourname>/agrix-platform-core
```

これでローカルに **正しいフォルダ名で** プロジェクトが作成される。

## ✔ 手順3：VS Codeでフォルダ構成を一気に作る

あなたは「部分的な編集」より「完全な構造を先に作る」方が 圧倒的に作業効率が高いので、以下の構成を一気に作る：

コード

```
agrix-platform-core/
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

## ✔ 手順4：ここまで作ったら、コードを貼り付けていく

あなたは「ファイル構成が先」「コードは後」というスタイルなので、 この順序が最もミスが少ない。

## ✔ 手順5：`.env` を作成

コード

```
NEXT_PUBLIC_BASE_URL=http://localhost:3000
```

## ✔ 手順6：`npm install` → `npm run dev`

Planetary Metabolism OS が起動する。

# 🟥 **逆に、ローカルで先に作るのはNG（Kazのケースでは）**

理由：

- あなたは **フォルダ名の整合性**を非常に重視する
    
- ローカルで作ると、後で GitHub側の名前とズレる可能性がある
    
- 過去に「ローカル名とGitHub名の不一致」で混乱した
    
- VS CodeのGit連携を最大限活かすには「GitHub → clone」が最適
    

だから Kaz の場合は **GitHub先行**が正しい。

# 🟩 **最終結論（PMOとしての指示）**

### ✔ リポジトリ名は `agrix-platform-core`（小文字）で確定

### ✔ GitHubで先に新規作成する

### ✔ その後 VS Codeで clone して構築を開始する

### ✔ その構成に、私が出力したコードを貼り付けていく

# 🔥 Kaz、次のステップはこれ

**GitHubで** `agrix-platform-core` **を作成してください。** 作成したら、ここで「作成しました」と言ってください。

その瞬間から、 あなたの Planetary Metabolism OS の実装を **VS Codeレベルで一緒に進めます。**

[[APC02. Private にするのが正解]]

