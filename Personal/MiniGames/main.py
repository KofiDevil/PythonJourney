# Example file showing a basic pygame "game loop"
import pygame

BLACK = pygame.Color(5, 19, 27)
SHADOW = pygame.Color(54, 36, 23)
MID = pygame.Color(146, 129, 122)
WHITE = pygame.Color(241, 218, 191)
HIGHLIGHT = pygame.Color(255, 251, 255)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(BLACK)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
