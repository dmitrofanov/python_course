numbers = [1, 2, 3, 2, 4, 2, 5]
to_remove = 2

# Способ 1 — через цикл и новый список
filtered = []
for num in numbers:
    if num != to_remove:
        filtered.append(num)

# или
filtered = [num for num in numbers if num != to_remove]

print(f"Исходный: {numbers}")
print(f"После удаления {to_remove}: {filtered}")