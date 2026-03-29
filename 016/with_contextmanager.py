from contextlib import contextmanager

@contextmanager
def temporary_file(filename, content):
    """Создаёт временный файл и гарантированно удаляет его"""
    print(f"Создаём файл {filename}")
    with open(filename, "w") as f:
        f.write(content)
    
    try:
        yield filename  # Возвращаем имя файла в блок with
    finally:
        print(f"Удаляем файл {filename}")
        import os
        os.remove(filename)

# Использование
with temporary_file("temp.txt", "Временные данные") as fname:
    print(f"Работаем с файлом {fname}")
    with open(fname, "r") as f:
        print("Содержимое:", f.read())
print("Файл уже удалён")