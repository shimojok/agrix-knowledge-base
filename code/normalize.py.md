# normalizer/normalize.py
import uuid
from datetime import datetime

def normalize(posts):
    normalized = []

    for p in posts:
        normalized.append({
            "id": str(uuid.uuid4()),
            "source": p.get("source"),
            "text": p.get("text"),
            "url": p.get("url", None),
            "timestamp": datetime.utcnow().isoformat()
        })

    return normalized