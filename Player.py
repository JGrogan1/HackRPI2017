import pygame
import Game
from Animation import *


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        # TODO: fix the params for this
        self.right_anim = Animation("resources/walking.png", 60, 100, 6, 6)
        self.left_anim = Animation("resources/walking_left.png", 60, 100, 6, 6)
        self.current_anim = self.right_anim
        self.image = self.current_anim.get_current_frame()

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0

        # List of sprites we can bump against
        self.level = None
        self.lives = 0
        self.reverse_gravity = False

        self.moving = False

    def set_animation_gravity(self):
        right = True
        if self.current_anim != self.right_anim:
            right = False
        if not self.reverse_gravity:
            self.right_anim = Animation("resources/walking.png", 60, 100, 6, 6)
            self.left_anim = Animation("resources/walking_left.png", 60, 100, 6, 6)
        else:
            self.right_anim = Animation("resources/upside_down_walking.png", 60, 100, 6, 6)
            self.left_anim = Animation("resources/upside_down_walking_left.png", 60, 100, 6, 6)
        if right:
            self.current_anim = self.right_anim
        else:
            self.current_anim = self.left_anim
        self.image = self.current_anim.get_current_frame()

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if not self.reverse_gravity:
                # Reset our position based on the top/bottom of the object.
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
            else:
                # Reset our position based on the top/bottom of the object.
                if self.change_y < 0:
                    self.rect.top = block.rect.bottom
                elif self.change_y > 0:
                    self.rect.bottom = block.rect.top

            # Stop our vertical movement
            self.change_y = 0

        if self.moving:
            self.current_anim.update()
        self.image = self.current_anim.get_current_frame()

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if not self.reverse_gravity:
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += .35
            # See if we are on the ground.
            if self.rect.y >= Game.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = Game.SCREEN_HEIGHT - self.rect.height
        else:
            if self.change_y == 0:
                self.change_y = -1
            else:
                self.change_y -= .35
            # See if we are on the ceiling.
            if self.rect.y <= 0 and self.change_y <= 0:
                self.change_y = 0
                self.rect.y = 0

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        if not self.reverse_gravity:
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 2

            # If it is ok to jump, set our speed upwards
            if len(platform_hit_list) > 0 or self.rect.bottom >= Game.SCREEN_HEIGHT:
                self.change_y = -10
        else:
            self.rect.y -= 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y += 2

            # If it is ok to jump, set our speed upwards
            if len(platform_hit_list) > 0 or self.rect.top <= 0:
                self.change_y = 10

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.current_anim = self.left_anim
        self.change_x = -6
        self.moving = True

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.current_anim = self.right_anim
        self.change_x = 6
        self.moving = True

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.current_anim.reset()
        self.image = self.current_anim.get_current_frame()
        self.moving = False

    def width(self):
        return self.image.get_rect().size[0]

    def height(self):
        return self.image.get_rect().size[1]
