"""
ЗАДАНИЕ: Анализ версий ПО

DevOps собирает информацию об установленных версиях ПО на серверах.
Дан словарь server -> список софта (каждый софт — словарь с name и version)

Нужно:
1. Найти все серверы, где установлен Python
2. Найти все уникальные версии Python
3. Для каждого сервера вывести список установленного ПО
4. Найти серверы с устаревшей версией (Python < 3.9)
"""

software = {
    "web1": [
        {"name": "nginx", "version": "1.22"},
        {"name": "python", "version": "3.8"},
        {"name": "node", "version": "16.5"},
    ],
    "web2": [
        {"name": "nginx", "version": "1.24"},
        {"name": "python", "version": "3.11"},
        {"name": "java", "version": "11"},
    ],
    "db1": [
        {"name": "postgres", "version": "14"},
        {"name": "python", "version": "3.9"},
        {"name": "redis", "version": "6.2"},
    ],
    "backup1": [
        {"name": "python", "version": "3.6"},
        {"name": "bash", "version": "5.1"},
    ],
}

# Твоё решение:
