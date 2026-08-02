"""
Дан список чисел. Найди все уникальные пары чисел,
разность которых равна 2 (a - b = 2 или b - a = 2).
"""

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
target_diff = 2

result = set()

# for a in numbers:
#     for b in numbers[1:]:
#         if a - b == target_diff or b - a == target_diff:
#             result.append((a, b))
# print(result)

for a in numbers:
    for b in numbers[1:]:
        if abs(a - b) == target_diff:
            sort_numbers = tuple(sorted((a, b)))
            result.add(sort_numbers)
print(result)


        