import pygame
import Game

class Spike(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, upside_down):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        if upside_down:
            self.image = pygame.image.load("resources/upside_down_spike.png").convert_alpha()
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load("resources/spike.png").convert_alpha()
            self.rect = self.image.get_rect()
