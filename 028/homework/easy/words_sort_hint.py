words = ["собака", "ёж", "бегемот", "кот", "носорог", "лис"]

sorted_words = sorted(words, key=len)

print(f"Исходный: {words}")
print(f"Отсортировано по длине: {sorted_words}")