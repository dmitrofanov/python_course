"""
Дан список чисел. Найди второй по величине элемент
(не используя sort и max для всей задачи).
"""

numbers = [10, 5, 8, 20, 15, 20, 3]

unique_numbers = set(numbers)

first = numbers[0]
second = None

for n in unique_numbers:
    