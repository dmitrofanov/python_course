vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
text = input("Введите строку: ")

count = 0
for char in text:
    if char in vowels:
        count += 1

print(f"Количество гласных: {count}")