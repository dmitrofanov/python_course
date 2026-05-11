"""
Дан список словарей с данными о сотрудниках.
Нужно создать словарь, где ключ — имя сотрудника,
а значение — список его проектов.
"""

employees = [
    {"name": "Анна", "project": "Альфа"},
    {"name": "Иван", "project": "Бета"},
    {"name": "Анна", "project": "Гамма"},
    {"name": "Иван", "project": "Альфа"},
    {"name": "Мария", "project": "Бета"},
    {"name": "Анна", "project": "Дельта"},
]

project_dict = {}

for employee in employees:
    name = employee["name"]
    project = employee["project"]
    
    if name not in project_dict:
        project_dict[name] = []
    
    project_dict[name].append(project)

print(project_dict)