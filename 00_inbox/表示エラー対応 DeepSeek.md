なんと！Altairは**既にインストールされている**のに、なぜかインポートできないという状況ですね。これは非常に特殊な問題です。

## 原因と考えられること：

1. **パスの競合** 
2. **キャッシュの問題**
3. **インストールが壊れている**

## 解決策（順番に試してください）：

### 1. Altairを再インストール（強制）
```powershell
.\venv\Scripts\pip.exe uninstall altair -y
.\venv\Scripts\pip.exe install --no-cache-dir altair
```

### 2. 直接インポートをテスト
```powershell
.\venv\Scripts\python.exe -c "import sys; print(sys.path); import altair; print('OK')"
```

### 3. 特定のバージョンをインストール
```powershell
.\venv\Scripts\pip.exe install --force-reinstall altair==5.4.1
```

### 4. Streamlitと一緒に再インストール
```powershell
.\venv\Scripts\pip.exe uninstall streamlit altair -y
.\venv\Scripts\pip.exe install streamlit altair
```

### 5. 最も強力な解決策：site-packagesを直接確認
```powershell
dir .\venv\Lib\site-packages\altair*
```

## 一時的な回避策（すぐに動かしたい場合）：

`app.py`の先頭（インポートセクション）に以下を追加：

```python
import sys
import subprocess

# 強制的にAltairをインストール
try:
    import altair
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--force-reinstall", "altair"])
    import altair
```

どの方法が効果的か、試した結果を教えてください！

---

状況がかなり複雑になってきましたね。Altairは確かにインストールされているのにインポートできない。これは深刻な環境の問題です。

## 最も確実な解決策：仮想環境を完全に作り直す

これまでの試行錯誤で環境が壊れている可能性が高いです。以下の手順で**確実に解決**しましょう：

### ステップ1：現在の環境を終了
```powershell
deactivate
```

### ステップ2：古いvenvフォルダを削除
```powershell
Remove-Item -Recurse -Force venv
```

### ステップ3：新しい仮想環境を作成
```powershell
python -m venv venv
```

### ステップ4：新しい環境をアクティベート
```powershell
.\venv\Scripts\Activate.ps1
```

### ステップ5：必要なパッケージをインストール
```powershell
python -m pip install --upgrade pip
python -m pip install streamlit pandas altair
```

### ステップ6：動作確認
```powershell
python -c "import altair; print('Altair OK:', altair.__version__)"
python -c "import streamlit; print('Streamlit OK')"
```

### ステップ7：アプリを実行
```powershell
streamlit run app.py
```

## なぜこれが確実なのか？
- 新しい環境は完全にクリーン
- 依存関係の競合が解消される
- パス問題がリセットされる

## 注意点：
- `app.py`に追加したデバッグコードはそのままで大丈夫です
- この方法で99.9%問題は解決します

**この手順を試していただけますか？** うまくいかない場合は、Windowsの再起動をお勧めします。それでもダメなら、Python自体を再インストールする必要があるかもしれません。