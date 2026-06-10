"""
Дан список слов. Оставь только те слова, длина которых больше 3 букв.
"""

words = ["кот", "собака", "ёж", "бегемот", "лис", "носорог", "кит"]

# for word in words:
#     if len(word) > 3:
#         print(word)

[print(word) for word in words if len(word) > 3]