temperatures = [18, 22, 25, 19, 23, 21, 20]

average = sum(temperatures) / len(temperatures)
print(f"Средняя температура: {average:.1f}°C")

max_temp = max(temperatures)
min_temp = min(temperatures)
print(f"Максимальная: {max_temp}°C")
print(f"Минимальная: {min_temp}°C")

hot_days = 0
for temp in temperatures:
    if temp > 20:
        hot_days += 1
print(f"Дней с температурой >20°C: {hot_days}")