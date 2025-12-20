## 1. Написать программу которая выводит таблицу умножения для заданного числа

# number = int(input('Введите число для таблицы умножения: '))
# for i in range(1,10):
#     result = number * i
#     print(f"{number} * {i} = {result}")

# 2. «Умный анализатор списка»
#     Запрашивает у пользователя числа через запятую, преобразует в список.
#     Используя цикл for, находит:
#         Сумму всех чисел.
#         Максимальное и минимальное число (без max()/min()!).
#         Количество чётных чисел (через if и %).
#     Усложнение: Вывести числа, которые больше среднего арифметического всего списка.

# numbers = input('Введите числа через запятую : ')
# numbers_list = numbers.split(',')
# total = 0
# for number in numbers_list:
#     total += int(number)
# print(f'Сумма чисел: {total}')


# x = float('-inf')
# for number in numbers_list:
#     if int(number) > x:
#         x = int(number)
# print(f'Максимальное число: {x}')
# for number in numbers_list:
#     if int(number) < x:
#         x = int(number)
# print(f'Минимальное число: {x}')

# even_number = 0
# for number in numbers_list:
#     if int(number) %2 == 0:
#         even_number += 1
# print(f'Количество четных чисел : {even_number}')


# count = 0
# for number in numbers_list:
#     count += 1
# average_sum = total / count
# z = 0
# for number in numbers_list:
#     if int(number) > average_sum:
#         z = int(number)
# print(f'Число больше среднего арифмитического: {z}')


# 3. «Поисковик дубликатов»
#     Дан список: items = ["яблоко", "банан", "киви", "яблоко", "апельсин", "банан", "яблоко"].
#     С помощью вложенных циклов for (или for и оператора in) найти и вывести все элементы, которые встречаются больше одного раза, но каждый дубликат вывести только один раз (например, "яблоко, банан").

items = ["яблоко", "банан", "киви", "яблоко", "апельсин", "банан", "яблоко"]
