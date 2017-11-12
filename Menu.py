import pygame
import Game
import Settings

def main():
    """ Main Program """
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()

    # Set the height and width of the screen
    screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))

    pygame.display.set_caption("Menu")

    screen.fill((0, 105, 255))
    screen.blit(pygame.font.SysFont("Comic Sans MS", 40).render("Welcome Citizano!", 1, (255, 0, 0)), (200, 200))
    """Render buttons here"""
    start_img = pygame.image.load("resources/start_game.png").convert()
    settings_img = pygame.image.load("resources/settings.png").convert()

    start_button = screen.blit(start_img, (33, Game.SCREEN_HEIGHT / 2))
    settings_button = screen.blit(settings_img, (Game.SCREEN_WIDTH - 33 - 600, Game.SCREEN_HEIGHT / 2))

    pygame.mixer.music.load("resources/menu_loop.mp3")
    pygame.mixer.music.set_volume(.100)
    pygame.mixer.music.play(-1)


    done = False
    continue_to_start = False
    continue_to_settings = False
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
        pygame.display.flip()

    if continue_to_start:
        continue_to_start = False
        print("Clicked start button!")
        Game.run()
    if continue_to_settings:
        continue_to_settings = False
        print("Clicked settings button!")
        Settings.run()

    pygame.quit()

if __name__ == "__main__":
    main()