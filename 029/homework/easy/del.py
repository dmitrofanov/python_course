"""
Дан словарь. Удали ключ, который вводит пользователь.
Если ключа нет — выведи сообщение.
"""

student = {"name": "Ольга", "age": 22, "group": "A-101", "grade": 85}
key = input("Введите ключ для удаления: ")

if key in student:
    del student[key]
    print(f'Ключ {key} удален')
    print(f'Новый словарь {student}')
else:
    print(f'Ключа {key} нет в словаре')
    print(f'Словарь {student} остался прежним')
