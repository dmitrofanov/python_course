# Функции.

def create_profile(name, age, city='msk', hobby):
    print(name, age, city, hobby)
create_profile('pavel',5,'MSK','it')
create_profile(age=5,name='pavel',city='spb',hobby='it')

# В функции выше name, age, city, hobby - это параметры. Внутри тела функции параметры работают как переменные и с ними можно делать всё тоже самое, что и с обычными переменными.

# Задания:
# 1) Создай функцию create_profile. Пусть она возвращает словарь, в котором ключами будут являться названия параметров, а значениями фактические аргументы переданные в функцию при вызове. Приведи два варианта, один с использованием функции dict, а другой с помощью литерала.
# 2) Создай функцию show_profile. Пусть она принимает словарь, в котором ожидаются ключи name, age, city, hobby и печатает красивую шапку, в формате:
'''
=== ВАШ ПРОФИЛЬ ===
Имя: Анна
Возраст: 25
Город: Сан-Франциско
Хобби: Рисование
'''
# 3) Объедини вызовы функций show_profile и create_profile. Возвращаемое значение функции create_profile должно попадать на вход функции show_profile.

def create_profile(name, age, city='msk', hobby='it'):
    return {'name': name, 'age': age, 'city': city, 'hobby': hobby}
def show_profile(profile):
    print('=== ВАШ ПРОФИЛЬ ===')
    print('Имя:',profile['name'])
    print('Возраст:',profile['age'])
    print('Город:',profile['city'])
    print('Хобби:',profile['hobby'])
show_profile(create_profile('pavel',5,'MSK','it'))
show_profile(create_profile(age=5,name='dima',city='spb',hobby='worker'))




# 4) Создай функцию ask_number. Функция должна принимать два параметра. Первый параметр это строка, которая показывается при запросе числе с помощью функции input. Второй параметр это тоже строка, которая показывается при ошибке приведения пользовательского ввода к числу. Функция ask_number должна работать пока пользователь не введёт валидное число и тогда она это число возвращает.

def ask_number(stroka1,stroka2):
    while True:
        try:
            chislo = int(input(stroka1))
            break
        except ValueError:
            print(stroka2)
    return chislo
print(ask_number('Введите число: ','Ошибка,это не число!'))