def filter_even(numbers):
    evens = []
    for number in numbers:
        if number% 2 == 0:
            evens.append(number)
    return evens

def square_all(numbers):
    squares = []
    for number in numbers:
        squares.append(number * number)
    return squares

def sum_all(numbers):
    return sum(numbers)

# Решение
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_all(square_all(filter_even(numbers)))
print(f"Сумма квадратов чётных чисел: {result}")

# Проверка по шагам:
print(f"Чётные: {filter_even(numbers)}")
print(f"Их квадраты: {square_all(filter_even(numbers))}")
print(f"Сумма: {sum_all(square_all(filter_even(numbers)))}")