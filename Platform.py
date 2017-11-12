import pygame
import Game


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        self.image = pygame.image.load("resources/dirt_texture.png").convert()
        self.rect = pygame.Rect(0, 0, width, height)
