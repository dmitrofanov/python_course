import requests
import os
from dotenv import load_dotenv




# Загружаем переменные окружения
load_dotenv()

# Получаем API ключ (если бы он нужен)
api_key = os.getenv("API_KEY")

# Делаем запрос к публичному API
url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)

# Проверяем статус ответа
if response.status_code == 200:
    # print(response.content)
    # print('='*80)
    # print(response.json())
    data = response.json()
    rub_rate = data["rates"]["RUB"]
    print(f"Курс USD к RUB: {rub_rate}")
else:
    print(f"Ошибка: {response.status_code}")