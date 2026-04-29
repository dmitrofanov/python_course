"""
ЗАДАЧА: Система голосования

Есть список голосов пользователей. Нужно:
1. Подсчитать голоса за каждого кандидата
2. Определить победителя (кого выбрало большинство)
3. Если есть ничья — вывести всех кандидатов с максимальным количеством голосов
4. Вывести процент голосов для каждого кандидата
"""

votes = [
    "Иванов", "Петров", "Сидоров", "Иванов", "Петров",
    "Иванов", "Кузнецов", "Сидоров", "Иванов", "Петров",
    "Петров", "Иванов", "Сидоров", "Кузнецов", "Иванов",
    "Петров", "Сидоров", "Иванов", "Петров", "Кузнецов", "Петров"
]

results = {}
for lastname in votes:
    results[lastname]= results.get(lastname,0) + 1
print(results)

max_votes = max(results.values())
for lastname,count in results.items():
    if count == max_votes:
        print(f'{lastname} - {max_votes}')

for lastname,count in results.items():
    s = count / len(votes) * 100
    print(lastname,s)
