import requests
import json

response = requests.get("https://newsapi.org/v2/top-headlines?category=technology&apiKey=your_newsapi_key")
news_data = response.json()
print(news_data)