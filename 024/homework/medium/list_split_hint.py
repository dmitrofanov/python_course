numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

even = []
odd = []
multiple_of_three = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
    
    if num % 3 == 0:
        multiple_of_three.append(num)

print(f"Чётные: {even}")
print(f"Нечётные: {odd}")
print(f"Кратные 3: {multiple_of_three}")