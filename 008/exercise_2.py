"""
ЗАДАЧА: Обработать список покупок и подсчитать итог

Список покупок
purchases = [
    {"name": "Ноутбук", "price": 50000, "quantity": 1},
    {"name": "Мышь", "price": 1500, "quantity": 1},
    {"name": "Блокнот", "price": 300, "quantity": 3},
    {"name": "Наушники", "price": 8000, "quantity": 1},
    {"name": "Ручка", "price": 50, "quantity": 5}
]

Функции:
1. filter_expensive(items, threshold) - фильтрует дорогие товары: price > threshold
2. calculate_total(items) - считает общую стоимость: price * quantity
3. apply_discount(total, discount_percent) - применяет скидку: total * (1 - discount_percent / 100)
4. format_receipt(final_sum) - форматирует чек: "К оплате: ХХХ руб."

Обработай список покупок:
format_receipt(
    apply_discount(
        calculate_total(
            filter_expensive(purchases, 1000)
        ),
        10  # 10% скидка
    )
)
"""

purchases = [
    {"name": "Ноутбук", "price": 50000, "quantity": 1},
    {"name": "Мышь", "price": 1500, "quantity": 1},
    {"name": "Блокнот", "price": 300, "quantity": 3},
    {"name": "Наушники", "price": 8000, "quantity": 1},
    {"name": "Ручка", "price": 50, "quantity": 5}
]

def filter_expensive(items, threshold):
    result = []
    for item in items:
        if item['price'] > threshold:
            result.append(item)
    return result

# calculate_total(items) - считает общую стоимость: price * quantity

def calculate_total(items):
    result = 0
    for item in items:
        result += item['price'] * item['quantity']
    return result

#apply_discount(total, discount_percent) - применяет скидку: total * (1 - discount_percent / 100)

def apply_discount(total, discount_percent):
    return total * (1 - discount_percent / 100)

#format_receipt(final_sum) - форматирует чек: "К оплате: ХХХ руб."

def format_receipt(final_sum):
    return f"К оплате: {final_sum} руб."

print(format_receipt(
    apply_discount(
        calculate_total(
            filter_expensive(purchases, 49999)
        ),
        10  # 10% скидка
    )
))