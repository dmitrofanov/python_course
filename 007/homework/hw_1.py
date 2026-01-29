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
    even_numbers = list()
    for even_number in numbers:
        if even_number % 2 == 0:
            even_numbers.append(even_number)
    return even_numbers

def square_all(filter_even):
    square_numbers = list()
    for square_number in filter_even:
        square_numbers.append(square_number ** 2)
    return square_numbers

def sum_all(square_all):
    total = 0
    for sum_number in square_all:
        total = total + sum_number
    return total

print(sum_all(square_all(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))))
          
