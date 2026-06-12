import pygame

pygame.init()

screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('Dino-Reverse')
clock = pygame.time.Clock()


cactus_Image = pygame.image.load('C:/Users/Фрошикейн/PyGame/Game/Image/Cactus.jpg')
dino_Image = pygame.image.load('C:/Users/Фрошикейн/PyGame/Game/Image/Dino.jpg')
dino_Image = pygame.transform.scale(dino_Image, (120, 120))
ground_Image = pygame.image.load('C:/Users/Фрошикейн/PyGame/Game/Image/ground.png')

ground_group = pygame.sprite.Group()
cactus_group = pygame.sprite.Group()

ground_event = pygame.USEREVENT
cactus_event = pygame.USEREVENT +1
pygame.time.set_timer(ground_event, 2000)

class Ground(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        self.rect.x -= 3
        if self.rect.right <0:
            self.kill() 

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
                self.rect.y -= 1
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
        if event.type == pygame.KEYDOWN:
            dino.in_jump = True
        if event.type == ground_event:
            g = Ground(ground_Image, (900, 450))
            ground_group.add(g)

    screen.fill((0, 0, 0))
    dino.jump()
    dino.draw()
    ground_group.update()
    ground_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)
