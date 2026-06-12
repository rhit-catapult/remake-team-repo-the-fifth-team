import pygame
import sys
import my_character
import random
import block
import time
class Map:
    def __init__(self, screen, blocks, speed):
        self.screen = screen
        self.blocks = blocks
        self.speed = speed
    def update_map(self):
        for block in self.blocks:
            block.speed = self.speed
            block.update()
    def draw_map(self):
        for block in self.blocks:
            block.draw()

def test_map():
    screen = pygame.display.set_mode((640, 480))
    block_list = []
    for i in range(50):
        block_list.append(block.Block(screen, 50, 50, 50 * i, 430, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
    map = Map(screen, block_list, 2)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("white")
        map.update_map()
        map.draw_map()
        pygame.display.update()
# test_map()
