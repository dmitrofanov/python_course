"""
Дан список и число k. Раздели список на подсписки длины k,
а затем каждый подсписок переверни.
Пример: [1, 2, 3, 4, 5, 6, 7, 8], k=3 → [3, 2, 1, 6, 5, 4, 7, 8]
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3

new_list = []
for i in range(0, len(numbers), k):
    chunk = numbers[i:i+k]
    reversed_chunk = chunk[::-1]
    new_list.extend(reversed_chunk)
print(new_list)