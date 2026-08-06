"""
Даны два списка: имена и возраст. Создай словарь {имя: возраст}.
Придумай как можно больше способов сделать это.
Какой способ тебе понравился больше всего?
"""

names = ["Анна", "Иван", "Мария", "Петр"]
ages = [25, 30, 22, 28]

users_zip = {}
users_zip = dict(zip(names, ages))
print(users_zip)


users_cycle = {}
for i in range(len(names)):
    users_cycle[names[i]] = ages[i]

print(users_cycle)
