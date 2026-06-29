"""
Дан список. Удали все вхождения заданного элемента.
Пример: [1, 2, 3, 2, 4, 2, 5], удалить 2 → [1, 3, 4, 5]
"""

numbers = [1, 2, 3, 2, 4, 2, 5]
to_remove = 2

# clean_numbers = []
# for number in numbers:
#     if number != to_remove:
#         clean_numbers.append(number)

clean_numbers = [number for number in numbers if number != to_remove]

print(clean_numbers)