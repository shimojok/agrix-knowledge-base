# main.py
import asyncio
from fetcher.linkedin import fetch_linkedin_posts
from fetcher.gatesnotes import fetch_gatesnotes
from fetcher.threads import fetch_threads
from normalizer.normalize import normalize
from router.scorer import score_post
from responder.composer import compose_response
from publisher.github_sync import save_to_github

async def run_pipeline():
    posts = []

    posts += fetch_linkedin_posts("https://www.linkedin.com/in/billgates/")
    posts += fetch_gatesnotes()
    posts += await fetch_threads("thisisbillgates")

    normalized = normalize(posts)
    scored = [score_post(p) for p in normalized]

    responses = []
    for p in scored:
        if p["rank"] in ["A", "B"]:
            responses.append({
                "post": p,
                "response": compose_response(p)
            })

    save_to_github(responses, "daily_responses.json")

asyncio.run(run_pipeline())