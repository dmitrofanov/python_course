servers = [
    {"name": "web1", "role": "web"},
    {"name": "web2", "role": "web"},
    {"name": "db1", "role": "database"},
    {"name": "db2", "role": "database"},
    {"name": "cache1", "role": "cache"},
    {"name": "backup1", "role": "backup"},
    {"name": "web3", "role": "web"},
]

by_role = {}

for server in servers:
    role = server["role"]
    name = server["name"]
    
    if role not in by_role:
        by_role[role] = []
    by_role[role].append(name)

print("Серверы по ролям:")
for role, names in sorted(by_role.items()):
    print(f"  {role}: {', '.join(names)} (всего: {len(names)})")