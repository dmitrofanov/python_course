data = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5]

encoded = []
if data:
    current = data[0]
    count = 1
    
    for item in data[1:]:
        if item == current:
            count += 1
        else:
            encoded.append((current, count))
            current = item
            count = 1
    encoded.append((current, count))

print(f"Исходный список (длина {len(data)}): {data}")
print(f"Сжатое представление: {encoded}")
print(f"Сжатый размер: {len(encoded)} элементов")