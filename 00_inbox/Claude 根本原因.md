python upload_to_pinecone.py

python check_index.py

setx PINECONE_API_KEY "pcsk_42TJLw_CxeRTrkgSYD3TJR4KqH93Qg8yaFLNRiw5AkrrbN1AXEZTbpLPyX46kwzaemXyHm"


全体を確認しました。ファイル読み込みロジックはそのまま活かして、埋め込み部分を`upsert_records`に置き換えます。バッチ処理も追加します(1件ずつ送るより大幅に速くなります)。

```python
import os
import glob
from pinecone import Pinecone

# ----- APIキーは環境変数から読み込む -----
# 事前に PowerShell で以下を実行しておいてください(1回だけでOK):
#   setx PINECONE_API_KEY "あなたの新しいAPIキー"
# 設定後は一度PowerShellを閉じて開き直してください(反映のため)
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
# -------------------------------------------------

VAULT_PATH = r"C:\Users\user\OneDrive\BioNexus_vault"
BATCH_SIZE = 90  # 統合埋め込みインデックスは1リクエストの上限があるため小分けにする

print("[1/4] Pineconeに接続中...")
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("agrix-knowledge-base")
print("[2/4] Pineconeに接続しました。(統合埋め込み: llama-text-embed-v2 を使用)")

print(f"[3/4] Obsidian Vaultを読み込み中: {VAULT_PATH}")
md_files = glob.glob(os.path.join(VAULT_PATH, "**/*.md"), recursive=True)
print(f"ファイル数: {len(md_files)} 個のMarkdownファイルが見つかりました。")

print("[4/4] アップロードを開始します（時間がかかることがあります）...")

batch = []
uploaded_count = 0
skipped = []

def flush_batch(batch):
    """バッチをPineconeに送信する"""
    if not batch:
        return
    index.upsert_records(namespace="__default__", records=batch)

for i, file_path in enumerate(md_files):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if len(content.strip()) < 50:
            continue

        file_name = os.path.basename(file_path)
        folder_name = os.path.basename(os.path.dirname(file_path))

        batch.append({
            "_id": f"file_{i}",
            "text": content[:8000],       # ← embedding対象。Pineconeが自動でベクトル化
            "filename": file_name,
            "folder": folder_name,
            "full_path": file_path,
            "content_preview": content[:500],
        })
        uploaded_count += 1

        if len(batch) >= BATCH_SIZE:
            flush_batch(batch)
            batch = []
            print(f"   {uploaded_count}/{len(md_files)} ファイルをアップロードしました。")

    except Exception as e:
        skipped.append((os.path.basename(file_path), str(e)))
        print(f"   SKIP: {os.path.basename(file_path)} - {e}")

# 残り(端数)のバッチを送信
flush_batch(batch)

print("すべてのファイルのアップロードが完了しました。")
print(f"成功: {uploaded_count} 件 / スキップ: {len(skipped)} 件")
if skipped:
    print("スキップされたファイル:")
    for name, err in skipped:
        print(f"  - {name}: {err}")
print("Pineconeダッシュボードでレコード数を確認してください。")
```

### 主な変更点

1. **`SentenceTransformer`を完全に削除** — ローカルでのベクトル化が不要になり、実行速度・メモリ負荷ともに改善します
2. **`upsert_records`＋バッチ処理** — 1件ずつ送っていた従来より高速。`BATCH_SIZE=90`は余裕を持った値ですが、エラーが出るようなら`50`程度に下げてください
3. **APIキーは環境変数化** — 前回お伝えした通り、貼っていただいたキーは**必ずPineconeダッシュボードでrotateしてください**。新しいキーを発行したら:
    
    ```powershell
    setx PINECONE_API_KEY "新しいキー"
    ```
    
    を実行し、PowerShellを再起動してから使ってください

### 実行前の確認事項

- `full_path`や`content_preview`などメタデータのフィールド名は自由に変更できます(`text`だけは`field_map`の設定上固定です)
- 実行後、`pc.describe_index("agrix-knowledge-base")`で`total_vector_count`を見れば件数が正しく増えているか確認できます

まずはAPIキーのrotate → 環境変数設定を先に済ませてから実行してみてください。エラーが出たらそのログを貼ってもらえれば続けて対応します。

---

「rotateする」とは、**今使っているAPIキーを無効化して、新しいキーを発行し直すこと**です。

### なぜ必要か

さきほどのやり取りで、Kazさんが貼ってくれたコードの中に実際のPinecone APIキー(`pcsk_7PKqJK...`)がそのまま含まれていました。このキーは今この会話のログに残ってしまっています。もし何らかの形でこの会話やコードが第三者の目に触れると、そのキーを使って誰でもKazさんのPineconeアカウント(データの読み書き・削除)にアクセスできてしまいます。

