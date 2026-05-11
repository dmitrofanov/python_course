"""
Дан словарь. Запроси у пользователя ключ.
Если ключ есть — выведи значение, если нет — выведи "Ключ не найден".
"""

user_data = {"name": "Анна", "age": 25, "city": "Москва"}

key_input = input("Введите ключ в словаре: ")

if key_input in user_data.keys():
    print(user_data[key_input])
else:
    print("Ключ не найден")