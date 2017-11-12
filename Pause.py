import pygame
import Menu
import Game

def run():
    pygame.init()
    pygame.display.set_caption("Pause")
    screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

    pause_img = pygame.image.load("resources/pause.png").convert_alpha()
    screen.blit(pause_img, (0, 0))

    joysticks = []
    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[i].init()
        print("Detected joystick '", joysticks[i].get_name(), "'")
    done = False
    go_to_menu = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if (event.type == pygame.JOYBUTTONDOWN and (joysticks[0].get_button(7) or joysticks[0].get_button(1))) or (event.type == pygame.KEYUP and event.key == pygame.K_p):
                done = True
            elif (event.type == pygame.JOYBUTTONDOWN and joysticks[0].get_button(6)) or (event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE):
                done = True
                go_to_menu = True
        pygame.display.flip()
    if go_to_menu:
        return True
    return False
