質問👉下記のデータ入出力フォーマット利用の、具体的は方法を教えてください。

- **Contract-First (TypeScript / Python Protocol 型の採用):**
    
    データ構造の伝達にはJSONではなく、**TypeScriptのinterface**または**PythonのPydanticモデル＋Docstring**を利用します。型定義の中に計算ロジックや制約条件をコメントとして埋め込むことで、AIが省略しにくくなります。
    
- **Mermaid.js + 逐条解説プロトコル:**
    
    図解データとしてMermaidコードを出力させると同時に、「図内の全ノード（A, B, C...）について、それぞれの内部処理ステップを文章で全て書き出せ」というルールをセットで課します。
    
---

回答👉

**Contract-First**および**Mermaid.js + 逐条解説プロトコル**の具体的な導入手順と、AIエージェントに指示を出すためのプロンプトテンプレートです。

この2つのフォーマットを導入することで、AIがよく行う「構造（骨組み）だけ作って中身を `// TODO` や要約で省略する行為」を物理的に封じ込めることができます。

### 1. Contract-First（Python Pydantic / TypeScript Protocol）の具体的手法

JSONは「値のデータ型」しか表現できませんが、PythonのPydanticモデル（またはTypeScriptのinterface）を使うと、**「型の制約」「ドメインロジック」「バリデーション（評価式）」をコード自体に埋め込む**ことができます。

#### ① ドメインモデル定義の作成例（AIへ渡す「型契約書」）

例えば、MBT55の代謝計算モジュールやハイパーサイクルの状態遷移を、次のようなファイル（`contracts/mbt55_metabolism.py`）としてあらかじめ定義・固定します。


```Python
from pydantic import BaseModel, Field, field_validator
from typing import List, Dict, Optional

class MetaboliteRateContract(BaseModel):
    """
    [MBT55 代謝反応速度計算プロトコル]
    このモデルは、ハイパーサイクル内での基質濃度変化と代謝触媒効率を厳密に計算するための契約です。
    """
    substrate_id: str = Field(..., description="基質識別子 (例: 'SUB_001')")
    concentration: float = Field(..., ge=0.0, le=100.0, description="基質濃度 (mM)。0〜100の範囲内必須")
    inhibition_factor: float = Field(..., ge=0.0, le=1.0, description="阻害係数 (0.0=阻害なし, 1.0=完全阻害)")

    @field_validator('concentration')
    def validate_concentration_limit(cls, v):
        # ロジック記述: 臨界値80.0mMを超える場合はハイパーサイクルフィードバック抑制が発動する
        if v > 80.0:
            # AIはこのコメントとバリデーションロジックに従って実装コードを生成しなければならない
            pass
        return v

class HypercycleNodeContract(BaseModel):
    """
    [ハイパーサイクル構成ノードの入出力仕様]
    """
    node_id: str = Field(..., description="ノードID")
    inputs: List[MetaboliteRateContract]
    outputs: List[MetaboliteRateContract]
    
    def calculate_catalytic_efficiency(self) -> float:
        """
        【必須実装ロジック】
        効率 E = sum(outputs) / (sum(inputs) * (1 - inhibition_factor))
        ※生成AIは本関数を省略せず、完全なPythonコードとして実装すること。
        """
        raise NotImplementedError("AIはこのインターフェースを元に完全なロジックを実装してください")
```

#### ② AIエージェントへの指示プロンプト（Contract-First適用）

```Plaintext
【指示】
添付の Python Contract ファイル（mbt55_metabolism.py）の型定義とDocstring内の要求仕様に従い、
`calculate_catalytic_efficiency` を含む完全な計算モジュールクラス `MBT55MetabolismEngine` を実装してください。

【厳格ルール】
1. Pydanticモデルで定義された制約（ge, le, validator）をすべてガード節としてコード内に含めてください。
2. `// TODO` や `pass` などの省略記法は一切禁止します。すべての計算式を具体的に記述してください。
```

### 2. Mermaid.js + 逐条解説プロトコルの具体的手法

Mermaidで図を出力させるだけだと、AIはノード（箱）を数個描いて満足します。**「図」と「全ノードの詳細テキスト解説」を一対一で強制的に連動させる**プロトコル（ルール）を適用します。

#### ① プロンプト指示テンプレート

```Plaintext
【指示】
AGRIXとHealthBookにおける「MBT55代謝データ同期処理フロー」の詳細設計書を作成してください。

