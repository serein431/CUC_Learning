import pygame,sys

from pygame.locals import *
from math import pi
pygame.init()

screen = pygame.display.set_mode((1000, 600))
background = pygame.image.load("BG.jpg")
pygame.display.set_caption('BackGround')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# screen.fill(WHITE)
# pygame.draw.circle(screen, BLACK, [200, 150], 30)
while True:
    screen.blit(background, (100, 50))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
