numbers = [1, 2, 3, 2, 4, 2, 5, 6, 2, 7, 2, 8]
target = 2

indices = []
for i, num in enumerate(numbers):
    if num == target:
        indices.append(i)

print(f"Элемент {target} встречается на позициях: {indices}")