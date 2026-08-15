"""
Дано два словаря. Объедини их так, чтобы при совпадении ключей
значение из второго словаря перезаписывало значение из первого.
"""

dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"b": 10, "d": 20, "e": 30, "f": 40}

result1 = {}

for key_1, value_1 in dict1.items():
    result1[key_1] = value_1

for key_2, value_2 in dict2.items():
    result1[key_2] = value_2

print(result1)

#или

result2 = dict1.copy()
for key, value in dict2.items():
    result2[key] = value

print(result2)


