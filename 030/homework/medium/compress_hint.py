data = [1, 1, 2, 2, 2, 3, 1, 1, 4, 4, 4, 4, 5]

compressed = []
for i in range(len(data)):
    if i == 0 or data[i] != data[i - 1]:
        compressed.append(data[i])

print(f"Исходный: {data}")
print(f"Сжатый: {compressed}")