"""
Дан словарь с паролями пользователей. Добавь к каждому паролю
суффикс "_2025" и создай новый словарь.
"""

users = {
    "alice": "qwerty123",
    "bob": "password456",
    "charlie": "letmein789"
}

updated_users = {}
for username, password in users.items():
    updated_users[username] = password + "_2025"

print(f"Старые пароли: {users}")
print(f"Новые пароли: {updated_users}")