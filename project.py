import pygame
import sys
import json
import os
import block
import map
import cube
import menu
import random

def load_best():
    if os.path.exists("cube_jump_best.json"):
        try:
            with open("cube_jump_best.json", "r") as f:
                return json.load(f).get("best", 0)
        except Exception:
            return 0
    return 0


def save_best(value):
    try:
        with open("cube_jump_best.json", "w") as f:
            json.dump({"best": value}, f)
    except Exception:
        pass

def main():
    fonts = pygame.font.get_fonts()
    for font in sorted(fonts):
        print(font)

    pygame.init()
    W, H = 1200, 700
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Cube Jump")
    clock = pygame.time.Clock()
    map_type = 0
    block_list = []
    for i in range(31):
        block_list.append(block.Block(screen, 40, 40, 40 * i, screen.get_height() - 40, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
    map1 = map.Map(screen, block_list, 6, "Background.png", 3)
    cube1 = cube.Cube(screen, (0, 200, 200), map1)
    menu1 = menu.Menu(screen, "main", cube1)
    inf_reset = True
    level_reset = True
    msg_number = random.randint(0, 5)
    running = True
    while running:
        clock.tick(60)
        # Check for held inputs
        keys = pygame.key.get_pressed()
        mouse_buttons = pygame.mouse.get_pressed()
        cube1.jump_requested = (keys[pygame.K_SPACE] or mouse_buttons[0]) and menu1.mode in ["infinite", "level_1"]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cube1.jump()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and menu1.mode == "infinite":
                cube1.jump()
            elif event.type == pygame.MOUSEBUTTONDOWN and menu1.mode == "level_1":
                cube1.jump()
            elif event.type == pygame.MOUSEBUTTONDOWN and menu1.mode == "main":
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] >= screen.get_width() / 2 - menu1.main_button_width / 2 and mouse_pos[0] <=  screen.get_width() / 2 + menu1.main_button_width / 2 and mouse_pos[1] >=  screen.get_height() / 2 + menu1.main_button_height / 3 and mouse_pos[1] <=  screen.get_height() / 2 + menu1.main_button_height * 4/3:
                    menu1.mode = "infinite"
                    menu1.score = 0
                    msg_number = random.randint(0, 5)
                    if random.random() < 0.001:
                        msg_number = 0.001
                    pygame.mixer.music.load("BGM_Infinite.mp3")
                    pygame.mixer.music.play(-1)
                    map1.type = 0
                    inf_reset = True
                    level_reset = False
                    cube1.reset()
                    map1.speed = 6
                elif mouse_pos[0] >= screen.get_width() / 2 - menu1.main_button_width / 2 and mouse_pos[0] <=  screen.get_width() / 2 + menu1.main_button_width / 2 and mouse_pos[1] >= screen.get_height() / 2 + menu1.main_button_height * 1.5 and mouse_pos[1] <=  screen.get_height() / 2 + menu1.main_button_height * 2.5:
                    menu1.mode = "level_1"
                    menu1.score = 0
                    msg_number = random.randint(0, 5)
                    if random.random() < 0.001:
                        msg_number = 0.001
                    pygame.mixer.music.load("Level_1.mp3")
                    pygame.mixer.music.play(1)
                    map1.type = 1
                    inf_reset = False
                    level_reset = True
                    map1.blocks.clear()
                    map1.generate(inf_reset, level_reset)
                    cube1.reset()
                    map1.speed = 6
            elif event.type == pygame.MOUSEBUTTONDOWN and menu1.mode == "loss":
                mouse_pos = pygame.mouse.get_pos()
                menu1.score = 0
                if mouse_pos[0] >= screen.get_width() / 2 - menu1.main_button_width / 2 and mouse_pos[0] <=  screen.get_width() / 2 + menu1.main_button_width / 2 and mouse_pos[1] >= screen.get_height() / 2 - menu1.main_button_height * 1.25 and mouse_pos[1] <=  screen.get_height() / 2 - menu1.main_button_height * 0.25:
                    if map1.type == 0:
                        menu1.mode = "infinite"
                        msg_number = random.randint(0, 5)
                        if random.random() < 0.001:
                            msg_number = 0.001
                        pygame.mixer.music.load("BGM_Infinite.mp3")
                        pygame.mixer.music.play(-1)
                        map1.type = 0
                        inf_reset = True
                        level_reset = False
                        map1.blocks.clear()
                        map1.generate(inf_reset, level_reset)
                    else:
                        menu1.mode = "level_1"
                        msg_number = random.randint(0, 5)
                        if random.random() < 0.001:
                            msg_number = 0.001
                        pygame.mixer.music.load("Level_1.mp3")
                        pygame.mixer.music.play(1)
                        map1.type = 1
                        inf_reset = False
                        level_reset = True
                        map1.blocks.clear()
                        map1.generate(inf_reset, level_reset)
                    map1.update_map()
                    cube1.reset()
                    cube1.update()
                    map1.speed = 6
                elif mouse_pos[0] >= screen.get_width() / 2 - menu1.main_button_width / 2 and mouse_pos[0] <=  screen.get_width() / 2 + menu1.main_button_width / 2 and mouse_pos[1] >= screen.get_height() / 2 + menu1.main_button_height * 0.25 and mouse_pos[1] <=  screen.get_height() / 2 + menu1.main_button_height * 1.25:
                    menu1.mode = "main"
                    map1.type = 0
                    inf_reset = True
                    map1.blocks.clear()
                    cube1.reset()
                    menu1.score = 0
                    map1.speed = 6
            elif event.type == pygame.MOUSEBUTTONDOWN and menu1.mode == "win":
                mouse_pos = pygame.mouse.get_pos()
                menu1.score = 0
                if mouse_pos[0] >= screen.get_width() / 2 - menu1.main_button_width / 2 and mouse_pos[0] <=  screen.get_width() / 2 + menu1.main_button_width / 2 and mouse_pos[1] >= screen.get_height() / 2 - menu1.main_button_height * 1.25 and mouse_pos[1] <=  screen.get_height() / 2 - menu1.main_button_height * 0.25:
                    if map1.type == 0:
                        menu1.mode = "infinite"
                        msg_number = random.randint(0, 5)
                        if random.random() < 0.001:
                            msg_number = 0.001
                        pygame.mixer.music.load("BGM_Infinite.mp3")
                        pygame.mixer.music.play(-1)
                        map1.type = 0
                        inf_reset = True
                        level_reset = False
                        map1.blocks.clear()
                        map1.generate(inf_reset, level_reset)
                    else:
                        menu1.mode = "level_1"
                        msg_number = random.randint(0, 5)
                        if random.random() < 0.001:
                            msg_number = 0.001
                        pygame.mixer.music.load("Level_1.mp3")
                        pygame.mixer.music.play(1)
                        map1.type = 1
                        inf_reset = False
                        level_reset = True
                        map1.blocks.clear()
                        map1.generate(inf_reset, level_reset)
                    map1.update_map()
                    cube1.reset()
                    cube1.update()
                    map1.speed = 6
                elif mouse_pos[0] >= screen.get_width() / 2 - menu1.main_button_width / 2 and mouse_pos[0] <=  screen.get_width() / 2 + menu1.main_button_width / 2 and mouse_pos[1] >= screen.get_height() / 2 + menu1.main_button_height * 0.25 and mouse_pos[1] <=  screen.get_height() / 2 + menu1.main_button_height * 1.25:
                    menu1.mode = "main"
                    map1.type = 0
                    inf_reset = True
                    map1.blocks.clear()
                    cube1.reset()
                    menu1.score = 0
                    map1.speed = 6
        if menu1.mode == "main":
            menu1.draw_main_menu()      
        elif menu1.mode == "loss":
            menu1.score = round(menu1.score, 2)
            menu1.draw_loss_ui(msg_number) 
        elif menu1.mode == "win":
            menu1.score = round(menu1.score, 2)
            menu1.draw_win_ui(msg_number)
        else:
            map1.draw_background()
            cube1.update()
            cube1.draw(screen)
            map1.update_map()
            map1.generate(inf_reset, level_reset)
            map1.draw_map()
            if menu1.mode == "infinite":
                menu1.score += 1/60
            if menu1.mode == "level_1":
                menu1.score += 100/10500
                if menu1.score >= 100:
                    menu1.mode = "win"
            menu1.score = round(menu1.score, 2)
            menu1.draw_game_ui()
            inf_reset = False
            level_reset = False
            if cube1.loss:
                menu1.mode = "loss"
                pygame.mixer.music.stop()
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()