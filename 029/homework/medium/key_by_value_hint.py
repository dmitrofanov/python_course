countries = {
    "Россия": "Москва",
    "Франция": "Париж",
    "Италия": "Рим",
    "Германия": "Берлин",
    "Испания": "Мадрид",
    "Португалия": "Лиссабон"
}

capital = input("Введите столицу для поиска: ")

found_countries = []
for country, cap in countries.items():
    if cap == capital:
        found_countries.append(country)

if found_countries:
    print(f"Столица {capital} принадлежит: {', '.join(found_countries)}")
else:
    print(f"Столица {capital} не найдена")