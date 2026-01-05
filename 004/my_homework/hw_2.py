# 2) Что хранят встроенные типы данных
#     Создать список. Добавить в него 4 элемента разных типов.
#     Создать множество. Добавить в него 4 элемента разных типов.
#     Создать словарь. Добавить в него 4 пары ключ-значение. Значения должны быть разных типов, ключи могут быть строками, числами или кортежами.
#     Создать кортеж. Добавить в него 4 элемента разных типов.

#Список

my_list = []
my_list.append(10)
my_list.append(3.14)
my_list.append("hello")
my_list.append(True)

print("Список:", my_list)

my_list = ['100', '77.7', 'hi' , 'False']
new_list = ['500' '99.9', 'new', 'True']
my_list.extend(new_list)

print('Список:', my_list)


#Множество

my_set = {'1000', 'QWERTY', '1.0', 'False'}
my_set.add(4)
my_set.add('privet')
my_set.add(',')
my_set.add('True')
print('Множество:', my_set)

#Словарь
my_dict = dict(code=200, status='OK',)
my_dict['Pavel'] = 'Rus'
my_dict['ab', 'cd', 'ef'] = 'xyz'
my_dict['1000.0'] = 2
my_dict['age'] = 36
print('Словарь: ',my_dict)

#Кортеж
my_tuple1 = ('123', 'abc', '10.0', 'True')
my_tuple2 = ('321', 'ABC', '20.00', 'False')
my_tuple1 += my_tuple2
print('Кортеж: ',my_tuple1)