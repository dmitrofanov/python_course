employees = [
    {"name": "Анна", "project": "Альфа"},
    {"name": "Иван", "project": "Бета"},
    {"name": "Анна", "project": "Гамма"},
    {"name": "Иван", "project": "Альфа"},
    {"name": "Мария", "project": "Бета"},
    {"name": "Анна", "project": "Дельта"},
]

# Преобразование
projects_by_name = {}
for emp in employees:
    name = emp["name"]
    project = emp["project"]
    
    if name not in projects_by_name:
        projects_by_name[name] = []
    projects_by_name[name].append(project)

print("Сотрудники и их проекты:")
for name, projects in sorted(projects_by_name.items()):
    print(f"  {name}: {', '.join(projects)}")