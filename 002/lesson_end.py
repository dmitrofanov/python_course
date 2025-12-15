secret = 100
answer =int(input('Введите число: '))
while secret != answer:
    if answer > secret:
            print('Попробуйте уменьшить.')
    elif answer < secret:
            print('Попробуйте увеличить.')
    answer = int(input('Введите число: '))
print('Вы угадали')

