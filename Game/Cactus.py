import random
import pygame
from Setting import FLOOR_Y


class Cactus(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        # Кактусы получаются трёх разных размеров
        height = random.choice([60, 80, 100])
        width = int(height * 0.75)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.right = 0            # появляется за левым краем экрана
        self.rect.bottom = FLOOR_Y

    def update(self, speed):
        self.rect.x += speed           # кактус едет к динозавру