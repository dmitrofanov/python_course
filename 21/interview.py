students = {}
students['students'] = [
    {'name': 'Анна', 'age': 20, 'courses': [
        {'name': 'Math', 'grade': 5},
        {'name': 'English', 'grade': 4}
    ]},
    {'name': 'Пётр', 'age': 25, 'courses': [
        {'name': 'Math', 'grade': 3},
        {'name': 'English', 'grade': 5}
    ]}
]

#посчитать количество студентов
print(len(students['students']))

#средний возраст
total = 0
for student in students['students']:
    total += student["age"]
avg = total / len(students['students'])
print(avg)

#или

print(sum(student["age"] for student in students['students']) / len(students['students']))

#посчитать средний балл по математике

total = 0
count = 0
for student in students['students']:
    for course in student["courses"]:
        if course["name"] == "Math":
            total += course["grade"]
            count += 1
print(f'средний балл по математике: {total / count}')
