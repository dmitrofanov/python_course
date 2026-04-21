people = {
    "Анна": 25,
    "Иван": 30,
    "Мария": 25,
    "Петр": 30,
    "Ольга": 28
}

by_age = {}

for name, age in people.items():
    if age not in by_age:
        by_age[age] = []
    by_age[age].append(name)

print("Группировка по возрасту:")
for age, names in sorted(by_age.items()):
    print(f"  {age} лет: {', '.join(names)}")