word = "программирование"

# Ручной способ
letter_count = {}

for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print("Частота букв:")
for letter, count in letter_count.items():
    print(f"  '{letter}': {count}")

# С помощью класса Counter
from collections import Counter
letter_count = Counter(word)
print("Частота букв:")
for letter, count in letter_count.items():
    print(f"  '{letter}': {count}")
