#Создать функцию, принимающую список оценок от 1 до 5 и возвращающую среднюю оценку
def average_rating(numbers):
    for num in numbers:
        result = sum(numbers) / len(numbers)
        return result
print(average_rating([5, 4, 5, 1]))