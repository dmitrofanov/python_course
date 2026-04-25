"""
Дано два словаря. Объедини их в один.
Если ключи совпадают, значение должно быть суммой.
"""

dict1 = {"a": 5, "b": 10, "c": 15}
dict2 = {"b": 3, "c": 7, "d": 20}

new_dict = {}
for key, value in dict1.items():
    new_dict[key] = value

for key, value in dict2.items():
    if key in new_dict:
        new_dict[key] += value
    else:
        new_dict[key] = value
print(new_dict)