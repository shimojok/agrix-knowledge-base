# responder/composer.py
def compose_response(post):
    text = post["text"]

    return f"""
Bill さんが触れたテーマは、Planetary Metabolism OS の中核と強く結びついています。

特に以下の点で、BioNexus Project と因果的に統合できます：

• PBPEモデルによる地球規模の経済・気候評価  
• MBT55微生物群ハイパーサイクルによる生物学的安全性  
• AGRIX Platform OS による農業・食料システムの最適化  
• HealthBook MI による予測型健康モデル  

投稿内容：
「{text[:200]}...」

この論点は、Kaz が Planetary Social Innovation Architect として議論すべき重要領域です。
"""