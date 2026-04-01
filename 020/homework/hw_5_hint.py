phone_book = {}

# Добавляем контакты
phone_book["Анна"] = "12345"
phone_book["Иван"] = "67890"
phone_book["Мария"] = "11111"

print("Номер Анны:", phone_book["Анна"])

# Добавляем Петра
phone_book["Петр"] = "55555"

# Меняем номер Ивана
phone_book["Иван"] = "99999"

# Выводим все контакты
print("\nВсе контакты:")
for name, phone in phone_book.items():
    print(f"  {name}: {phone}")