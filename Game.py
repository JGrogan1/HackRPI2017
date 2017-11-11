import pygame
import Level as lvl
import Player as pl

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255,192,203)

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def run():
    """ Main Program """
    pygame.init()

    # Set the height and width of the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Platformer Jumper")

    # Create the player
    player = pl.Player()

    # Create all the levels
    level_list = []
    level_list.append(lvl.Level_01(player))

    # Set the current level
    current_level = level_list[0]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    active_sprite_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # All clones
    clones = []

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_r:
                    clones.append([player.width(), player.height(), player.rect.x, player.rect.y])
                    current_level.reset(clones)
                if event.key == pygame.K_ESCAPE:
                    clones.clear()
                    current_level.full_reset()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()