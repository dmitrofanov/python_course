def infinite_counter():
    """Бесконечный счётчик"""
    n = 0
    while True:
        yield n
        n += 1

# Осторожно! Этот цикл бесконечный
counter = infinite_counter()
for i in counter:
    print(i)
    if i > 10:  # нужно условие выхода
        break

# Практический пример: бесконечная последовательность Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i, num in enumerate(fib):
    if i > 10:
        break
    print(f"fib({i}) = {num}")