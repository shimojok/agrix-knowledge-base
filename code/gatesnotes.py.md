# fetcher/gatesnotes.py
import feedparser

def fetch_gatesnotes():
    feed = feedparser.parse("https://www.gatesnotes.com/rss")
    posts = []

    for entry in feed.entries:
        posts.append({
            "source": "GatesNotes",
            "title": entry.title,
            "text": entry.summary,
            "url": entry.link
        })

    return posts