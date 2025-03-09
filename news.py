import requests
import json

YANDEX_GPT_API_URL = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
YANDEX_OAUTH_TOKEN = "your_yandex_oauth_token"
YANDEX_FOLDER_ID = "your_yandex_folder_id"

HEADERS = {
    "Authorization": f"Bearer {YANDEX_OAUTH_TOKEN}",
    "Content-Type": "application/json",
}

def get_news():
    # Пример API для новостей (можно заменить на другой источник)
    response = requests.get("https://newsapi.org/v2/top-headlines?category=technology&apiKey=your_newsapi_key")
    news_data = response.json()
    
    # Получаем заголовки новостей
    news_titles = [article["title"] for article in news_data["articles"][:5]]
    return "\n".join(news_titles)

def ask_yandex_gpt(prompt):
    data = {
        "modelUri": f"gpt://{YANDEX_FOLDER_ID}/yandexgpt/latest",
        "completionOptions": {"temperature": 0.7, "maxTokens": 500},
        "messages": [{"role": "user", "text": prompt}],
    }
    
    response = requests.post(YANDEX_GPT_API_URL, headers=HEADERS, data=json.dumps(data))
    return response.json()["result"]["alternatives"][0]["message"]["text"]

# Получаем свежие новости
news = get_news()
prompt = f"Проанализируй и выдели главное из этих IT-новостей: \n{news}"

# Отправляем в Yandex GPT
result = ask_yandex_gpt(prompt)
print(result)