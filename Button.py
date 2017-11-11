import pygame
import Game

class Button(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, player, clone_list):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        self.image = pygame.Surface([100, 20])
        self.image.fill(Game.RED)
        self.player = player

        self.rect = self.image.get_rect()
        self.clone_list = clone_list

    def update(self):
        collided = pygame.sprite.collide_rect(self.player, self)
        clone_collisions = pygame.sprite.spritecollide(self, self.clone_list, False)
        if collided or len(clone_collisions) != 0:
            self.image.fill(Game.PINK)
        else:
            self.image.fill(Game.RED)

