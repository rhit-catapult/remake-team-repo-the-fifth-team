import pygame
import sys
import cube
import random
import block
import time
class Map:
    def __init__(self, screen, blocks, speed, bg, bg_speed):
        self.screen = screen
        self.blocks = blocks
        self.speed = speed
        self.last_gen = 0
        self.count = 0
        self.bg1 = pygame.transform.scale(pygame.image.load(bg), (1200, 660))
        self.bg2 = pygame.transform.scale(pygame.image.load(bg), (1200, 660))
        self.bg_speed = bg_speed
        self.bg1_x = 0
        self.bg1_y = 0
        self.bg2_x = self.screen.get_width()
        self.bg2_y = 0
        self.type = 0
        self.level_1_block_count = 0
        self.level_1_time_elapsed = 0
    def update_map(self):
        self.bg1_x -= self.bg_speed
        self.bg2_x -= self.bg_speed
        if(self.bg1_x <= -1200):
            self.bg1_x = self.screen.get_width()
        if(self.bg2_x <= -1200):
            self.bg2_x = self.screen.get_width()
        for block in self.blocks:
            block.speed = self.speed
            block.update()
    def draw_background(self):
        # self.screen.fill((255, 255, 255))
        self.screen.blit(self.bg1, (self.bg1_x, self.bg1_y))
        self.screen.blit(self.bg1, (self.bg2_x, self.bg2_y))
    def draw_map(self):
        for block in self.blocks:
            block.draw()
    def generate(self, reset_i, reset_l):
        self.blocks = [bloc for bloc in self.blocks if not bloc.off_screen()]
        if self.type == 0:
            if reset_i:
                self.blocks.clear()
                for i in range(31):
                    self.blocks.append(block.Block(self.screen, 40, 40, 40 * i, self.screen.get_height() - 40, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
            if self.blocks[len(self.blocks) - 1].x <= self.screen.get_width():
                comp = 20
                if self.last_gen < 0:
                    self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40 - comp, self.screen.get_height() - 40, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                else:
                    self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 40, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                self.count += 1
                # if self.count != 2:
                #     self.last_gen = 0
                if self.count == 1 and self.last_gen < 0:
                    if random.random() < 0.1:
                        pick = self.last_gen
                    else:
                        pick = random.randint(-2, 3)
                    if pick < 0:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 60 - comp, self.screen.get_height() - 80, self.speed, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 1:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40 - comp, self.screen.get_height() - 80, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 2:
                        for i in range(2):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40 - comp, self.screen.get_height() - 120 + i * 40, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 3 and self.blocks[len(self.blocks) - 4].y > self.screen.get_height() - 40 and  self.blocks[len(self.blocks) - 4].type != "spike":
                        for i in range(3):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40 - comp, self.screen.get_height() - 160 + i * 40, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    self.last_gen = pick
                    self.count = 0
                elif self.count == 1:
                    if(random.random() < 0.5):
                        pick = self.last_gen
                    else:
                        pick = random.randint(-2, 3)
                    if pick == -1:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 60, self.screen.get_height() - 80, self.speed, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 1:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 2:
                        for i in range(2):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 120 + i * 40, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pick == 3 and self.blocks[len(self.blocks) - 4].y > self.screen.get_height() - 40 and  self.blocks[len(self.blocks) - 4].type != "spike":
                        for i in range(3):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 160 + i * 40, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    self.last_gen = pick
                    self.count = 0
        elif self.type == 1:
            # Music-synchronized level generation for Level_1.mp3 (169.30 seconds)
            if reset_l:
                self.level_1_time_elapsed = 0
                self.level_1_block_count = 0
                self.blocks.clear()
                # Initialize starting blocks like type 0
                for i in range(31):
                    self.blocks.append(block.Block(self.screen, 40, 40, 40 * i, self.screen.get_height() - 40, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    self.level_1_block_count += 1
            
            self.level_1_time_elapsed += 1 / 60.0
            
            # Generate one block per frame, tracking block count for pattern
            if self.blocks[len(self.blocks) - 1].x <= self.screen.get_width():
                current_time = self.level_1_time_elapsed
                block_count = self.level_1_block_count
                
                # Always add base floor block
                self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 40, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                
                # First 3 seconds: no obstacles
                if current_time < 3:
                    pass  # Just floor blocks
                
                # INTRO (3-30s): Introduce vertical with 3-block platforms
                elif current_time < 30:
                    if block_count % 26 == 24:  # Spike every 26 blocks
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, self.speed, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    if block_count % 30 == 29:  # Start 3-block platform every 30 blocks
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    if block_count % 30 == 30:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 120, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    if block_count % 30 == 31:
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 160, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                
                # VERSE 1 (30-60s): Up-down height variations
                elif current_time < 60:
                    # Pattern: low-mid-high-mid-low cycle with spikes
                    pattern = block_count % 24
                    if pattern == 23:  # Spike at ground level
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, self.speed, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 0 or pattern == 5:  # Mid-height (2 blocks)
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 120, self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 12:  # High peak (4 blocks)
                        for h in range(4):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                
                # CHORUS (60-90s): Complex vertical challenges with valleys
                elif current_time < 90:
                    pattern = block_count % 28
                    if pattern == 27:  # Spike
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, self.speed, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 0:  # Low valley - back to floor
                        pass  # Just floor
                    elif pattern == 6:  # Jump to medium (3 blocks)
                        for h in range(3):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 14:  # High peak (5 blocks)
                        for h in range(5):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 20:  # Drop back down (2 blocks)
                        for h in range(2):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                
                # VERSE 2 (90-120s): Frequent height changes with spikes
                elif current_time < 120:
                    pattern = block_count % 20
                    if pattern == 19:  # Spike
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, self.speed, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 0:  # High (4 blocks)
                        for h in range(4):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 8:  # Drop to medium (2 blocks)
                        for h in range(2):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 14:  # Low (1 block = floor)
                        pass
                
                # BRIDGE (120-150s): Extreme vertical challenge - tall peaks and deep valleys
                elif current_time < 150:
                    pattern = block_count % 26
                    if pattern == 25:  # Spike gauntlet
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, self.speed, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 0:  # Very high tower (6 blocks)
                        for h in range(6):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 6:  # Drop dramatically to low (1 block)
                        pass
                    elif pattern == 10:  # Jump back up to medium-high (4 blocks)
                        for h in range(4):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 16:  # Down again (1 block)
                        pass
                    elif pattern == 20:  # Final peak before outro (5 blocks)
                        for h in range(5):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                
                # OUTRO (150-169.3s): Cool down with moderate vertical sections
                else:
                    pattern = block_count % 22
                    if pattern == 21:  # Occasional spike
                        self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80, self.speed, "spike", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 5:  # Medium platform (3 blocks)
                        for h in range(3):
                            self.blocks.append(block.Block(self.screen, 40, 40, self.screen.get_width() + 40, self.screen.get_height() - 80 - (h * 40), self.speed, "normal", (0, 0, 0), 5, (150, 150, 150)))
                    elif pattern == 13:  # Return to floor
                        pass
                
                self.level_1_block_count += 1
            

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
