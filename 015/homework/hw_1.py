"""
ЗАДАЧА: Валидация конфигурационного файла

DevOps часто проверяет конфиги перед деплоем.
Проверь, что в конфиге есть все обязательные поля.
"""
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

# Твой алгоритм:
# 1. Пройди по всем обязательным полям
# 2. Проверь, что они есть в конфиге
# 3. Собери список отсутствующих