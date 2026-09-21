

---

`AKG019`（統合型対話＆メタボリック・シミュレーション Web システム）で求められていた Streamlit Web UI アプリケーションのコードですね。

先ほど確定させた最新の `update_rag_index.py` や `ask_rag.py` と同じく、**実環境の絶対パス基準**（`BASE_DIR = C:\Users\user\bionexus-engine`）で動作し、パスの混乱や読み込みエラーが発生しないよう明確に配置パスを定義した完全版コードを出力します。

### 保存場所とファイル構造の明確化

このコードは、`bionexus-engine` 配下の `app.py` として配置・保存してください。

```Plaintext
C:\Users\user\
├── agrix-knowledge-base/          # Obsidian Vault (SSOT)
│   └── data/                      # 共通JSONデータ
│       └── hamada_137_risk_matrix.json[cite: 3]
│
└── bionexus-engine/               # ★ Python実行環境[cite: 3]
    ├── app.py                     # ★【今回出力するコード】(Web UIメインスクリプト)[cite: 3]
    ├── bionexus_sim_engine.py     # 代謝・SOCシミュレーションエンジン[cite: 3]
    ├── chroma_db/                 # ベクトルデータベース[cite: 3]
    └── scripts/                   # 各種 CLI スクリプト[cite: 3]
        ├── update_rag_index.py[cite: 3]
        └── ask_rag.py[cite: 3]
```

### `app.py` (最新完全版)

**【配置パス】**: `C:\Users\user\bionexus-engine\app.py`　済
[cite: 3]

