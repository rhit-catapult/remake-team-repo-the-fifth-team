import pygame
import sys


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
    def draw(self):
        pygame.draw.rect(self.screen, "blue", (self.x, self.y, 20, 20))


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


# Testing the classes
# click the green arrow to the left or run "Current File" in PyCharm to test this class
if __name__ == "__main__":
    test_character()
