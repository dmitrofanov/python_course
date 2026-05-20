from settings import BOARD_HEIGHT, BOARD_WIDTH, UP, DOWN, RIGHT ,LEFT

class Snake:
    def __init__(self):
        self.coordinates = [(1,5),(1,6),(1,7), (1,8), (1,9)]
        self.direction = RIGHT
    
    def move(self,food):
        x, y = self.coordinates[0]
        if self.direction == DOWN:
            if y + 1 > BOARD_HEIGHT:
                y = -1
            y = y + 1

        elif self.direction == UP:
            if y - 1 < 0:
                y = BOARD_WIDTH
            y = y - 1
        
        elif self.direction == LEFT:
            if x - 1 < 0:
                x = BOARD_WIDTH
            x = x - 1

        elif self.direction == RIGHT:
            if x + 1 > BOARD_WIDTH:
                x = -1
            x = x + 1
        
        self.coordinates.insert(0,(x, y))      
        if (x, y) == food:
            pass 
        else:
            self.coordinates.pop()