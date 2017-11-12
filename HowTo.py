import pygame
import Game


def run():
    pygame.init()

    # Set the height and width of the screen
    screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

    image = pygame.image.load("resources/howto.png").convert()
    rect = image.get_rect()
    screen.blit(image, rect)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.KEYUP:
                done = True

        pygame.display.flip()
