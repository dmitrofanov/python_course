words = ["кот", "собака", "слон", "бегемот", "носорог"]

longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"Самое длинное слово: {longest_word} ({len(longest_word)} букв)")