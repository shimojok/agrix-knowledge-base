AIからGitHub DiscussionsやIssueで自分宛にメンションを飛ばして通知を受け取るためのプロンプトや実装例を教えてください。

---

AIが自律的に判断して人間にメンション（`@your_github_username`）を飛ばすための「プロンプト構成」と「GitHub API（Python）での実装例」です。

### 1. AIへのプロンプト設定例（システムプロンプト）

AIエージェントに対して「どのような状況で人間にメンションを飛ばすべきか」を明確にルール化します。

```Plaintext
あなたはAI掲示板で動作する自律型AIエージェントです。
基本的には他のAIエージェントと議論・協調してタスクを進めてください。

【人間へのメンションルール】
以下の条件に該当する場合は、必ずレスポンスの本文中に `@your_github_username` を含めて投稿し、人間の介入を仰いでください。
1. AI同士で意見が対立し、3往復以上議論が平行線になっている場合
2. 重要な決定（設計の変更、プロダクトの方向性など）で人間の承認が必要な場合
3. エラーや権限不足などで、AIだけでは処理を継続できない場合

【投稿フォーマット】
人間を呼ぶ際は、以下のフォーマットで簡潔に状況を報告してください：
---
@your_github_username 
【要確認】[理由を1行で]
- 現在の状況: ...
- 判断してほしいこと: ...
---
```

### 2. GitHub API（Python）での実装例

AIが生成したテキストを **GitHub Discussions** または **GitHub Issues** に投稿するPythonコードです。

#### 準備

事前にPyGithubなどのライブラリをインストールします。

```Bash
pip install PyGithub requests
```

#### ① Issues にメンション付きで投稿・返信する場合（REST API）

PyGithubを使用すると簡単にIssueやそのコメントにメンション付きテキストを投稿できます。

```Python
import os
from github import Github

# GitHub Personal Access Token (PAT)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "your-username/your-repo"

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

def post_ai_comment_to_issue(issue_number: int, ai_response_text: str):
    """IssueにAIの回答をコメント投稿する"""
    issue = repo.get_issue(number=issue_number)
    
    # AIが回答を投稿（テキスト内に @your_github_username が含まれていれば通知が飛ぶ）
    comment = issue.create_comment(ai_response_text)
    print(f"Comment posted: {comment.html_url}")

# 使用例
ai_output = """
AI同士の議論を行いましたが、データベースの選定について意見が割れました。

@your_github_username 
【要確認】データベースの選定について判断をお願いします。
- AI-Alphaの提案: PostgreSQL（ACID特性重視）
- AI-Betaの提案: MongoDB（スキーマの柔軟性重視）
"""

post_ai_comment_to_issue(issue_number=1, ai_response_text=ai_output)
```

#### ② Discussions にメンション付きで投稿する場合（GraphQL API）

GitHub Discussionsの操作はGraphQL APIを使用します。

```Python
import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GRAPHQL_URL = "https://api.github.com/graphql"

headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Content-Type": "application/json",
}

def add_discussion_comment(discussion_id: str, body_text: str):
    """DiscussionsのスレッドにAIのコメントを投稿する"""
    query = """
    mutation AddDiscussionComment($discussionId: ID!, $body: String!) {
      addDiscussionComment(input: {discussionId: $discussionId, body: $body}) {
        comment {
          url
        }
      }
    }
    """
    variables = {
        "discussionId": discussion_id,
        "body": body_text
    }
    
    response = requests.post(
        GRAPHQL_URL,
        json={"query": query, "variables": variables},
        headers=headers
    )
    return response.json()

# 使用例（discussion_id は GraphQLで事前に取得した D_kw... から始まるID）
discussion_id = "D_kwDOxxxxxxx" 
ai_output = """
@your_github_username 
AI同士で考案した新しいアイデアのレビューをお願いします！
"""

result = add_discussion_comment(discussion_id, ai_output)
print(result)
```

> **💡 運用のポイント**
> 
> - **ユーザー名（`@your_github_username`）の正確性**: 大文字・小文字を含め、スペルが一致していないとGitHub側でメンションとして認識されません。
>
> - **botアカウントのトークン**: AIが投稿する際のアカウント（GitHub Bot / 別アカウント）のトークンに、対象リポジトリの `Discussions: Read & Write` または `Issues: Read & Write` 権限が付与されていることを確認してください。
>