import pygame
from pygame.locals import *

from event import check_exit

RED = (255, 0, 0)
GRAY = (155, 155, 155)
BACKGROUND_COLOR = GRAY
SIZE_DISPLAY_WIDTH = 800
SIZE_DISPLAY_HEIGHT = 800
CELL_SIZE = 50
PADDING_SIZE = 2
TILE_SIZE = CELL_SIZE - PADDING_SIZE
BOARD_WIDTH = SIZE_DISPLAY_WIDTH // CELL_SIZE


def square(display, color , x, y):
    pygame.draw.rect(display, color, (x, y, TILE_SIZE, TILE_SIZE))

def game_loop():
    DISPLAY = pygame.display.set_mode((SIZE_DISPLAY_WIDTH, SIZE_DISPLAY_HEIGHT))
    pygame.init()
    while True:
        # Проверяем, не нажат ли крестик (нужно ли завершить игру)
        check_exit()

        # Рисуем фон
        for x in range(BOARD_WIDTH):
            square(DISPLAY, BACKGROUND_COLOR, x * CELL_SIZE + PADDING_SIZE, PADDING_SIZE)

        # Обновляем экран
        pygame.display.flip()

if __name__ == '__main__':
    game_loop()