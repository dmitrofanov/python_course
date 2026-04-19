"""
ЗАДАЧА: Анализ банковских транзакций

Дан список транзакций. Каждая транзакция — словарь с полями:
date, amount, type ('income' или 'expense'), category.

Нужно:
1. Подсчитать общий доход и расход
2. Найти категорию, на которую потрачено больше всего
3. Найти день с максимальной суммой трат
4. Построить словарь: месяц -> сумма доходов/расходов
"""

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
