students = {}
students['students'] = [
    {'name': 'Анна', 'age': 20, 'courses': [
        {'name': 'Math', 'grade': 5},
        {'name': 'English', 'grade': 4}
    ]},
    {'name': 'Пётр', 'age': 25, 'courses': [
        {'name': 'Math', 'grade': 3},
        {'name': 'English', 'grade': 5},
        {'name': 'Literacture', 'grade': 5}
    ]}
]
from collections import defaultdict
students = students['students']
course_stats = defaultdict(list)
for student in students:
    for course in student['courses']:
        course_stats[course['name']].append(course['grade'])
# print(course_stats)
for course in course_stats:
    print(f'Средняя оценка по {course}: {sum(course_stats[course]) / len(course_stats[course]):.2f}')
courses_total = sum(grade for grades in course_stats.values() for grade in grades)
courses_count = sum(len(grades) for grades in course_stats.values())
if courses_count:
    print(f'Средняя оценка по всем курсам: {courses_total / courses_count:.2f}')
else:
    print('Список студентов пуст, либо нет данных о предметах')