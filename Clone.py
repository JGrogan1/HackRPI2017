import pygame
import Game
from Animation import *


class Clone(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, right, upside_down):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        if right and not upside_down:
            self.anim = Animation("resources/idle.png", 60, 100, 6, 6)
        elif right and upside_down:
            self.anim = Animation("resources/upside_down_idle.png", 60, 100, 6, 6)
        elif not right and not upside_down:
            self.anim = Animation("resources/idle_left.png", 60, 100, 6, 6)
        else:
            self.anim = Animation("resources/upside_down_idle_left.png", 60, 100, 6, 6)
        self.image = self.anim.get_current_frame()

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        self.anim.update()
        self.image = self.anim.get_current_frame()
