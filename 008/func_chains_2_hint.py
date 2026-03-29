def filter_expensive(items, threshold):
    """Оставляет только товары дороже threshold"""
    expensive = []
    for item in items:
        if item["price"] > threshold:
            expensive.append(item)
    return expensive

def calculate_total(items):
    """Считает общую стоимость"""
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total

def apply_discount(total, discount_percent):
    """Применяет скидку в процентах"""
    return total * (1 - discount_percent / 100)

def format_receipt(final_sum):
    """Форматирует итоговую сумму"""
    return f"К оплате: {final_sum:.2f} руб."

# Список покупок
purchases = [
    {"name": "Ноутбук", "price": 50000, "quantity": 1},
    {"name": "Мышь", "price": 1500, "quantity": 1},
    {"name": "Блокнот", "price": 300, "quantity": 3},
    {"name": "Наушники", "price": 8000, "quantity": 1},
    {"name": "Ручка", "price": 50, "quantity": 5}
]

print("Обработка дорогих покупок (дороже 1000 руб.) со скидкой 10%:")

# Композиция функций - одна длинная строка
result = format_receipt(
    apply_discount(
        calculate_total(
            filter_expensive(purchases, 1000)
        ),
        10
    )
)

print(result)

# Разберем по шагам
print("\nШаги обработки:")
expensive_items = filter_expensive(purchases, 1000)
print(f"1. Дорогие товары (>{1000} руб.):")
for item in expensive_items:
    print(f"   - {item['name']}: {item['price']} × {item['quantity']}")

total = calculate_total(expensive_items)
print(f"2. Общая сумма: {total:.2f} руб.")

with_discount = apply_discount(total, 10)
print(f"3. Со скидкой 10%: {with_discount:.2f} руб.")

print(f"4. Форматированный чек: {format_receipt(with_discount)}")