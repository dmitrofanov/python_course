try:
    with open("016/shopping.txt", "r", encoding="utf-8") as file:
        data = file.read()
        # Имитируем ошибку
        x = 1 / 0
except ZeroDivisionError:
    print("Ошибка! Но файл всё равно закрыт")