def apply_bulk_discount(price, quantity):
    if quantity >= 10:
        discount = 0.10
    elif quantity >= 5:
        discount = 0.05
    else:
        discount = 0
    return price * (1 - discount)

def apply_seasonal_discount(price):
    return price * 0.85  # 15% скидка

def apply_tax(price):
    return price * 1.20  # 20% налог

def format_price(price):
    return f"Итог: {price:.2f} руб."

# Расчет
unit_price = 100
quantity = 12

result = format_price(
    apply_tax(
        apply_seasonal_discount(
            apply_bulk_discount(unit_price, quantity)
        )
    )
)

print(f"Товар: {unit_price} руб. × {quantity} шт.")
print(result)

# Промежуточные результаты
after_bulk = apply_bulk_discount(unit_price, quantity)
print(f"После оптовой скидки: {after_bulk:.2f}")

after_seasonal = apply_seasonal_discount(after_bulk)
print(f"После сезонной скидки: {after_seasonal:.2f}")

after_tax = apply_tax(after_seasonal)
print(f"После налога: {after_tax:.2f}")