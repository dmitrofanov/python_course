grades = {
    "Анна": [5, 4, 5],
    "Иван": [3, 4, 4],
    "Мария": [5, 5, 4, 3]
}

# Каркас функции add_grade:
def add_grade(student, grade):
    if student in grades:
        grades[student].______(grade)
    else:
        grades[student] = [grade]  # создаём новый список с одной оценкой

# Каркас функции get_average:
def get_average(student):
    if student in grades:
        grade_list = grades[student]
        average = ______(grade_list) / ______(grade_list)
        return average
    else:
        return 0