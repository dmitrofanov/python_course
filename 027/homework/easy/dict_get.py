"""
Дан словарь и список ключей. Для каждого ключа выведи значение,
а если ключа нет — выведи "Не найдено".
"""

user = {"name": "Иван", "age": 30, "city": "Питер"}
keys_to_check = ["name", "age", "email", "phone"]


for key in keys_to_check:
    value = user.get(key, 'Такого ключа нет')
    print(f'{key} - {value}')