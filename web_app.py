from flask import Flask, render_template, request
from search import search_all
from intelligence import summarize_results

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    papers = []
    equipment = []
    query = ""
    summary = ""

    if request.method == "POST":
        query = request.form.get("query", "")
        papers, equipment = search_all(query)
        summary = summarize_results(query, papers, equipment)

    return render_template("index.html", papers=papers, equipment=equipment, query=query, summary=summary)

if __name__ == "__main__":
    app.run(debug=True)