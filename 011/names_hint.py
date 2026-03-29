names = ["анна", "иван", "мария", "петр", "елена"]

# 1. Имена с большой буквы
capitalized = [name.title() for name in names]
print("С большой буквы:", capitalized)

# 2. Только длинные имена
long_names = [name for name in names if len(name) > 4]
print("Длинные имена:", long_names)

# 3. Приветствия
greetings = [f"Привет, {name.title()}!" for name in names]
print("Приветствия:", greetings)

# 4. Длины имён
name_lengths = [len(name) for name in names]
print("Длины имён:", name_lengths)

# Бонус: имена, начинающиеся на гласную
vowel_names = [name.title() for name in names if name[0] in "аеёиоуыэюя"]
print("Имена на гласную:", vowel_names)