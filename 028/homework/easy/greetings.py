"""
Дан список имён. Создай новый список с приветствиями:
"Привет, Анна!", "Привет, Иван!" и т.д.
"""

names = ["Анна", "Иван", "Мария", "Петр"]
# result = []
# for name in names:
#     result.append("Привет, " + name + "!")
# print(result)

result = [f"Привет, {name} !" for name in names]
print(result)