"""
Дан список слов. Сгруппируй их по первой букве.
Внутри каждой группы слова должны быть отсортированы по алфавиту.
"""

words = ["яблоко", "арбуз", "банан", "ананас", "вишня", "алыча", "груша", "абрикос"]

groups = {}

for word in words:
    if word[0] in groups:
        groups[word[0]].append(word)
    else:
        groups[word[0]] = [word]

for letter in groups:
    groups[letter].sort()

print(groups)