"""
ЗАДАЧА: Учёт товаров на складе

Дан список товаров. Каждый товар — словарь с полями: название, категория, количество, цена.
Нужно:
1. Вывести все товары, количество которых меньше 10 (пора заказывать)
2. Посчитать общую стоимость всех товаров (количество * цена)
3. Найти категорию с максимальной суммарной стоимостью
4. Вывести топ-3 самых дорогих товара (по цене за единицу)
"""

inventory = [
    {"name": "Молоко", "category": "молочка", "quantity": 5, "price": 80},
    {"name": "Хлеб", "category": "выпечка", "quantity": 15, "price": 50},
    {"name": "Сыр", "category": "молочка", "quantity": 3, "price": 350},
    {"name": "Яблоки", "category": "фрукты", "quantity": 20, "price": 120},
    {"name": "Масло", "category": "молочка", "quantity": 8, "price": 150},
    {"name": "Печенье", "category": "выпечка", "quantity": 12, "price": 90},
    {"name": "Бананы", "category": "фрукты", "quantity": 25, "price": 100},
]

for product in inventory:
    if product["quantity"] < 10:
        print(f'Пора заказывать {product["name"]}')

print(f"Общая стоимость всех товаров {sum(product["quantity"] * product["price"] for product in inventory)}")

category_total = {}
for product in inventory:
    x = product["category"]
    y = product["quantity"] * product["price"]
    category_total[x] = category_total.get(x,0) + y
print(max(category_total.items(), key = lambda x: x[1]))

print(f'Самые дорогие товары: {", ".join(product["name"] for product in sorted(inventory, key = lambda x : -x["price"]) [:3])}')
