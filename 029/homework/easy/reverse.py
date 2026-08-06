"""
Дана строка. Переверни её, преобразовав в список и используя .reverse() и reversed().
"""

text = "привет мир"

text_list = list(text)
text_list.reverse()
print("".join(text_list))

print("".join(list(reversed(text))))