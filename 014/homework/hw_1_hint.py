class TreasureHunter:
    def __init__(self):
        """Начинаем с позиции [0, 0]"""
        self.x = 0
        self.y = 0
        # Границы поля (0-4 включительно)
        self.min_bound = 0
        self.max_bound = 4
    
    def move(self, command):
        """Выполняет одну команду движения"""
        for cmd in command:  # Проходим по каждой букве в команде
            if cmd == 'U' and self.y > self.min_bound:
                self.y -= 1  # Вверх
            elif cmd == 'D' and self.y < self.max_bound:
                self.y += 1  # Вниз
            elif cmd == 'L' and self.x > self.min_bound:
                self.x -= 1  # Влево
            elif cmd == 'R' and self.x < self.max_bound:
                self.x += 1  # Вправо
            # Если команда пытается выйти за границы - просто игнорируем
    
    def find_treasure(self, commands):
        """Принимает строку команд и возвращает итоговые координаты"""
        self.move(commands)  # Выполняем все команды
        return [self.x, self.y]  # Возвращаем финальную позицию

