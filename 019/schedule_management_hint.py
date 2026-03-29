schedule = {
    "понедельник": [
        {"name": "Математика", "time": "09:00", "teacher": "Иванова"},
        {"name": "Физика", "time": "10:30", "teacher": "Петров"},
        {"name": "Информатика", "time": "12:00", "teacher": "Сидоров"},
    ],
    "вторник": [
        {"name": "Русский язык", "time": "09:00", "teacher": "Смирнова"},
        {"name": "Литература", "time": "10:30", "teacher": "Смирнова"},
    ],
    "среда": [
        {"name": "Математика", "time": "09:00", "teacher": "Иванова"},
        {"name": "Химия", "time": "10:30", "teacher": "Кузнецов"},
        {"name": "Биология", "time": "12:00", "teacher": "Кузнецов"},
        {"name": "Физкультура", "time": "13:30", "teacher": "Орлов"},
    ],
    "четверг": [
        {"name": "История", "time": "09:00", "teacher": "Васильев"},
        {"name": "Обществознание", "time": "10:30", "teacher": "Васильев"},
    ],
    "пятница": [
        {"name": "Английский язык", "time": "09:00", "teacher": "Новикова"},
        {"name": "Математика", "time": "10:30", "teacher": "Иванова"},
        {"name": "Физика", "time": "12:00", "teacher": "Петров"},
    ],
}

print("=" * 50)
print("1. Занятия в понедельник:")
for lesson in schedule["понедельник"]:
    print(f"  {lesson['time']} - {lesson['name']} ({lesson['teacher']})")

print("\n2. День с максимальным количеством занятий:")
max_day = max(schedule.items(), key=lambda x: len(x[1]))
print(f"  {max_day[0]}: {len(max_day[1])} занятий")

print("\n3. Общее количество часов занятий в неделю:")
total_lessons = sum(len(lessons) for lessons in schedule.values())
total_hours = total_lessons * 1.5
print(f"  Всего занятий: {total_lessons}")
print(f"  Всего часов: {total_hours:.1f}")

print("\n4. Занятия, начинающиеся в 10:30:")
for day, lessons in schedule.items():
    for lesson in lessons:
        if lesson["time"] == "10:30":
            print(f"  {day}: {lesson['name']} ({lesson['time']})")