import pygame
import sys
import json
import os
import block
import map
import math
import cube

class Cube:
    def __init__(self, screen, color, map):
        self.screen = screen
        self.size = 39
        self.x = 80
        self.y = self.screen.get_height() - 40 - self.size
        self.vy = 0
        self.gravity = 0.8
        self.jump_strength = -14
        self.on_ground = True
        self.color = color
        self.rotation = 0
        self.map = map
        if self.on_ground:
         self.vy = self.jump_strength
        self.on_ground = False
        self.jump_held = True
        self.jump_time = 0.0
        if not hasattr(self, "max_jump_time"):
            self.max_jump_time = 0.20  
        self.max_jump_time = 0.20 
def hold_jump(self, holding, dt=0.0):
   def release_jump(self):
    self.jump_held = False
    self.jump_time = getattr(self, "max_jump_time", 0.20)
    if getattr(self, "jump_held", False) and holding and not self.on_ground and self.jump_time < self.max_jump_time:
        self.vy += self.jump_strength * dt * 3.0
        self.jump_time += dt
    if not holding:
        self.jump_held = False
        self.jump_time = self.max_jump_time

def release_jump(self):
    self.jump_held = False
    self.jump_time = getattr(self, "max_jump_time", 0.20)


    def reset(self):
        self.y = self.screen.get_height() - 40 - self.size
        self.vy = 0
        self.on_ground = True
        self.rotation = 0
    def jump(self):
        if self.on_ground:
            self.vy = self.jump_strength
            self.on_ground = False
            def jump(self):
                def check_triangle_collision(self, block):
                    x1, y1 = block.x, block.y
        x2, y2 = block.x - block.width / 2, block.y + block.height
        x3, y3 = block.x + block.width / 2, block.y + block.height
        
        def sign(px, py, ax, ay, bx, by):
            return (px - bx) * (ay - by) - (ax - bx) * (py - by)
        
        def point_in_triangle(px, py):
            d1 = sign(px, py, x1, y1, x2, y2)
            d2 = sign(px, py, x2, y2, x3, y3)
            d3 = sign(px, py, x3, y3, x1, y1)
            
            has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
            has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
            
            return not (has_neg and has_pos)
        
        cube_corners = [
            (self.x, self.y),
            (self.x + self.size, self.y),
            (self.x, self.y + self.size),
            (self.x + self.size, self.y + self.size)
        ]
        
        for cx, cy in cube_corners:
            if point_in_triangle(cx, cy):
                return True
        
        triangle_vertices = [(x1, y1), (x2, y2), (x3, y3)]
        for tx, ty in triangle_vertices:
            if self.x <= tx <= self.x + self.size and self.y <= ty <= self.y + self.size:
                return True
        
        return False

    def update(self):
        self.y += self.vy
        count_collisions = 0
        for block in self.map.blocks:
            # Check side collision with normal blocks
            if (self.x + self.size >= block.x and self.x + self.size <= block.x + 3 and self.y + self.size > block.y and self.y < block.y + block.height and block.y < self.screen.get_height() - 40):
                self.color = (255, 0, 0)
            elif block.type == "spike" and self.check_triangle_collision(block):
                self.color = (255, 0, 0)
            elif block.x >= self.x - self.size and block.x <= self.x + self.size and self.y >= block.y - self.size and block.y < self.screen.get_height() - 40 and block.type == "normal":
                self.y = block.y - self.size
                self.vy = 0
                count_collisions += 1
                if not self.on_ground:
                    self.rotation = 0
                self.on_ground = True
        if self.y >= self.screen.get_height() - 40 - self.size:
            self.y = self.screen.get_height() - 40 - self.size
            self.vy = 0
            if not self.on_ground:
                self.rotation = 0
            self.on_ground = True
        elif count_collisions == 0:
            self.on_ground = False
            self.rotation = (self.rotation + 8) % 360
            self.vy += self.gravity
            

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