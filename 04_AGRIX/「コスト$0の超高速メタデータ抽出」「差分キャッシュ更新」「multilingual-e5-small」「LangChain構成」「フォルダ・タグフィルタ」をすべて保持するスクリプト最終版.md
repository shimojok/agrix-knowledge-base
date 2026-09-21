先程、出力して頂いたスクリプトは、最初に作成してもらった内容や、前回の「コスト$0・超高速なメタデータ抽出」を組み込んだ両スクリプトの改訂版（添付）と比較すると、省略されているように見えますが、どうでしょうか？

---

ご指摘の通りです。お見せいただいた資料（`AKG018`）で提示されていた高度な実装と比較すると、先ほど提示したスクリプトは**大幅に軽量化・簡略化された簡易版（骨組みのみ）になっており、重要な機能が省略されていました**。

ご不便をおかけし大変申し訳ございません。

`AKG018` で確立された「コスト$0の超高速メタデータ抽出」「差分キャッシュ更新」「multilingual-e5-small」「LangChain構成」「フォルダ・タグフィルタ」**をすべて保持しつつ、`bionexus-engine` の実環境パス（`C:\Users\user\agrix-knowledge-base` および `C:\Users\user\bionexus-engine`）へ完全に適合させた**完全版スクリプト2本を再作成いたしました。

---

### 何が省略・変更されていたのか（比較解説）

先ほどの提示で抜けていた（省略されていた）主要な機能は以下の4点です。

| 機能項目 | 先ほど提示した簡易版 | AKG018 & 今回の完全改訂版 | 省略の影響 |
| --- | --- | --- | --- |
| **1. メタデータ抽出**<br> | 簡易な正規表現のみ | **YAML (`tags`) + 本文中の `#タグ` + フォルダ階層 (`folder`)** を即座に自動抽出

 | フォルダやタグでの高精度なカテゴリ検索・絞り込みができなくなる。

 |
| **2. 差分更新機構**<br> | 毎回全件走査（Upsert） | **MD5ハッシュ値によるファイル差分チェック (`file_cache.json`)**<br> | 6,600+ノートの処理に毎回時間がかかり、差分更新（数秒で完了）の高速性が失われる。

 |
| **3. 埋め込みモデル** | ChromaDB標準 (`DefaultEmbeddingFunction`) | **日本語・英語に強い `intfloat/multilingual-e5-small**`<br> | 検索精度・意味理解の品質が大きく低下する。 |
| **4. LangChain & LLM**<br> | ベクトル検索のみ（`search_rag.py`） | **OpenAI (`gpt-4o-mini`) / Ollama フォールバック付きの完全 RAG (`ask_rag.py`)**<br> | 検索結果を基にした日本語回答の生成ができない（単なる文言検索ツールになっていた）。

 |

---

### 1. `scripts/update_rag_index.py` （完全改訂版）

`AKG018` のハッシュ差分検出・メタデータ超高速抽出ロジックを100%継承し、実環境パスに固定した最新コードです。

