"""
Дан список чисел. Построй словарь, где ключи — диапазоны,
а значения — список чисел из этих диапазонов.
Диапазоны: 0-9, 10-19, 20-29, 30-39, 40-49, 50+
"""

numbers = [5, 12, 23, 8, 35, 42, 15, 28, 7, 33, 45, 18, 52, 9, 37, 48, 55, 89]

ranges = {
    "0-9": [],
    "10-19": [],
    "20-29": [],
    "30-39": [],
    "40-49": [],
    "50+": []
}

for num in numbers:
    if num < 10:
        ranges["0-9"].append(num)
    elif num < 20:
        ranges["10-19"].append(num)
    elif num < 30:
        ranges["20-29"].append(num)
    elif num < 40:
        ranges["30-39"].append(num)
    elif num < 50:
        ranges["40-49"].append(num)
    else:
        ranges["50+"].append(num)

for key, value in ranges.items():
    print(key, value)