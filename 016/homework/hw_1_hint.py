class Greeter:
    def __enter__(self):
        print("Добро пожаловать!")
    
    def __exit__(self, *args):
        print("До свидания!")

# Тест
with Greeter():
    print("Работаем...")