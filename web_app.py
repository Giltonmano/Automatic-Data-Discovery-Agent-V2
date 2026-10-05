from flask import Flask, render_template, request
from search import search_all
from intelligence import summarize_results
from connector_arxiv import fetch_arxiv
from app import fetch_semantic_scholar
from database import save_paper

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    papers = []
    equipment = []
    query = ""
    summary = ""

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            # Fetch live from both sources
            fresh_papers = fetch_arxiv(query) + fetch_semantic_scholar(query)
            for paper in fresh_papers:
                save_paper(paper)

            # Now search everything stored (old + newly fetched)
            papers, equipment = search_all(query)
            summary = summarize_results(query, papers, equipment)

    return render_template("index.html", papers=papers, equipment=equipment, query=query, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)