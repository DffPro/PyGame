import pygame
import random
import pygame.freetype

pygame.init()

screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('Dino-Reverse')
clock = pygame.time.Clock()
font = pygame.freetype.Font(None, 40)

cactus_Image = pygame.image.load('C:/Users/Фрошикейн/PyGame/Game/Image/Cactus.jpg')
cactus_Image = pygame.transform.scale(cactus_Image, (60, 80))
dino_Image = pygame.image.load('C:/Users/Фрошикейн/PyGame/Game/Image/Dino.jpg')
dino_Image = pygame.transform.scale(dino_Image, (120, 120))
ground_Image = pygame.image.load('C:/Users/Фрошикейн/PyGame/Game/Image/ground.png')
ground_Image = pygame.transform.scale(ground_Image, (900, 142))

ground_group = pygame.sprite.Group()
cactus_group = pygame.sprite.Group()

ground_event = pygame.USEREVENT
cactus_event = pygame.USEREVENT +1
pygame.time.set_timer(ground_event, 1000)
pygame.time.set_timer(cactus_event, 4000)


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        self.rect.x -= -5
        if self.rect.right < 0:
            self.kill() 

class Cactus(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
    def update(self):
        self.rect.x -= -5
        if self.rect.right > 1000:
            self.kill()
            dino.score +=1
        if self.rect.colliderect(dino.rect):
            dino.game_status = 'Menu' 

class Dino():
    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.y = 0
        self.step = 5
        self.max_jump = 40
        self.in_jump = False
        self.score = 0
        self.game_status = 'Game'
    
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
g = Ground(ground_Image, (300, 550))
ground_group.add(g)
g = Ground(ground_Image, (900, 550))
ground_group.add(g)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            dino.in_jump = True
        if event.type == ground_event:
            g = Ground(ground_Image, (10, 550))
            ground_group.add(g)
        if event.type == cactus_event:
            pygame.time.set_timer(cactus_event, random.randint(4000, 8500))
            c = Cactus(cactus_Image, (1, 520))
            cactus_group.add(c)

    screen.fill((255, 255, 255))
    if dino.game_status == 'Game':
        ground_group.draw(screen)
        cactus_group.update()
        cactus_group.draw(screen)
        dino.jump()
        dino.draw()
        font.render_to(screen, (850, 50), str(dino.score), (0,0,0))
        ground_group.update()
    else:
        font.render_to(screen, (450, 200), 'Game over', (0,0,0 ))
    pygame.display.flip()
    clock.tick(60)
