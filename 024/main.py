import pygame
from pygame.locals import *

from event import check_exit, change_direction
from settings import FPS
from entity import Snake


def game_loop():
    from draw import draw_background, draw_snake, draw_food
    pygame.init()
    clock = pygame.time.Clock()
    snake = Snake()
    food = (5, 5)
    while True:
        # Проверяем, не нажат ли крестик (нужно ли завершить игру)
        check_exit()
        
        draw_background()
        snake.move(food)
        draw_snake(snake.coordinates)
        draw_food(food)
        change_direction(snake)

        # Обновляем экран
        clock.tick(FPS)
        pygame.display.flip()

if __name__ == '__main__':
    game_loop()