import pygame
import sys
import json
import os
import block
import map
import cube
import random

class Menu:
    def __init__(self, screen, mode, cube):
        self.screen = screen
        self.mode = mode
        self.button_size = 1
        self.main_button_width = self.button_size * self.screen.get_width() / 4
        self.main_button_height = self.button_size * self.screen.get_height() / 9
        self.color = (0, 100, 100)
        self.cube = cube
        self.font = pygame.font.SysFont("segoeuiemoji", 60)
        self.text_color = (255, 255, 0)
        self.score = 0
        self.font2 = pygame.font.SysFont("segoeuiemoji", 30)
        self.font_special = pygame.font.SysFont("wingdings", 60)
        self.font_label = pygame.font.SysFont("segoeuiemoji", 15)
    def draw_main_menu(self):
        self.screen.fill((0, 0, 0))
        title = self.font.render("ALGEBRA RUN", True, self.text_color)
        self.screen.blit(title, (self.screen.get_width() / 2 - title.get_width() / 2, 150))
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 + self.main_button_height / 3, self.main_button_width, self.main_button_height),)
        button1_label = self.font2.render("INFINITE" , True, (255, 255, 0))
        self.screen.blit(button1_label, (self.screen.get_width() / 2 - button1_label.get_width() / 2, self.screen.get_height() / 2 + self.main_button_height* 5/6 - button1_label.get_height() / 2))
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 + self.main_button_height * 1.5, self.main_button_width, self.main_button_height),)
        button2_label = self.font2.render("THE ONE LEVEL" , True, (255, 255, 0))
        self.screen.blit(button2_label, (self.screen.get_width() / 2 - button2_label.get_width() / 2, self.screen.get_height() / 2 + self.main_button_height * 2 - button1_label.get_height() / 2))
        other_title = self.font2.render("By The Fifth Team" , True, (255, 255, 255))
        self.screen.blit(other_title, (self.screen.get_width() - other_title.get_width(), self.screen.get_height() - other_title.get_height()))
    def draw_game_ui(self):
        score_text = self.font2.render(str(self.score), True, (255, 255, 0))
        self.screen.blit(score_text, (0, 0))
    def draw_loss_ui(self, msg_number):
        if msg_number == 0:
            title = self.font.render("SKILL ISSUE", True, (255, 255, 0))
        elif msg_number == 1:
            title = self.font.render("I feel you see this frequently...", True, (255, 255, 0))
        elif msg_number == 2:
            title = self.font.render("Tip: you can jump", True, (255, 255, 0))
        elif msg_number == 3:
            title = self.font.render("Maybe try jumping...", True, (255, 255, 0))
        elif msg_number == 4:
            title = self.font.render("Tip: avoid the spikes...", True, (255, 255, 0))
        elif msg_number == 5:
            title = self.font.render("Tip: don't be bad...", True, (255, 255, 0))
        if msg_number == 0.001:
            title = self.font_special.render("Check the bottom\nright of the poster", True, (255, 255, 0))
        
        self.screen.blit(title, (self.screen.get_width() / 2 - title.get_width() / 2, 120))
        sub_title = self.font2.render("SCORE: "  + str(self.score), True, (255, 255, 0))
        self.screen.blit(sub_title, (self.screen.get_width() / 2 - sub_title.get_width() / 2, 200))
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 - self.main_button_height * 1.25, self.main_button_width, self.main_button_height),)
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 + self.main_button_height * 0.25, self.main_button_width, self.main_button_height),)
        button1_label = self.font2.render("RETRY" , True, (255, 255, 0))
        self.screen.blit(button1_label, (self.screen.get_width() / 2 - button1_label.get_width() / 2, self.screen.get_height() / 2 - self.main_button_height * 0.75 - button1_label.get_height() / 2))
        button2_label = self.font2.render("MAIN MENU" , True, (255, 255, 0))
        self.screen.blit(button2_label, (self.screen.get_width() / 2 - button2_label.get_width() / 2, self.screen.get_height() / 2 + self.main_button_height * 0.75 - button2_label.get_height() / 2))
    def draw_win_ui(self, msg_number):
        if msg_number == 0:
            title = self.font.render("GOOD ENOUGH", True, (255, 255, 0))
        elif msg_number == 1:
            title = self.font.render("You cheated didn't you?", True, (255, 255, 0))
        elif msg_number == 2:
            title = self.font.render("Congrats on beating the easiest level", True, (255, 255, 0))
        elif msg_number == 3:
            title = self.font.render("You're never getting that time back", True, (255, 255, 0))
        elif msg_number == 4:
            title = self.font.render("So you DO have fingers!", True, (255, 255, 0))
        elif msg_number == 5:
            title = self.font.render("That was only 2 and a half minutes", True, (255, 255, 0))
        title = self.font.render("GOOD ENOUGH", True, (255, 255, 0))
        self.screen.blit(title, (self.screen.get_width() / 2 - title.get_width() / 2, 120))
        sub_title = self.font2.render("SCORE: "  + str(self.score), True, (255, 255, 0))
        self.screen.blit(sub_title, (self.screen.get_width() / 2 - sub_title.get_width() / 2, 200))
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 - self.main_button_height * 1.25, self.main_button_width, self.main_button_height),)
        pygame.draw.rect(self.screen, self.color, (self.screen.get_width() / 2 - self.main_button_width / 2, self.screen.get_height() / 2 + self.main_button_height * 0.25, self.main_button_width, self.main_button_height),)

