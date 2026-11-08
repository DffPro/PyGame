import pygame
from Setting import FLOOR_Y, GRAVITY, JUMP_FORCE


class Dino:
    def __init__(self, image, x):
        self.image = image
        self.x = x
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.centerx = self.x
        self.rect.bottom = FLOOR_Y
        self.velocity_y = 0
        self.on_ground = True
        self.score = 0

    @property
    def hitbox(self):
        return self.rect.inflate(-40, -30)

    def jump(self):
        if self.on_ground:
            self.velocity_y = JUMP_FORCE
            self.on_ground = False

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.bottom >= FLOOR_Y:
            self.rect.bottom = FLOOR_Y
            self.velocity_y = 0
            self.on_ground = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)