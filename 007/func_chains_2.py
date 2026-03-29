"""
ЗАДАЧА 2: Обработка текста

1. Напиши функцию make_upper(text), которая возвращает текст в ВЕРХНЕМ регистре
2. Напиши функцию add_farewell(text), которая добавляет " прощай!!!" в конец

Протестируй:
1) Сделай "привет" громким и добавь прощание: 
   add_farewell(make_upper("привет"))
2) Что будет, если поменять порядок?
   make_upper(add_farewell("привет"))
   
Подумай: почему результаты разные?
"""

def make_upper(text):
    return text.upper()
def add_farewell(text):
    return text + " прощай!!!"
print(add_farewell(make_upper("привет")))
print(make_upper(add_farewell("привет")))