words = ["кот", "собака", "слон", "бегемот", "носорог", "лис", "волк", "ёж"]

groups = {}
for word in words:
    length = len(word)
    if length not in groups:
        groups[length] = []
    groups[length].append(word)

print("Группировка по длине:")
for length in sorted(groups.keys()):
    print(f"  {length} букв(ы): {', '.join(groups[length])}")