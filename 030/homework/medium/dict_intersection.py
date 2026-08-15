"""
Дано два словаря. Найди ключи, значения которых совпадают.
Пример: {'a': 1, 'b': 2, 'c': 3} и {'d': 2, 'e': 1, 'f': 4} → {'a': 1, 'b': 2}
"""

dict_a = {"a": 1, "b": 2, "c": 3, "d": 4}
dict_b = {"x": 2, "y": 4, "z": 6, "w": 1}

result = {}

for key_a, value_a in dict_a.items():
    if value_a in dict_b.values():
        result[key_a] = value_a
print(result)

