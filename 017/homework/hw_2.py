"""
ЗАДАНИЕ: Мониторинг дисков

Система мониторинга собирает данные о свободном месте на дисках.
Нужно определить, на каких серверах заканчивается место.

Данные: словарь server -> список дисков (каждый диск — словарь с mount_point и free_gb)

Задачи:
1. Пройди по всем серверам
2. Для каждого сервера проверь все диски
3. Если свободного места меньше 10 ГБ — выведи предупреждение
4. Посчитай общее свободное место на каждом сервере
5. Найди сервер с минимальным свободным местом
"""

disk_data = {
    "web1": [
        {"mount": "/", "free_gb": 15},
        {"mount": "/var", "free_gb": 8},
        {"mount": "/tmp", "free_gb": 12},
    ],
    "db1": [
        {"mount": "/", "free_gb": 25},
        {"mount": "/data", "free_gb": 6},
        {"mount": "/backup", "free_gb": 45},
    ],
    "backup1": [
        {"mount": "/", "free_gb": 5},
        {"mount": "/storage", "free_gb": 120},
    ],
}

# Твоё решение:
name_server = None
min_space = float("inf")
for server in disk_data:
    print(server)
    free_space = 0
    for disk in disk_data[server]:
        # print(disk)
        if disk["free_gb"] < 10:
            print(f'Мало места на диске {disk["mount"]} на сервере {server}')
        free_space += disk["free_gb"]
    if free_space < min_space:
        name_server = server
        min_space = free_space
    print(f'Общее свободное место на сервере: {server} {free_space}')
    print(f'Минимальное свободное место на дисках {min_space} на сервере {name_server}')


    
