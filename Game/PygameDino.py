import pygame

pygame.init()

screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption('Dino-Reverse')
clock = pygame.time.Clock()
font = pygame.freetype.Font(None, 40)

cactus_Image = pygame.image.load('C:\Users\Фрошикейн\PyGame\Game\Image\Cactus.jpg')
dino_Image = pygame.image.load('Image/Dino.jpg')
dino_Image = pygame.transform.scale(dino_Image, (50, 50))
ground_Image = pygame.image.load('Image/ground.png')


class Dino():
    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.y = 0
        self.max_jump = 40
        self.in_jump = False
    
    def jump(self):
        if self.in_jump:
            if self.y < self.max_jump:
                self.y += 1
                self.rect.y += 1
            elif self.y < self.max_jump * 2:
                self.y += 1 
                self.rect.y += 1 
            else:
                self.in_jump = False
                self.y = False
    
    def draw(self):
        screen.blit(self.image, self.rect)

dino = Dino(dino_Image, (100, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event == pygame.KEYDOWN:
            dino.in_jump = True

    screen.fill((0,0,0))
    dino.draw()
    dino.jump
    pygame.display.flip()
    clock.tick(60)
