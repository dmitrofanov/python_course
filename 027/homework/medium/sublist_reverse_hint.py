numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3

result = []
for i in range(0, len(numbers), k):
    chunk = numbers[i:i + k]
    result.extend(chunk[::-1])

print(f"Исходный: {numbers}")
print(f"После инвертирования кусков по {k}: {result}")