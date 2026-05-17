import pygame
from pygame.locals import *

from event import check_exit
from settings import FPS, BOARD_HEIGHT, BOARD_WIDTH, UP, DOWN, RIGHT ,LEFT

class Snake:
    def __init__(self):
        self.coordinates = [(1,5),(1,6),(1,7), (1,8), (1,9)]
        self.direction = DOWN
    
    def move(self):
        if self.direction == DOWN:
            x, y = self.coordinates[0]
            if y + 1 > BOARD_HEIGHT:
                y = -1
            self.coordinates.insert(0,(x, y + 1))
            self.coordinates.pop()

        elif self.direction == UP:
            x, y = self.coordinates[0]
            if y - 1 < 0:
                y = BOARD_WIDTH
            self.coordinates.insert(0,(x, y - 1))
            self.coordinates.pop()
        
        elif self.direction == LEFT:
            x, y = self.coordinates[0]
            if x - 1 < 0:
                x = BOARD_WIDTH
            self.coordinates.insert(0,(x - 1, y))
            self.coordinates.pop()

        elif self.direction == RIGHT:
            x, y = self.coordinates[0]
            if x + 1 > BOARD_WIDTH:
                x = -1
            self.coordinates.insert(0,(x + 1, y))
            self.coordinates.pop()


def game_loop():
    from draw import draw_background, draw_snake
    pygame.init()
    clock = pygame.time.Clock()
    snake = Snake()
    while True:
        # Проверяем, не нажат ли крестик (нужно ли завершить игру)
        check_exit()
        
        # Рисуем фон
        draw_background()
        snake.move()
        draw_snake(snake.coordinates)

        # Обновляем экран
        clock.tick(FPS)
        pygame.display.flip()

if __name__ == '__main__':
    game_loop()