import pygame
import Game


class Button(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, player, clone_list, platform, level):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        self.image = pygame.image.load("resources/button.png").convert()
        self.player = player

        self.rect = self.image.get_rect()
        self.clone_list = clone_list
        self.platform = platform
        self.current_level = level
        self.removed = False

    def update(self):
        collided = pygame.sprite.collide_rect(self.player, self)
        clone_collisions = pygame.sprite.spritecollide(self, self.clone_list, False)
        if collided or len(clone_collisions) != 0:
            self.image = pygame.image.load("resources/buttonPressed.png").convert_alpha()
            if not self.removed:
                self.platform.rect.x -= self.current_level.world_shift
                self.current_level.platform_list.remove(self.platform)
                self.removed = True
        else:
            self.image = pygame.image.load("resources/button.png").convert()
            if self.removed:
                self.platform.rect.x += self.current_level.world_shift
                self.removed = False
                self.current_level.platform_list.add(self.platform)
