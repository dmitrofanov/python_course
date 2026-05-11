numbers = [10, 5, 8, 20, 15, 20, 3]

largest = numbers[0]
second = None

for num in numbers[1:]:
    if num > largest:
        second = largest
        largest = num
    elif num != largest and (second is None or num > second):
        second = num

print(f"Список: {numbers}")
print(f"Второй по величине: {second}")