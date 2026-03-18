"""
ЗАДАНИЕ: Группировка серверов по ролям

У DevOps есть список серверов, и каждый сервер имеет роль.
Нужно сгруппировать их по ролям для удобства управления.

Данные: список серверов (каждый сервер — словарь с именем и ролью)

Задачи:
1. Создай пустой словарь by_role = {}
2. Пройди по всем серверам
3. Для каждого сервера возьми его роль
4. Добавь имя сервера в список для этой роли
5. Выведи результат: роль -> список серверов
"""

servers = [
    {"name": "web1", "role": "web"},
    {"name": "web2", "role": "web"},
    {"name": "db1", "role": "database"},
    {"name": "db2", "role": "database"},
    {"name": "cache1", "role": "cache"},
    {"name": "backup1", "role": "backup"},
    {"name": "web3", "role": "web"},
]

# Твоё решение:
by_role = {}

for server in servers:
    role = server["role"]
    name = server["name"]
    
    if role not in by_role:
        by_role[role] = []
    by_role[role].append(name)

print(by_role)