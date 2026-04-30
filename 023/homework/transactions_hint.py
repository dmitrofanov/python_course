transactions = [
    ("еда", 500),
    ("транспорт", 300),
    ("еда", 200),
    ("кафе", 1000),
    ("транспорт", 150),
    ("еда", 400),
    ("кафе", 500),
    ("развлечения", 800),
]

# Суммируем по категориям
category_total = {}
for category, amount in transactions:
    category_total[category] = category_total.get(category, 0) + amount

print("Суммы по категориям:")
for category, total in sorted(category_total.items()):
    print(f"  {category}: {total} руб.")

# Поиск максимума и минимума
max_category = max(category_total.items(), key=lambda x: x[1])
min_category = min(category_total.items(), key=lambda x: x[1])

print(f"\nМаксимум: {max_category[0]} ({max_category[1]} руб.)")
print(f"Минимум: {min_category[0]} ({min_category[1]} руб.)")