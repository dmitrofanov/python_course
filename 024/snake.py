import pygame
from pygame.locals import *

from event import check_exit

def game_loop():
    from draw import draw_background, draw_snake
    pygame.init()
    snake = [(1,1),(1,2),(1,3)]
    while True:
        # Проверяем, не нажат ли крестик (нужно ли завершить игру)
        check_exit()
        
        # Рисуем фон
        draw_background()

        draw_snake(snake)

        # Обновляем экран
        pygame.display.flip()

if __name__ == '__main__':
    game_loop()