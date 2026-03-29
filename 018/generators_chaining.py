def read_large_file(file_path):
    """Читает большой файл построчно, не загружая целиком"""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

# Использование — память не растёт
def error_logs(lines):
    for line in lines:
        if "ERROR" in line:
            # print(f"Найдена ошибка: {line}")
            # Можно остановиться после первой ошибки
            # break
            yield line

errors = error_logs(read_large_file("huge_log.txt"))
print(errors)