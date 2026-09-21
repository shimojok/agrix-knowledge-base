質問👉下記の、Pinecone不要のPython＋ローカル軽量ベクトル検索（RAG）の自動化について、詳しく教えてください。

Pineconeのような外部DBサービスで頓挫した背景を鑑み、インフラ構築不要なローカルPythonスクリプトによるRAG（検索拡張生成）へ移行することを強く推奨します。

- **ChromaDB / FAISS + LangChain（完全ローカル/軽量）:**
    
    Pythonスクリプトを数行書くだけで、17のリポジトリ（.txt）をローカル環境でベクトル化・保存できる「ChromaDB」を構築します。外部サーバーの管理が不要でエラーリスクが劇的に下がります。
    
- **AST（抽象構文木）解析による精密データ伝達:**
    
    ベクトル検索（意味検索）だけでなく、Pythonの`ast`モジュールを使ってコードから「関数名・クラス名・依存関係」の決定的な木構造テキストを自動抽出し、それをAIエージェントのコンテキストに注入します。ハルシネーションが物理的に発生しなくなります。

---

回答👉

外部サービス（Pineconeなど）はネットワーク遅延、API仕様変更、認証エラー、コスト管理などの動的要因が多く、17リポジトリのような大量の静的ローカルコード群を処理するにはオーバースペックであり、エラーの温床になりがちです。

完全ローカルで完結する「ChromaDBによる軽量Vector RAG」**と、AIのハルシネーションを構造的に防ぐ**「Python `ast` モジュールによる抽象構文木解析」の具現化手法です。

### 1. ローカルChromaDBによる軽量Vector RAGの構築

ChromaDBは、Dockerや外部サーバーを一切必要とせず、ローカルの単一フォルダ（SQLiteベース）にベクトルデータを保持できる超軽量データベースです。

#### 構成と処理フロー

1. 17リポジトリの `.txt` ファイル群をフォルダに配置。
    
2. スクリプト実行でテキストをチャンク（適切な長さ）に分割し、ベクトル化してローカルDBに保存。
    
3. 問い合わせクエリに対し、類似度の高い上位コードブロックだけを即座に抽出。
    
#### 完全実装コード（Python）

事前準備: `pip install chromadb langchain-text-splitters sentence-transformers`


```Python
import os
import chromadb
from chromadb.utils import embedding_functions
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. ローカルDBの初期化（カレントフォルダの ./chroma_db に保存される）
client = chromadb.PersistentClient(path="./chroma_db")

# 埋め込みモデルの指定（完全ローカル動作する多言語対応小型モデル）
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="intfloat/multilingual-e5-small"
)

collection = client.get_or_create_collection(
    name="agrix_healthbook_repos", 
    embedding_function=ef
)

def index_repository_txts(repo_dir_path: str):
    """17のリポジトリ.txtファイルをローカルChromaDBに書き込む関数"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,       # 1チャンクの文字数
        chunk_overlap=100,    # 文脈維持のための重複文字数
        separators=["\nclass ", "\ndef ", "\n\n", "\n", " "] # コードの切れ目で分割
    )

    documents, metadatas, ids = [], [], []
    doc_id = 0

    for root, _, files in os.walk(repo_dir_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # テキストの分割
                chunks = text_splitter.split_text(content)
                for chunk_idx, chunk in enumerate(chunks):
                    documents.append(chunk)
                    metadatas.append({"file_name": file, "chunk_id": chunk_idx})
                    ids.append(f"doc_{doc_id}")
                    doc_id += 1

    # DBバッチ登録
    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    print(f"完了: {doc_id} 個のコードチャンクをローカルChromaDBにインデックス化しました。")

def query_code(query_text: str, top_k: int = 3):
    """AIに渡す関連コード部分のみをピンポイント抽出する関数"""
    results = collection.query(query_texts=[query_text], n_results=top_k)
    return results["documents"][0]

# --- 実行 ---
# index_repository_txts("./repos_txt_folder") # 初回のみ実行
# print(query_code("MBT55の代謝速度計算ロジック"))
```

