import feedparser
from urllib.parse import quote

def fetch_arxiv(query, max_results=5):
    encoded_query = quote(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results={max_results}"
    feed = feedparser.parse(url)

    results = []
    for entry in feed.entries:
        results.append({
            "title": entry.title,
            "published": entry.published,
            "link": entry.link,
            "summary": entry.summary,
            "source": "arXiv"
        })
    return results 