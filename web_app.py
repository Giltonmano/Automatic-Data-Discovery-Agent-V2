from flask import Flask, render_template, request
from search import search_all
from intelligence import summarize_results
from connector_arxiv import fetch_arxiv
from connector_web import fetch_web
from app import fetch_semantic_scholar
from database import save_paper, save_equipment

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
            fresh_papers = fetch_arxiv(query) + fetch_semantic_scholar(query)
            for paper in fresh_papers:
                save_paper(paper)

            web_results = fetch_web(query)
            for item in web_results:
                save_equipment(item)

            papers, equipment = search_all(query)

            # Web results are ranked by meaning, so they may not contain the exact
            # words typed. Make sure fresh ones always show up.
            seen = {row[4] for row in equipment}
            for item in web_results:
                if item["link"] not in seen:
                    equipment.append((item["name"], item["model"], item["price"],
                                      item["specs"], item["link"], item["source"]))

            summary = summarize_results(query, papers, equipment)

    return render_template("index.html", papers=papers, equipment=equipment, query=query, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)