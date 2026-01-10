import requests

query = "artifical intelligence"
api="2f9b9d5a99f74f71af8c7fb4beebd67c"

url = "https://newsapi.org/v2/everything?q={query}&from=2025-12-10&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()

articles = data["articles"]
for article in articles:
    print(article["title"], article["url"])
    print("\n*********************************\n")