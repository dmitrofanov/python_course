"""
ЗАДАЧА: Группировка по категориям

Дан список товаров. Каждый товар — словарь с полями: name, category, price.
Нужно:
1. Сгруппировать товары по категориям (словарь: категория -> список товаров)
2. Для каждой категории посчитать:
   - Количество товаров
   - Среднюю цену
   - Самый дорогой товар
3. Вывести категорию с максимальным количеством товаров
"""

products = [
    {"name": "Футболка", "category": "одежда", "price": 1000},
    {"name": "Джинсы", "category": "одежда", "price": 2500},
    {"name": "Кепка", "category": "одежда", "price": 800},
    {"name": "Мышь", "category": "электроника", "price": 1200},
    {"name": "Клавиатура", "category": "электроника", "price": 2500},
    {"name": "Книга", "category": "книги", "price": 500},
    {"name": "Тетрадь", "category": "книги", "price": 80},
    {"name": "Наушники", "category": "электроника", "price": 3000},
]

from collections import defaultdict

categories = defaultdict(list)
# categories["Отпуск"].append("веселый")

#№1
# for product in products:
#     categories[product["category"]].append(product["name"])

### или
# categories = {}
# for product in products:
#     if product["category"] not in categories:
#         categories[product["category"]] = []
#     categories[product["category"]].append(product["name"])

#№2
for product in products:
    categories[product["category"]].append(product)
from pprint import pprint
pprint(categories)



# 2. Для каждой категории посчитать:
#    - Количество товаров
#    - Среднюю цену
#    - Самый дорогой товар

for category in categories:
    print(f'В категории {category}: товаров {len(categories[category])} шт.')

