student = {"name": "Ольга", "age": 22, "group": "A-101", "grade": 85}
key = input("Введите ключ для удаления: ")

if key in student:
    del student[key]
    print(f"Ключ '{key}' удалён")
    print(f"Словарь после удаления: {student}")
else:
    print(f"Ключ '{key}' не найден")