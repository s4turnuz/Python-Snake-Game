import random
import pygame
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255)) # white color

apple = pygame.Surface((10,10))
apple.fill((255,0,0)) # red color
apple_pos = (random.randint(0,590), random.randint(0,590))

my_direction = LEFT

while True:
    for event in pygame.event.get(): # exit to game
        if event.type == QUIT:
            pygame.quit()
    
    screen.fill((0,0,0)) # clear the screen
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()