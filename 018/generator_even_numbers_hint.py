"""
Напиши генератор even_numbers(n), который выдаёт первые n чётных чисел.
"""
def even_numbers(n):
    for i in range(n):
        yield i * 2

# Тест
print("Первые 5 чётных чисел:")
for num in even_numbers(5):
    print(num)