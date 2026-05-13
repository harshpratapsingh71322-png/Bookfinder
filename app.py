from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

def get_book_data(query):
    safe_query = urllib.parse.quote_plus(query)
    
    # 5 alag websites ke direct search links aur branding
    return [
        {
            "store": "Amazon", 
            "price": "Check Best Deal", 
            "link": f"https://www.amazon.in/s?k={safe_query}+book", 
            "img": "https://www.vectorlogo.zone/logos/amazon/amazon-icon.svg",
            "offer": "Prime Delivery"
        },
        {
            "store": "Flipkart", 
            "price": "View Offers", 
            "link": f"https://www.flipkart.com/search?q={safe_query}+book", 
            "img": "https://www.vectorlogo.zone/logos/flipkart/flipkart-icon.svg",
            "offer": "Bank Discounts"
        },
        {
            "store": "Bookswagon", 
            "price": "Check Price", 
            "link": f"https://www.bookswagon.com/searchresults.aspx?kw={safe_query}", 
            "img": "https://d2g9wbak88q7p6.cloudfront.net/images/bookswagon-logo.png",
            "offer": "Lowest Shipping"
        },
        {
            "store": "Snapdeal", 
            "price": "View Prices", 
            "link": f"https://www.snapdeal.com/search?keyword={safe_query}+book", 
            "img": "https://www.vectorlogo.zone/logos/snapdeal/snapdeal-icon.svg",
            "offer": "Cashback Available"
        },
        {
            "store": "MyPustak", 
            "price": "Free/Used Books", 
            "link": f"https://www.mypustak.com/search?q={safe_query}", 
            "img": "https://www.mypustak.com/static/media/logo.8e5a7444.png",
            "offer": "Social Initiative"
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
    
