products = [
    {"name": "Футболка", "category": "одежда", "price": 1000},
    {"name": "Джинсы", "category": "одежда", "price": 2500},
    {"name": "Кепка", "category": "одежда", "price": 800},
    {"name": "Мышь", "category": "электроника", "price": 1200},
    {"name": "Клавиатура", "category": "электроника", "price": 2500},
    {"name": "Книга", "category": "книги", "price": 500},
    {"name": "Тетрадь", "category": "книги", "price": 80},
    {"name": "Наушники", "category": "электроника", "price": 3000},
]

# Группировка по категориям
categories = {}

for product in products:
    cat = product["category"]
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(product)

print("Анализ по категориям:")
print("=" * 50)

for cat, items in categories.items():
    count = len(items)
    prices = [item["price"] for item in items]
    avg_price = sum(prices) / count
    max_price_item = max(items, key=lambda x: x["price"])
    
    print(f"\n{cat.upper()}:")
    print(f"  Количество: {count}")
    print(f"  Средняя цена: {avg_price:.0f} руб.")
    print(f"  Самый дорогой: {max_price_item['name']} ({max_price_item['price']} руб.)")
    print(f"  Товары: {', '.join([item['name'] for item in items])}")

# Категория с максимальным количеством товаров
max_category = max(categories.items(), key=lambda x: len(x[1]))
print(f"\nКатегория с максимальным количеством товаров: {max_category[0]} ({len(max_category[1])} шт.)")