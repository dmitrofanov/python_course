names = ["Анна", "Иван", "Мария", "Петр"]

greetings = []
for name in names:
    greetings.append(f"Привет, {name}!")

# или

greetings = [f"Привет, {name}" for name in names]

print(f"Приветствия: {greetings}")