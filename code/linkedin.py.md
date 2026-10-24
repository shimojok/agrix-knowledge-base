# fetcher/linkedin.py
import requests
from bs4 import BeautifulSoup
import json

def fetch_linkedin_posts(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    posts = []
    for div in soup.find_all("div", class_="feed-shared-update-v2"):
        text = div.get_text(strip=True)
        posts.append({
            "source": "LinkedIn",
            "text": text,
            "url": url
        })

    return posts