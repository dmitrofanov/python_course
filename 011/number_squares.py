"""
ЗАДАЧА 1: Квадраты чисел

Есть список чисел: numbers = [1, 2, 3, 4, 5]

1. Обычным циклом for создай список squares1 с квадратами этих чисел
2. С помощью list comprehension создай список squares2 с квадратами
3. Сравни оба подхода

Потом сделай:
4. Квадраты только чётных чисел из исходного списка
5. Квадраты чисел, которые больше 2
"""


"""
Ожидаемый вывод:
Цикл: [1, 4, 9, 16, 25]
Comprehension: [1, 4, 9, 16, 25]
Квадраты чётных: [4, 16]
Квадраты > 2: [9, 16, 25]
"""

numbers = [1, 2, 3, 4, 5]
squares1 = []
for i in numbers:
    squares1.append(i ** 2)
print(squares1)

squares2 = [i ** 2 for i in numbers]
print(squares2)

squares3 = [i ** 2 for i in numbers if i % 2 == 0]
print(squares3)

squares4= [i ** 2 for i in numbers if i > 2]
print(squares4)


