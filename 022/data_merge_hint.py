students = [
    {"id": 1, "name": "Анна"},
    {"id": 2, "name": "Иван"},
    {"id": 3, "name": "Мария"},
    {"id": 4, "name": "Петр"},
    {"id": 5, "name": "Ольга"},
]

grades = [
    {"student_id": 1, "grade": 5},
    {"student_id": 1, "grade": 4},
    {"student_id": 1, "grade": 5},
    {"student_id": 2, "grade": 4},
    {"student_id": 2, "grade": 3},
    {"student_id": 3, "grade": 5},
    {"student_id": 3, "grade": 5},
    {"student_id": 3, "grade": 4},
    {"student_id": 4, "grade": 3},
    {"student_id": 4, "grade": 2},
    {"student_id": 5, "grade": 5},
    {"student_id": 5, "grade": 4},
]

# Объединение данных
student_data = {}

for student in students:
    student_data[student["id"]] = {
        "name": student["name"],
        "grades": []
    }

for grade in grades:
    student_id = grade["student_id"]
    if student_id in student_data:
        student_data[student_id]["grades"].append(grade["grade"])

# Расчёт среднего балла
for student_id, data in student_data.items():
    grades_list = data["grades"]
    if grades_list:
        avg = sum(grades_list) / len(grades_list)
        data["average"] = avg
    else:
        data["average"] = 0

# Сортировка по среднему баллу
sorted_students = sorted(student_data.items(), key=lambda x: x[1]["average"], reverse=True)

print("Студенты и их успеваемость:")
print("-" * 50)
for student_id, data in sorted_students:
    print(f"{data['name']}: {data['grades']} -> средний балл {data['average']:.1f}")

# Лучший студент
best = sorted_students[0]
print(f"\nЛучший студент: {best[1]['name']} (средний балл {best[1]['average']:.1f})")