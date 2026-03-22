"""
ЗАДАНИЕ: Анализ версий ПО

DevOps собирает информацию об установленных версиях ПО на серверах.
Дан словарь server -> список софта (каждый софт — словарь с name и version)

Нужно:
1. Найти все серверы, где установлен Python
2. Найти все уникальные версии Python
3. Для каждого сервера вывести список установленного ПО
4. Найти серверы с устаревшей версией (Python < 3.9)
"""

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
        {"name": "sql", "version": "3.9"},
        {"name": "redis", "version": "6.2"},
    ],
    "backup1": [
        {"name": "python", "version": "3.11"},
        {"name": "bash", "version": "5.1"},
    ],
}

# Твоё решение:
# значение уникального запоминать надо в множество

install_python = []
python_versions = set()
for server in software:
    installed = []
    for install_prog in software[server]:
        if install_prog["name"] == "python":
            install_python.append(server)
            python_versions.add(install_prog["version"])
            major_version, minor_version = install_prog["version"].split('.')
            if  int(major_version) < 3 or int(minor_version) < 9:
                print(f'Сервер {server} имеет устаревшую версию питона')

        installed.append(f'{install_prog["name"]} {install_prog["version"]}')
    print(f'Установленные сервисы на сервере {server} {installed}')


print(f'Python установлен на сервере: {install_python}')
print(f'Уникальная версия Python: {python_versions}')





