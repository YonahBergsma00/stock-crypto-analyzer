import requests

def fetch_news(ticker: str, api_key: str, page_size: int = 10) -> list:
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": ticker,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": api_key
    }

    response = requests.get(url, params = params)
    data = response.json()

    headlines = [article["title"] for article in data.get("articles", [])]

    return headlines