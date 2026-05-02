"""
Дан список слов. Сгруппируй их в словарь, где ключ — первая буква,
а значение — список слов, начинающихся с этой буквы.
"""

words = ["яблоко", "арбуз", "ананас", "банан", "вишня", "алыча", "груша"]

new_words = {}
for word in words:
    one_letter = word[0]
    if one_letter not in new_words:
        new_words[one_letter] = []
    new_words[one_letter].append(word)
print(new_words)
