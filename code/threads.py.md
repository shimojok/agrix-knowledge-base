# fetcher/threads.py
from pyppeteer import launch

async def fetch_threads(username):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(f"https://www.threads.net/@{username}")

    posts = await page.evaluate("""
        () => Array.from(document.querySelectorAll('div[role="article"]'))
            .map(div => div.innerText)
    """)

    await browser.close()

    return [{"source": "Threads", "text": p} for p in posts]