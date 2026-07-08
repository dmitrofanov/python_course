"""
Дан список и размер чанка. Разбей список на подсписки указанного размера.
Последний чанк может быть короче.
Пример: [1, 2, 3, 4, 5, 6, 7, 8], chunk_size=3 → [[1, 2, 3], [4, 5, 6], [7, 8]]
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3

result = []
for i in range(0, len(numbers), 3):
    chunk = numbers[i:i + chunk_size]
    result.append(chunk)

print(result)