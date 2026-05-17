"""
Дан список чисел и два пустых списка. Распредели числа:
- чётные числа в один список
- нечётные числа в другой список
- числа, кратные 3, дополнительно отметь (например, добавить в третий список)
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

even_numbers = []
odd_numbers = []
multiples = []

for n in numbers:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
    
    if n % 3 == 0:
        multiples.append(n)
    

print(even_numbers)
print(odd_numbers)
print(multiples)

