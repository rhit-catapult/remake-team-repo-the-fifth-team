import pygame
import sys
import cube
import random
import block
import time
class Map:
    def __init__(self, screen, blocks, speed):
        self.screen = screen
        self.blocks = blocks
        self.speed = speed
        self.last_gen = 0
        self.count = 0
    def update_map(self):
        for block in self.blocks:
            block.speed = self.speed
            block.update()
    def draw_map(self):
        for block in self.blocks:
            block.draw()
    def generate(self, type):
        for bloc in self.blocks:
            if bloc.off_screen():
                self.blocks.remove(bloc)
        if type == 0:
            if self.blocks[len(self.blocks) - 1].x <= self.screen.get_width():
                comp = 20
                if self.last_gen == -1:
                    self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40 - comp, self.screen.get_height() - 40, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
                else:
                    self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 40, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
                self.count += 1
                if self.count != 2:
                    self.last_gen = 0
                if self.count == 2 and self.last_gen == -1:
                    pick = random.randint(-2, 3)
                    if pick < 0:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 60 - comp, self.screen.get_height() - 80, 5, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 1:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40 - comp, self.screen.get_height() - 80, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 2:
                        for i in range(2):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40 - comp, self.screen.get_height() - 120 + i * 40, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 3 and self.last_gen == 2:
                        for i in range(3):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40 - comp, self.screen.get_height() - 160 + i * 40, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    self.last_gen = pick
                    self.count = 0
                elif self.count == 2:
                    pick = random.randint(-1, 3)
                    if pick == -1:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 60, self.screen.get_height() - 80, 5, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 1:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 2:
                        for i in range(2):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 120 + i * 40, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 3 and self.last_gen == 2:
                        for i in range(3):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 160 + i * 40, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    self.last_gen = pick
                    self.count = 0
        elif type == 1:
            pass
                    

def test_map():
    screen = pygame.display.set_mode((1200, 700))
    block_list = []
    for i in range(31):
        block_list.append(block.Block(screen, 40, 40, 40 * i, screen.get_height() - 40, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
    map = Map(screen, block_list, 4)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill("white")
        map.update_map()
        map.draw_map()
        map.generate(0)
        pygame.display.update()
# test_map()
