numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print("Исходный список:", numbers)

n = len(numbers)

for i in range(n - 1):
    # Ищем минимум в оставшейся части
    min_index = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    
    # Меняем местами
    if min_index != i:
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    
    print(f"Шаг {i+1}: {numbers}")

print("\nОтсортированный список:", numbers)