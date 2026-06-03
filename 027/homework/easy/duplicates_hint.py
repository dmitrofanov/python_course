items = [1, 2, 3, 4, 2, 5, 6, 3]

has_duplicates = False
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i] == items[j]:
            has_duplicates = True
            break
    if has_duplicates:
        break

print(f"Список: {items}")
print(f"Есть повторы: {has_duplicates}")