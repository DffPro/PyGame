import os
import random
import pygame
import pygame.freetype

from Setting import *
from Cactus import Cactus
from Ground import Ground
from Dino import Dino


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Dino-Reverse')
        self.clock = pygame.time.Clock()
        self.font = pygame.freetype.Font(None, 40)
        self.small_font = pygame.freetype.Font(None, 28)

        self.load_images()

        self.ground = Ground(self.ground_image, 479)
        self.dino = Dino(self.dino_image, 800)
        self.cactus_group = pygame.sprite.Group()

        self.speed = START_SPEED
        self.high_score = self.load_high_score()
        self.status = 'Game'
        self.running = True

        pygame.time.set_timer(CACTUS_EVENT, 2500)

    def load_images(self):
        def load(name, size=None):
            path = os.path.join(IMAGE_DIR, name)
            image = pygame.image.load(path)
            if size:
                image = pygame.transform.scale(image, size)
            return image

        self.cactus_image = load('Cactus.jpg')  
        self.dino_image = load('Dino.jpg', (120, 120))
        self.ground_image = load('ground.png', (WIDTH, 142))

    def load_high_score(self):
        try:
            with open(SCORE_FILE, 'r') as file:
                return int(file.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open(SCORE_FILE, 'w') as file:
            file.write(str(self.high_score))

    def restart(self):
        self.cactus_group.empty()
        self.dino.reset()
        self.speed = START_SPEED
        self.status = 'Game'

    def game_over(self):
        self.status = 'Menu'
        if self.dino.score > self.high_score:
            self.high_score = self.dino.score
            self.save_high_score()

    def update_speed(self):
        level = self.dino.score // SPEED_UP_EVERY
        self.speed = min(START_SPEED + level, MAX_SPEED)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif self.status == 'Game':
                    if event.key in (pygame.K_SPACE, pygame.K_UP):
                        self.dino.jump()
                else:
                    if event.key == pygame.K_SPACE:
                        self.restart()

            elif event.type == CACTUS_EVENT:
                pygame.time.set_timer(CACTUS_EVENT, random.randint(1800, 4500))
                if self.status == 'Game':
                    self.cactus_group.add(Cactus(self.cactus_image))

    def update(self):
        if self.status != 'Game':
            return

        self.ground.update(self.speed)
        self.cactus_group.update(self.speed)
        self.dino.update()

        for cactus in self.cactus_group:
            if cactus.rect.left > WIDTH:        
                cactus.kill()
                self.dino.score += 1
                self.update_speed()
            elif cactus.rect.colliderect(self.dino.hitbox):
                self.game_over()

    def draw(self):
        self.screen.fill((255, 255, 255))

        if self.status == 'Game':
            self.ground.draw(self.screen)
            self.cactus_group.draw(self.screen)
            self.dino.draw(self.screen)
            self.font.render_to(self.screen, (820, 30),
                                str(self.dino.score), (0, 0, 0))
            self.small_font.render_to(self.screen, (20, 30),
                                      f'Рекорд: {self.high_score}', (100, 100, 100))
        else:
            self.font.render_to(self.screen, (300, 200),
                                'Game over :(', (0, 0, 0))
            self.small_font.render_to(self.screen, (300, 260),
                                      f'Счёт: {self.dino.score}', (0, 0, 0))
            self.small_font.render_to(self.screen, (300, 295),
                                      f'Рекорд: {self.high_score}', (0, 0, 0))
            self.small_font.render_to(self.screen, (230, 350),
                                      'SPACE - заново, ESC - выход', (0, 0, 0))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()


if __name__ == '__main__':
    Game().run()
