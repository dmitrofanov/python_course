vowels = "аеёиоуыэюя"
words = ["кот", "собака", "ёж", "бегемот", "носорог", "лис", "слон", "кит"]

def count_vowels(word):
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

sorted_words = sorted(words, key=count_vowels)

print("Слова по возрастанию гласных:")
for word in sorted_words:
    print(f"  {word} ({count_vowels(word)} гласных)")