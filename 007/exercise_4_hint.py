def apply_discount(price, percent):
    discounted = price * (1 - percent/100)
    print(f"Цена после скидки {percent}%: {discounted:.2f}")
    return discounted

def add_tax(price, tax_rate):
    with_tax = price * (1 + tax_rate/100)
    print(f"Цена с налогом {tax_rate}%: {with_tax:.2f}")
    return with_tax

def format_price(price):
    return f"Итоговая цена: {price:.2f} руб."

# Рассчитываем
original_price = 1000

# Вариант 1: По шагам (понятнее)
discounted_price = apply_discount(original_price, 20)
price_with_tax = add_tax(discounted_price, 10)
result = format_price(price_with_tax)

# Вариант 2: В одну строку (компактнее)
result2 = format_price(add_tax(apply_discount(original_price, 20), 10))

print("\nРезультат (по шагам):", result)
print("Результат (в одну строку):", result2)