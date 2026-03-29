"""
ЗАДАЧА 4: Форматирование товара

1. Функция apply_discount(price, percent) - возвращает цену со скидкой
   Формула: price * (1 - percent/100)
2. Функция add_tax(price, tax_rate) - возвращает цену с налогом
   Формула: price * (1 + tax_rate/100)
3. Функция format_price(price) - возвращает строку "Цена: ХХХ руб."

Рассчитай цену товара:
1) Исходная цена: 1000 руб.
2) Скидка 20%
3) Налог 10%
4) Форматирование

Подумай, в каком порядке нужно вызывать функции?
"""

def apply_discount(price, percent):
    return price * (1 - percent/100) 
def add_tax(price, tax_rate):
    return price * (1 + tax_rate/100)
def format_price(price):
    return f"Цена: {price} руб."

print(format_price(add_tax(apply_discount(1000,20),10)))