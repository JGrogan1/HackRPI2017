import pygame

def run():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == pygame.K_p:
                done = True
