from Models.Game_object import GameObject
from Setting import CACTUS_RATIO, FLOOR_Y, WIDTH


class Cactus(GameObject):
    def __init__(self, height):
        width = int(height * CACTUS_RATIO)
        super().__init__(width, height)
        self.rect.right = 0           
        self.rect.bottom = FLOOR_Y

    def update(self, speed):
        self.rect.x += speed          

    def is_off_screen(self):
        return self.rect.left > WIDTH