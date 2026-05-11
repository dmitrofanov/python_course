import pygame
from settings import *

DISPLAY = pygame.display.set_mode((SIZE_DISPLAY_WIDTH, SIZE_DISPLAY_HEIGHT))

def square(color , x, y):
    pygame.draw.rect(DISPLAY, color, (x * CELL_SIZE + PADDING_SIZE, y * CELL_SIZE + PADDING_SIZE, TILE_SIZE, TILE_SIZE))

def draw_background():
    # Рисуем фон
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            square(BACKGROUND_COLOR, x , y)

def draw_snake(snake):
    for x, y in snake:
        square(SNAKE_COLOR, x, y)

