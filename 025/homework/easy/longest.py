"""
Дан список слов. Найди самое длинное слово и его длину.
"""
words = ["кот", "собака", "слон", "бегемот", "носорог"]
max_word= words[0]
for word in words:
    if len(word) > len(max_word):
        max_word= word

print(f"Длинное слово: {max_word} ; Длина слова {len(max_word)}")