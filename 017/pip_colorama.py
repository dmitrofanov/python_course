from colorama import init, Fore, Back, Style
import time
from tqdm import tqdm

# Инициализация colorama (для Windows)
init()

# Цветной вывод
print(Fore.RED + "Это красный текст")
print(Fore.GREEN + "Это зелёный текст")
print(Back.YELLOW + Fore.BLACK + "Жёлтый фон, чёрный текст")
print(Style.RESET_ALL + "Обычный текст")

# Прогресс-бар
print("Загрузка данных:")
for i in tqdm(range(100)):
    time.sleep(0.02)  # имитация работы