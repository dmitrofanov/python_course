votes = [
    "Иванов", "Петров", "Сидоров", "Иванов", "Петров",
    "Иванов", "Кузнецов", "Сидоров", "Иванов", "Петров",
    "Петров", "Иванов", "Сидоров", "Кузнецов", "Иванов",
    "Петров", "Сидоров", "Иванов", "Петров", "Кузнецов"
]

# Подсчёт голосов
results = {}
for vote in votes:
    results[vote] = results.get(vote, 0) + 1

total_votes = len(votes)

print("Результаты голосования:")
print("-" * 40)

# Сортируем по убыванию голосов
sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

for candidate, count in sorted_results:
    percent = (count / total_votes) * 100
    print(f"{candidate}: {count} голосов ({percent:.1f}%)")

# Определяем победителя
max_votes = max(results.values())
winners = [candidate for candidate, count in results.items() if count == max_votes]

print("\n" + "=" * 40)
if len(winners) == 1:
    print(f"Победитель: {winners[0]} ({max_votes} голосов)")
else:
    print(f"Ничья между: {', '.join(winners)} ({max_votes} голосов)")