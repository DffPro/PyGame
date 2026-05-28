import pygame

pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Dino-Reverse')
clock = pygame.time.Clock()
font = pygame.freetype.Font(None, 40)

cactus_Image = pygame.image.load('Image/Cactus.jpg')
dino_Image = pygame.image.load('Image/Dino.jpg')
dino_Image = pygame.transform.scale
ground_Image = pygame.image.load('Image/ground.png')


class Dino():
    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    
    def draw(self):
        screen.blit(self.image, self.rect)

dino = Dino(dino_Image, (100, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0,0,0))
    dino.draw()
    pygame.display.flip()
    clock.tick(60)