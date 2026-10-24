# router/scorer.py
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# agrix-knowledge-base の embedding をロード
import json
with open("config/agrix_embeddings.json") as f:
    AGRIX_EMB = np.array(json.load(f))

def semantic_similarity(text):
    emb = model.encode(text)
    sims = np.dot(AGRIX_EMB, emb) / (np.linalg.norm(AGRIX_EMB, axis=1) * np.linalg.norm(emb))
    return float(np.max(sims))

def domain_match(text):
    keywords = ["GHG", "soil", "carbon", "microbiome", "PBPE", "MBT55", "AGRIX"]
    score = sum(k.lower() in text.lower() for k in keywords) / len(keywords)
    return score

def impact_potential(text):
    impact_terms = ["climate", "agriculture", "health", "AI", "food security"]
    score = sum(t.lower() in text.lower() for t in impact_terms) / len(impact_terms)
    return score

def score_post(post):
    s = semantic_similarity(post["text"])
    d = domain_match(post["text"])
    i = impact_potential(post["text"])

    total = (0.5*s + 0.3*d + 0.2*i) * 100

    rank = "A" if total >= 80 else "B" if total >= 60 else "C" if total >= 40 else "D"

    return {
        **post,
        "semantic": s,
        "domain": d,
        "impact": i,
        "score": total,
        "rank": rank
    }