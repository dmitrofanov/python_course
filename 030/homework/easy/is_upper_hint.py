text = "ПрИвЕт МиР"

uppercase_letters = []
for char in text:
    if char.isupper():
        uppercase_letters.append(char)

print(f"Заглавные буквы: {uppercase_letters}")