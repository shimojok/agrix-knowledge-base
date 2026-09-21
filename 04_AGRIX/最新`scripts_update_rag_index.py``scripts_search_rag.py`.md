インデックス更新スクリプト
`scripts/update_rag_index.py`　
ChromaDB のベクトル検索をテストするスクリプト
`scripts/search_rag.py` 

この２つのスクリプトの最新バージョンを出力してください。
また、数回、変更されていますが、何が変わったのか説明してください。

---

`bionexus-engine` の実環境構造に完全に準拠した、**`scripts/update_rag_index.py`** および **`scripts/search_rag.py`** の最新バージョンです。


### 1. `scripts/update_rag_index.py` (最新バージョン)

**【役割】** Vault内のノートやJSONマトリックスが更新された際に、ChromaDBのインデックスを差分・再構築して最新化するスクリプト。

  
```Python
import os
import sys
import json
import glob
from typing import List, Dict, Any
import chromadb
from chromadb.utils import embedding_functions

# プロジェクトルートのパス解決
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

VAULT_DIR = r"C:\Users\user\agrix-knowledge-base"
CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")
HAMADA_JSON_PATH = os.path.join(VAULT_DIR, "data", "hamada_137_risk_matrix.json")

def get_chroma_client():
    return chromadb.PersistentClient(path=CHROMA_DB_DIR)

def update_index():
    print(f"[INFO] ChromaDB インデックス更新を開始します...")
    print(f"[INFO] Target Vault: {VAULT_DIR}")
    print(f"[INFO] Target ChromaDB: {CHROMA_DB_DIR}")

    client = get_chroma_client()
    embedding_fn = embedding_functions.DefaultEmbeddingFunction()
    collection = client.get_or_create_collection(
        name="bionexus_knowledge",
        embedding_function=embedding_fn
    )

    documents = []
    metadatas = []
    ids = []

    # 1. Hamada 137 Risk Matrix JSON のロード・インデックス化
    if os.path.exists(HAMADA_JSON_PATH):
        with open(HAMADA_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            for idx, record in enumerate(data):
                disease_id = record.get("disease_id", f"DIS-{idx}")
                disease_name = record.get("disease_name", "")
                phytos = ", ".join(record.get("target_phytochemicals", []))
                category = record.get("category", "General")
                
                doc_text = f"疾患ID: {disease_id}\n疾患名: {disease_name}\n分類: {category}\n有効ファイトケミカル: {phytos}"
                
                documents.append(doc_text)
                metadatas.append({
                    "source": "hamada_137_risk_matrix.json",
                    "disease_id": disease_id,
                    "category": category,
                    "mode": "HealthBook"
                })
                ids.append(f"hamada_{disease_id}")
        print(f"[INFO] 浜田137リスクマトリックス ({len(data)}件) を読み込みました。")

    # 2. Vault内のMarkdownノートのロード・インデックス化
    md_files = glob.glob(os.path.join(VAULT_DIR, "**", "*.md"), recursive=True)
    print(f"[INFO] Vault内の Markdown ファイル: {len(md_files)} 件を発見")

    for file_path in md_files:
        rel_path = os.path.relpath(file_path, VAULT_DIR)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if not content.strip():
                    continue

                # ノートを簡易的にセクション/チャンク分割
                chunks = [c.strip() for c in content.split("\n\n") if len(c.strip()) > 20]
                for c_idx, chunk in enumerate(chunks[:10]): # 各ノート上限10チャンク
                    documents.append(chunk)
                    metadatas.append({
                        "source": rel_path,
                        "type": "markdown",
                        "mode": "Integrated"
                    })
                    ids.append(f"doc_{hash(rel_path)}_{c_idx}")
        except Exception as e:
            print(f"[WARN] ファイル読み込みスキップ ({rel_path}): {e}")

    # ChromaDB Upsert実行
    if documents:
        # 大量データの場合はバッチ処理
        batch_size = 100
        for i in range(0, len(documents), batch_size):
            collection.upsert(
                documents=documents[i:i+batch_size],
                metadatas=metadatas[i:i+batch_size],
                ids=ids[i:i+batch_size]
            )
        print(f"[SUCCESS] 計 {len(documents)} 件の文書/チャンクをChromaDBに更新・登録しました。")
    else:
        print("[WARN] 更新対象のドキュメントが見つかりませんでした。")

if __name__ == "__main__":
    update_index()
```

