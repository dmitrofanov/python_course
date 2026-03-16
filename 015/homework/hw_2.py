"""
ЗАДАЧА: Мониторинг доступности серверов

DevOps должен регулярно проверять, какие серверы доступны.
Напиши программу, которая имитирует ping и сообщает о недоступных серверах.
"""
servers = [
    {"name": "web1", "ip": "192.168.1.10", "status": "online"},
    {"name": "web2", "ip": "192.168.1.11", "status": "online"},
    {"name": "db1", "ip": "192.168.1.20", "status": "offline"},
    {"name": "cache1", "ip": "192.168.1.30", "status": "online"},
    {"name": "backup1", "ip": "192.168.1.40", "status": "offline"},
]

# Твой алгоритм:
# 1. Пройди по всем серверам
# 2. Проверь статус
# 3. Собери статистику и недоступные серверы

# Решение:

offline_servers=[]
online_count=0
offline_count=0

for server in servers:
    if server["status"] == "online":
        online_count += 1
    elif server["status"] == "offline":
        offline_count += 1
        offline_servers.append(server["name"])

print(f"Всего серверов {online_count + offline_count}")  
print(f"Серверов онлайн: {online_count}")
print(f"Серверов оффлайн: {offline_count}")

print("Недоступны сервера:")
for offline_server in offline_servers:
    print(f'- {offline_server}')



