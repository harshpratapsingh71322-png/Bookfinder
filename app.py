from flask import Flask, render_template, request
import urllib.parse # Link banane ke liye

app = Flask(__name__)

def get_book_data(query):
    # Encode query taaki spaces '+' ban jayein (e.g. "RD Sharma" -> "RD+Sharma")
    safe_query = urllib.parse.quote_plus(query)
    
    return [
        {
            "store": "Amazon", 
            "price": "Check Price", 
            "link": f"https://www.amazon.in/s?k={safe_query}", 
            "color": "#FF9900"
        },
        {
            "store": "Flipkart", 
            "price": "Check Price", 
            "link": f"https://www.flipkart.com/search?q={safe_query}", 
            "color": "#2874F0"
        },
        {
            "store": "Bookswagon", 
            "price": "Check Price", 
            "link": f"https://www.bookswagon.com/searchresults.aspx?kw={safe_query}", 
            "color": "#d02e2e"
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
    
