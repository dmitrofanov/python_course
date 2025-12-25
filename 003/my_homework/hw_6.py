#Создать функцию, принимающую список оценок от 1 до 5, рассчитывающую среднюю оценку и печатающую среднюю оценку текстом ("кол", "два", "три", "четыре", "пять"). Использовать функцию созданную в задании 5.
def average_rating(numbers):
    for num in numbers:
        result = sum(numbers) / len(numbers)
    if result < 2:
        print('кол')
    elif result < 3:
        print('два')
    elif result < 4:
        print('три')
    elif result < 5:
        print('четыре')
    elif result == 5:
        print('пять')
    print(result)
average_rating([5, 5, 5, 5])