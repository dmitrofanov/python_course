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

# 1. Серверы с Python
python_servers = []
for server, apps in software.items():
    if any(app["name"] == "python" for app in apps):
        python_servers.append(server)

print("Серверы с Python:", python_servers)

# 2. Уникальные версии Python
python_versions = set()
for apps in software.values():
    for app in apps:
        if app["name"] == "python":
            python_versions.add(app["version"])

print("Версии Python:", sorted(python_versions))

# 3. ПО на каждом сервере
print("\nПО на серверах:")
for server, apps in software.items():
    app_list = [f"{app['name']} {app['version']}" for app in apps]
    print(f"  {server}: {', '.join(app_list)}")

# 4. Устаревший Python (< 3.9)
old_python_servers = []
for server, apps in software.items():
    for app in apps:
        if app["name"] == "python":
            version = float(app["version"])
            if version < 3.9:
                old_python_servers.append(server)
                break

print(f"\nСерверы с Python < 3.9: {old_python_servers}")