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

print("1. Сотрудники старше 30 лет:")
older_than_30 = [emp for emp in employees if emp["age"] > 30]
for emp in older_than_30:
    print(f"  {emp['name']} ({emp['age']} лет) - {emp['department']} - {emp['salary']} руб.")

print("\n2. Сортировка по зарплате (от высокой к низкой):")
sorted_by_salary = sorted(employees, key=lambda x: x["salary"], reverse=True)
for emp in sorted_by_salary:
    print(f"  {emp['name']}: {emp['salary']} руб.")

print("\n3. Группировка по отделам:")
departments = {}
for emp in employees:
    dept = emp["department"]
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(emp)

for dept, members in departments.items():
    print(f"\n  {dept}:")
    for emp in members:
        print(f"    - {emp['name']} ({emp['salary']} руб.)")

print("\n4. Средняя зарплата по отделам:")
for dept, members in departments.items():
    salaries = [emp["salary"] for emp in members]
    avg_salary = sum(salaries) / len(salaries)
    print(f"  {dept}: {avg_salary:.0f} руб.")