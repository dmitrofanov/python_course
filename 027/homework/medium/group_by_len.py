"""
Дан список слов. Сгруппируй их по длине слова:
ключ — длина, значение — список слов этой длины.
"""
words = ["кот", "собака", "слон", "бегемот", "носорог", "лис", "волк", "ёж"]

sorted_words = {}

for word in words:
    length_word= len(word)
    if length_word not in sorted_words:
        sorted_words[length_word] = []
    sorted_words[length_word].append(word)
print(sorted_words)