ChromaDBのインデックスが作成されたので、実際にベクトル検索をテストするための検索用スクリプトを作成してください。

---

既に作成・検証を行った **`scripts/search_rag.py`** が、正に ChromaDB のベクトル検索をテストするための専用スクリプトです。

`multilingual-e5-small`（384次元）の仕様に準拠し、`query:` プレフィックスを自前で付与して類似度スコア付きで上位結果を取得するコードとなっています。

最新の `scripts/search_rag.py` のコードを再掲します。

```Python
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# DBディレクトリとモデルの指定 (384次元)
DB_DIR = "./chroma_db"
MODEL_NAME = "intfloat/multilingual-e5-small"

def main():
    print("--- BioNexus Engine: ローカルベクトル検索テスト (e5-small) ---")
    
    # 1. DBの存在確認
    if not os.path.exists(DB_DIR):
        print(f"【エラー】ChromaDB ({DB_DIR}) が存在しません。インデックス作成完了後に実行してください。")
        return

    # 2. ローカルEmbeddingモデルのロード
    print("Embedding モデルをロード中...")
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)

    # 3. 既存の ChromaDB に接続
    db = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )

    # 4. 検索インタラクティブループ
    print("\n準備完了！検索クエリを入力してください（終了するには 'q' と入力）:\n")
    while True:
        raw_query = input("クエリ > ").strip()
        if not raw_query:
            continue
        if raw_query.lower() == 'q':
            print("検索を終了します。")
            break

        # e5 モデルの検索精度向上のため "query: " プレフィックスを付与
        formatted_query = f"query: {raw_query}"

        print(f"\n『{raw_query}』の検索結果上位 3 件を取得中...")
        
        # 類似度スコア付きで検索
        results = db.similarity_search_with_score(formatted_query, k=3)

        if not results:
            print("該当する結果は見つかりませんでした。")
            continue

        for i, (doc, score) in enumerate(results, 1):
            source = doc.metadata.get("source", "不明")
            print(f"\n--- [結果 {i}] (距離スコア: {score:.4f}) ---")
            print(f"ファイルパス: {source}")
            print("内容プレビュー:")
            print(doc.page_content[:300] + ("..." if len(doc.page_content) > 300 else ""))
            print("-" * 50)
        print("\n" + "=" * 50 + "\n")

if __name__ == "__main__":
    main()
```

### 実行コマンド

ターミナルで以下を実行することで、単体テストを行えます。


```PowerShell
python scripts/search_rag.py
```