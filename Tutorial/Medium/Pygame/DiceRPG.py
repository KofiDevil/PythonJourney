import sys
import pygame
from pygame.locals import *

pygame.init()

def pygame_intial():
    DISPLAYSURF = pygame.display.set_mode((300, 300))
    FPS = pygame.time.Clock()
    FPS.tick(60)

def object_create():
    object1 = pygame.Rect((20, 50), (50, 100))
    object2 = pygame.Rect((10, 10), (100, 100))
    print(object1.colliderect(object2))
    print(object1.collidepoint(50, 75))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255,0, 0)

# Game loop begins
def main():
    pygame_intial()
    object_create()   
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()