【出力フォーマット指定】
1. 【全体図】: Mermaid.js (sequenceDiagram または flowchart TD) でシステムフローを描画してください。
   ・全ノードには `NodeA[処理名]`, `NodeB[処理名]` のように一意のIDを付与してください。

2. 【逐条解説（省略厳禁）】:
   Mermaid図に登場する「すべてのノード（NodeA, NodeB...）」および「すべての矢印（遷移）」について、以下のフォーマットで例外なく詳細を全記述してください。

   ---
   ■ ノードID: [ノード名]
   ・入力データ: (型、構造)
   ・内部処理ロジック: (アルゴリズム、条件分岐、例外処理をステップバイステップで全記述)
   ・出力データ: (型、構造)
   ・エラーハンドリング: (失敗時のロールバック処理)
   ---

※「以下同様」や「他のノードも同様の処理を行う」といった省略は一切禁止します。すべてのノードを書き切ってください。
```

#### ② 生成される出力イメージ（AIからのレスポンス）

````Markdown
### 1. システムフロー図 (Mermaid)

```mermaid
flowchart TD
    NodeA[AGRIX: 代謝データ受信] --> NodeB[MBT55: 濃度バリデーション]
    NodeB -->|正常| NodeC[HealthBook: ハイパーサイクル評価 engine]
    NodeB -->|異常(臨界値オーバー)| NodeD[フィードバック抑制イベント発生]
````

### 2. 逐条解説

■ ノード NodeA: [AGRIX: 代謝データ受信]

・入力データ: HTTP POST payload (JSON: `MetaboliteRateContract` 互換)

・内部処理ロジック:

1. 受信したリクエストヘッダーの認証トークンを検証。
    
2. 受信タイムスタンプを付与し、ローカルキュー（Redis）に一時保存。
    
3. JSONペイロードを Python の `MetaboliteRateContract` オブジェクトへキャスト。
    
    ・出力データ: `MetaboliteRateContract` インスタンス
    ・エラーハンドリング: パース失敗時は 400 Bad Request を返し、エラーログを出力。
    
■ ノード NodeB: [MBT55: 濃度バリデーション]

・入力データ: `MetaboliteRateContract` インスタンス

・内部処理ロジック:

1. `concentration` の値を取得。
    
2. 0.0 <= concentration <= 100.0 の範囲チェックを実施。
    
3. concentration > 80.0 の場合、フラグ `is_overlimit = True` をセットし NodeD へ分岐。
    
4. 範囲内の場合、NodeC へデータを渡す。
    
    ・出力データ: 検証済みオブジェクト + 分岐フラグ
    ・エラーハンドリング: 範囲外データは `ValidationError` をスローし、監視システム（Sentry）に通知。
    
（...以下、NodeC, NodeD についても一切省略せずに全記述...）

```

---

### 導入による効果と運用ポイント

1. **仕様のブレ（ハルシネーション）が停止する**
   `Contract-First` により、AIは自ら適当なデータ構造を捏造できなくなります。PythonのPydanticモデルがそのまま「仕様のアンカー（重し）」として機能します。
2. **AIのトークン節約（要約癖）を解除できる**
   「Mermaidの全ノードIDに対して逐条解説を書く」というルールがあるため、AIは「途中で説明をやめる」ことが構造上できなくなります。

まずは最も重要度の高い **「MBT55共通モジュール」の型定義ファイル（Python Pydantic）を1つ手動または厳密に作成**し、それをすべてのAIエージェントへの入力コンテキストとして固定することをお勧めします。

<ElicitationsGroup message="このフォーマットに関して、さらに深掘りしたい部分はありますか？">
  <Elicitation label="実際のMBT55/AGRIX向けPydantic Contract（型定義ファイル）の作成例を見る" query="AGRIXとHealthBookで共通利用できる「MBT55代謝機能・ハイパーサイクル」用の実践的なPython Pydantic Contract（型定義コード）の具体例を作成してください。"/>
  <Elicitation label="Claude/Geminiにこのルールを強制するシステムプロンプト（System Prompt）の作成" query="ClaudeやGeminiのSystem Prompt（カスタム指示）に直接組み込める、Contract-FirstおよびMermaid逐条解説を強制するテンプレートを作成してください。"/>
</ElicitationsGroup>
```

[[PD2. Python＋ローカル軽量ベクトル検索（RAG）の自動化]]
