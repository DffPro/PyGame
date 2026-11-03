import pygame

class Cactus(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self, dino):
        self.rect.x -= -5
        if self.rect.right > 1000:
            self.kill()
            dino.score +=1
        if self.rect.colliderect(dino.rect):
            dino.game_status = 'Menu' 