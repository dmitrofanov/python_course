def digit_sum(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

numbers = [123, 45, 67, 8, 91, 234, 56, 789]

sorted_numbers = sorted(numbers, key=digit_sum)

print("Сортировка по сумме цифр:")
for num in sorted_numbers:
    print(f"  {num} (сумма цифр: {digit_sum(num)})")