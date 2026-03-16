# Список пакетов до установки
pip list

# Установка пакета
pip install requests

# Сохранение зависимостей
pip freeze > requirements.txt

# Содержимое requirements.txt
cat requirements.txt

# Установка из requirements.txt (на другом компьютере)
pip install -r requirements.txt

# Выход из окружения
deactivate