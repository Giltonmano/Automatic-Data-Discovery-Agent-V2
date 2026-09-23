from flask import Flask, render_template, request
from search import search_all

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    papers = []
    equipment = []
    query = ""

    if request.method == "POST":
        query = request.form.get("query", "")
        papers, equipment = search_all(query)

    return render_template("index.html", papers=papers, equipment=equipment, query=query)
if __name__ == "__main__":
    app.run(debug=True) 