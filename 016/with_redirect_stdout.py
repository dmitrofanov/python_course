from contextlib import redirect_stdout

with open("output.txt", "w", encoding="utf-8") as file:
    with redirect_stdout(file):
        print("В файл")
        print("И это в файл")
print("В консоль")