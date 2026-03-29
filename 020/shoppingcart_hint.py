cart = [
    {"name": "Футболка", "price": 1000, "quantity": 2},
    {"name": "Джинсы", "price": 2500, "quantity": 1},
    {"name": "Кепка", "price": 800, "quantity": 3},
    {"name": "Кроссовки", "price": 3500, "quantity": 1},
    {"name": "Носки", "price": 200, "quantity": 5},
]

# Решение
print("Содержимое корзины:")
print("-" * 40)

total_sum = 0
most_expensive_item = None
max_total_item = None
max_price = 0
max_total = 0

for item in cart:
    item_total = item["price"] * item["quantity"]
    total_sum += item_total
    
    # Проверяем самый дорогой товар (по цене за единицу)
    if item["price"] > max_price:
        max_price = item["price"]
        most_expensive_item = item["name"]
    
    # Проверяем товар с максимальной итоговой стоимостью
    if item_total > max_total:
        max_total = item_total
        max_total_item = item["name"]
    
    print(f"{item['name']}: {item['price']} × {item['quantity']} = {item_total} руб.")

print("-" * 40)
print(f"Общая сумма: {total_sum} руб.")
print(f"Самый дорогой товар (за штуку): {most_expensive_item} ({max_price} руб.)")
print(f"Товар с максимальной итоговой стоимостью: {max_total_item} ({max_total} руб.)")