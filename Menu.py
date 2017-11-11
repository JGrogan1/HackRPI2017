import pygame


def main():
    """ Main Program """
    pygame.init()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    # Set the height and width of the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Platformer Jumper")

    screen.fill((0, 105, 255))
    screen.blit(pygame.font.SysFont("Britannic Bold", 40).render("Welcome !", 1, (255, 0, 0)), (200, 200))
    """Render buttons here"""
    start_button_img = pygame.image.load("resources/start_game.png")
    start_button = screen.blit(start_button_img, (100, SCREEN_HEIGHT / 2))

    end_it=False
    proceed_to_game = False
    while (end_it==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_it = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if start_button.collidepoint(pos):
                    proceed_to_game = True
                    end_it = True
        pygame.display.flip()
    if proceed_to_game:
        print ("Clicked button!")
        """GO TO GAME"""
    pygame.quit()

if __name__ == "__main__":
    main()