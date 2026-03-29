numbers = [1, 2, 3, 4, 5]

# 1. Обычный цикл
squares1 = []
for n in numbers:
    squares1.append(n ** 2)
print("Цикл:", squares1)

# 2. List comprehension
squares2 = [n ** 2 for n in numbers]
print("Comprehension:", squares2)

# 3. Только чётные
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("Квадраты чётных:", even_squares)

# 4. Только больше 2
big_squares = [n ** 2 for n in numbers if n > 2]
print("Квадраты > 2:", big_squares)