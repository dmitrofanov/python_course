word = "программирование"
letters = ["п", "р", "о", "г", "а", "м", "и", "с", "е", "н", "т"]

missing = []
for letter in letters:
    if letter not in word:
        missing.append(letter)

if missing:
    print(f"Отсутствуют буквы: {missing}")
else:
    print("Все буквы присутствуют в слове")