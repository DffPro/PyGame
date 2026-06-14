import pygame

pygame.init()

screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('Dino-Reverse')
clock = pygame.time.Clock()


cactus_Image = pygame.image.load('C:/Users/Фрошикейн/PyGame/Game/Image/Cactus.jpg')
dino_Image = pygame.image.load('C:/Users/Фрошикейн/PyGame/Game/Image/Dino.jpg')
dino_Image = pygame.transform.scale(dino_Image, (120, 120))
ground_Image = pygame.image.load('C:/Users/Фрошикейн/PyGame/Game/Image/ground.png')
ground_Image = pygame.transform.scale(ground_Image, (900, 142))

ground_group = pygame.sprite.Group()
cactus_group = pygame.sprite.Group()

ground_event = pygame.USEREVENT
cactus_event = pygame.USEREVENT +1
pygame.time.set_timer(ground_event, 1000)

class Ground(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        self.rect.x -= -3
        if self.rect.right <0:
            self.kill() 

class Dino():
    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.y = 0
        self.step = 5
        self.max_jump = 40
        self.in_jump = False
    
    def jump(self):
        if self.in_jump:
            if self.y < self.max_jump:
                self.y += 1
                self.rect.y -= self.step
            elif self.y < self.max_jump * 2:
                self.y += 1 
                self.rect.y += self.step
            else:
                self.in_jump = False
                self.y = False
    
    def draw(self):
        screen.blit(self.image, self.rect)

dino = Dino(dino_Image, (800, 500))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            dino.in_jump = True
        if event.type == ground_event:
            g = Ground(ground_Image, (100, 550))
            ground_group.add(g)

    screen.fill((0, 0, 0))
    ground_group.draw(screen)
    dino.jump()
    dino.draw()
    ground_group.update()
    pygame.display.flip()
    clock.tick(60)
