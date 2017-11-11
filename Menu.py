import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def main():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Platformer Jumper")

    screen.fill((0, 105, 255))
    screen.blit(pygame.font.SysFont("Comic Sans MS", 40).render("Welcome Citizano!", 1, (255, 0, 0)), (200, 200))
    """Render buttons here"""
    start_img = pygame.image.load("resources/start_game.png")
    settings_img = pygame.image.load("resources/settings.png")

    start_button = screen.blit(start_img, (33, SCREEN_HEIGHT / 2))
    settings_button = screen.blit(settings_img, (SCREEN_WIDTH - 33 - 600, SCREEN_HEIGHT / 2))

    end_it = False
    proceed_to_game = False
    go_to_settings = False

    while (end_it==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_it = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                end_it = True
                pos = pygame.mouse.get_pos()
                if start_button.collidepoint(pos):
                    proceed_to_game = True
                if settings_button.collidepoint(pos):
                    go_to_settings = True
        pygame.display.flip()

    if proceed_to_game:
        proceed_to_game = False
        print ("Clicked start button!")
        """GO TO GAME"""
    if go_to_settings:
        go_to_settings = False
        print ("Clicked settings button!")
        """GO TO SETTINGS"""
    pygame.quit()

if __name__ == "__main__":
    main()