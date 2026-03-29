"""
ЗАДАЧА 4: Рассчитай итоговую цену со скидками

Функции:
1. apply_bulk_discount(price, quantity) - скидка за количество:
   - 10% если quantity >= 10
   - 5% если quantity >= 5
   - иначе 0%
2. apply_seasonal_discount(discounted_price) - дополнительная сезонная скидка 15%
3. apply_tax(price) - добавляет налог 20%
4. format_price(price) - форматирует в "Итог: XXX.XX руб."

Рассчитай для товара ценой 100 руб., количеством 12 штук:
format_price(apply_tax(apply_seasonal_discount(apply_bulk_discount(100, 12))))
"""


def apply_bulk_discount(price, quantity):
    if quantity >= 10:
        return price * 0.9
    elif quantity >=5:
        return price * 0.95
    else:
        return price

def apply_seasonal_discount(discounted_price):
   return discounted_price * 0.85

def apply_tax(price):
    return price * 1.2

def format_price(price):
    return f"Итог: {price} руб."

print(format_price(apply_tax(apply_seasonal_discount(apply_bulk_discount(100, 12)))))

    
    
   