words = ["яблоко", "арбуз", "ананас", "банан", "вишня", "алыча", "груша"]

groups = {}
for word in words:
    first_letter = word[0]
    if first_letter not in groups:
        groups[first_letter] = []
    groups[first_letter].append(word)

print("Группировка по первой букве:")
for letter, word_list in sorted(groups.items()):
    print(f"  {letter}: {', '.join(word_list)}")