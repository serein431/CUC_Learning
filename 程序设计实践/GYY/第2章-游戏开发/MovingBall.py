import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 400), 0, 32)

pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)

img = pygame.image.load('pic/yundong.png')

imgx = 10
imgy = 10

direction = 'right'

while True:
    screen.fill(WHITE)
    if direction == 'right':
        imgx += 5
        if imgx == 380:
            direction = 'down'
    elif direction == 'down'