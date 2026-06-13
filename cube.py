import pygame
import sys
import json
import os
import block
import map
import cube

class Cube:
    def __init__(self, screen, color, map):
        self.screen = screen
        self.size = 40
        self.x = 80
        self.y = self.screen.get_height() - 40 - self.size
        self.vy = 0
        self.gravity = 0.8
        self.jump_strength = -15
        self.on_ground = True
        self.color = color
        self.rotation = 0

    def reset(self):
        self.y = self.screen.get_height() - 40 - self.size
        self.vy = 0
        self.on_ground = True
        self.rotation = 0

    def jump(self):
        if self.on_ground:
            self.vy = self.jump_strength
            self.on_ground = False

    def update(self):
        self.vy += self.gravity
        self.y += self.vy
        if self.y >= self.screen.get_height() - 40 - self.size:
            self.y = self.screen.get_height() - 40 - self.size
            self.vy = 0
            if not self.on_ground:
                self.rotation = 0
            self.on_ground = True
        else:
            self.rotation = (self.rotation + 8) % 360

    def rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)

    def draw(self, surface):
        cx = self.x + self.size / 2
        cy = self.y + self.size / 2
        surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.rect(surf, self.color, (0, 0, self.size, self.size), border_radius=4)
        pygame.draw.rect(surf, (255, 255, 255), (0, 0, self.size, self.size), 2, border_radius=4)
        rotated = pygame.transform.rotate(surf, -self.rotation)
        rect = rotated.get_rect(center=(cx, cy))
        surface.blit(rotated, rect.topleft)