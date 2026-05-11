scores = {"математика": 85, "физика": 92, "химия": 78, "биология": 88}

total = sum(scores.values())
print(f"Сумма оценок: {total}")
print(f"Средний балл: {total / len(scores):.1f}")