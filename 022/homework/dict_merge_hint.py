dict1 = {"a": 5, "b": 10, "c": 15}
dict2 = {"b": 3, "c": 7, "d": 20}

result = {}

# Сначала добавляем все из первого словаря
for key, value in dict1.items():
    result[key] = value

# Добавляем из второго: если ключ есть — суммируем
for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print("Результат:", result)