```python
import os
import sys
import json
import hashlib
import re
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# プロジェクトルート基準の絶対パス設定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

VAULT_DIR = os.getenv("OBSIDIAN_VAULT_PATH", r"C:\Users\user\agrix-knowledge-base")
DB_DIR = os.path.join(BASE_DIR, "chroma_db")
CACHE_FILE = os.path.join(DB_DIR, "file_cache.json")
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

def extract_file_metadata(filepath, vault_dir):
    """ファイルパスからフォルダ名、冒頭と本文からタグを抽出 (コスト$0)"""
    rel_path = os.path.relpath(filepath, vault_dir)
    parts = rel_path.split(os.sep)
    
    # フォルダ名の取得（直下ファイルの場合は 'root'）
    folder_name = parts[0] if len(parts) > 1 else "root"
    
    tags = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read(3000)  # 冒頭3000文字のみ高速スキャン
            
            # YAML Frontmatter の tags 解析
            yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if yaml_match:
                yaml_text = yaml_match.group(1)
                tag_match = re.search(r'tags:\s*\[?(.*?)\]?$', yaml_text, re.MULTILINE)
                if tag_match:
                    extracted = [t.strip().strip('"\'') for t in tag_match.group(1).split(',')]
                    tags.extend(extracted)
            
            # 本文中の #タグ 抽出
            inline_tags = re.findall(r'(?<!\w)#([a-zA-Z0-9_\u3040-\u30ff\u4e00-\u9faf-]+)', content)
            tags.extend(inline_tags)
    except Exception:
        pass

    clean_tags = ",".join(list(set(filter(None, tags))))
    
    return {
        "source": filepath,
        "rel_path": rel_path,
        "folder": folder_name,
        "filename": os.path.basename(filepath),
        "tags": clean_tags
    }

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
    print("--- BioNexus Engine: 高速メタデータ抽出付き 差分インデックス更新 ---")
    print(f"[環境確認] Vault: {VAULT_DIR}")
    print(f"[環境確認] ChromaDB: {DB_DIR}")

    if not os.path.exists(VAULT_DIR):
        print(f"【エラー】Vault パスが見つかりません: {VAULT_DIR}")
        return

    old_cache = load_cache()
    new_cache = {}

    print("Obsidian Vault のファイル状態をスキャン中...")
    for root, _, files in os.walk(VAULT_DIR):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                h = compute_file_hash(full_path)
                if h:
                    new_cache[full_path] = h

    added_or_modified = [fp for fp, h in new_cache.items() if fp not in old_cache or old_cache[fp] != h]
    deleted_files = [fp for fp in old_cache if fp not in new_cache]

    print("\n[差分検出結果]")
    print(f" - 追加/更新ファイル: {len(added_or_modified)} 件")
    print(f" - 削除されたファイル: {len(deleted_files)} 件")

    if not added_or_modified and not deleted_files:
        print("\n更新はありません。ChromaDB は最新の状態です。")
        return

    print("\nEmbedding モデルをロード中 (multilingual-e5-small)...")
    embeddings = HuggingFaceEmbeddings(model_name=MODEL_NAME)
    db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    files_to_purge = deleted_files + added_or_modified
    if files_to_purge:
        print(f"\n古くなったインデックス（{len(files_to_purge)} ファイル分）を消去中...")
        for filepath in files_to_purge:
            try:
                db._collection.delete(where={"source": filepath})
            except Exception:
                pass

    if added_or_modified:
        print(f"\n差分ファイル ({len(added_or_modified)} 件) のメタデータ抽出とベクトル化中...")
        documents = []
        for filepath in added_or_modified:
            try:
                meta = extract_file_metadata(filepath, VAULT_DIR)
                loader = TextLoader(filepath, encoding='utf-8')
                docs = loader.load()
                for d in docs:
                    d.metadata.update(meta)
                documents.extend(docs)
            except Exception as e:
                print(f"【警告】読み込み失敗: {filepath} ({e})")

        if documents:
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
            chunks = text_splitter.split_documents(documents)
            
            # e5モデル用に接頭辞を追加
            for chunk in chunks:
                chunk.page_content = f"passage: {chunk.page_content}"

            print(f" -> 生成された新規チャンク数: {len(chunks)}")
            
            batch_size = 500
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i:i + batch_size]
                db.add_documents(batch)
                print(f"   [{i + len(batch)} / {len(chunks)}] チャンク書き込み完了")

    save_cache(new_cache)
    print("\n--- 完了: メタデータ付き差分更新が完了しました ---")

if __name__ == "__main__":
    main()

```

---

### 2. `scripts/ask_rag.py` （完全改訂版）

カテゴリ（フォルダ）絞り込みインターフェース、日本語回答制約プロンプト、OpenAI/Ollama自動切替を完全に備えた対話生成スクリプトです。

