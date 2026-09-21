ローカルの単一フォルダ（SQLiteベース）にベクトルデータを保持する方法を具体的に教えてください。

---

ローカルの単一フォルダ（SQLiteベース）にベクトルデータを保存・管理する具体的な方法は、大きく分けて **1) ChromaDB等の軽量ベクトルDBライブラリを使う方法** と **2) SQLite本体＋拡張機能（sqlite-vec / sqlite-vss）を使う方法** の2つがあります。

どちらも外部サーバー（DockerやDocker Compose、Cloudサービスなど）が一切不要で、指定した **単一のローカルフォルダ内にすべてのデータ（ベクトル・メタデータ・SQLiteファイル）がまとまって永続化** されます。

### 方法1：ChromaDB（最もシンプル・推奨）

ChromaDBは内部でデフォルトで **SQLite** と **HNSWインデックス** を組み合わせて動いています。`PersistentClient` でフォルダパスを指定するだけで、そのフォルダ内にすべてのファイルが自動生成されます。

#### 1. フォルダ構成

実行すると、指定したフォルダ（例: `./my_vector_db`）内に次のようなファイルが作成されます。

```Plaintext
my_vector_db/
 ├── chroma.sqlite3        <-- メタデータやテキストを保持するSQLiteデータベース
 └── [UUIDフォルダ]/       <-- ベクトル空間の高速検索インデックス (HNSW)
```

#### 2. 実装コード（Python）

```Python
import chromadb
from chromadb.utils import embedding_functions

# 1. 保存先となる「単一ローカルフォルダ」のパスを指定
DB_FOLDER_PATH = "./my_vector_db"

# PersistentClientを使うことで、SQLiteベースで指定フォルダへ保存されます
client = chromadb.PersistentClient(path=DB_FOLDER_PATH)

# 2. 日本語・コードに強いEmbeddingモデルの読み込み（ローカルCPUで動作）
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="intfloat/multilingual-e5-small"
)

# 3. コレクション（テーブルのようなもの）の作成
collection = client.get_or_create_collection(
    name="my_documents",
    embedding_function=ef
)

# 4. データの登録（テキストを渡すと、自動でベクトル化されてSQLite等に保存される）
collection.add(
    documents=[
        "MBT55の基質濃度が80mMを超えるとフィードバック抑制が発生する。",
        "HealthBookの認証基盤はOAuth2.0とJWTを利用して構築されている。"
    ],
    metadatas=[{"source": "mbt55.py"}, {"source": "auth.py"}],
    ids=["doc1", "doc2"]
)

print("保存完了！指定したフォルダに sqlite3 ファイルが作成されました。")

# 5. データの検索
results = collection.query(
    query_texts=["MBT55の抑制条件は何ですか？"],
    n_results=1
)

print("\n--- 検索結果 ---")
print(results["documents"][0][0])
```

### 方法2：SQLite + sqlite-vec（完全単一 `.db` ファイル構成）

「フォルダ内をUUID等で散らかさず、**本当に単一の `.db`（SQLite）ファイル1つだけにまとめたい**」という場合は、**`sqlite-vec`** というSQLite公式拡張機能ライブラリを使うのが最も確実です。

#### 1. 必要なライブラリのインストール

```Bash
pip install sqlite-vec sentence-transformers
```

#### 2. 実装コード（Python）

通常の `sqlite3` ライブラリに `sqlite_vec` をロードさせて、ベクトルの保存とコサイン類似度検索（KNN検索）を行います。

```Python
import sqlite3
import sqlite_vec
from sentence_transformers import SentenceTransformer

# 1. 埋め込みモデルの準備（ベクトル次元数: 384次元）
model = SentenceTransformer("intfloat/multilingual-e5-small")

# 2. 単一のSQLiteデータベースファイルを作成・接続
db_path = "./my_vector_store.db"
conn = sqlite3.connect(db_path)

# sqlite-vec 拡張機能を読み込む
conn.enable_load_extension(True)
sqlite_vec.load(conn)
conn.enable_load_extension(False)

cursor = conn.cursor()

# 3. ベクトル格納用の仮想テーブルを作成 (float[384] はベクトルの次元数)
cursor.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS vec_documents USING vec0(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_text TEXT,
        embedding float[384]
    );
""")

# 4. データのテキスト作成とベクトル化
documents = [
    "MBT55の基質濃度が80mMを超えるとフィードバック抑制が発生する。",
    "HealthBookの認証基盤はOAuth2.0とJWTを利用して構築されている。"
]

# ベクトル変換（multilingual-e5 は "passage: " を前置するのが推奨）
embeddings = model.encode([f"passage: {doc}" for doc in documents])

# 5. SQLiteデータベースへ保存
for doc, emb in zip(documents, embeddings):
    cursor.execute(
        "INSERT INTO vec_documents(document_text, embedding) VALUES (?, ?)",
        (doc, sqlite_vec.serialize_float32(emb.tolist()))
    )
conn.commit()

# 6. 検索処理（クエリをベクトル化してKNN検索）
query_text = "MBT55の抑制条件は何ですか？"
query_emb = model.encode(f"query: {query_text}")

# sqlite-vecの `vec_distance_cosine` 関数で類似度が高い順に抽出
cursor.execute("""
    SELECT 
        document_text,
        vec_distance_cosine(embedding, ?) AS distance
    FROM vec_documents
    ORDER BY distance ASC
    LIMIT 1;
""", (sqlite_vec.serialize_float32(query_emb.tolist()),))

result = cursor.fetchone()

print("\n--- 検索結果 ---")
print(f"テキスト: {result[0]}")
print(f"距離（小さいほど類似）: {result[1]:.4f}")

conn.close()
```

### ChromaDB と sqlite-vec の選び方

|**比較項目**|**方法1：ChromaDB**|**方法2：sqlite-vec**|
|---|---|---|
|**ファイル構成**|単一フォルダ（`.sqlite3` + HNSWディレクトリ）|**完全に1つの `.db` ファイルのみ**|
|**自動ベクトル化**|**あり**（テキストを渡すだけで自動変換）|**なし**（Python側で数行書いてベクトル化が必要）|
|**検索速度（大容量データ）**|**超高速**（HNSWインデックスによる近似検索）|データ数万件程度まで高速（全件KNN検索）|
|**導入の難易度**|**極めて簡単**（数行で動く）|SQLiteのSQL知識が少し必要|

#### 推奨

17のリポジトリ（.txt）のようにテキスト量が比較的大きく、Pythonスクリプトで手軽に構築したい場合は「方法1：ChromaDB」が圧倒的にメンテナンスしやすくおすすめです。

一方、「バックアップや移動を `.db` ファイル1個のコピペだけで完全に終わらせたい」場合は「方法2：sqlite-vec」が最適です。