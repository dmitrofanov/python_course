import os



class ChangeDir:
    def __init__(self, new_path):
        self.new_path = new_path
        self.old_path = None
    
    def __enter__(self):
        self.old_path = os.getcwd()
        os.chdir(self.new_path)
        print(f"Перешли в {self.new_path}")
        return self
    
    def __exit__(self, *args):
        os.chdir(self.old_path)
        print(f"Вернулись в {self.old_path}")

# Использование
print("Текущая директория:", os.getcwd())
with ChangeDir("tmp"):
    print("Внутри with:", os.getcwd())
    # Что-то делаем во временной директории
print("После with:", os.getcwd())