data = {
    "группа_А": [1, 2, 3, 4, 5],
    "группа_В": [10, 20],
    "группа_С": [100, 200, 300, 400],
    "группа_D": [1000],
    "группа_E": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

# Сортировка по длине значений
sorted_items = sorted(data.items(), key=lambda x: len(x[1]), reverse=True)
sorted_data = dict(sorted_items)

print("Сортировка по длине списков (от большей к меньшей):")
for key, value in sorted_data.items():
    print(f"  {key}: {len(value)} элементов - {value}")