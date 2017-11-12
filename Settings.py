import pygame
import Game
import Menu


def run():
    pygame.init()

    screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

    settings_img = pygame.image.load("resources/settings.png").convert()
    back_img = pygame.image.load("resources/backButton.png").convert()
    volume_knob_img = pygame.image.load("resources/slider.png").convert()
    volume_knob_img.set_colorkey((255, 0, 255))
    volume_bar_img = pygame.image.load("resources/volume_bar.png").convert()
    volume_bar_img.set_colorkey((255, 0, 255))

    volume_pos = 120 + (880 * pygame.mixer.music.get_volume())
    screen.blit(settings_img, (0,0))
    screen.blit(volume_knob_img, (volume_pos, Game.SCREEN_HEIGHT / 3 + 91))
    back_button = screen.blit(back_img, (Game.SCREEN_WIDTH / 2 - 150, Game.SCREEN_HEIGHT / 2 + 150))

    """Controller init"""
    joysticks = []
    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[i].init()
        print("Detected joystick '", joysticks[i].get_name(), "'")

    done = False
    continue_to_back = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.JOYBUTTONDOWN and (joysticks[0].get_button(0) or joysticks[0].get_button(1)):
                done = True
                continue_to_back = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if back_button.collidepoint(pos):
                    done = True
                    continue_to_back = True

            if (event.type == pygame.JOYHATMOTION and joysticks[0].get_hat(0) == (-1, 0)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                new_vol = pygame.mixer.music.get_volume() - 0.05
                screen.blit(volume_bar_img, (86, Game.SCREEN_HEIGHT / 3 + 90))
                if new_vol <= 0:
                    pygame.mixer.music.set_volume(0)
                    volume_pos = 120
                    screen.blit(volume_knob_img, (volume_pos, Game.SCREEN_HEIGHT / 3 + 91))
                else:
                    volume_pos = 120 + (880 * new_vol)
                    screen.blit(volume_knob_img, (volume_pos, Game.SCREEN_HEIGHT / 3 + 91))
                    pygame.mixer.music.set_volume(new_vol)

            if (event.type == pygame.JOYHATMOTION and joysticks[0].get_hat(0) == (1, 0)) or (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                new_vol = pygame.mixer.music.get_volume() + 0.05
                screen.blit(volume_bar_img, (86, Game.SCREEN_HEIGHT / 3 + 90))
                if new_vol >= 1:
                    pygame.mixer.music.set_volume(1)
                    volume_pos = 1050
                    screen.blit(volume_knob_img, (volume_pos, Game.SCREEN_HEIGHT / 3 + 91))
                else:
                    volume_pos = 120 + (880 * new_vol)
                    screen.blit(volume_knob_img, (volume_pos, Game.SCREEN_HEIGHT / 3 + 91))
                    pygame.mixer.music.set_volume(new_vol)

            pygame.display.flip()

    if continue_to_back:
        print("Clicked back button!")
        Menu.main(pygame.mixer.music.get_volume())
