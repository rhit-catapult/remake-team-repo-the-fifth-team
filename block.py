import pygame
import sys
import my_character
import random
import time
class Block:
    def __init__(self, screen, width, height, x, y, speed, type, color, border, border_color):
        self.screen = screen
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed
        self.type = type
        self.color = color
        self.border = border
        self.border_color = border_color
    def update(self):
        self.x -= self.speed
    def draw(self):
        if self.type == "normal":
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
            if self.border > 0:
                pygame.draw.line(self.screen, self.border_color, (self.x, self.y), (self.x + self.width, self.y), self.border)
                pygame.draw.line(self.screen, self.border_color, (self.x, self.y), (self.x, self.y + self.height), self.border)
                pygame.draw.line(self.screen, self.border_color, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), self.border)
                pygame.draw.line(self.screen, self.border_color, (self.x, self.y + self.height), (self.x + self.width, self.y + self.width), self.border)
        else:
            pygame.draw.polygon(self.screen, self.color, [(self.x, self.y,), (self.x - self.width / 2, self.y + self.height), (self.x + self.width / 2, self.y + self.height)])
            if self.border > 0:
                pygame.draw.line(self.screen, self.border_color, (self.x, self.y), (self.x + self.width / 2, self.y + self.height), self.border)
                pygame.draw.line(self.screen, self.border_color, (self.x, self.y), (self.x - self.width / 2, self.y + self.height), self.border)
                pygame.draw.line(self.screen, self.border_color, (self.x - self.width / 2, self.y + self.height), (self.x + self.width / 2, self.y + self.height), self.border)
    def off_screen(self):
        return self.x < -self.width

def test_block():
    screen = pygame.display.set_mode((640, 480))
    block = Block(screen, 50, 50, 600, 200, 2, "spike", (0, 0, 0), 5, (150, 150, 150))
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("white")
        block.update()
        block.draw()
        pygame.display.update()
# test_block()
