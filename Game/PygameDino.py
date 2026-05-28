import pygame

pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Dino-Reverse')
clock = pygame.time.Clock()
font = pygame.freetype.Font(None, 40)

class Dino():
    cactus_Image = pygame.image.load('Image/Cactus.jpg')
    dino_Image = pygame.image.load('Image/Dino.jpg')
    ground_Image = pygame.image.load('Image/ground.png')

dino = Dino(dino_Image, (100, 450))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0,0,0))
    dino.draw()
    pygame.display.flip()
    clock.tick(60)