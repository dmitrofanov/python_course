"""
Дан список. Проверь, есть ли в нём повторяющиеся элементы,
НЕ используя set() и count().
"""

items = [1, 2, 3, 4, 2, 5, 6, 3, 1, 6]

has_dublicates = False 

print(list(enumerate(items)))
for index, num in enumerate(items):
    for num2 in items[index + 1:]:
        if num == num2:
            has_dublicates = True
            print(f'Число {num} уже встречалось')

print(f'Были дубликаты {has_dublicates}')