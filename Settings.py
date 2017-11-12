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
    volume_knob_img = pygame.image.load("resources/volume_knob.png").convert()
    volume_bar_img = pygame.image.load("resources/volume_bar.png")
    volume_pos = 200

    done = False
    continue_to_back = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if back_button.collidepoint(pos):
                    done = True
                    continue_to_back = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                print("Current volume: %d percent" % ((100 * (pygame.mixer.music.get_volume()))))
                new_vol = pygame.mixer.music.get_volume() - 0.05
                volume_bar = screen.blit(volume_bar_img, (200, Game.SCREEN_HEIGHT / 3))
                if new_vol <= 0:
                    pygame.mixer.music.set_volume(0)
                    volume_pos = 200
                    volume_knob = screen.blit(volume_knob_img, (volume_pos, Game.SCREEN_HEIGHT / 3))
                else:
                    volume_pos -= 44
                    volume_knob = screen.blit(volume_knob_img, (volume_pos, Game.SCREEN_HEIGHT / 3))
                    pygame.mixer.music.set_volume(new_vol)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print("Current volume: %d percent" % ((100 * (pygame.mixer.music.get_volume()))))
                new_vol = pygame.mixer.music.get_volume() + 0.05
                volume_bar = screen.blit(volume_bar_img, (200, Game.SCREEN_HEIGHT / 3))
                if new_vol >= 1:
                    pygame.mixer.music.set_volume(1)
                    volume_pos = 1080
                    volume_knob = screen.blit(volume_knob_img, (volume_pos, Game.SCREEN_HEIGHT / 3))
                else:
                    volume_pos += 44
                    volume_knob = screen.blit(volume_knob_img, (volume_pos, Game.SCREEN_HEIGHT / 3))
                    pygame.mixer.music.set_volume(new_vol)

            pygame.display.flip()

    if continue_to_back:
        continue_to_back = False
        print("Clicked back button!")
        Menu.main()