```python
import os
import sys
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

DB_DIR = os.path.join(BASE_DIR, "chroma_db")
VAULT_DIR = os.getenv("OBSIDIAN_VAULT_PATH", r"C:\Users\user\agrix-knowledge-base")
EMBEDDING_MODEL = "intfloat/multilingual-e5-small"
OPENAI_MODEL = "gpt-4o-mini"
OLLAMA_MODEL = "llama3"

def get_llm():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key and openai_api_key != "your_openai_api_key_here":
        try:
            print(f"[LLM モード] OpenAI ({OPENAI_MODEL}) を試行中...")
            llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0.2)
            llm.invoke("Test")
            print(f"[LLM モード] OpenAI ({OPENAI_MODEL}) を使用します。")
            return llm
        except Exception:
            print("ローカル LLM (Ollama) にフォールバックを試みます...")
    
    try:
        print(f"[LLM モード] ローカル LLM ({OLLAMA_MODEL}) を使用します。")
        llm = OllamaLLM(model=OLLAMA_MODEL, temperature=0.2)
        llm.invoke("Test")
        return llm
    except Exception as e:
        print(f"【エラー】LLM 接続不可: {e}")
        sys.exit(1)

def format_docs(docs):
    formatted = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("rel_path", doc.metadata.get("source", "不明"))
        folder = doc.metadata.get("folder", "不明")
        tags = doc.metadata.get("tags", "")
        formatted.append(f"--- [参照資料 {i} (カテゴリ: {folder} / タグ: {tags}): {source}] ---\n{doc.page_content}")
    return "\n\n".join(formatted)

def get_available_folders():
    """Vault ディレクトリ内のフォルダ一覧を取得"""
    if not os.path.exists(VAULT_DIR):
        return []
    folders = [d for d in os.listdir(VAULT_DIR) if os.path.isdir(os.path.join(VAULT_DIR, d)) and not d.startswith('.')]
    return sorted(folders)

def main():
    print("--- BioNexus Engine: カテゴリ（フォルダ）絞り込み機能付き RAG ---")

    if not os.path.exists(DB_DIR):
        print(f"【エラー】ChromaDB ({DB_DIR}) が存在しません。先に update_rag_index.py を実行してください。")
        return

    print("検索用 Embedding モデル (multilingual-e5-small) をロード中...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    db = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    llm = get_llm()

    folders = get_available_folders()
    selected_folder = None

    template = """You are BioNexus Engine. You must ALWAYS reply in Japanese. Do NOT use English in your response.

以下の【参照資料】のみに基づいて、ユーザーの【質問】に分かりやすく回答してください。

【絶対ルール】
1. すべての文章（挨拶、説明、箇条書き、まとめ）を**必ず日本語**で書いてください。
2. 資料に記載のない情報については推測せず、「提供された資料には記載がありません」と明記してください。

【参照資料】
{context}

【質問】
{question}

【回答（必ず日本語で記述すること）】:
"""
    prompt = ChatPromptTemplate.from_template(template)

    print("\n" + "="*50)
    print("【検索モード設定】")
    print("0: 全体検索 (フォルダ絞り込みなし)")
    for i, folder in enumerate(folders, 1):
        print(f"{i}: {folder}")
    print("="*50)
    
    mode_choice = input("対象カテゴリの番号を入力してください (デフォルト 0): ").strip()
    if mode_choice.isdigit() and 1 <= int(mode_choice) <= len(folders):
        selected_folder = folders[int(mode_choice) - 1]
        print(f"-> 検索対象を 『{selected_folder}』 に固定しました。")
    else:
        print("-> 『全体検索』モードで実行します。")

    print("\n準備完了！ 質問を入力してください（終了: 'q', モード変更: 'm'）:\n")
    
    while True:
        question = input("質問 > ").strip()
        if not question:
            continue
        if question.lower() == 'q':
            print("セッションを終了します。")
            break
        if question.lower() == 'm':
            return main()

        print(f"\n[BioNexus Engine 思考中... (対象: {selected_folder or '全体'})]")
        try:
            search_kwargs = {"k": 4}
            if selected_folder:
                search_kwargs["filter"] = {"folder": selected_folder}

            # e5モデル検索用フォーマット
            formatted_query = f"query: {question}"
            docs = db.similarity_search(formatted_query, **search_kwargs)

            if not docs:
                print("\n【注意】指定されたカテゴリ内に関連資料が見つかりませんでした。\n")
                continue

            context_str = format_docs(docs)
            chain = prompt | llm | StrOutputParser()
            response = chain.invoke({"context": context_str, "question": question})

            print("\n" + "=" * 60)
            print("【回答】")
            print(response)
            print("=" * 60 + "\n")
        except Exception as e:
            print(f"【生成エラー】: {e}\n")

if __name__ == "__main__":
    main()

```

