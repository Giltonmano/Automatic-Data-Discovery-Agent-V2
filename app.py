import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")

def fetch_semantic_scholar(query, max_results=5):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {"query": query, "fields": "title,abstract,url,year", "limit": max_results}
    headers = {"x-api-key": api_key}

    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return []

    data = response.json()
    results = []
    for paper in data.get("data", []):
        results.append({
            "title": paper.get("title"),
            "published": str(paper.get("year")),
            "link": paper.get("url"),
            "summary": paper.get("abstract") or "",
            "source": "Semantic Scholar"
        })
    return results