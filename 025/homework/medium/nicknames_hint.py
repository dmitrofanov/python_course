adjectives = ["Хитрый", "Быстрый", "Тихий", "Смелый", "Весёлый"]
nouns = ["Лис", "Волк", "Ёж", "Кот", "Пёс"]

nicknames = []
for adj in adjectives:
    for noun in nouns:
        nicknames.append(adj + noun)

# Берём первые 10 (можно перемешать)
print("Примеры никнеймов:")
for nick in nicknames[:10]:
    print(f"  {nick}")