# Блоки else и finally вместе

try:
    число = int(input("Введите число: "))
    результат = 10 / число
except ValueError: # Если не смогли преобразовать в int
    print("Это было не число!")
except ZeroDivisionError: # Если деление на ноль
    print("На ноль делить нельзя!")
else:
    print('Ошибок не было')
finally:
    print('Подчищаем за собой')