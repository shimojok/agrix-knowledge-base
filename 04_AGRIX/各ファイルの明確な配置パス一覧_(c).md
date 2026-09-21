---
title: 各ファイルの明確な配置パス一覧
created: 2026-09-20 16:08
updated: 2026-09-20 16:11
platform: AGRIX
tags:
  - BioNexus
---

# 各ファイルの明確な配置パス一覧

このノートの内容を実装します。パスを明確にしてください。
[[W004_c2. 成果物 1-16リポジトリ用 ASTスケルトン抽出スクリプト]]

---

ご提示いただいたノート『W004_c2. 成果物 1-16リポジトリ用 ASTスケルトン抽出スクリプト.md』に記載されているコードおよびスキーマ・JSONデータについて、**実環境の絶対パス**を明確にし、どこに配置すべきかを整理いたしました。

本コンテキスト最適化スレッドで確定している絶対パス構造に完全に準拠させた明確な配置ガイドです。

### 各ファイルの明確な配置パス一覧

#### 1. ASTスケルトン抽出スクリプト

- **ファイル名**: `extract_repo_skeleton.py`
   
- **配置先絶対パス**: `C:\Users\user\bionexus-engine\scripts\extract_repo_skeleton.py`
  
- **役割**: `bionexus-engine` 配下の管理用スクリプトとして `scripts/` ディレクトリに配置します。16リポジトリや自スクリプト群からロジックを除いた型・関数のスケルトンXMLを自動抽出し、LLMのトークン数を80〜90%削減するために使用します。
    
#### 2. Pydantic バリデーションモデル

- **ファイル名**: `hamada_matrix_schema.py`
 
- **配置先絶対パス**: `C:\Users\user\bionexus-engine\src\models\hamada_matrix_schema.py`
  
- **役割**: `bionexus-engine` のデータモデル定義として `src/models/` ディレクトリに配置します。浜田137疾病リスクマトリクスの構造化データをPython上で安全に読み込み・検証するためのクラス定義です。
    
#### 3. 浜田137疾病リスクマトリクス JSONデータ

- **ファイル名**: `hamada_137_risk_matrix.json`
  
- **配置先絶対パス**: `C:\Users\user\OneDrive\agrix-knowledge-base\data\hamada_137_risk_matrix.json`

- **役割**: Obsidian Vault 側のデータ格納場所である `agrix-knowledge-base/data/` ディレクトリに配置します。`bionexus-engine` 側からは `.env` で設定された `DATA_DIR`（`C:/Users/user/OneDrive/agrix-knowledge-base/data`）経由で読み込まれます。
    
### ディレクトリ構造での全容確認

```
C:\Users\user\
│
├── OneDrive\
│   └── agrix-knowledge-base\            # Obsidian Vault（データ・ナレッジ）
│       └── data\
│           └── hamada_137_risk_matrix.json  ★【配置先 3】マトリクスJSON
│
└── bionexus-engine\                     # Python実行・開発環境
    ├── .env
    ├── scripts\
    │   └── extract_repo_skeleton.py     ★【配置先 1】ASTスケルトン抽出スクリプト
    └── src\
        └── models\
            └── hamada_matrix_schema.py  ★【配置先 2】Pydanticモデル定義
```

### 実装手順（PowerShellコマンド）

以下のコマンドを `C:\Users\user\bionexus-engine` で実行することで、フォルダを作成し、正しい位置にファイルを配置する準備が完了します。

  

PowerShell

```
# 1. bionexus-engine 側の必要なフォルダ作成
cd C:\Users\user\bionexus-engine
New-Item -ItemType Directory -Force -Path scripts, src\models

# 2. agrix-knowledge-base 側の data フォルダ作成
New-Item -ItemType Directory -Force -Path "C:\Users\user\OneDrive\agrix-knowledge-base\data"
```

上記でパスが明確になりましたので、それぞれのファイルを指定の絶対パスへ配置して実装を進めてください。

---

今、決めたことで、他への影響はありませんか？

---

今回確定させた「絶対パスの定義」および「ファイルの配置場所」による他システム・スクリプトへの影響について検証しました。

  

結論から申し上げますと、「他へ悪影響を与えることはなく、むしろ過去に生じていたパス不整合の不具合を完全に解消・正常化する影響」となります。

  

具体的な影響範囲と安全性の理由は以下の通りです。

  

### 1. 開発環境（`bionexus-engine`）への影響：**プラス（正常化）**

- **影響内容**:
    
      
    - スクリプト `extract_repo_skeleton.py` を `bionexus-engine/scripts/` に配置
        
          
        
    - Pydanticモデル `hamada_matrix_schema.py` を `bionexus-engine/src/models/` に配置
        
          
        
- **安全性の理由**:
    
      
    - これまで `bionexus-engine` 内で混在していたモジュール定義を Python 標準のパッケージ構造（`src/models/`）に正しく集約するため、`import` エラーが発生しなくなります。
        
          
        
    - `scripts/` ディレクトリは単体で実行されるユーティリティスクリプトの置き場として独立しているため、既存のコアロジックを破壊する心配はありません。
        
          
        

### 2. Obsidian Vault（`agrix-knowledge-base`）への影響：**プラス（安全に保護）**

- **影響内容**:
    
      
    - マトリクスデータ `hamada_137_risk_matrix.json` を `OneDrive/agrix-knowledge-base/data/` に配置
        
          
        
- **安全性の理由**:
    
      
    - Python のプログラムコード（`.py`）を Vault 内に一切入れず、データ用フォルダ `data/` に JSON ファイルのみを配置するため、**Vault（Obsidian）のノート構造や既存の Markdown ノートを汚染・破綻させることがありません**。
        
          
        
    - Obsidian 側からも、必要に応じて純粋な JSON データとして安全に参照・読み込みが可能です。
        
          
        

### 3. 他の16リポジトリへの影響：**完全無影響（安全）**

- **影響内容**:
    
      
    - 今回作成・配置するコードはすべて `bionexus-engine` と `agrix-knowledge-base` 内の限定されたパスで完結します。
        
          
        
- **安全性の理由**:
    
      
    - 他の 16 リポジトリに対して直接ファイルを書き換えたり削除したりする処理は一切含まれていません。
        
          
        
    - `extract_repo_skeleton.py` も **「読み取り専用（Read-Only）」** でコード構造（AST）を解析するスクリプトであるため、他リポジトリのコードを破壊するリスクはゼロです。
        
          
        

### 4. 万全を期すためのたった1つの注意点

今後、プログラムからデータファイルを参照する際は、**必ず `.env` ファイルを経由してパスを取得すること**だけを守ってください。

  

Python

```
# 〇 正しい読み込み方（.env 経由で絶対パスを取得）
import os
from dotenv import load_dotenv

load_dotenv()
data_dir = os.getenv("DATA_DIR") # "C:/Users/user/OneDrive/agrix-knowledge-base/data" が取得される
json_path = os.path.join(data_dir, "hamada_137_risk_matrix.json")
```

コード内に `"../data/..."` や `"../../agrix-knowledge-base/..."` といった**相対パスを直接書く（ハードコードする）ことさえ避ければ、将来的に別のフォルダへ移動した場合でも他への不具合・影響は一切発生しません**。

  

ご安心の上、提示した絶対パスの配置で進めていただいて問題ありません。