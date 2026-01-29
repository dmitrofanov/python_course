"""
ЗАДАЧА 1: Отфильтруй и преобразуй числа

Создай 3 функции:
1. filter_even(numbers) - возвращает список только чётных чисел
2. square_all(numbers) - возвращает список квадратов чисел
3. sum_all(numbers) - возвращает сумму всех чисел в списке

Создай цепочку, которая:
1) Фильтрует чётные числа из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2) Возводит их в квадрат
3) Считает сумму квадратов

Выполни в одну строку: sum_all(square_all(filter_even(исходный_список)))
"""

def filter_even(numbers):
    evens = list()
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

def square_all(numbers):
    squares = list()
    for number in numbers:
        squares.append(number ** 2)
    return squares

def sum_all(numbers):
    return sum(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_all(square_all(filter_even(numbers)))
print(f"Сумма квадратов чётных чисел: {result}")
          
