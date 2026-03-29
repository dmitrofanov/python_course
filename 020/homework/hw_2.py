"""
ЗАДАЧА: Поиск дубликатов

Дан список чисел. Напиши программу, которая:
1. Находит и выводит все числа, которые встречаются больше одного раза
2. Выводит количество повторений для каждого такого числа

Используй словарь для подсчёта частоты.
"""

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1, 8, 9, 2]

# Решение
repeat_numbers = {}

for number in numbers:
    repeat_numbers[number] = repeat_numbers.get(number, 0) +1

print(repeat_numbers)

duplicates ={num:quantity for num, quantity in repeat_numbers.items() if quantity > 1}
print(f'Количество повторений {duplicates}')

