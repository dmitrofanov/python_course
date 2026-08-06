words = ["яблоко", "арбуз", "банан", "ананас", "вишня", "алыча", "груша", "абрикос"]

groups = {}
for word in words:
    first = word[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(word)

# Сортируем каждую группу
for letter in groups:
    groups[letter].sort()

print("Группировка по первой букве:")
for letter in sorted(groups.keys()):
    print(f"  {letter}: {', '.join(groups[letter])}")