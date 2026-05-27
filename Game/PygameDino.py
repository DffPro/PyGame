import pygame

pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Dino-Reverse')
clock = pygame.time.Clock()
font = pygame.freetype.Font(None, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)