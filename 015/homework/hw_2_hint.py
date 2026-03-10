servers = [
    {"name": "web1", "ip": "192.168.1.10", "status": "online"},
    {"name": "web2", "ip": "192.168.1.11", "status": "online"},
    {"name": "db1", "ip": "192.168.1.20", "status": "offline"},
    {"name": "cache1", "ip": "192.168.1.30", "status": "online"},
    {"name": "backup1", "ip": "192.168.1.40", "status": "offline"},
]

online_count = 0
offline_servers = []

for server in servers:
    if server["status"] == "online":
        online_count += 1
    else:
        offline_servers.append(server)

print(f"Всего серверов: {len(servers)}")
print(f"Доступно: {online_count}")
print(f"Недоступно: {len(offline_servers)}")

if offline_servers:
    print("\nПроблемные серверы:")
    for server in offline_servers:
        print(f"  {server['name']} ({server['ip']})")

# Процент доступности
availability = (online_count / len(servers)) * 100
print(f"\nДоступность: {availability:.1f}%")