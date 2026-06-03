user = {"name": "Иван", "age": 30, "city": "Питер"}
keys_to_check = ["name", "age", "email", "phone"]

for key in keys_to_check:
    value = user.get(key, "Не найдено")
    print(f"{key}: {value}")