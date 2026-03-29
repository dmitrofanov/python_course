inventory = [
    {"name": "Молоко", "category": "молочка", "quantity": 5, "price": 80},
    {"name": "Хлеб", "category": "выпечка", "quantity": 15, "price": 50},
    {"name": "Сыр", "category": "молочка", "quantity": 3, "price": 350},
    {"name": "Яблоки", "category": "фрукты", "quantity": 20, "price": 120},
    {"name": "Масло", "category": "молочка", "quantity": 8, "price": 150},
    {"name": "Печенье", "category": "выпечка", "quantity": 12, "price": 90},
    {"name": "Бананы", "category": "фрукты", "quantity": 25, "price": 100},
]

print("=" * 50)
print("1. Товары для дозаказа (осталось <10):")
for item in inventory:
    if item["quantity"] < 10:
        print(f"  {item['name']}: {item['quantity']} шт. (заказать ещё!)")

print("\n2. Общая стоимость всех товаров:")
total_value = 0
for item in inventory:
    item_total = item["quantity"] * item["price"]
    total_value += item_total
    print(f"  {item['name']}: {item['quantity']} × {item['price']} = {item_total} руб.")
print(f"  ИТОГО: {total_value} руб.")

print("\n3. Категория с максимальной суммарной стоимостью:")
category_total = {}
for item in inventory:
    cat = item["category"]
    value = item["quantity"] * item["price"]
    category_total[cat] = category_total.get(cat, 0) + value

max_category = max(category_total.items(), key=lambda x: x[1])
print(f"  {max_category[0]}: {max_category[1]} руб.")

print("\n4. Топ-3 самых дорогих товара (цена за единицу):")
# Сортируем по цене
sorted_by_price = sorted(inventory, key=lambda x: x["price"], reverse=True)
for i, item in enumerate(sorted_by_price[:3], 1):
    print(f"  {i}. {item['name']}: {item['price']} руб.")