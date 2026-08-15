"""
Дан список и элемент. Найди все индексы, на которых встречается этот элемент.
"""

numbers = [1, 2, 3, 2, 4, 2, 5, 6, 2, 7, 2, 8]
target = 2

for index, value in enumerate(numbers):
    if value == target:
        print(f'Элемент {target} встречается на позиции {index}')