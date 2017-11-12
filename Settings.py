import pygame
import Game
import Menu

def run():
    pygame.init()
    pygame.display.set_caption("Settings")

    screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))
    screen.fill((255, 255, 255))

    back_img = pygame.image.load("resources/back.png").convert()
    back_button = screen.blit(back_img, (Game.SCREEN_WIDTH / 2 - 300, Game.SCREEN_HEIGHT / 2))

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if back_button.collidepoint(pos):
                    done = True
                    print("Clicked back button!")
                    Menu.main()
        pygame.display.flip()
