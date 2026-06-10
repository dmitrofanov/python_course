"""
Дан список. Проверь, есть ли в нём повторяющиеся элементы,
НЕ используя set() и count().
"""

items = [1, 2, 3, 4, 2, 5, 6, 3, 1]

dublicate_items = {}

print(list(enumerate(items)))
for index, num in enumerate(items):
    for num2 in items[index:]: