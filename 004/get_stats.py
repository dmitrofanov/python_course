# Функция get_stats(text)
#     Написать функцию, которая принимает строку text и возвращает словарь со статистикой:
#         length — общее количество символов.
#         words — количество слов (разбить по пробелам).
#         uppercase — количество заглавных букв. (char.isupper())
#     Что тренируем: Работу со строками, цикл for, условный if, создание и возврат словаря.
def get_stats(text):
    # stats = {}
    length = len(text)
    words = len(text.split(' '))
    uppercase = 0
    for char in text:
        if char.isupper():
            uppercase += 1
    # stats['lenght'] = length
    # stats['words'] = words
    # stats['uppercase'] = uppercase
    return dict(hh = length, bb = words, xx = uppercase)
#    return {'lenght': length, 'words': words, 'uppercase': uppercase}

print(get_stats('Privet Pavel'))
     