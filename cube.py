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
        self.jump_strength = -18
        self.on_ground = True
        self.color = color
        self.color_backup = color
        self.rotation = 0
        self.map = map
        self.loss = False
        self.jump_requested = False

    def reset(self):
        self.loss = False
        self.color = self.color_backup
        self.y = self.screen.get_height() - 40 - self.size
        self.vy = 0
        self.on_ground = True
        self.rotation = 0
    def jump(self):
        if self.on_ground:
            self.vy = self.jump_strength
            self.on_ground = False

    def check_triangle_collision(self, block):
        x1, y1 = block.x, block.y
        if not block.flipped:
            x2, y2 = block.x - block.width / 2, block.y + block.height
            x3, y3 = block.x + block.width / 2, block.y + block.height
        else:
            x2, y2 = block.x - block.width / 2, block.y - block.height
            x3, y3 = block.x + block.width / 2, block.y - block.height
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
        self.jump_strength = -18
        self.gravity = 0.8
        flipped = False
        for block in self.map.blocks:
            if block.flipped and block.x <= self.x + self.size and block.x + block.width >= self.x:
                self.jump_strength = 18
                self.gravity = -0.8
                flipped = True
            
        if self.loss:
            self.vy = 0
            self.map.speed = 0
        self.y += self.vy
        count_collisions = 0
        was_on_ground = self.on_ground
        for block in self.map.blocks:
            if not block.flipped and self.x + self.size >= block.x and self.x + self.size < block.x + 2 and self.y + self.size > block.y and self.y < block.y + block.height and block.y < self.screen.get_height() - 40:
                self.color = (255, 0, 0)
                self.vy = 0
                self.loss = True
                self.map.speed = 0
            elif not block.flipped and block.type == "spike" and self.check_triangle_collision(block):
                self.color = (255, 0, 0)
                self.vy = 0
                self.loss = True
                self.map.speed = 0
            elif not block.flipped and block.x >= self.x - self.size and block.x <= self.x + self.size and self.y >= block.y - self.size and block.y < self.screen.get_height() - 40 and block.type == "normal":
                self.y = block.y - self.size
                self.vy = 0
                count_collisions += 1
                if not self.on_ground:
                    self.rotation = 0
                self.on_ground = True
        for block in self.map.blocks:
            if block.flipped and self.x + self.size >= block.x and self.x + self.size < block.x + 2 and self.y < block.y + block.height and self.y + self.size > block.y and block.y > 40:
                self.color = (255, 0, 0)
                self.vy = 0
                self.loss = True
                self.map.speed = 0
            elif block.flipped and block.type == "spike" and self.check_triangle_collision(block):
                self.color = (255, 0, 0)
                self.vy = 0
                self.loss = True
                self.map.speed = 0
            elif block.flipped and block.x >= self.x - self.size and block.x <= self.x + self.size and self.y <= block.y + block.height and block.type == "normal":
                self.y = block.y + block.height
                self.vy = 0
                count_collisions += 1
                if not self.on_ground:
                    self.rotation = 0
                self.on_ground = True
        if self.y >= self.screen.get_height() - 40 - self.size and not flipped or self.y <= 40 and flipped:
            self.vy = 0
            if not self.on_ground:
                self.rotation = 0
            self.on_ground = True
        elif count_collisions == 0 and not self.loss:
            self.on_ground = False
            self.rotation = (self.rotation + 8) % 360
            self.vy += self.gravity
        
        # Auto-jump when landing if jump is requested
        if self.on_ground and not was_on_ground and self.jump_requested and not self.loss:
            self.jump()
            

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