なので「見られてしまった可能性がある古いキー」は無効化し、「誰にも見られていない新しいキー」に差し替える、という対応が安全です。

### 手順(Pineconeの場合)

1. [Pineconeのダッシュボード](https://app.pinecone.io/)にログイン
2. 左側メニューの **API Keys** を開く
3. 今使っているキー(`pcsk_7PKqJK...`で始まるもの)を探し、**Delete**または**Revoke**をクリック
4. 同じ画面で **Create API Key** から新しいキーを発行
5. 発行された新しいキーをコピー
6. PowerShellで環境変数として保存:
    
    ```powershell
    setx PINECONE_API_KEY "ここに新しいキーを貼る"
    ```
    
7. PowerShellのウィンドウを一度閉じて、新しく開き直す(環境変数を反映させるため)
8. 確認:
    
    ```powershell
    echo $env:PINECONE_API_KEY
    ```
    
    新しいキーが表示されればOKです

これで古いキーはもう使えなくなり、新しいキーはコード上に書かれることなく安全に使えます。手順を進めてみて、詰まったところがあれば教えてください。

---

流れはほぼそれで合っていますが、**新しいKeyを直接ファイルにペーストするのは避けてください**。せっかくrotateしても、また同じ問題(キーがコード内に書かれてしまう)が起きてしまいます。

正しい手順はこうです。

### 1. まず新しいKeyを環境変数に設定(ファイルを触る前に)

PowerShellで:

```powershell
setx PINECONE_API_KEY "新しいキーをここに貼る"
```

実行したら、**一度PowerShellのウィンドウを閉じて、新しく開き直してください**(これをしないと環境変数が反映されません)。

新しいPowerShellを開いたら確認:

```powershell
echo $env:PINECONE_API_KEY
```

新しいキーが表示されればOKです。

### 2. `upload_to_pinecone.py`を上書き

さきほど渡したコードをそのまま`upload_to_pinecone.py`に上書き保存してください。このコードは

```python
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
```

という形になっているので、**ファイルの中にキーを書く必要は一切ありません**。環境変数から自動で読み込まれます。

### 3. 実行

```powershell
cd C:\Users\user\Desktop\pinecone_upload
python upload_to_pinecone.py
```

---

まとめると:

- ✅ 新しいKey → `setx`で環境変数に設定(ファイルには書かない)
- ✅ コード → さきほどのバージョンでそのまま上書き
- ✅ 実行 → `python upload_to_pinecone.py`

この順番で進めてみてください。`setx`のところで新しいPowerShellを開き直すのを忘れずに。実行後、エラーが出たらログを貼ってください。

---

原因が分かりました。**「429エラー」と「Batch size exceeds 96」は別々の問題に見えますが、根はひとつです。**

### 根本原因

前回渡したコードのこの部分にバグがあります:

```python
if len(batch) >= BATCH_SIZE:
    flush_batch_with_retry(batch)   # ← ここで失敗すると
    batch = []                       # ← この行が実行されない
    print(...)
```

`flush_batch_with_retry`が429エラーで失敗すると、例外がそのまま投げられ、**`batch = []`が実行されずに終わります**。するとバッチが空にならないまま次のファイルがどんどん追加され続け、バッチが膨れ上がっていきます。

その結果:

1. 最初は429(トークン制限)でエラー
2. バッチがリセットされないまま肥大化し続け、ついに**Pinecone側の1リクエストあたりの上限である96件**を超える
3. `Batch size exceeds 96`エラーになり、さらにリセットされず無限に肥大化 → 以降ずっとSKIP

つまり「一度失敗すると、その後は永遠に失敗し続ける」設計になっていました。ここを直します。

### 修正版

```python
import os
import glob
import time
from pinecone import Pinecone

PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]

VAULT_PATH = r"C:\Users\user\OneDrive\BioNexus_vault"
BATCH_SIZE = 30              # 96件上限に対して余裕を持たせる
SLEEP_BETWEEN_BATCHES = 10.0  # バッチ間の待機秒数
MAX_RETRIES = 6

print("[1/4] Pineconeに接続中...")
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("agrix-knowledge-base")
print("[2/4] Pineconeに接続しました。(統合埋め込み: llama-text-embed-v2 を使用)")

print(f"[3/4] Obsidian Vaultを読み込み中: {VAULT_PATH}")
md_files = glob.glob(os.path.join(VAULT_PATH, "**/*.md"), recursive=True)
print(f"ファイル数: {len(md_files)} 個のMarkdownファイルが見つかりました。")

print("[4/4] アップロードを開始します（時間がかかることがあります）...")

def flush_batch_with_retry(batch):
    """成功したらTrue、リトライ上限に達したらFalseを返す(例外は投げない)"""
    if not batch:
        return True
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            index.upsert_records(namespace="__default__", records=batch)
            return True
        except Exception as e:
            msg = str(e)
            if "429" in msg or "RESOURCE_EXHAUSTED" in msg:
                wait = min(60, 10 * attempt)
                print(f"   [レート制限] {wait}秒待って再試行します ({attempt}/{MAX_RETRIES})")
                time.sleep(wait)
            else:
                print(f"   [バッチ失敗・リトライ対象外] {msg}")
                return False
    print("   [失敗] リトライ上限に達しました。このバッチ分はスキップします。")
    return False

batch = []
uploaded_count = 0
skipped_batches = 0
skipped_files = []

def process_batch_and_reset():
    """バッチを送信し、成功・失敗に関わらず必ず空にする"""
    global batch, uploaded_count, skipped_batches
    ok = flush_batch_with_retry(batch)
    if ok:
        uploaded_count += len(batch)
    else:
        skipped_batches += 1
        for rec in batch:
            skipped_files.append(rec["filename"])
    batch = []  # ← 成功・失敗どちらでも必ずリセット(これが今回の修正の核心)

for i, file_path in enumerate(md_files):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if len(content.strip()) < 50:
            continue

        file_name = os.path.basename(file_path)
        folder_name = os.path.basename(os.path.dirname(file_path))

        batch.append({
            "_id": f"file_{i}",
            "text": content[:8000],
            "filename": file_name,
            "folder": folder_name,
            "full_path": file_path,
            "content_preview": content[:500],
        })

        if len(batch) >= BATCH_SIZE:
            process_batch_and_reset()
            print(f"   進捗: {uploaded_count} 件成功 / {i+1}/{len(md_files)} ファイル処理済み")
            time.sleep(SLEEP_BETWEEN_BATCHES)

    except Exception as e:
        skipped_files.append(os.path.basename(file_path))
        print(f"   SKIP(読み込みエラー): {os.path.basename(file_path)} - {e}")

# 端数バッチ
process_batch_and_reset()

print("すべてのファイルの処理が完了しました。")
print(f"成功: {uploaded_count} 件 / 失敗バッチ: {skipped_batches} 件 / 失敗ファイル数: {len(skipped_files)} 件")
if skipped_files:
    print("失敗したファイル一覧(先頭20件):")
    for name in skipped_files[:20]:
        print(f"  - {name}")
print("Pineconeダッシュボードでレコード数を確認してください。")
```

### 今回の修正ポイント

1. **`batch = []`を必ず実行する** — `process_batch_and_reset()`関数にまとめ、成功・失敗どちらの場合も最後にリセットするようにしました。これがバッチ肥大化を防ぎます。
2. **`BATCH_SIZE = 30`** — 96件の上限からかなり余裕を持たせ、トークン数超過(429)も起きにくくしました。
3. **例外の判定を`Exception`全体に変更** — 前回`PineconeApiException`をimportしていましたが、SDKバージョンによってはクラスパスが違い、正しく捕捉できていなかった可能性があります。文字列に`"429"`が含まれるかで判定する形に変え、確実に拾えるようにしました。
4. **リトライしても失敗した分は記録だけして先に進む** — 4932ファイルの処理が途中で止まらないようにしています。

実行時間の目安として、30件ごとに10秒待つ設定だと、4932ファイル全体で**2〜3時間程度**かかる可能性があります。もし時間がかかりすぎる場合は、Pineconeのダッシュボードでプランをアップグレードしてtokens per minuteの上限を上げる方法もあります。

まずこのバージョンで実行してみて、最初の5分程度のログを見せてもらえますか?「レート制限」の待機メッセージが出てちゃんと成功に転じているか確認したいです。


---

はい、問題ありません。

### 理由

- `_id`は`f"file_{i}"`という形で、`glob.glob()`で取得したファイル一覧の**インデックス番号**から作られています
- ファイル構成(vault内のファイル数や配置)が実行の間に変わっていなければ、同じファイルには毎回同じ`_id`が割り当てられます
- Pineconeの`upsert`(および`upsert_records`)は「同じIDが存在すればデータを上書き」という仕様なので、**再実行しても重複データにはならず、正しく更新されるだけ**です

### 再実行前に一つだけ確認してほしいこと

Vault内でファイルの追加・削除・リネームをしていないか、念のため確認してください。もし途中でファイルを増減させていた場合、`i`の採番がズレて、**同じファイルが別の`_id`になり重複登録される**可能性があります。特に何もしていなければ気にしなくて大丈夫です。

### 再実行コマンド

```powershell
python upload_to_pinecone.py
```

そのまま実行して問題ありません。今回の修正で「一度失敗しても次のバッチはちゃんとリセットされて進む」ようになっているはずなので、最初の5分ほどのログを見せてもらえれば、正常に回復しているか確認します。