import pygame
import sys
import my_character


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Geometry Dash - Wave Mode")
    screen = pygame.display.set_mode((640, 480))
    
    # creates a Character from the my_character.py file
    character = my_character.Character(screen, 100, 380)

    # let's set the framerate
    clock = pygame.time.Clock()
    
    camera_x = 0
    base_position = character.x  # Track base position for camera
    
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Handle continuous key presses for movement
        keys = pygame.key.get_pressed()
        # Wave mode: hold space to go up
        character.wave_control(keys[pygame.K_SPACE])
        
        # Auto move forward (constant movement)
        base_position += 2
        character.x = base_position
        
        # Update character physics
        character.update()
        
        # Camera follows base position
        camera_x = base_position - screen.get_width() // 3

        # Fill the screen with background color
        screen.fill((200, 200, 255))

        # Draw the character at fixed screen position (1/4 from left)
        character.draw(screen_x=screen.get_width() // 4)

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()



if __name__ == "__main__":
    main()
