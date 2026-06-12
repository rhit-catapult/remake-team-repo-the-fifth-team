import pygame
import sys
import my_character
import random
import time




class Character:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 5
        self.velocity_y = 0
        self.gravity = 0.5
        self.jump_power = 12
        self.ground_level = screen.get_height() - 20  # Floor is at the bottom of the screen
        self.is_jumping = False

    def move(self, dx, dy=0):
        """Move the character horizontally by dx pixels"""
        self.x += dx * self.speed
        # Keep character within screen bounds horizontally
        self.x = max(0, min(self.x, self.screen.get_width() - 20))

    def jump(self):
        """Make the character jump if on the ground"""
        if not self.is_jumping:
            self.velocity_y = -self.jump_power
            self.is_jumping = True


    def update(self):
        """Update character physics (gravity and jumping)"""
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # Keep character within screen bounds vertically
        if self.y <= 0:  # Prevent going above the screen
            self.y = 0
            self.velocity_y = 0
        
        # Check if character reached ground level
        if self.y >= self.ground_level:
            self.y = self.ground_level
            self.velocity_y = 0
            self.is_jumping = False

    def draw(self):
        pygame.draw.rect(self.screen, "blue", (self.x, self.y, 20, 20))
        pygame.draw.circle(self.screen, "red", (self.x + 5, self.y + 5), 3)
        pygame.draw.circle(self.screen, "red", (self.x + 15, self.y + 5), 3)


# This function is called when you run this file, and is used to test the Character class individually.
# When you create more files with different classes, copy the code below, then
# change it to properly test that class
def test_character():
    # TODO: change this function to test your class
    screen = pygame.display.set_mode((640, 480))
    character = Character(screen, 400, 400)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("white")
        character.draw()
        pygame.display.update()


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((640, 480))
    # creates a Character from the my_character.py file
    character = my_character.Character(screen,100, 400)

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        # Handle continuous key presses for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character.move(-1)
        if keys[pygame.K_RIGHT]:
            character.move(1)
        if keys[pygame.K_SPACE]:
            character.jump()

        
        # Update character physics
        character.update()

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # draws the character every frame
        character.draw()

        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()



main()