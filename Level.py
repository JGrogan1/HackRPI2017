import pygame
import Platform as plat
import Button as bt
import Game

class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.button_list = pygame.sprite.Group()
        self.player = player

        # Background image
        self.background = pygame.image.load("resources/test.jpg")
        self.rect = self.background.get_rect()

        self.world_shift = 0

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        for button in self.button_list:
            button.update()
        self.button_list.update()
        self.platform_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.blit(self.background, self.rect)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.button_list.draw(screen)

    def reset(self, clones):
        lives = self.player.lives
        if lives == 0:
            return
        self.__init__(self.player, clones)
        self.player.lives = lives - 1

    def full_reset(self):
        self.__init__(self.player)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for button in self.button_list:
            button.rect.x += shift_x


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player, clones=[]):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform
        level = [[210, 70, 0, 600],
                 [210, 70, 200, 400],
                 [210, 70, 600, 300],
                 [210, 70, 800, 600]]

        buttons = [([50, 580], level[3]), ([200, 400], level[2])]

        player.rect.x = 340
        player.rect.y = Game.SCREEN_HEIGHT - player.rect.height
        player.lives = 5

        # Adds clones that aren't part of the spawn point as platforms
        clone_list = pygame.sprite.Group()
        for platform in clones:
            block = plat.Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            clone_list.add(block)
        pygame.sprite.spritecollide(self.player, clone_list, True)
        for clone in clone_list:
            self.platform_list.add(clone)

        # Go through the array above and add platforms
        for platform in level:
            block = plat.Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            self.platform_list.add(block)
            for button in buttons:
                if platform == button[1]:
                    but = bt.Button(self.player, clone_list, block, self)
                    but.rect.x = button[0][0]
                    but.rect.y = button[0][1]
                    self.button_list.add(but)