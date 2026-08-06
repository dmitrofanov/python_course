"""
Дан список слов. Отсортируй их по количеству гласных букв
(от наименьшего к наибольшему).
"""

vowels = "аеёиоуыэюя"
words = ["кот", "собака", "ёж", "бегемот", "носорог", "лис", "слон", "кит"]

def vowel_count(word):
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

print(sorted(words, key=vowel_count))
