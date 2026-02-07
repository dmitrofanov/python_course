class Timer:
    def __init__(self, start_time):
        # Сохрани start_time в атрибут time
        self.time = start_time
    
    def tick(self):
        # Уменьши self.time на 1, но не ниже 0
        if self.time > 0:
            self.time -= 1
        return self.time
    
    def is_done(self):
        # Верни True если время вышло (time == 0)
        return self.time == 0
    
    def reset(self, new_time):
        # Установи новое значение времени
        self.time = new_time
    
    def status(self):
        # Дополнительный метод: показывает текущее время
        return f"Осталось: {self.time} сек."

# Тестируем
timer = Timer(5)
print("Создан таймер на 5 секунд")
print(timer.status())

for i in range(7):
    timer.tick()
    print(f"Тик {i+1}: {timer.status()}, Завершен? {timer.is_done()}")
    
timer.reset(3)
print(f"\nСбросили на 3 секунды: {timer.status()}")