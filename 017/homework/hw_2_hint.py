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

warning_threshold = 10

print("Проверка дискового пространства:")
print("-" * 50)

server_total = {}

for server, disks in disk_data.items():
    print(f"\nСервер {server}:")
    server_free = 0
    
    for disk in disks:
        free = disk["free_gb"]
        server_free += free
        status = "✅" if free >= warning_threshold else "⚠️"
        print(f"  {status} {disk['mount']}: {free} ГБ свободно")
        
        if free < warning_threshold:
            print(f"    ⚠️  ВНИМАНИЕ: мало места на {disk['mount']}!")
    
    server_total[server] = server_free

print("\n" + "="*50)
print("Общее свободное место по серверам:")
for server, total in server_total.items():
    print(f"  {server}: {total} ГБ")

min_server = min(server_total.items(), key=lambda x: x[1])
print(f"\nСамый заполненный сервер: {min_server[0]} ({min_server[1]} ГБ всего)")