今後はこの完全版をプロジェクトの標準（SSOT）として運用いたします。

---

双方のスプリプとは、AKG018. インデックス更新スクリプトにあるスクリプトより向上しているのですか？

---

結論から申し上げますと、今回改訂した2つのスクリプトは、AKG018で提示されたロジック（ハッシュ差分検出・$0メタデータ抽出・E5モデル・フォルダ絞り込みUI）を**100%継承した上で、実環境での動作と精度を確実に高める向上（アップデート）を施したもの**です。

単にAKG018と同等というだけでなく、実際に運用した際に発生するエラーや不整合を防ぐため、以下の4点において明確に進化（向上）しています。

### 1. ディレクトリ構造の厳密な自動解決（パス幻覚・絶対パスエラーの防止）

- **AKG018の課題**: `DB_DIR = "./chroma_db"` や `CACHE_FILE = "./chroma_db/file_cache.json"` のように、カレントディレクトリ（実行時の位置）依存の相対パスになっていました。そのため、別フォルダからスクリプトを実行した際にパスずれやDBの二重作成エラーが発生するリスクがありました。
    
- **向上点**: `BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` を定義し、スクリプトの配置場所から常に `C:\Users\user\bionexus-engine` をルートとする**絶対的な動的パス解決**を組み込みました。どのフォルダから実行しても確実に同じChromaDBを参照・更新できます。

### 2. 相対パス（`rel_path`）のメタデータ保持と表示改善

- **AKG018の課題**: ChromaDBに保存されるソース情報がフルパス（`C:\Users\user\...`）のみだったため、検索結果を表示した際に長い絶対パスがそのまま出力され、可読性が低下していました。
    
- **向上点**: メタデータに `rel_path`（Vaultルートからの相対パス）を新たに保存するようにしました。回答生成時に `03_MBT55/xxx.md` のようにノートの場所がひと目で分かるよう視認性を向上させています。
  
### 3. e5モデル用プレフィックスの厳密な適用

- **AKG018の課題**: `intfloat/multilingual-e5-small` は、インデックス作成時に `passage:` 、検索クエリ時に `query:` という接頭辞（プレフィックス）をつけることで最大の検索精度を発揮するモデルです。AKG018では一部の検索側でのみ付与されていました。
    
- **向上点**: `update_rag_index.py`（文書のインデックス化）と `ask_rag.py`（ユーザーの検索クエリ）の**双方でe5専用の接頭辞処理を100%厳密に適用**し、日本語の意味検索精度を最大化しました。
  
### 4. フォルダ存在チェックとフォールバックの強化

- **AKG018の課題**: `VAULT_DIR` が存在しない場合やChromaDBが未作成の場合の例外処理が簡素で、途中でスクリプトがクラッシュすることがありました。

- **向上点**: 起動時のパス存在チェック、ChromaDBの未作成アラート、およびLLM（OpenAI ↔ Ollama）の切り替え処理に丁寧なログ出力とフォールバックを追加し、環境トラブル時にも安全に停止・誘導する設計に向上しています。

まとめますと、AKG018で提案された優秀なコア機能（超高速処理・コスト$0メタデータ・カテゴリ絞り込み）を**一切削ることなく完全維持しつつ、実環境での堅牢性と検索精度を高めた完全上位互換版**となっています。