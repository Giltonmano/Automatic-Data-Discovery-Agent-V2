import feedparser
import sqlite3

query = "centrifuge"
url = f"https://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"

feed = feedparser.parse(url)

conn =sqlite3.connect("data/papers.db")
cursor = conn.cursor()

for entry in feed.entries:
    try:
        cursor.execute("""
            INSERT INTO papers (title, published, link, summary, source)
            VALUES (?, ?, ?, ?, ?)
        """, (entry.title, entry.published, entry.link, entry.summary, "arXiv"))
        print("Saved:", entry.title)
    except sqlite3.IntegrityError:
        print("Entry already exists, skipped:", entry.title)

conn.commit()
conn.close()
