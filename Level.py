import pygame
import Platform as plat
import Clone
import Spike as sp
import Button as bt
import Goal as gl
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
        self.background = pygame.image.load("resources/bg.png").convert()
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
        for platform in self.platform_list:
            screen.blit(platform.image, platform.rect, pygame.Rect(0, 0, platform.rect.width, platform.rect.height))
        self.button_list.draw(screen)
        self.spike_list.draw(screen)
        self.goal_list.draw(screen)

        # Draw the lives counter
        font = pygame.font.Font(None, 32)
        lives = font.render("Lives Left: " + str(self.player.lives), 1, (255, 255, 255))
        screen.blit(lives, (30, 20))

    def reset(self, clones):
        lives = self.player.lives
        if lives == 0:
            return
        size = len(self.platform_list.sprites())
        self.__init__(self.player, clones)
        if size != len(self.platform_list.sprites()):
            self.player.lives = lives - 1
        else:
            self.player.lives = lives

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
            block = Clone.Clone(platform[4], platform[5])
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
            block = sp.Spike(spike[2])
            block.rect.x = spike[0]
            block.rect.y = spike[1]
            self.spike_list.add(block)

        for goal in goals:
            block = gl.Goal(goal[0], goal[1])
            block.rect.x = goal[2]
            block.rect.y = goal[3]
            self.goal_list.add(block)


# Create platforms for the level
class Level01(Level):
    """ Definition for level 1. """

    def __init__(self, player, clones=[]):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform
        platforms = [[1000, Game.SCREEN_HEIGHT, -1000, 0],
                     [1000, 60, 0, Game.SCREEN_HEIGHT - 50],
                     [1000, 60, 1000, Game.SCREEN_HEIGHT - 50],
                     [1000, 60, 2000, Game.SCREEN_HEIGHT - 50],
                     [1000, 60, 3000, Game.SCREEN_HEIGHT - 50],
                     [200, 100, 760, Game.SCREEN_HEIGHT - 140],
                     [200, 220, 1160, Game.SCREEN_HEIGHT - 260],
                     [200, 220, 1560, Game.SCREEN_HEIGHT - 260],
                     [200, 220, 1560, Game.SCREEN_HEIGHT - 480],
                     [200, 220, 2200, Game.SCREEN_HEIGHT - 260],
                     [1000, Game.SCREEN_HEIGHT, 3000, 0]]

        buttons = [([1410, Game.SCREEN_HEIGHT - 70], platforms[8])]

        spikes = []
        for i in range(20):
            spikes.append([1775+20*i, Game.SCREEN_HEIGHT - 100, False])

        goal = [[100, 100, 2750, Game.SCREEN_HEIGHT - 150]]

        player.rect.x = 100
        player.rect.y = Game.SCREEN_HEIGHT - player.rect.height - 50
        player.lives = 3

        Level.create(self, platforms, buttons, spikes, goal, clones)


class Level02(Level):
    """ Definition for level 2. """

    def __init__(self, player, clones=[]):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform
        platforms = [[1000, Game.SCREEN_HEIGHT, -1000, 0],
                     [500, Game.SCREEN_HEIGHT / 2, 0, Game.SCREEN_HEIGHT / 2],
                     [500, Game.SCREEN_HEIGHT /2 , 2000, Game.SCREEN_HEIGHT / 2],
                     [1000, 100, 0, Game.SCREEN_HEIGHT - 60],
                     [1000, 100, 1000, Game.SCREEN_HEIGHT - 60],
                     [1000, 100, 2000, Game.SCREEN_HEIGHT - 60],
                     [1000, Game.SCREEN_HEIGHT, 2500, 0]]

        spikes = []
        for i in range(75):
            spikes.append([500 + 20 * i, Game.SCREEN_HEIGHT - 100, False])

        goal = [[100, 100, 2250, Game.SCREEN_HEIGHT/2-100]]

        player.rect.x = 100
        player.rect.y = Game.SCREEN_HEIGHT/2 - player.rect.height
        player.lives = 4

        Level.create(self, platforms, [], spikes, goal, clones)  # no buttons


class Level03(Level):
    """ Definition for level 3. """

    def __init__(self, player, clones=[]):
        """ Create level 3. """

        # Call the parent constructor
        Level.__init__(self, player)

        # Array with width, height, x, and y of platform
        platforms = [[1000, Game.SCREEN_HEIGHT, -1000, 0],
                     [280, 160+160+80, 0, 0],
                     [200, 160, 0, Game.SCREEN_HEIGHT - 140],
                     [120, 120, 280, Game.SCREEN_HEIGHT - 120],
                     [120, 140, 280, 0],
                     [200, 120, 200+80+120+80, 0],
                     [280, 90+160+140, 200+80+140, 160+140],
                     [1000, 120, 280, 155+160+90+155+40],
                     [1000, Game.SCREEN_HEIGHT, 200+80+120+80+200, 0]]

        spikes = []
        for i in range(4):
            spikes.append([200 + 20 * i, 400, True])
            spikes.append([200 + 20 * i, Game.SCREEN_HEIGHT - 50, False])
            spikes.append([400 + 20 * i, 0, True])
            spikes.append([420 + 20 * i, 250, False])

        goal = [[100, 100, Game.SCREEN_WIDTH-700, 160]]

        player.rect.x = 60
        player.rect.y = Game.SCREEN_HEIGHT - 160 - player.rect.height
        player.lives = 3

        Level.create(self, platforms, [], spikes, goal, clones)  # no buttons
