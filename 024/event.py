import sys

import pygame
from pygame.locals import *
from settings import UP , DOWN, RIGHT, LEFT

# Проверяем, не нажат ли крестик (нужно ли завершить игру)
def check_exit():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        else:
            pygame.event.post(event)

def change_direction(snake):
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                snake.direction = UP
            elif event.key == K_DOWN:
                snake.direction = DOWN
            elif event.key == K_RIGHT:
                snake.direction = RIGHT
            elif event.key == K_LEFT:
                snake.direction = LEFT
                

    


