"""
Дана строка. Создай список всех заглавных букв в ней.
"""

text = "ПрИвЕт МиР"

new_list= []
for symbol in text:
    if symbol.isupper() :
        new_list.append(symbol)
print(new_list)