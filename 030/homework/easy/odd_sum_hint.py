numbers = [10, 20, 30, 40, 50, 60, 70, 80]

sum_odd = 0
for i in range(1, len(numbers), 2):
    sum_odd += numbers[i]

print(f"Сумма на нечётных индексах: {sum_odd}")