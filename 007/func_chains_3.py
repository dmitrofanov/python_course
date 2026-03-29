"""
ЗАДАЧА 3: Математический конвейер

Напиши 3 маленькие функции:
1. square(x) - возвращает квадрат числа
2. increment(x) - возвращает число + 1
3. half(x) - возвращает половину числа

Вычисли выражение: increment(square(half(10)))

По шагам:
1) half(10) = 5
2) square(5) = 25
3) increment(25) = 26

Сделай так, чтобы программа выводила каждый промежуточный шаг
"""

def square(x):
    y = x ** 2
    print('square', y)
    return y

def increment(x):
    y = x + 1
    print('increment', y)
    return y

def half(x):
    y = x / 2
    print('half', y)
    return y

print(increment(square(half(10))))