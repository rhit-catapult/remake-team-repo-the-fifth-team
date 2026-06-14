import pygame
import sys
import json
import os
import block
import map
import cube

class Menu:
    def __init__(self, screen, mode):
        self.screen = screen
        self.mode = mode
        self.button_size = 1
        self.main_button_width = self.button_size * self.screen.get_width() / 4
        self.main_button_height = self.button_size * self.screen.get_height() / 9
        self.color = (0, 100, 100)
    def draw_main_menu(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 + self.main_button_height / 3, self.main_button_width, self.main_button_height),)
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 + self.main_button_height * 1.5, self.main_button_width, self.main_button_height),)