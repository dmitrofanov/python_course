#Создать функцию, печатающую таблицу умножения для заданного числа
def m_table(number):
    for i in range(1,10):
        result = number * i
        print(f"{number} * {i} = {result}")
m_table(5)
