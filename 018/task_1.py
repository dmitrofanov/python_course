"""
Напиши генератор even_numbers(n), который выдаёт первые n чётных чисел.
"""

def even_numbers(n):
    for i in range(n):
        yield i * 2
print(list(even_numbers(10)))