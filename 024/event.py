import sys

import pygame
from pygame.locals import *

# Проверяем, не нажат ли крестик (нужно ли завершить игру)
def check_exit():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