```Python
import os
import sys
import json
import streamlit as st
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. パス構成の明確化（絶対基準設定）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# 接続パスの確定
VAULT_DIR = os.getenv("OBSIDIAN_VAULT_PATH", r"C:\Users\user\agrix-knowledge-base")
DB_DIR = os.path.join(BASE_DIR, "chroma_db")
HAMADA_JSON_PATH = os.path.join(VAULT_DIR, "data", "hamada_137_risk_matrix.json")

EMBEDDING_MODEL = "intfloat/multilingual-e5-small"
OPENAI_MODEL = "gpt-4o-mini"
OLLAMA_MODEL = "llama3"

load_dotenv()

# Streamlit ページ基本設定
st.set_page_config(
    page_title="BioNexus Engine - Integrated Web System",
    page_icon="🧬",
    layout="wide"
)

# --- バックエンド初期化関数群 ---

@st.cache_resource
def load_vector_db():
    """ChromaDB ベクトルデータベースのロード"""
    if not os.path.exists(DB_DIR):
        return None
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

def get_llm():
    """OpenAI / Ollama LLM の自動判別ロード"""
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key and openai_api_key != "your_openai_api_key_here":
        try:
            llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0.2)
            llm.invoke("Test")
            return llm, f"OpenAI ({OPENAI_MODEL})"
        except Exception:
            pass
    try:
        llm = OllamaLLM(model=OLLAMA_MODEL, temperature=0.2)
        llm.invoke("Test")
        return llm, f"Local Ollama ({OLLAMA_MODEL})"
    except Exception as e:
        return None, f"エラー: LLMに接続できません ({e})"

def get_available_folders():
    """Vault 内のフォルダ一覧取得"""
    if not os.path.exists(VAULT_DIR):
        return []
    folders = [d for d in os.listdir(VAULT_DIR) if os.path.isdir(os.path.join(VAULT_DIR, d)) and not d.startswith('.')]
    return sorted(folders)

def load_hamada_matrix():
    """浜田137リスクマトリックスのロード"""
    if os.path.exists(HAMADA_JSON_PATH):
        try:
            with open(HAMADA_JSON_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return None
    return None

# --- UI レイアウト構成 ---

st.title("🧬 BioNexus Engine Web Dashboard")
st.caption("AGRIX / HealthBook / PBPE Marketplace 統合知能基盤 Dashboard")

# サイドバー構成
st.sidebar.header("⚙️ システム設定・制御")

# 1. 動作環境ステータス表示
db = load_vector_db()
if db:
    st.sidebar.success("✅ ChromaDB: 接続完了")
else:
    st.sidebar.error("❌ ChromaDB: 未構築 (update_rag_index.py を実行してください)")

llm, llm_status = get_llm()
st.sidebar.info(f"🤖 LLM Engine: {llm_status}")

st.sidebar.markdown("---")

# 2. RAG 検索範囲（モード・カテゴリ）設定
st.sidebar.subheader("🎯 RAG 検索範囲指定")
folders = get_available_folders()
category_options = ["全体検索 (絞り込みなし)"] + folders
selected_category = st.sidebar.selectbox("対象カテゴリ (Vault Folder)", category_options)

target_folder = None if selected_category == "全体検索 (絞り込みなし)" else selected_category

# メイン画面のタブ設定
tab1, tab2, tab3 = st.tabs(["💬 RAG 統合対話", "📊 浜田137リスク解析", "🧪 代謝・SOCシミュレーション"])

# --- TAB 1: RAG 統合対話 ---
with tab1:
    st.header("💬 Knowledge Base RAG Chat")
    st.write(f"現在の検索対象: **{selected_category}**")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt_text := st.chat_input("質問を入力してください (例: MBT55の4つの機能ブロックとは？)"):
        st.session_state.messages.append({"role": "user", "content": prompt_text})
        with st.chat_message("user"):
            st.markdown(prompt_text)

        with st.chat_message("assistant"):
            if not db or not llm:
                st.error("システムが正しく初期化されていないため回答できません。")
            else:
                with st.spinner("Vault 検索 & 回答生成中..."):
                    search_kwargs = {"k": 4}
                    if target_folder:
                        search_kwargs["filter"] = {"folder": target_folder}

                    formatted_query = f"query: {prompt_text}"
                    docs = db.similarity_search(formatted_query, **search_kwargs)

                    if not docs:
                        res_text = "指定されたカテゴリ内に関連する情報が見つかりませんでした。"
                        st.markdown(res_text)
                    else:
                        # コンテキスト構築
                        formatted_docs = []
                        for i, d in enumerate(docs, 1):
                            src = d.metadata.get("rel_path", d.metadata.get("source", "不明"))
                            fld = d.metadata.get("folder", "不明")
                            formatted_docs.append(f"--- [参照資料 {i} ({fld}): {src}] ---\n{d.page_content}")
                        
                        context_str = "\n\n".join(formatted_docs)

                        template = """You are BioNexus Engine. You must ALWAYS reply in Japanese.

以下の【参照資料】のみに基づいて、ユーザーの【質問】に分かりやすく回答してください。

【参照資料】
{context}

【質問】
{question}

【回答（必ず日本語で記述）】:
"""
                        prompt = ChatPromptTemplate.from_template(template)
                        chain = prompt | llm | StrOutputParser()
                        res_text = chain.invoke({"context": context_str, "question": prompt_text})

                        st.markdown(res_text)
                        
                        with st.expander("📚 参照ノート・根拠ソースを表示"):
                            for doc in docs:
                                st.write(f"- **{doc.metadata.get('rel_path', 'ソース不明')}** (Folder: {doc.metadata.get('folder', '-')})")

                    st.session_state.messages.append({"role": "assistant", "content": res_text})

# --- TAB 2: 浜田137リスク解析 ---
with tab2:
    st.header("📊 浜田137疾病リスク・ファイトケミカルマトリックス")
    matrix_data = load_hamada_matrix()

    if not matrix_data:
        st.warning(f"データファイルが見つかりません: `{HAMADA_JSON_PATH}`")
    else:
        st.success(f"浜田137リスクマトリックス ({len(matrix_data)}件) を読み込みました。")
        search_disease = st.text_input("🔍 疾病名またはファイトケミカルで検索", "")

        filtered_data = []
        for item in matrix_data:
            d_name = item.get("disease_name", "")
            phytos = " ".join(item.get("target_phytochemicals", []))
            if search_disease.lower() in d_name.lower() or search_disease.lower() in phytos.lower():
                filtered_data.append(item)

        st.dataframe(filtered_data, use_container_width=True)

# --- TAB 3: 代謝・SOCシミュレーション ---
with tab3:
    st.header("🧪 BioNexus 微生物代謝 & 土壌有機炭素 (SOC) シミュレータ")
    st.write("有機物投入量 $I$ および MBT55 活性化係数 $\eta$ による SOC 動態推移モデル")

    col1, col2 = st.columns(2)
    with col1:
        input_I = st.slider("有機物投入量 I (t-C/ha/年)", 0.0, 10.0, 3.5, 0.1)
        input_kd = st.slider("SOC 分解率 k_d (1/年)", 0.01, 0.10, 0.03, 0.005)
    with col2:
        input_eta = st.slider("MBT55 腐植化促進率 η", 0.1, 1.0, 0.4, 0.05)
        years = st.slider("シミュレーション期間 (年)", 5, 50, 20, 5)

    # 簡易ODEオイラー法計算
    C_s = 30.0  # 初期SOC (t-C/ha)
    timeline = [0]
    soc_values = [C_s]

    for y in range(1, years + 1):
        dCs_dt = input_I - (input_kd * C_s) + (input_I * input_eta * 0.2)
        C_s += dCs_dt
        timeline.append(y)
        soc_values.append(round(C_s, 2))

    import pandas as pd
    df_sim = pd.DataFrame({"経過年数": timeline, "SOC蓄積量 (t-C/ha)": soc_values})
    
    st.line_chart(df_sim.set_index("経過年数"))
    st.metric("最終到達 SOC 蓄積量", f"{soc_values[-1]} t-C/ha", delta=f"{round(soc_values[-1] - 30.0, 2)} t-C/ha")
```

### アプリケーションの起動手順

1. **ターミナル（PowerShell等）を開き、`bionexus-engine` ディレクトリに移動**
    [cite: 3]
    
    ```PowerShell
    cd C:\Users\user\bionexus-engine
    ```
    
2. **Streamlit アプリを起動**
    
    ```PowerShell
    streamlit run app.py
    ```
    
3. **ブラウザで確認**
    
    - 自動的にブラウザが開きます（通常は `http://localhost:8501`）。
        
    - サイドバーでフォルダを絞り込んだ対話（Tab 1）、137疾病マトリックスの検索（Tab 2）、SOC蓄積モデルの可視化（Tab 3）が一体となって動作します。

