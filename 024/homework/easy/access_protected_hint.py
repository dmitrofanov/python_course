user_data = {"name": "Анна", "age": 25, "city": "Москва"}

key = input("Введите ключ для поиска: ")

# Способ 1
if key in user_data:
    print(f"Значение: {user_data[key]}")
else:
    print("Ключ не найден")

# Способ 2 (более питоничный)
# print(user_data.get(key, "Ключ не найден"))