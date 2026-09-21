17のリポジトリ（.txt）が格納されたフォルダを一括読み込みし、ChromaDBにローカル保存する完全なPythonスクリプトを作成してください。

---

17のリポジトリ（.txt形式）が格納されたフォルダを一括でスキャンし、段落・コード単位でテキストを分割してローカルの **ChromaDB** に保存・インデックス化する完全な Python スクリプトを作成しました。

外部のベクトルDBサービス（Pinecone等）を使わず、すべてローカル環境（`./chroma_db` フォルダ）内でSQLiteデータベースとして完結するため、インフラ構築の手間や外部APIエラーのリスクを完全に排除できます。

### 事前準備（ライブラリのインストール）

事前に以下のライブラリをインストールしてください。

```Bash
pip install chromadb sentence-transformers tqdm
```

### 一括インデックス化スクリプト (`build_local_rag.py`)

以下のスクリプトを保存し、17のリポジトリ `.txt` が入ったフォルダパスを指定して実行してください。

```Python
import os
import glob
from typing import List, Dict
from tqdm import tqdm

import chromadb
from chromadb.utils import embedding_functions


class RepositoryLocalRAGBuilder:
    """
    17のリポジトリ(.txt)を一括読み込みし、ローカルChromaDBに保存するビルダー
    """

    def __init__(
        self,
        db_path: str = "./chroma_db",
        collection_name: str = "agrix_healthbook_repos",
        model_name: str = "intfloat/multilingual-e5-small"
    ):
        """
        :param db_path: ローカル保存先のデータベースディレクトリ
        :param collection_name: ChromaDBコレクション名
        :param model_name: 埋め込みモデル（ローカル動作する多言語対応日本語・コード学習モデル）
        """
        print(f"[1/4] ChromaDBクライアントを初期化中... (保存先: {db_path})")
        self.client = chromadb.PersistentClient(path=db_path)

        # 多言語・コード文脈に強い軽量なローカルEmbeddingモデルを使用
        self.ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=model_name
        )

        print(f"[2/4] コレクション '{collection_name}' を取得または作成中...")
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.ef,
            metadata={"hnsw:space": "cosine"}  # コサイン類似度で検索
        )

    def _split_code_or_text(
        self,
        text: str,
        chunk_size: int = 1000,
        overlap: int = 150
    ) -> List[str]:
        """
        コード・文章構造を保持しながら指定文字数サイズでチャンク分割する簡易スプリッター
        """
        # クラス定義や関数定義、空行などの境界で優先的に分割
        separators = ["\nclass ", "\ndef ", "\n\n", "\n", " "]
        
        chunks = []
        start = 0
        text_len = len(text)

        while start < text_len:
            end = start + chunk_size
            if end >= text_len:
                chunks.append(text[start:].strip())
                break

            # できるだけきれいな切れ目（セパレータ）を探す
            best_cut = end
            for sep in separators:
                pos = text.rfind(sep, start + chunk_size // 2, end)
                if pos != -1:
                    best_cut = pos
                    break

            chunk_str = text[start:best_cut].strip()
            if chunk_str:
                chunks.append(chunk_str)

            # 重複（overlap）を持たせて次のチャンクへ
            start = max(start + 1, best_cut - overlap)

        return chunks

    def build_from_folder(
        self,
        repos_folder: str,
        chunk_size: int = 1000,
        overlap: int = 150,
        batch_size: int = 100
    ):
        """
        指定フォルダ内の全.txtファイルをインデックス化
        """
        txt_files = glob.glob(os.path.join(repos_folder, "**", "*.txt"), recursive=True)
        
        if not txt_files:
            print(f"エラー: 指定されたフォルダ '{repos_folder}' 内に .txt ファイルが見つかりませんでした。")
            return

        print(f"[3/4] 検出された {len(txt_files)} 個のファイルからテキストをインポート中...")

        documents = []
        metadatas = []
        ids = []
        doc_count = 0

        for file_path in tqdm(txt_files, desc="ファイル読み込み"):
            file_name = os.path.basename(file_path)
            rel_path = os.path.relpath(file_path, repos_folder)

            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except Exception as e:
                print(f"警告: ファイル {file_path} の読み込みに失敗しました: {e}")
                continue

            if not content.strip():
                continue

            # テキストをチャンクに分割
            chunks = self._split_code_or_text(content, chunk_size=chunk_size, overlap=overlap)

            for idx, chunk in enumerate(chunks):
                doc_count += 1
                documents.append(chunk)
                metadatas.append({
                    "file_name": file_name,
                    "relative_path": rel_path,
                    "chunk_index": idx,
                    "total_chunks": len(chunks)
                })
                # ユニークなID（ファイル名_チャンク番号）
                ids.append(f"{file_name}_chunk_{idx}")

        print(f"[4/4] 計 {doc_count} 個のテキストチャンクをChromaDBに書き込み中（バッチ処理）...")

        # バッチサイズごとにChromaDBに追加登録
        for i in range(0, len(documents), batch_size):
            batch_docs = documents[i:i + batch_size]
            batch_meta = metadatas[i:i + batch_size]
            batch_ids = ids[i:i + batch_size]
            
            self.collection.add(
                documents=batch_docs,
                metadatas=batch_meta,
                ids=batch_ids
            )

        print(f"\n✅ 完了! {len(txt_files)} ファイル ({doc_count} チャンク) がローカルDBに保存されました。")

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """
        指定クエリに対する類似テキストチャンクを検索
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )

        formatted_results = []
        if results and results["documents"]:
            docs = results["documents"][0]
            metas = results["metadatas"][0]
            distances = results["distances"][0] if "distances" in results else [0]*len(docs)

            for doc, meta, dist in zip(docs, metas, distances):
                formatted_results.append({
                    "file_name": meta.get("file_name"),
                    "path": meta.get("relative_path"),
                    "chunk_index": meta.get("chunk_index"),
                    "distance": dist,
                    "content": doc
                })

        return formatted_results


# ==========================================
# 実行スクリプトのメイン処理
# ==========================================
if __name__ == "__main__":
    # 1. 17のリポジトリ.txtが保存されているフォルダパスを指定してください
    REPOS_DIR = "./repository_txts"  # <--- ここをご自身のパスに変更してください

    # ダミーフォルダとテスト用のファイルを作成（動作確認用）
    if not os.path.exists(REPOS_DIR):
        os.makedirs(REPOS_DIR, exist_ok=True)
        with open(os.path.join(REPOS_DIR, "mbt55_sample.txt"), "w", encoding="utf-8") as f:
            f.write("""
class MBT55MetabolismCalculator:
    def __init__(self, base_rate: float):
        self.base_rate = base_rate

    def calculate_catalytic_rate(self, substrate_conc: float) -> float:
        '''MBT55の基質濃度から代謝触媒速度を求める計算式'''
        if substrate_conc > 80.0:
            return self.base_rate * 0.2  # ハイパーサイクルフィードバック抑制
        return self.base_rate * (substrate_conc / 10.0)
""")
        print(f"サンプルフォルダ '{REPOS_DIR}' とテストファイルを作成しました。")

    # 2. ビルダーの初期化とインデックス構築
    builder = RepositoryLocalRAGBuilder(
        db_path="./chroma_db",                  # ローカルDBの保存場所
        collection_name="agrix_healthbook_repos" # コレクション名
    )

    # インデックス構築の実行
    builder.build_from_folder(
        repos_folder=REPOS_DIR,
        chunk_size=800,  # チャンク文字数
        overlap=100      # チャンク間のオーバーラップ文字数
    )

    # 3. 検索テスト
    print("\n--- [検索テスト] ---")
    test_query = "MBT55 代謝触媒速度 ハイパーサイクル 80.0"
    search_results = builder.search(test_query, top_k=2)

    for i, res in enumerate(search_results, 1):
        print(f"\n[結果 {i}] 取得元: {res['path']} (距離: {res['distance']:.4f})")
        print("--------------------------------------------------")
        print(res["content"])
        print("--------------------------------------------------")
```

### このスクリプトの特徴と運用ガイド

1. **インフラ・外部サービス完全不要:**
    
    初回実行時に多言語対応の埋め込みモデル（約120MB）が自動ダウンロードされ、ローカルの `./chroma_db` フォルダ内に直接データが蓄積されます。
    
2. **コード構造に合わせた自動チャンク割（スプリッター）:**
    
    単純に文字数でぶった切るのではなく、`class` や `def` 、改行などのセパレータを考慮してコードや解説テキストの区切りの良いところで分割します。
    
3. **二回目以降の高速読み出し:**
    
    インデックス作成完了後は、`builder.search("検索したい機能名やキーワード")` を呼ぶだけで**数ミリ秒〜数10ミリ秒**で17リポジトリ中の該当箇所のみを抽出できます。
    
このスクリプトで抽出した上位数個のコードチャンクをプロンプトに添付することで、AIエージェント（ClaudeやGemini等）に対して**コンテキストを溢れさせずに高密度な入力**を与えることが可能になります。

[[PD4. ローカルの単一フォルダ（SQLiteベース）]]
