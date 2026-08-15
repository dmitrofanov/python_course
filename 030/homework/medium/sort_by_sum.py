"""
Дан список чисел. Отсортируй его по сумме цифр каждого числа.
"""

numbers = [123, 45, 67, 8, 91, 234, 56, 789]

def digit_sum(number):
    digit_sum = 0
    for digit in str(number):
        digit_sum += int(digit)

    return digit_sum


sorted_numbers = sorted(numbers, key=digit_sum)

print(f'Сумма отсортированная: {sorted_numbers}')

    