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
        self.spike_list = pygame.sprite.Group()
        self.goal_list = pygame.sprite.Group()
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
        self.spike_list.update()
        self.goal_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.blit(self.background, self.rect)

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.button_list.draw(screen)
        self.spike_list.draw(screen)
        self.goal_list.draw(screen)

    def reset(self, clones):
        lives = self.player.lives
        if lives == 0:
            return
        self.__init__(self.player, clones)
        self.player.lives = lives - 1

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

        for spike in self.spike_list:
            spike.rect.x += shift_x

        for goal in self.goal_list:
            goal.rect.x += shift_x

    def create(self, platforms, buttons, spikes, goals, clones):
        # Adds clones that aren't part of the spawn point as platforms
        clone_list = pygame.sprite.Group()
        for platform in clones:
            block = plat.Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            clone_list.add(block)
        pygame.sprite.spritecollide(self.player, clone_list, True)
        for clone in clone_list:
            self.platform_list.add(clone)

        # Go through the array above and add platforms
        for platform in platforms:
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

        for spike in spikes:
            block = plat.Platform(spike[0], spike[1])
            block.image.fill(Game.GRAY)
            block.rect.x = spike[2]
            block.rect.y = spike[3]
            self.spike_list.add(block)

        for goal in goals:
            block = plat.Platform(goal[0], goal[1])
            block.image.fill(Game.YELLOW)
            block.rect.x = goal[2]
            block.rect.y = goal[3]
            self.goal_list.add(block)

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player, clones=[]):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform
        platforms = [[1000, Game.SCREEN_HEIGHT, -1000, 0],
                     [5000, 50, 0, Game.SCREEN_HEIGHT - 50],
                     [200, 100, 750, Game.SCREEN_HEIGHT-150],
                     [200, 225, 1150, Game.SCREEN_HEIGHT - 275],
                     [200, 225, 1550, Game.SCREEN_HEIGHT - 275],
                     [200, 225, 1550, Game.SCREEN_HEIGHT - 500],
                     [200, 225, 2200, Game.SCREEN_HEIGHT - 275],
                     [1000, Game.SCREEN_HEIGHT, 3000, 0]]

        buttons = [([1400, Game.SCREEN_HEIGHT - 70], platforms[5])]

        spikes = [[400, 50, 1775, Game.SCREEN_HEIGHT - 100]]

        goal = [[100, 100, 200, Game.SCREEN_HEIGHT - 150]]

        player.rect.x = 100
        player.rect.y = Game.SCREEN_HEIGHT - player.rect.height - 50
        player.lives = 100

        Level.create(self, platforms, buttons, spikes, goal, clones)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 1. """

    def __init__(self, player, clones=[]):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform
        platforms = [[200, Game.SCREEN_HEIGHT, -200, 0],
                     [5000, 50, 0, Game.SCREEN_HEIGHT-50],
                     [200, 100, 750, Game.SCREEN_HEIGHT-150],
                     [200, 225, 1150, Game.SCREEN_HEIGHT - 275],
                     [200, 225, 1550, Game.SCREEN_HEIGHT - 275],
                     [200, 225, 1550, Game.SCREEN_HEIGHT - 500],
                     [200, 225, 2200, Game.SCREEN_HEIGHT - 275],
                     [200, 225, 2200, Game.SCREEN_HEIGHT - 275]]

        buttons = [([1400, Game.SCREEN_HEIGHT - 70], platforms[5])]

        spikes = [[400, 50, 1775, Game.SCREEN_HEIGHT - 100]]

        goal = [[100, 100, 2750, Game.SCREEN_HEIGHT - 150]]

        player.rect.x = 100
        player.rect.y = Game.SCREEN_HEIGHT - player.rect.height - 50
        player.lives = 100

        Level.create(self, platforms, buttons, spikes, goal, clones)

class Level_03(Level):
    """ Definition for level 1. """

    def __init__(self, player, clones=[]):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform
        platforms = [[1000, Game.SCREEN_HEIGHT, -1000, 0],
                     [500, Game.SCREEN_HEIGHT/2,0,Game.SCREEN_HEIGHT/2],
                     [500,Game.SCREEN_HEIGHT/2,2000,Game.SCREEN_HEIGHT/2],
                     [1000, Game.SCREEN_HEIGHT, 2500, 0]]



        spikes = [[1500, 50, 500, Game.SCREEN_HEIGHT - 100]]

        goal = [[100, 100, 2250, Game.SCREEN_HEIGHT/2-100]]

        player.rect.x = 100
        player.rect.y = Game.SCREEN_HEIGHT/2 - player.rect.height
        player.lives = 4

        Level.create(self, platforms, [], spikes, goal, clones)

