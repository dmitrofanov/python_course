original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2, "f": 1, "g": 4}

inverted = {}
for key, value in original.items():
    if value not in inverted:
        inverted[value] = []
    inverted[value].append(key)

# Убираем списки для уникальных значений
result = {}
for value, keys in inverted.items():
    if len(keys) == 1:
        result[value] = keys[0]
    else:
        result[value] = keys

print(f"Исходный словарь: {original}")
print(f"Инвертированный: {result}")