numbers = [1, 2, 3, 2, 4, 5, 3, 6, 7, 1, 8, 9, 2]

counts = {}

# Подсчитываем частоту
for num in numbers:
    counts[num] = counts.get(num, 0) + 1

print("Повторяющиеся числа:")
for num, count in counts.items():
    if count > 1:
        print(f"  {num} встречается {count} раза")
