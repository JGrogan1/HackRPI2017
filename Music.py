import pygame

class Music:
    def __init__(self, vol):
        self.volume = vol
        pygame.mixer.music.load("resources/menu_loop.mp3")
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.play(-1)
