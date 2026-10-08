import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TAVILY_API_KEY")

def fetch_web(query, max_results=5):
    response = requests.post(
        "https://api.tavily.com/search",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"query": query, "max_results": max_results, "search_depth": "basic"},
        timeout=20,
    )
    if response.status_code != 200:
        print("Tavily request failed:", response.status_code)
        return []

    results = []
    for item in response.json().get("results", []):
        results.append({
            "name": item.get("title", ""),
            "model": "",
            "price": "See link",
            "specs": (item.get("content") or "")[:300],
            "link": item.get("url", ""),
            "source": "Web (Tavily)",
        })
    return results