# Пример решения (упрощённое)
import requests
from colorama import Fore, init
from tqdm import tqdm
import time

init()

# Координаты городов (упрощённо)
cities = {
    "москва": (55.75, 37.62),
    "питер": (59.93, 30.33),
    "новосибирск": (55.04, 82.93),
    "екатеринбург": (56.83, 60.60),
}

city = input("Введите город: ").lower()

if city in cities:
    lat, lon = cities[city]
    
    # Запрос погоды
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["current_weather"]["temperature"]
        
        # Цветной вывод в зависимости от температуры
        if temp > 20:
            print(Fore.GREEN + f"В {city.capitalize()} {temp}°C — тепло!")
        elif temp > 10:
            print(Fore.YELLOW + f"В {city.capitalize()} {temp}°C — нормально")
        else:
            print(Fore.CYAN + f"В {city.capitalize()} {temp}°C — холодно")
        print(Fore.RESET)
    else:
        print("Ошибка получения данных")
else:
    print("Город не найден в базе")