'''
Задание: Поиск "Клада" на сетке (Пространственное мышление)

Цель: Научить работать с координатами и движением в абстрактном пространстве.

Задание:
Представь поле 5х5. Кладоискатель начинает в левом верхнем углу (координаты [0, 0]). У него есть карта с командами.

    Создай класс TreasureHunter.

    В __init__ у него должны быть координаты x и y (начинаются с 0).

    Напиши метод move(command), где команда — это строка из букв: "U" (вверх, y-1), "D" (вниз, y+1), "L" (влево, x-1), "R" (вправо, x+1). Метод должен менять координаты. Если игрок выходит за границы поля (0-4), координаты не меняются (стоим на месте).

    Напиши метод find_treasure(commands), который принимает строку с командами (например, "RRDD"), выполняет их по очереди и возвращает итоговые координаты [x, y].
'''
# class TreasureHunter:
#     pass

# # Пример использования
# hunter = TreasureHunter()
# print(hunter.find_treasure("RRDD"))  # [2, 2]
# print(hunter.find_treasure("RRRRR")) # [4, 0]

# # Можно создать нового охотника или сбросить позицию старого
# hunter2 = TreasureHunter()
# print(hunter2.find_treasure("U"))  # [0, 0] - вверх нельзя, стоим на месте


class TreasureHunter:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self,command):
        if command == 'U':
            new_y = self.y - 1
            if 0<= new_y <= 4:
                self.y = new_y
        elif command == 'D':
            new_y = self.y + 1
            if 0<= new_y <= 4:
                self.y = new_y
        elif command == 'L':
            new_x = self.x - 1
            if 0<= new_x <= 4:
                self.x = new_x
        elif command == 'R':
            new_x = self.x + 1
            if 0<= new_x <= 4:
                self.x = new_x
        return self.x,self.y
    
    def find_treasure(self, commands):
        for command in commands:
            self.move(command)
        return self.x, self.y


hunter = TreasureHunter()
# print(hunter.move("R"))

# print(hunter.find_treasure("RRDD"))  # [2, 2]
print(hunter.find_treasure("RRRRR")) # [4, 0]