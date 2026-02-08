"""
ЗАДАЧА: Создай класс Server (Сервер)

1. В __init__ принимай name (имя сервера)
2. Создай атрибуты: is_online = False, connected_users = 0
3. Создай метод start() - включает сервер (is_online = True)
4. Создай метод stop() - выключает сервер (is_online = False)
5. Создай метод connect() - добавляет пользователя если сервер включен
6. Создай метод disconnect() - убирает пользователя (но не ниже 0)
7. Создай метод status() - показывает статус сервера

Имитируй работу сервера: включи, подключи 3 пользователей, покажи статус.
"""

class Server:
    def __init__(self,name):
        self.name = name
        self.is_online = False
        self.connected_users = 0
        print(f'Создали сервер {self.name}')
    
    def start(self):
        self.is_online = True
        print(f'Включаем сервер {self.name}')
    
    def stop(self):
        if self.connected_users > 0:
            print(f'Ошибка,сервер {self.name} выключить нельзя,есть подключенные пользователи!')
        else:    
            self.is_online = False
            print(f'Выключаем сервер {self.name}')
    
    def connect(self, user_name):
        if self.is_online:
            self.connected_users += 1
            print(f'Добавлям пользователя {user_name}')
        else:
            print(f'Ошибка! Сервер выключен,добавить нельзя!')
    
    def disconnect(self):
        if self.connected_users > 0:
            self.connected_users -= 1
            print(f'Отключаем пользователя')
        else:
            print(f'Ошибка! Нет подключенных пользователей')
    
    def status(self):
        print(f'Статус сервера: {self.is_online}, Количество подключенных пользователей: {self.connected_users}')

server = Server('App1')
server.start()
server.connect('user1')
server.connect('user2')
server.disconnect()
server.stop()
server.status()


