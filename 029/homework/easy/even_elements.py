"""
Дан список. Выведи элементы, стоящие на чётных индексах (0, 2, 4...).
"""

items = ["a", "b", "c", "d", "e", "f", "g", "h", "z"]

new_items = []
for i in range(0, len(items), 2):
    new_items.append(i)
print(new_items)