items = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 7, 7]

# Количество удалений = общее количество - количество уникальных
unique_count = len(set(items))
deletions = len(items) - unique_count

print(f"Исходный список (длина {len(items)}): {items}")
print(f"Уникальных элементов: {unique_count}")
print(f"Нужно удалить: {deletions}")