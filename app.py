from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Fake search results for demo (Real scraping needs specific headers)
def get_book_data(query):
    # As a 9th grader, focus on this logic later
    # Currently returning a list of stores and prices
    return [
        {"store": "Amazon", "price": "499", "link": "#", "color": "#FF9900"},
        {"store": "Flipkart", "price": "475", "link": "#", "color": "#2874F0"},
        {"store": "Bookswagon", "price": "510", "link": "#", "color": "#d02e2e"}
    ]

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    book_name = ""
    if request.method == "POST":
        book_name = request.form.get("book_name")
        results = get_book_data(book_name)
    return render_template("index.html", results=results, book_name=book_name)

if __name__ == "__main__":
    app.run(debug=True)
  
