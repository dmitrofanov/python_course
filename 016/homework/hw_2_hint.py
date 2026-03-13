servers = [
    {"name": "web1", "cpu": 4, "ram": 16, "disk": 256, "status": "online"},
    {"name": "web2", "cpu": 4, "ram": 16, "disk": 256, "status": "online"},
    {"name": "db1", "cpu": 8, "ram": 32, "disk": 1024, "status": "online"},
    {"name": "backup1", "cpu": 2, "ram": 8, "disk": 2048, "status": "offline"},
    {"name": "cache1", "cpu": 2, "ram": 4, "disk": 64, "status": "online"},
]

print("Имена серверов:", [server["name"] for server in servers])

total_cpu = sum(server["cpu"] for server in servers)
print(f"Всего ядер CPU: {total_cpu}")

max_ram_server = max(servers, key=lambda s: s["ram"])
print(f"Сервер с максимальной RAM: {max_ram_server['name']} ({max_ram_server['ram']} ГБ)")

offline_servers = [s["name"] for s in servers if s["status"] == "offline"]
print(f"Offline серверы: {offline_servers}")

avg_disk = sum(s["disk"] for s in servers) / len(servers)
print(f"Средний объем диска: {avg_disk:.0f} ГБ")