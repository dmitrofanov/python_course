data = {
    "a": 1, "b": 2, "c": 1, "d": 3, "e": 2,
    "f": 1, "g": 4, "h": 2, "i": 1, "j": 5
}

# Подсчитываем частоту значений
value_freq = {}
for value in data.values():
    value_freq[value] = value_freq.get(value, 0) + 1

# Находим максимальную частоту
max_freq = max(value_freq.values())

# Собираем значения с максимальной частотой
most_frequent = [value for value, freq in value_freq.items() if freq == max_freq]

print(f"Словарь: {data}")
print(f"Самые частые значения: {most_frequent} (встречаются {max_freq} раза)")