import pygame
import Game


def main():
    pygame.init()
    screen = pygame.display.set_mode((Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT))
    pygame.display.set_caption("Test Controller")
    screen.fill((0, 105, 255))

    joysticks = []
    for i in range(0, pygame.joystick.get_count()):
        joysticks.append(pygame.joystick.Joystick(i))
        joysticks[i].init()
        print ("Detected joystick '", joysticks[i].get_name(), "'")
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print ("Received event 'Quit', exiting.")
                done = True
            if (event.type == pygame.JOYBUTTONDOWN and (joysticks[0].get_button(7) or joysticks[0].get_button(1))) or (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                print("Button pressed")
        pygame.display.flip()


if __name__ == "__main__":
    main()
