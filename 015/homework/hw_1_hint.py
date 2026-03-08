config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        # "username" отсутствует!
        "password": "secret"
    },
    "server": {
        "port": 8080
        # "workers" отсутствует!
    }
}

required_fields = [
    ("database", "host"),
    ("database", "port"),
    ("database", "username"),
    ("database", "password"),
    ("server", "port"),
    ("server", "workers"),
]

# Решение:
missing_fields = []

for section, field in required_fields:
    if section not in config:
        missing_fields.append(f"{section} (секция отсутствует)")
    elif field not in config[section]:
        missing_fields.append(f"{section}.{field}")

if missing_fields:
    print("❌ Конфиг невалиден! Отсутствуют поля:")
    for field in missing_fields:
        print(f"  - {field}")
else:
    print("✅ Конфиг валиден")