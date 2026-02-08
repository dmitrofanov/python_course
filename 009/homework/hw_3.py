"""
ЗАДАЧА: Создай класс Timer (Таймер)

1. В __init__ принимай start_time (начальное время)
2. Сохрани его в атрибут time
3. Создай метод tick() - уменьшает time на 1, но не ниже 0
4. Создай метод is_done() - возвращает True если time == 0
5. Создай метод reset(new_time) - устанавливает новое время

Создай таймер на 5 секунд, сделай несколько тиков, проверь статус.
"""

class Timer:
    def __init__(self, start_time):
        self.time = start_time
    
    def tick(self):
        if self.time > 0:
            self.time -= 1
        return self.time #(почему тут нужен return?)
    
    def is_done(self):
        return self.time == 0
    
    def reset(self, new_time):
        self.time = new_time
    
    def status(self):
        return f"Осталось: {self.time} сек."

timer = Timer(10)
print("Создан таймер на 5 секунд")
print(timer.status())

while not timer.is_done():
    timer.tick()
    print(f"{timer.status()}, Завершен? {timer.is_done()}")

# for i in range(5): # (Почему тут цикл?)
#     timer.tick()
#     print(f"Тик {i+1}: {timer.status()}, Завершен? {timer.is_done()}")
