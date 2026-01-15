###############################################################
## Типы данных
###############################################################
# Переменные

## Коробка с этикеткой
age = 34
## Переклеивание этикетки
age = 42
## Множество этикеток
the_answer = 42

print(age == the_answer)
print(id(age), id(the_answer))
print(age is the_answer)

# Константы
THIS_IS_A_CONSTANT = 3.14
API_URL = 'https://someapiurl.com'

###############################################################
## Типы данных
###############################################################
## Изменяемые
### * Список - list
ids1 = [123, 234, 345]
print(ids1)
ids2 = list(ids1)
print(ids2)
print(ids1 == ids2, ids1 is ids2)

### Массив байтов - bytearray

### * Множество - set
moves1 = {12, 12, 12, 14, 15}
print(moves1)
moves2 = set(moves1)
print(moves2)
print(moves1 == moves2, moves1 is moves2)

### * Словарь - dict
response1 = {'code': 200, 'status': 'OK', 'payload': '<p>Hello there!</p>'}
print(response1)
response2 = dict(code=200, status='OK', payload='<p>Hello there!</p>')
print(response2) 
print(response1 == response2, response1 is response2)


## Не изменяемые

### * Булево значение - bool
is_active = True
is_closed = False
is_valid = True
print(is_active, is_closed, is_active == is_valid, is_active is is_valid)

### * Целое число - int
age = 34
thirty_four = 34
print(age, age == thirty_four, age is thirty_four)

### * Число с плавающей точкой - float
pi = 3.14
three_and_fourteen = 3.14
print(pi, pi == three_and_fourteen, pi is three_and_fourteen)

### Комплексное число - complex

### * Текстовая строка - str
greeting1 = 'Hello there!'
greeting2 = "Hello there!"
print(greeting1, greeting1 == greeting2, greeting1 is greeting2)


### * Кортеж - tuple
record1 = (123, 42, 50) # id, age, balance
print(record1)
record2 = 123, 42, 50
print(record2)
record3 = tuple([123, 42, 50])
print(record3)
print(record1 == record2, record2 == record3, record1 is record2, record2 is record3)
print(id(record2), id(record3))

### Байты - bytes

### Фиксированное множество - frozenset


###############################################################
## Вызов метода
###############################################################
fruits = ['banana', 'orange', 'apple']
print(fruits)
fruits.append('Pineapple')




###############################################################
## Задания
###############################################################
# Программа калькулятор для сложения двух чисел
input()
print

# Программа "Анкета". Спрашивает имя, возраст, город и выводит всё через f строку.
input()
name = 'Dima'
i_am_an_f_string = f'Hello {name}'
print(i_am_an_f_string)