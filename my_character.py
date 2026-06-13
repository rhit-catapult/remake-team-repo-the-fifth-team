import pygame
import sys


class Character:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 5
        self.velocity_y = 0
        self.gravity = 0.3
        self.move_distance = 30  # Distance to move per keypress
        self.ground_level = screen.get_height() - 35  # Adjusted for arrow
        self.is_touching_ground = True
        self.size = 35  # Arrow size
        self.moving_up = False  # Track if currently moving up

    def move(self, dx, dy=0):
        """Move the character horizontally by dx pixels"""
        self.x += dx * self.speed
        # Keep character within screen bounds horizontally
        self.x = max(0, min(self.x, self.screen.get_width() - self.size))

    def wave_control(self, is_pressed):
        """Control wave movement - rigid up and down movements"""
        if is_pressed and self.y > 50 and not self.moving_up:  # Move up when pressed
            self.velocity_y = -8  # Rigid upward movement
            self.moving_up = True
        elif not is_pressed and self.moving_up:
            self.moving_up = False  # Stop upward movement when released

    def update(self):
        
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
            self.is_touching_ground = True
        else:
            self.is_touching_ground = False

    def draw(self, screen_x=None):
        if screen_x is None:
            screen_x = self.x
        
        # Draw an arrow pointing right
        arrow_size = self.size
        arrow_y = self.y + arrow_size // 2
        
        # Arrow point (right side)
        points = [
            (screen_x + arrow_size, arrow_y),  # Right point
            (screen_x, arrow_y - arrow_size // 2),  # Top left
            (screen_x + arrow_size // 3, arrow_y),  # Middle
            (screen_x, arrow_y + arrow_size // 2),  # Bottom left
        ]
        
        # Draw the arrow
        pygame.draw.polygon(self.screen, "blue", points)
        
        # Draw an eye
        pygame.draw.circle(self.screen, "red", (int(screen_x + arrow_size // 3), int(arrow_y - arrow_size // 4)), 3)


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
