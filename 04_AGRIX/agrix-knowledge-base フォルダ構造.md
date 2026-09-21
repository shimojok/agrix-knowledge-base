```Plaintext
/agrix-knowledge-base/         ← 【Obsidian Vault / ナレッジ専用リポジトリ】
    ├── 00_inbox/
    ├── 01_Planetary_Problems/
    ├── ...
    ├── 11_AI_Development/
    ├── dailynote/
    └── slides/

/bionexus-engine/              ← 【システム開発用リポジトリ（新規作成）】
    ├── src/
    │   ├── rag/
    │   │   └── rag_engine.py      ← RAG検索エンジン
    │   ├── engines/
    │   │   ├── pbpe_engine.py    ← PBPE金融モデル（確定計算）
    │   │   ├── mbt_engine.py     ← MBT55モデル（確定計算）
    │   │   └── ghg_engine.py     ← GHG削減モデル（確定計算）
    │   └── data/
    │       └── canonical_data.json ← 数値テーブル
    ├── ui/                        ← ダッシュボード (Streamlit / Azure用)
    ├── chroma_db/                 ← 生成されたベクトルDB (Git管理対象外)
    ├── scripts/
    │   └── build_rag_index.py    ← Vault読み込み・インデックス生成スクリプト
    └── requirements.txt
```

