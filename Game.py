import pygame
import Level as lvl
import Player as pl
import Menu
import Pause

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 192, 203)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)

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
    level_list.append(lvl.Level_02(player))
    level_list.append(lvl.Level_03(player))
    level_list.append(lvl.Level_04(player))

    # Set the current level
    current_level_number = 3
    current_level = level_list[current_level_number]

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
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_r:
                    player.reverse_gravity = False
                    player.image = pygame.image.load("resources/scientist.png")
                    clones.append([player.width(), player.height(), -current_level.world_shift + player.rect.x, player.rect.y])
                    current_level.reset(clones)
                if event.key == pygame.K_ESCAPE:
                    player.reverse_gravity = False
                    player.image = pygame.image.load("resources/scientist.png")
                    clones.clear()
                    current_level.__init__(player)
                if event.key == pygame.K_2:
                    if player.reverse_gravity:
                        player.reverse_gravity = False
                        player.image = pygame.image.load("resources/scientist.png")
                    else:
                        player.reverse_gravity = True
                        player.image = pygame.image.load("resources/upside_down_scientist.png")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_p:
                    player.stop()
                    Pause.run()

        # Update the player.
        active_sprite_list.update()

        spikes = pygame.sprite.spritecollide(player, current_level.spike_list, False)
        if len(spikes) > 0:
            player.reverse_gravity = False
            player.image = pygame.image.load("resources/scientist.png")
            clones.clear()
            current_level.__init__(player)

        goals = pygame.sprite.spritecollide(player, current_level.goal_list, False)
        if len(goals) > 0:
            player.reverse_gravity = False
            player.image = pygame.image.load("resources/scientist.png")
            clones.clear()
            current_level_number += 1
            if current_level_number >= len(level_list):
                done = True
                continue
            current_level = level_list[current_level_number]
            current_level.__init__(player)
            player.level = current_level
            continue

        # Update items in the level
        current_level.update()

        left_scroll = SCREEN_WIDTH * .4
        right_scroll = SCREEN_WIDTH * .6
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= right_scroll:
            diff = player.rect.right - right_scroll
            player.rect.right = right_scroll
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= left_scroll:
            diff = left_scroll - player.rect.left
            player.rect.left = left_scroll
            current_level.shift_world(diff)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    Menu.main(pygame.mixer.music.get_volume())
