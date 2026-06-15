import pygame
import sys
import json
import os
import block
import map
import cube

class Menu:
    def __init__(self, screen, mode, cube):
        self.screen = screen
        self.mode = mode
        self.button_size = 1
        self.main_button_width = self.button_size * self.screen.get_width() / 4
        self.main_button_height = self.button_size * self.screen.get_height() / 9
        self.color = (0, 100, 100)
        self.cube = cube
        self.font = pygame.font.SysFont("yugothic", 60)
        self.text_color = (0, 0, 0)
        self.score = 0
    def draw_main_menu(self):
        self.screen.fill((255, 255, 255))
        title = self.font.render("ALGEBRA RUN", True, (0, 0, 0))
        self.screen.blit(title, (0, 0))
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 + self.main_button_height / 3, self.main_button_width, self.main_button_height),)
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 + self.main_button_height * 1.5, self.main_button_width, self.main_button_height),)
    def draw_infinite_ui(self):
        pass
    def draw_loss_ui(self):
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 - self.main_button_height * 1.25, self.main_button_width, self.main_button_height),)
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 + self.main_button_height * 0.25, self.main_button_width, self.main_button_height),)

