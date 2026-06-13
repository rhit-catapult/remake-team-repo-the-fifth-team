import pygame
import sys
import json
import os
import block
import map
import cube

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


def draw_hud(surface, width, height, score):
    score_text = pygame.font.SysFont("sans", 22).render(f"Score: {score}", True, (255, 255, 255))
    best_text = pygame.font.SysFont("sans", 22).render(f"Best: {score}", True, (255, 255, 255))
    surface.blit(score_text, (10, 10))
    surface.blit(best_text, (150, 10))

def main():
    pygame.init()
    W, H = 1200, 700
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Cube Jump")
    clock = pygame.time.Clock()
    score = 0
    block_list = []
    for i in range(31):
        block_list.append(block.Block(screen, 40, 40, 40 * i, screen.get_height() - 40, 5, "normal", (0, 0, 0), 5, (150, 150, 150)))
    map1 = map.Map(screen, block_list, 4)
    cube1 = cube.Cube(screen, (0, 200, 200), map1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cube1.jump()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cube1.jump()
        screen.fill((255, 255, 255))
        cube1.update()
        cube1.draw(screen)
        map1.update_map()
        map1.generate(0)
        map1.draw_map()
        draw_hud(screen, W, H, 0)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()