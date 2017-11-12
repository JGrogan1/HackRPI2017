import pygame


class SpriteSheet(object):
    def __init__(self, name, sprite_width, sprite_height):
        self.sheet = pygame.image.load(name).convert()
        self.sprite_width = sprite_width
        self.sprite_height = sprite_height

    def get_sprite(self, x, y):
        image = pygame.Surface([self.sprite_width, self.sprite_height]).convert()
        image.blit(self.sheet, (0, 0), (x * self.sprite_width, y * self.sprite_height, self.sprite_width, self.sprite_height))
        image.set_colorkey((255, 0, 255))
        return image
