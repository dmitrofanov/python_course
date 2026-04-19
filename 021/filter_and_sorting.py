"""
ЗАДАЧА: Фильтрация и сортировка сотрудников

Дан список сотрудников. Каждый сотрудник — словарь с полями:
name, age, department, salary.
Нужно:
1. Отфильтровать сотрудников старше 30 лет
2. Отсортировать их по зарплате (от высокой к низкой)
3. Сгруппировать по отделам
4. Для каждого отдела вывести среднюю зарплату
"""

employees = [
    {"name": "Анна", "age": 28, "department": "IT", "salary": 120000},
    {"name": "Иван", "age": 35, "department": "IT", "salary": 150000},
    {"name": "Мария", "age": 42, "department": "HR", "salary": 90000},
    {"name": "Петр", "age": 29, "department": "Sales", "salary": 80000},
    {"name": "Ольга", "age": 38, "department": "IT", "salary": 135000},
    {"name": "Сергей", "age": 45, "department": "HR", "salary": 95000},
    {"name": "Елена", "age": 31, "department": "Sales", "salary": 110000},
    {"name": "Дмитрий", "age": 33, "department": "IT", "salary": 125000},
] 