### 2. `scripts/search_rag.py` (最新バージョン)

**【役割】** ChromaDB上のベクトルインデックスに対してクエリを実行し、類似度の高いナレッジを抽出・テスト表示するスクリプト。

```Python
import os
import sys
import argparse
import chromadb
from chromadb.utils import embedding_functions

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")

def search(query_text: str, top_k: int = 3, mode: str = None):
    if not os.path.exists(CHROMA_DB_DIR):
        print(f"[ERROR] ChromaDB が存在しません: {CHROMA_DB_DIR}")
        print("先に `python scripts/update_rag_index.py` を実行してインデックスを作成してください。")
        return

    client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
    embedding_fn = embedding_functions.DefaultEmbeddingFunction()
    
    try:
        collection = client.get_collection(
            name="bionexus_knowledge",
            embedding_function=embedding_fn
        )
    except Exception as e:
        print(f"[ERROR] コレクション 'bionexus_knowledge' の取得に失敗しました: {e}")
        return

    print(f"\n🔍 検索クエリ: '{query_text}' (Top {top_k})")
    if mode:
        print(f"🎯 モードフィルタ: {mode}")

    where_clause = {"mode": mode} if mode else None

    results = collection.query(
        query_texts=[query_text],
        n_results=top_k,
        where=where_clause
    )

    print("\n=== 検索結果 (RAG Output) ===")
    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]
    distances = results.get("distances", [[]])[0] if "distances" in results else [0]*len(docs)

    if not docs:
        print("該当するナレッジが見つかりませんでした。")
        return

    for idx, (doc, meta, dist) in enumerate(zip(docs, metas, distances), 1):
        source = meta.get("source", "Unknown")
        print(f"\n--- [{idx}] Source: {source} (Distance: {dist:.4f}) ---")
        print(doc[:300] + ("..." if len(doc) > 300 else ""))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BioNexus Local RAG Vector Search Test")
    parser.add_argument("query", type=str, help="検索クエリ文字列")
    parser.add_argument("--top_k", type=int, default=3, help="取得件数")
    parser.add_argument("--mode", type=str, choices=["AGRIX", "HealthBook", "PBPE", "Integrated"], help="検索対象モード")

    args = parser.parse_args()
    search(args.query, args.top_k, args.mode)
```

### 変更点と進化の背景

過去のコードから今回出力した最新版にかけて、**具体的に以下の3点が変更・強化**されています。

  

#### 1. パス設計の厳密な実環境固定（パス幻覚・矛盾の防止）

- **旧**: `agrix-knowledge-base` 内にスクリプトを置こうとしたり、`../data/` などのあやふやな相対パスでJSONを参照していました。
    
      
    
- **新**: `BASE_DIR = C:\Users\user\bionexus-engine` を絶対的な基準軸に設定し、Obsidian Vault側のデータ（`C:\Users\user\agrix-knowledge-base\data\hamada_137_risk_matrix.json`）をブレずに明示参照するように修正しました。
    
      
    

#### 2. モード別検索（Tri-Mode RAG）のメタデータ対応

- **旧**: 単にすべてのテキストを混ぜてベクター化するのみで、AGRIX（農業）/ HealthBook（健康）/ PBPE（経済）の文脈切り替えができませんでした。
    
      
    
- **新**: インデックス作成時（`update_rag_index.py`）に `mode` メタデータ（`HealthBook`, `Integrated` 等）を自動付与し、検索時（`search_rag.py`）に `--mode HealthBook` のようにメタデータフィルタ（`where` 句）をかけて意図したドメインから精緻に抽出できるよう設計を強化しました。
    
      
    

#### 3. ベクターDBメタデータの拡張とJSON/Markdown複合対応

- **旧**: Markdownノートのみ、または単一のJSONのみを想定していました。
    
      
    
- **新**: 浜田137疾病リスク表（`hamada_137_risk_matrix.json`）の構造化データと、Obsidian Vault内のMarkdown自由記述ノート（`*.md`）の双方を一度のバッチ処理でキャッチし、1つのChromaDB（`bionexus_knowledge` コレクション）に一元統合・バッチUpsertできるよう拡張しました。