"""
ЗАДАЧА: Объединение данных о студентах

Есть два списка:
1. Список студентов с ID и именами
2. Список оценок с ID студента и оценкой

Нужно:
1. Объединить данные в один словарь: ID -> {name, grades}
2. Для каждого студента посчитать средний балл
3. Вывести всех студентов, отсортированных по среднему баллу
4. Найти студента с максимальным средним баллом
"""

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

student_data = {}
for student in students:
    student_data[student["id"]] = {"name":student["name"], "grades": []}

for grade in grades:
    student_grade = student_data[grade["student_id"]]
    student_grade["grades"].append(grade["grade"])

for id,data in student_data.items():
    sum_grades = sum(data["grades"])
    grades_count =len(data["grades"])
    avg = sum_grades / grades_count
    data["avg_grade"] = avg

sorted_students = sorted(student_data.values(),key= lambda x: x["avg_grade"],reverse=True)
print([f'Средняя оценка: {student["name"]} - {student["avg_grade"]}' for student in sorted_students])

top_student = max(sorted_students,key = lambda x : x["avg_grade"])
print(f'Max grade : {top_student["name"]}, {top_student["avg_grade"]}')


print(student_data)

