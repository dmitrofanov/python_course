users = {
    "alice": "qwerty123",
    "bob": "password456",
    "charlie": "letmein789"
}

updated_users = {}
for username, password in users.items():
    updated_users[username] = password + "_2025"

# или

updated_users = {
    username: password + '_2025'
    for username, password in users.items()
}

print(f"Старые пароли: {users}")
print(f"Новые пароли: {updated_users}")