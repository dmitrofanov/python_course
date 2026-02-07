class Server:
    def __init__(self, name):
        self.name = name
        self.is_online = False
        self.connected_users = 0
    
    def start(self):
        # Включи сервер
        self.is_online = True
        print(f"Сервер '{self.name}' запущен")
    
    def stop(self):
        # Выключи сервер
        self.is_online = False
        # При выключении все пользователи отключаются
        self.connected_users = 0
        print(f"Сервер '{self.name}' остановлен")
    
    def connect(self):
        # Если сервер включен, добавь одного пользователя
        if self.is_online:
            self.connected_users += 1
            print(f"Новый пользователь подключился к '{self.name}'")
            return True
        else:
            print(f"Ошибка: сервер '{self.name}' выключен")
            return False
    
    def disconnect(self):
        # Отключи одного пользователя (но не ниже 0)
        if self.connected_users > 0:
            self.connected_users -= 1
            print(f"Пользователь отключился от '{self.name}'")
        else:
            print(f"На сервере '{self.name}' нет пользователей")
    
    def status(self):
        # Покажи статус сервера
        status_text = "включен" if self.is_online else "выключен"
        return (f"Сервер: {self.name}\n"
                f"Статус: {status_text}\n"
                f"Пользователей: {self.connected_users}")

# Тестируем
server = Server("Основной сервер")
print(server.status())

server.start()
server.connect()
server.connect()
server.connect()

print("\n" + server.status())

server.disconnect()
print("\nПосле отключения:")
print(server.status())

server.stop()
print("\nПосле остановки:")
print(server.status())