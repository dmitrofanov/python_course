import sys

import pygame
from pygame.locals import *

pygame.init()

DISPLAY = pygame.display.set_mode((800, 800))

while True:
    # Проверяем, не нажат ли крестик (нужно ли завершить игру)
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
    
    # Рисуем змейку
    pygame.draw.rect(DISPLAY, (255, 0, 0), (2, 2, 48, 48))
    pygame.draw.rect(DISPLAY, (255, 0, 0), (52, 2, 48, 48))
    pygame.draw.rect(DISPLAY, (255, 0, 0), (102, 2, 48, 48))
    pygame.draw.rect(DISPLAY, (255, 0, 0), (152, 2, 48, 48))

    # Обновляем экран
    pygame.display.flip()

if __name__ == '__main__':
    pass