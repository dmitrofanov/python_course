names = ["Анна", "Иван", "Мария", "Петр"]
ages = [25, 30, 22, 28]

# Первый способ
people = {}
for i in range(len(names)):
    people[names[i]] = ages[i]

print(f"Словарь: {people}")

# Второй способ
people = {k: v for k, v in zip(names, ages)}

print(f"Словарь: {people}")

# Третий способ
people = dict(zip(names, ages))

print(f"Словарь: {people}")