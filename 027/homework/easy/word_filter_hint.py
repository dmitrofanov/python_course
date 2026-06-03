words = ["кот", "собака", "ёж", "бегемот", "лис", "носорог", "кит"]

long_words = []
for word in words:
    if len(word) > 3:
        long_words.append(word)

print(f"Слова длиннее 3 букв: {long_words}")