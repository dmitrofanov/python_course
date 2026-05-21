games = [
    ("Анна", "Иван"),
    ("Мария", "Петр"),
    ("Анна", "Мария"),
    ("Иван", "Петр"),
    ("Анна", "Петр"),
    ("Мария", "Иван"),
]

wins = {}
for winner, loser in games:
    wins[winner] = wins.get(winner, 0) + 1

print("Количество побед:")
for player, count in sorted(wins.items(), key=lambda x: x[1], reverse=True):
    print(f"  {player}: {count}")