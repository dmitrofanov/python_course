transactions = [
    {"date": "2025-04-01", "amount": 50000, "type": "income", "category": "salary"},
    {"date": "2025-04-02", "amount": 1500, "type": "expense", "category": "food"},
    {"date": "2025-04-03", "amount": 3000, "type": "expense", "category": "rent"},
    {"date": "2025-04-05", "amount": 2000, "type": "expense", "category": "food"},
    {"date": "2025-04-10", "amount": 800, "type": "expense", "category": "transport"},
    {"date": "2025-04-15", "amount": 10000, "type": "income", "category": "freelance"},
    {"date": "2025-04-20", "amount": 5000, "type": "expense", "category": "electronics"},
    {"date": "2025-04-25", "amount": 1200, "type": "expense", "category": "food"},
]

# Общий доход и расход
total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")

print(f"Общий доход: {total_income} руб.")
print(f"Общий расход: {total_expense} руб.")
print(f"Баланс: {total_income - total_expense} руб.")

# Категория с максимальными тратами
expenses_by_category = {}
for t in transactions:
    if t["type"] == "expense":
        cat = t["category"]
        expenses_by_category[cat] = expenses_by_category.get(cat, 0) + t["amount"]

max_category = max(expenses_by_category.items(), key=lambda x: x[1])
print(f"\nБольше всего потрачено на: {max_category[0]} ({max_category[1]} руб.)")

# День с максимальными тратами
expenses_by_day = {}
for t in transactions:
    if t["type"] == "expense":
        date = t["date"]
        expenses_by_day[date] = expenses_by_day.get(date, 0) + t["amount"]

max_day = max(expenses_by_day.items(), key=lambda x: x[1])
print(f"\nДень с максимальными тратами: {max_day[0]} ({max_day[1]} руб.)")

# Анализ по месяцам
month_stats = {}
for t in transactions:
    month = t["date"][:7]  # "2025-04"
    if month not in month_stats:
        month_stats[month] = {"income": 0, "expense": 0}
    
    if t["type"] == "income":
        month_stats[month]["income"] += t["amount"]
    else:
        month_stats[month]["expense"] += t["amount"]

print("\nСтатистика по месяцам:")
for month, stats in month_stats.items():
    balance = stats["income"] - stats["expense"]
    print(f"  {month}: доход {stats['income']}, расход {stats['expense']}, баланс {balance}")