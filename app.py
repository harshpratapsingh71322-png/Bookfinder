from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

def get_book_data(query):
    safe_query = urllib.parse.quote_plus(query)
    # 1000627725_2.jpg jaisa interface banane ke liye data structure
    return [
        {
            "title": f"{query} - Best Deal",
            "price": "₹475",
            "store": "Amazon.in",
            "img": "https://m.media-amazon.com/images/I/81TjYyV+7PL._AC_UF1000,1000_QL80_.jpg",
            "link": f"https://www.amazon.in/s?k={safe_query}",
            "special": "Special Offer"
        },
        {
            "title": f"All In One {query}",
            "price": "₹487",
            "store": "Flipkart",
            "img": "https://m.media-amazon.com/images/I/71YvM4Yv6WL._AC_UF1000,1000_QL80_.jpg",
            "link": f"https://www.flipkart.com/search?q={safe_query}",
            "special": "₹50 off with Bank Offer"
        },
        {
            "title": f"NCERT {query} Edition",
            "price": "₹232",
            "store": "Bookswagon",
            "img": "https://m.media-amazon.com/images/I/51Z9oO4YnBL.jpg",
            "link": f"https://www.bookswagon.com/searchresults.aspx?kw={safe_query}",
            "special": "Lowest Price"
        }
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
    
