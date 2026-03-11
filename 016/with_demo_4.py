import sys

with open("output.txt", "w", encoding="utf-8") as file: # что будет если убрать encoding?
    # Временно перенаправляем stdout в файл
    old_stdout = sys.stdout
    sys.stdout = file
    print("Это сообщение пойдёт в файл")
    print("И это тоже")
    sys.stdout = old_stdout

print("А это сообщение в консоль")