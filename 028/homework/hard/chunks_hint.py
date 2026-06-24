numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3

chunks = []
for i in range(0, len(numbers), chunk_size):
    chunk = numbers[i:i + chunk_size]
    chunks.append(chunk)

print(f"Исходный список: {numbers}")
print(f"Чанки по {chunk_size}: {chunks}")