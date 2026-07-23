"""
Дан словарь. Найди ключ, соответствующий заданному значению.
Если значений несколько — верни все ключи.
"""

countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Италия": "Рим",
    "Германия": "Берлин",
    "Испания": "Мадрид",
    "Португалия": "Лиссабон"
}
city = input("Введите город: ")

# new_dict = []
# for key, value in countries.items():
#     if value == city:
#         new_dict.append(key)
# print(new_dict)

#или
result = [key for key, value in countries.items() if value == city]
print(result)