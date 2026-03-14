# ЗАДАНИЕ: Проверка конфигурации сервисов

# DevOps часто валидирует конфигурации перед запуском сервисов.
# Есть конфигурация:

config = {
    "services": {
        "nginx": {
            "port": 80,
            "enabled": True
        },
        "postgres": {
            "port": 5432
            # отсутствует enabled
        },
        "redis": {
            # отсутствует port
            "enabled": True
        }
    }
}

# Обязательные поля для каждого сервиса:
# required_fields = ["port", "enabled"]
# Что нужно сделать
# Напиши код, который:
# 1️⃣ Пройдёт по всем сервисам в config["services"]
# 2️⃣ Проверит, что у каждого сервиса есть поля: port,enabled
# 3️⃣ Соберёт список отсутствующих полей

required_fields = ["port", "enabled"]
missing_fields = []
for service_name, service_config in config["services"].items():
    for field in required_fields:
        if field not in service_config:
            missing_fields.append(f"{service_name}.{field}")

if missing_fields:
    print("Конфиг сервисов не валиден:")
    for field in missing_fields:
        print(f"- {field}")
else:
    print("Конфиг валиден")

