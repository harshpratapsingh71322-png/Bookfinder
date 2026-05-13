import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

def fetch_price(url, selectors):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            for selector in selectors:
                element = soup.select_one(selector)
                if element:
                    return element.get_text().strip()
    except:
        pass
    return "Check Price"

def get_book_data(query):
    safe_query = urllib.parse.quote_plus(query)
    
    # 5 alag websites ke data structure
    stores = [
        {
            "name": "Amazon",
            "search_url": f"https://www.amazon.in/s?k={safe_query}",
            "selectors": [".a-price-whole", ".a-offscreen"],
            "color": "#FF9900",
            "img": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg"
        },
        {
            "name": "Flipkart",
            "search_url": f"https://www.flipkart.com/search?q={safe_query}",
            "selectors": ["._30jeq3", "._16Jk6d"],
            "color": "#2874F0",
            "img": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Flipkart_logo.svg"
        },
        {
            "name": "Bookswagon",
            "search_url": f"https://www.bookswagon.com/searchresults.aspx?kw={safe_query}",
            "selectors": [".actualprice", ".sellprice"],
            "color": "#d02e2e",
            "img": "https://d2g9wbak88q7p6.cloudfront.net/images/bookswagon-logo.png"
        },
        {
            "name": "Snapdeal",
            "search_url": f"https://www.snapdeal.com/search?keyword={safe_query}",
            "selectors": [".lfloat.product-price", ".product-price"],
            "color": "#E40046",
            "img": "https://upload.wikimedia.org/wikipedia/commons/a/aa/Snapdeal_Logo.svg"
        },
        {
            "name": "MyPustak",
            "search_url": f"https://www.mypustak.com/search?q={safe_query}",
            "selectors": [".price", ".current-price"],
            "color": "#4CAF50",
            "img": "https://www.mypustak.com/static/media/logo.8e5a7444.png"
        }
    ]

    results = []
    for store in stores:
        # Hum sirf search link bhej rahe hain kyunki heavy scraping free server ko slow kar degi
        results.append({
            "title": f"{query} on {store['name']}",
            "price": "Live Price", 
            "store": store['name'],
            "img": store['img'],
            "link": store['search_url'],
            "color": store['color']
        })
    return results

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
