 def get_book_data(query):
    safe_query = urllib.parse.quote_plus(query)
    return [
        {
            "store": "Amazon", "offer": "Prime Delivery",
            "link": f"https://www.amazon.in/s?k={safe_query}",
            "img": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg"
        },
        {
            "store": "Flipkart", "offer": "Best Discounts",
            "link": f"https://www.flipkart.com/search?q={safe_query}",
            "img": "https://p7.hiclipart.com/preview/439/171/840/flipkart-e-commerce-shopping-logo-samsung-galaxy-mobile-phones.jpg"
        },
        {
            "store": "Snapdeal", "offer": "Cashback",
            "link": f"https://www.snapdeal.com/search?keyword={safe_query}",
            "img": "https://upload.wikimedia.org/wikipedia/commons/a/aa/Snapdeal_Logo.svg"
        },
        {
            "store": "Bookswagon", "offer": "Lowest Price",
            "link": f"https://www.bookswagon.com/searchresults.aspx?kw={safe_query}",
            "img": "https://d2g9wbak88q7p6.cloudfront.net/images/bookswagon-logo.png"
        }
    ]
     
