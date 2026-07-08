grades = [95, 82, 67, 43, 91, 78, 55, 89, 73, 38, 60, 97, 84, 72, 59]

ranges = {
    "Отлично (>=90)": [],
    "Хорошо (70-89)": [],
    "Удовлетворительно (50-69)": [],
    "Плохо (<50)": []
}

for grade in grades:
    if grade >= 90:
        ranges["Отлично (>=90)"].append(grade)
    elif grade >= 70:
        ranges["Хорошо (70-89)"].append(grade)
    elif grade >= 50:
        ranges["Удовлетворительно (50-69)"].append(grade)
    else:
        ranges["Плохо (<50)"].append(grade)

print("Распределение оценок:")
for category, grades_list in ranges.items():
    count = len(grades_list)
    if count > 0:
        print(f"  {category}: {count} ({', '.join(map(str, grades_list))})")
    else:
        print(f"  {category}: {count}")