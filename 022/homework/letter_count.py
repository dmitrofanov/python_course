"""
Дано слово. Подсчитай, сколько раз встречается каждая буква.
Напиши два варианта, с использованием Counter и без него.
"""

word = "программирование"


from collections import Counter
letter_count = Counter(word)
print(dict(letter_count))


count_dict = {}
for letter in word:
    if letter in count_dict:
        count_dict[letter] += 1
    else:
        count_dict[letter] = 1
print(count_dict)