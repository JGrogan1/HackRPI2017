import pygame
from SpriteSheet import *

class Animation(object):
    def __init__(self, name, sprite_width, sprite_height, num_frames, delay):
        self.sheet = SpriteSheet(name, sprite_width, sprite_height)
        self.frames = []
        for i in range(num_frames):
            self.frames.append( self.sheet.get_sprite(i, 0) )

        self.current_tick = 0
        # Delay measures the amount of ticks to occur before the next frame is played.
        self.delay = delay
        self.frame_index = 0
        self.num_frames = num_frames
        self.current_frame = self.frames[0]

    def update(self):
        self.current_tick += 1
        if self.current_tick >= self.delay:
            self.current_tick = 0
            self.frame_index = (self.frame_index + 1) % self.num_frames
            self.current_frame = self.frames[ self.frame_index ]

    def get_current_frame(self):
        return self.current_frame
