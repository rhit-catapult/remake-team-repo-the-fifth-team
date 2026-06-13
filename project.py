import pygame
import sys
import json
import os

pygame.init()

W, H = 900, 320
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Cube Jump")
clock = pygame.time.Clock()
font = pygame.font.SysFont("sans", 22)
big_font = pygame.font.SysFont("sans", 36)

BG_COLOR = (20, 24, 60)
GRID_COLOR = (40, 48, 100)
GROUND_COLOR = (30, 34, 80)
CUBE_COLOR = (0, 230, 200)
SPIKE_COLOR = (255, 80, 120)
BLOCK_COLOR = (120, 90, 255)
TEXT_COLOR = (255, 255, 255)
MSG_COLOR = (160, 170, 220)

GROUND_Y = H - 60
BEST_FILE = "cube_jump_best.json"


def load_best():
    if os.path.exists(BEST_FILE):
        try:
            with open(BEST_FILE, "r") as f:
                return json.load(f).get("best", 0)
        except Exception:
            return 0
    return 0


def save_best(value):
    try:
        with open(BEST_FILE, "w") as f:
            json.dump({"best": value}, f)
    except Exception:
        pass


class Cube:
    def __init__(self):
        self.size = 32
        self.x = 80
        self.y = GROUND_Y - self.size
        self.vy = 0
        self.gravity = 0.8
        self.jump_strength = -13
        self.on_ground = True
        self.rotation = 0

    def reset(self):
        self.y = GROUND_Y - self.size
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
        if self.y >= GROUND_Y - self.size:
            self.y = GROUND_Y - self.size
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
        pygame.draw.rect(surf, CUBE_COLOR, (0, 0, self.size, self.size), border_radius=4)
        pygame.draw.rect(surf, (255, 255, 255), (0, 0, self.size, self.size), 2, border_radius=4)
        rotated = pygame.transform.rotate(surf, -self.rotation)
        rect = rotated.get_rect(center=(cx, cy))
        surface.blit(rotated, rect.topleft)


class Spike:
    def __init__(self, x):
        self.x = x
        self.size = 30

    def rect(self):
        return pygame.Rect(self.x + 6, GROUND_Y - self.size, self.size - 12, self.size)

    def update(self, speed):
        self.x -= speed

    def draw(self, surface):
        points = [
            (self.x, GROUND_Y),
            (self.x + self.size / 2, GROUND_Y - self.size),
            (self.x + self.size, GROUND_Y),
        ]
        pygame.draw.polygon(surface, SPIKE_COLOR, points)
        pygame.draw.polygon(surface, (255, 255, 255), points, 1)


class Block:
    def __init__(self, x, height):
        self.x = x
        self.size = 32
        self.height = height

    def rect(self):
        return pygame.Rect(self.x, GROUND_Y - self.height, self.size, self.height)

    def update(self, speed):
        self.x -= speed

    def draw(self, surface):
        r = self.rect()
        pygame.draw.rect(surface, BLOCK_COLOR, r, border_radius=4)
        pygame.draw.rect(surface, (255, 255, 255), r, 2, border_radius=4)


def build_level():
    """Empty level - no obstacles."""
    return []


class Game:
    def __init__(self):
        self.best = load_best()
        self.reset()

    def reset(self):
        self.cube = Cube()
        self.cube.reset()
        self.obstacles = build_level()
        self.speed = 6
        self.distance = 0
        self.score = 0
        self.message = "Press SPACE / click to jump."

    def update(self):
        self.cube.update()
        self.distance += self.speed
        self.score = int(self.distance / 10)

    def draw(self, surface):
        surface.fill(BG_COLOR)

        for gx in range(0, W, 40):
            pygame.draw.line(surface, GRID_COLOR, (gx, 0), (gx, H), 1)
        for gy in range(0, H, 40):
            pygame.draw.line(surface, GRID_COLOR, (0, gy), (W, gy), 1)

        pygame.draw.rect(surface, GROUND_COLOR, (0, GROUND_Y, W, H - GROUND_Y))
        pygame.draw.line(surface, CUBE_COLOR, (0, GROUND_Y), (W, GROUND_Y), 2)

        for obs in self.obstacles:
            if -50 < obs.x < W + 50:
                obs.draw(surface)

        self.cube.draw(surface)


def draw_hud(surface, game):
    score_text = font.render(f"Score: {game.score}", True, TEXT_COLOR)
    best_text = font.render(f"Best: {game.best}", True, TEXT_COLOR)
    surface.blit(score_text, (10, 10))
    surface.blit(best_text, (150, 10))

    msg_text = font.render(game.message, True, MSG_COLOR)
    surface.blit(msg_text, (W / 2 - msg_text.get_width() / 2, H - 24))


def main():
    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.cube.jump()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.cube.jump()

        game.update()
        game.draw(screen)
        draw_hud(screen, game)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()