"""
ЗАДАНИЕ: Инвентаризация серверов

У DevOps-инженера есть список серверов с их характеристиками.
Нужно проанализировать этот список.

Данные: список словарей, где каждый сервер — это словарь с ключами:
- name: имя сервера
- cpu: количество ядер
- ram: объем RAM в ГБ
- disk: объем диска в ГБ
- status: online/offline

Задачи:
1. Выведи имена всех серверов
2. Посчитай общее количество ядер CPU
3. Найди сервер с максимальной RAM
4. Выведи имена offline серверов
5. Посчитай средний объем диска
"""

servers = [
    {"name": "web1", "cpu": 4, "ram": 16, "disk": 256, "status": "online"},
    {"name": "web2", "cpu": 4, "ram": 16, "disk": 256, "status": "online"},
    {"name": "db1", "cpu": 8, "ram": 32, "disk": 1024, "status": "online"},
    {"name": "backup1", "cpu": 2, "ram": 8, "disk": 2048, "status": "offline"},
    {"name": "cache1", "cpu": 2, "ram": 4, "disk": 64, "status": "online"},
]

# Твои решения:
for server in servers:
    print(f'Имя сервера: {server["name"]}')

total = 0
# for server in servers:
#     x = server["cpu"]
#     total += x
# print(f'Общее количество ядер: {total}')
print(f'Общее количество ядер: {sum([server["cpu"] for server in servers])}')

name_server = None
max_ram = 0
for server in servers:
    if server["ram"] > max_ram:
        max_ram = server["ram"] 
        name_server = server["name"]
print(f'Сервер с max ram: {name_server}')

for server in servers:
    if server["status"] == "offline":
        print(f'Сервер не в сети: {server["name"]}')

total = 0
for server in servers:
    x = server["disk"]
    total += x
quantity = total /len(servers)
print(f'Средний объем диска {quantity}')
    

    



