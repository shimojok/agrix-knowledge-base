### テキストで見るデータの流れ

- **従来のローカルRAG**
    
    `Obsidianノート` ➔ （Pythonで解析） ➔ `ChromaDB` ➔ （LangChainで検索） ➔ `LLM` ➔ `Streamlit UI`
    
- **MCP導入後の拡張**
    
    `MCPクライアント（Cursor / Claude Desktop等）` ──(MCP規格)──> `MCPサーバー（Obsidian / ChromaDB）` ➔ `LLM`
    
    ※AI側から「Obsidianのノートを直接読みに行く」「ChromaDBを検索する」といったアクションを標準化されたプロトコルで自律的に実行できるようになります。

貴方が説明してくれた上記の内容で理解できました。

次に、MCP導入時に利用するツールにどのようなものがあるのか、説明してください。
その際、Obsidian プラグインのSemantic Notes Vault MCP、Vault Knowledge base　も比較検討してください。

---

データフローの整理で理解を深めていただき嬉しいです。

  

MCP（Model Context Protocol）を導入する際、エコシステムは大きく分けて「MCPクライアント（呼び出し側）」**と**「MCPサーバー（データ・ツール提供側）」**、そしてその2つを繋ぐ**「Obsidian向けMCP連携プラグイン・ツール」で構成されます。

  

全体像と、ご質問の「Semantic Notes Vault MCP」「Vault Knowledge Base」の比較を含めて解説します。

  

## 1. MCPエコシステムを構成する主なツール分類

MCP環境を構築するには、以下3つのレイヤーのツールを組み合わせて利用します。

  

Plaintext

```
【レイヤー1: MCPクライアント (利用者・指示側)】
  ├─ Cursor / Windsurf (AI内蔵コードエディタ)
  ├─ Claude Desktop (Anthropic公式PCアプリ)
  └─ Dify / Continue (オープンソース開発プラットフォーム・拡張機能)
          │
          │ (MCP標準プロトコル通信: JSON-RPC over Stdio/SSE)
          ▼
【レイヤー2: MCPサーバー (データ・処理の提供側)】
  ├─ Obsidian Vault MCP サーバー（ノート参照・検索）
  ├─ ChromaDB / Vector DB MCP サーバー（類似度検索）
  └─ Python Execution / SQLite MCP サーバー（計算・DB処理）
```

### レイヤー1: 代表的なMCPクライアント

- **Cursor / Windsurf**: コードを書きながら、`C:\Users\user\agrix-knowledge-base` のノートを直接AIに参照させてモデル実装やデバッグを行える開発エディタ。
    
      
    
- **Claude Desktop**: チャット画面からObsidianのノート群やChromaDBを横断検索させ、意思決定（Executive Briefing）の草案を作らせるためのPCアプリ。
    
      
    

## 2. Obsidian Vault向けMCPツールの比較検討

Obsidianのノート群（Vault）をMCPサーバー化してAIに読ませるアプローチにはいくつか代表的なツール・プラグインが存在します。ご提示いただいた2つを中心に特徴を比較します。

  

|**ツール・プラグイン名**|**アーキテクチャのタイプ**|**検索方式**|**主な特徴・メリット**|**課題・注意点**|
|---|---|---|---|---|
|**Semantic Notes Vault MCP**|Obsidianプラグイン 兼 MCPサーバー|ベクトル検索 (Semantic Search) ＋ テキスト検索|ノートの意味（文脈）を理解して検索。類似したテーマのノートを多次元で引き出すため、**ハルシネーション防止性能が高い**。|事前に埋め込み（Embedding）インデックスの生成が必要。|
|**Vault Knowledge Base (MCP)**|CLI / ローカルスクリプト型 MCPサーバー|キーワード検索 ＋ フロントメタデータ解析|Vault全体のディレクトリ構造や `$0` メタデータ、タグ、リンク構造を軽量に解析してAIに渡す。構造の把握が得意。|テキストの「意味的類似度」による抽象検索は苦手。|
|**Obsidian Local REST API + MCP** _(補足比較)_|REST API変換型 MCPサーバー|Obsidian内蔵検索 API 依存|Obsidianが起動していれば、既存のプラグインエコシステムをそのままMCP化できる。|Obsidianアプリ自体をバックグラウンドで起動しておく必要がある。|

## 3. 「Semantic Notes Vault MCP」vs「Vault Knowledge Base」詳細比較

### ① Semantic Notes Vault MCP（意味検索・ハルシネーション抑制重視）

- **仕組み**: ノート群をベクトル化（Semantic Embedding）し、AIからの定性的な質問（例: 「MBT55とファイトケミカルの相互作用の根拠は？」）に対して、最も文脈の近い段落をピンポイントで抽出して渡します。
    
      
    
- **評価**: **現在のプロジェクト（BioNexus）に最も推奨できます。** 137疾病やファイトケミカル、代謝シミュレーションの根拠ノートを正確にAIに参照させ、ハルシネーションを極限まで減らしたい目的に合致しています。
    
      
    

### ② Vault Knowledge Base（構造・メタデータ・検索スピード重視）

- **仕組み**: ノートの全件スキャン、フロントマター（`tags:`, `created:` など）、`[[内部リンク]]` のつながりを構造化してAIに提示します。
    
      
    
- **評価**: 「どのフォルダにどんなノートがあるか」「このタグが付いたノートの一覧は何か」といった、**Vault全体の整理や仕様把握をAIに行わせる際に威力を発揮**します。
    
      
    

## 4. BioNexusプロジェクトにおけるベストな組み合わせ

まずは最も開発・検証の恩恵を受けやすい以下の構成から試すのがおすすめです。

  

1. **MCPクライアント**: **Cursor**（コード開発時） または **Claude Desktop**（思考・検証時）
    
      
    
2. **Obsidian連携**: **Semantic Notes Vault MCP**
    
      
    - Obsidian内の `agrix-knowledge-base` をベクトル化してMCP経由で公開。
        
          
        
    - AI（Cursor/Claude）に「Vault内のノートのみを根拠にして回答して」と指示することで、開発中のハルシネーションを防止しつつ、コードやドキュメントの生成が可能になります。
        
          
        

この構成を導入することで、手動でPythonの検索スクリプトを動かさなくても、チャット画面やエディタ上で常にObsidianのSSOT（唯一の正しい情報源）を参照した開発・推論が行えるようになります。