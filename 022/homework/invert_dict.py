"""
Дан словарь, где ключи — имена, значения — возраст.
Создай новый словарь, где ключи — возраст, значения — список имён.
"""

people = {
    "Анна": 25,
    "Иван": 30,
    "Мария": 25,
    "Петр": 30,
    "Ольга": 28
}

new_dict= {}
# for name, age in people.items():
#     if age not in new_dict:
#         new_dict[age] = [name]
#     else:
#         new_dict[age].append(name)
# print(new_dict)

from collections import defaultdict
new_dict = defaultdict(list)

for name, age in people.items():
    new_dict[age].append(name)
print(new_dict)