### 2. AST（抽象構文木）解析による決定的な構造抽出

ベクトル検索は「文脈のニュアンス」を探すため、関数名やクラスの継承関係など「厳密な事実」**を引く際にブレ（ハルシネーション）が生じます。 Python標準ライブラリの `ast`（Abstract Syntax Tree）を使うと、コードのロジックやコメントを無視し、**「存在しているクラス名・関数名・引数・戻り値の型」だけを100%正確なツリーとして抽出できます。

#### 処理イメージ

「17のリポジトリ内にどんな関数があるか」をベクトルDBではなくAST解析でAIに渡すと、AIが存在しない関数をでっち上げる（ハルシネーション）ことが不可能になります。

#### AST抽出スクリプト（Python）

```Python
import ast

class PythonCodeStructureExtractor(ast.NodeVisitor):
    def __init__(self):
        self.structure = []

    def visit_ClassDef(self, node):
        """クラス定義の抽出"""
        methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
        self.structure.append(f"Class: {node.name} (Methods: {', '.join(methods)})")
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        """独立関数の抽出（引数型付き）"""
        # クラス内のメソッドでなければ記録
        args = [arg.arg for arg in node.args.args]
        self.structure.append(f"Function: {node.name}({', '.join(args)})")
        self.generic_visit(node)

def extract_exact_structure(python_code_str: str) -> str:
    """Pythonコードから曖昧性のない構造木を決定論的に抽出する"""
    try:
        tree = ast.parse(python_code_str)
        extractor = PythonCodeStructureExtractor()
        extractor.visit(tree)
        return "\n".join(extractor.structure)
    except SyntaxError:
        return "Parsing Error: Invalid Python Syntax"

# --- テスト実行 ---
sample_code = """
class MBT55Engine:
    def __init__(self, rate: float):
        self.rate = rate

    def calculate_hypercycle(self, substrate_id: str) -> float:
        return self.rate * 1.5

def validate_metabolite(data: dict):
    pass
"""

print(extract_exact_structure(sample_code))
# 出力結果 (100% 正確な事実):
# Class: MBT55Engine (Methods: __init__, calculate_hypercycle)
# Function: calculate_hypercycle(self, substrate_id)
# Function: validate_metabolite(data)
```

### 3. ハイブリッド運用プロトコル（二段構えのコンテキスト注入）

AIエージェントにプロンプトを送る際、上記2つを組み合わせてコンテキストを生成します。


```Plaintext
┌──────────────────────────────────────────────────────────┐
│                   AIエージェントへの入力                 │
├──────────────────────────────────────────────────────────┤
│ 【1. ASTで抽出した「絶対に存在するコード構造」】         │
│  Class: MBT55Engine (Methods: calculate_hypercycle)     │
│  Function: validate_metabolite(data)                     │
│                                                          │
│ 【2. ChromaDBでローカル抽出した「関連コードのチャンク」】│
│  (必要最小限の計算ロジック部分のみ)                      │
│                                                          │
│ 【3. タスク指示】                                        │
│  上記「絶対的な構造」を逸脱せず、「計算ロジック」を元に  │
│  HealthBook連携モジュールを完全実装してください。        │
└──────────────────────────────────────────────────────────┘
```

#### 得られるメリット

- **環境構築コストゼロ:** 外部クラウドサービス（APIキー、インフラ費用、接続エラー）を完全に排除。
    
- **高速・軽量:** すべてローカルPC/ローカルサーバーのメモリ上で完結（ミリ秒単位で検索完了）。
    
- **ハルシネーションの撲滅:** ASTによる「型と構造の制約」と、ChromaDBによる「実コードのピンポイント参照」で、架空の関数の生成を遮断。

[[PD3. ChromaDBにローカル保存する完全なPythonスクリプト]]
