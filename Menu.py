import pygame
import HowTo
import Game
import Settings
from Music import Music


def main(musicVol):
    """ Main Program """
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()

    # Set the height and width of the screen
    screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

    pygame.display.set_caption("The Adventures of The Evil Mad Scientist: Dr. Citizano")

    background_img = pygame.image.load("resources/title.png").convert()
    start_img = pygame.image.load("resources/playButton.png").convert()
    settings_img = pygame.image.load("resources/settingsButton.png").convert()
    exit_img = pygame.image.load("resources/exitButton.png").convert()
    arrow_img = pygame.image.load("resources/menuArrow.png").convert()
    arrow_img.set_colorkey((255, 0, 255))
    arrow_coverup_img = pygame.image.load("resources/buttonCover.png").convert()

    screen.blit(background_img, (0, 0))
    start_button = screen.blit(start_img, (Game.SCREEN_WIDTH - 33 - 600, Game.SCREEN_HEIGHT / 2))
    settings_button = screen.blit(settings_img, (Game.SCREEN_WIDTH - 33 - 600, Game.SCREEN_HEIGHT / 2 + 125))
    exit_button = screen.blit(exit_img, (Game.SCREEN_WIDTH - 33 - 600, Game.SCREEN_HEIGHT / 2 + 250))
    screen.blit(arrow_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2))


    Music(musicVol)

    joysticks = []
    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[i].init()
        print("Detected joystick '", joysticks[i].get_name(), "'")

    done = False
    continue_to_start = False
    continue_to_settings = False
    exit_game = False

    menu_selector = 0 #0 = start game, 1 = settings, 2 = quit
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if start_button.collidepoint(pos):
                    done = True
                    continue_to_start = True
                if settings_button.collidepoint(pos):
                    done = True
                    continue_to_settings = True
                if exit_button.collidepoint(pos):
                    done = True
                    exit_game = True

            if event.type == pygame.JOYHATMOTION and joysticks[0].get_hat(0) == (0, 1):
                if menu_selector > 0:
                    menu_selector -= 1
            if event.type == pygame.JOYHATMOTION and joysticks[0].get_hat(0) == (0, -1):
                if menu_selector < 2:
                    menu_selector += 1

            if menu_selector == 0:
                screen.blit(arrow_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2))
                screen.blit(arrow_coverup_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2 + 125))
                screen.blit(arrow_coverup_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2 + 250))
            if menu_selector == 1:
                screen.blit(arrow_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2 + 125))
                screen.blit(arrow_coverup_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2))
                screen.blit(arrow_coverup_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2 + 250))
            if menu_selector == 2:
                screen.blit(arrow_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2 + 250))
                screen.blit(arrow_coverup_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2))
                screen.blit(arrow_coverup_img, (Game.SCREEN_WIDTH - 33 - 600 - 100, Game.SCREEN_HEIGHT / 2 + 125))

            if event.type == pygame.JOYBUTTONDOWN and joysticks[0].get_button(0):
                if menu_selector == 0:
                    done = True
                    continue_to_start = True
                if menu_selector == 1:
                    done = True
                    continue_to_settings = True
                if menu_selector == 2:
                    done = True
                    exit_game = True

        pygame.display.flip()

    if continue_to_start:
        print("Clicked start button!")
        HowTo.run()
        Game.run()
    if continue_to_settings:
        print("Clicked settings button!")
        Settings.run()
    if exit_game:
        print("Goodbye!")

    pygame.quit()


if __name__ == "__main__":
    main(.1)