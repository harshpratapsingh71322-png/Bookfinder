from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

def get_book_data(query):
    safe_query = urllib.parse.quote_plus(query)
    # 5 alag websites ke search links
    return [
        {"store": "Amazon", "link": f"https://www.amazon.in/s?k={safe_query}", "color": "#FF9900", "icon": "A"},
        {"store": "Flipkart", "link": f"https://www.flipkart.com/search?q={safe_query}", "color": "#2874F0", "icon": "F"},
        {"store": "Bookswagon", "link": f"https://www.bookswagon.com/searchresults.aspx?kw={safe_query}", "color": "#d02e2e", "icon": "B"},
        {"store": "Snapdeal", "link": f"https://www.snapdeal.com/search?keyword={safe_query}", "color": "#E40046", "icon": "S"},
        {"store": "MyPustak", "link": f"https://www.mypustak.com/search?q={safe_query}", "color": "#4CAF50", "icon": "M"}
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
    
