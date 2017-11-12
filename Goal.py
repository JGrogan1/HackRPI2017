import pygame
import Game
from Animation import *

class Goal(pygame.sprite.Sprite):

    """ Platform the user can jump on """

    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        self.anim = Animation("resources/flask.png", 100, 100, 5, 6)
        self.image = self.anim.get_current_frame()

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def update(self):
        self.anim.update()
        self.image = self.anim.get_current_frame()
