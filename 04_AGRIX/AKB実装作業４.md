Obsidian Vault でノートが追加・更新された際に、全件再構築せずに差分だけを ChromaDB に反映するインデックス更新スクリプト (update_rag_index.py) を作成してください。

---

6,400件以上のノート（44,000+チャンク）を毎回フルビルドすると膨大な時間がかかるため、**ファイルの更新日時（タイムスタンプ）または内容のハッシュを管理して差分だけを適用する増量インデックス更新スクリプト**を作成しました。

削除されたファイルや編集されたファイルの旧データを ChromaDB からクリアし、新規・更新ファイルのみを再ベクトル化して反映します。

### `scripts/update_rag_index.py`

`bionexus-engine/scripts/` フォルダ内に **`update_rag_index.py`** を作成し、以下のコードを保存してください。

```Python
import os
import sys
import json
import hashlib
from dotenv import load_dotenv

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

VAULT_DIR = os.getenv("OBSIDIAN_VAULT_PATH", r"C:\Users\user\OneDrive\agrix-knowledge-base")
DB_DIR = "./chroma_db"
CACHE_FILE = "./chroma_db/file_cache.json"
MODEL_NAME = "intfloat/multilingual-e5-small"

def compute_file_hash(filepath):
    """ファイルのMD5ハッシュ値を計算"""
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception:
        return None

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def main():
    print("--- BioNexus Engine: インデックス差分更新 (update_rag_index) ---")

    if not os.path.exists(VAULT_DIR):
        print(f"【エラー】Vault パスが見つかりません: {VAULT_DIR}")
        return

    if not os.path.exists(DB_DIR):
        print(f"【エラー】ChromaDB ({DB_DIR}) が存在しません。初回は build_rag_index.py を実行してください。")
        return

    # 1. 現状の Vault ファイル一覧を取得 & ハッシュチェック
    old_cache = load_cache()
    new_cache = {}

    print("Obsidian Vault のファイル状態をスキャン中...")
    all_files = []
    for root, _, files in os.walk(VAULT_DIR):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                all_files.append(full_path)
                h = compute_file_hash(full_path)
                if h:
                    new_cache[full_path] = h

    # 2. 差分判定 (追加/更新/削除)
    added_or_modified = []
    for filepath, file_hash in new_cache.items():
        if filepath not in old_cache or old_cache[filepath] != file_hash:
            added_or_modified.append(filepath)

    deleted_files = [filepath for filepath in old_cache if filepath not in new_cache]

    print("\n[差分検出結果]")
    print(f" - 追加/更新ファイル: {len(added_or_modified)} 件")
    print(f" - 削除されたファイル: {len(deleted_files)} 件")

    if not added_or_modified and not deleted_files:
        print("\n更新はありません。ChromaDB は最新の状態です。")
        return

    # 3. ChromaDB & Embedding モデル接続
    print("\nEmbedding モデルをロード中...")
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)
    db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    # 4. 削除および更新対象ドキュメントの旧データを ChromaDB から削除
    files_to_purge = deleted_files + added_or_modified
    if files_to_purge:
        print(f"\n古くなったインデックス（{len(files_to_purge)} ファイル分）を消去中...")
        for filepath in files_to_purge:
            try:
                # メタデータの source (ファイルパス) でフィルタリングして削除
                db._collection.delete(where={"source": filepath})
            except Exception as e:
                pass

    # 5. 追加/更新ファイルをテキストロード & チャンク分割
    if added_or_modified:
        print(f"\n差分ファイル ({len(added_or_modified)} 件) の読み込みとベクトル化処理中...")
        documents = []
        for filepath in added_or_modified:
            try:
                loader = TextLoader(filepath, encoding='utf-8')
                docs = loader.load()
                documents.extend(docs)
            except Exception as e:
                print(f"【警告】読み込み失敗: {filepath} ({e})")

        if documents:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=100
            )
            chunks = text_splitter.split_documents(documents)
            
            # e5 モデル用に文章の先頭に "passage: " を付与
            for chunk in chunks:
                chunk.page_content = f"passage: {chunk.page_content}"

            print(f" -> 生成された新規チャンク数: {len(chunks)}")
            print("ChromaDB への保存を開始...")
            
            # バッチ登録
            batch_size = 500
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i + batch_size]
                db.add_documents(batch)
                print(f"   [{i + len(batch)} / {len(chunks)}] チャンク書き込み完了")

    # 6. キャッシュ更新と保存
    save_cache(new_cache)
    print("\n--- 完了: 差分インデックスの更新が正常に完了しました ---")

if __name__ == "__main__":
    main()
```

### 使い方・運用方法

#### 1. 差分更新の実行

Obsidian で新しいノートを追加したり、既存のノートを書き換えた後は、ターミナルで以下を実行するだけです。

  

PowerShell

```
python scripts/update_rag_index.py
```

- **全件再構築なし:** 数万件あってもスキャンは数秒で終わり、変更されたノート（数件〜数十件）だけを数秒でベクトル化して更新します。
    
- **削除検知:** Obsidian 側で消したノートも自動検知し、DB 内の対応チャンクを削除します。
    
### これで完成した BioNexus Engine 全体構成

|**スクリプト**|**役割**|**実行頻度**|
|---|---|---|
|`scripts/build_rag_index.py`|初回データベース全件インデックス構築|初回のみ（完了済み）|
|`scripts/search_rag.py`|単体での高速セマンティック検索テスト|動作確認用|
|`scripts/ask_rag.py`|**メインRAGエンジン**（検索 + ローカルLLM回答生成）|**日常的な質問応答で使用**|
|`scripts/update_rag_index.py`|**Obsidian ノートの追加・編集を反映**|**ノート更新時に随時実行**|

これで完全ローカル・コスト$0の堅牢な BioNexus Engine パイプラインが完成しました！早速 `update_rag_index.py` を実行して動作をテストしてみてください。

---


