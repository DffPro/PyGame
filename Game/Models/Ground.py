from Models.game_object import GameObject
from Setting import GROUND_HEIGHT, GROUND_IMAGE_Y, WIDTH


class Ground(GameObject):
    def __init__(self):
        super().__init__(WIDTH, GROUND_HEIGHT)
        self.rect.top = GROUND_IMAGE_Y
        self._offset = 0

    @property
    def offset(self):
        return self._offset

    def update(self, speed):
        # Остаток от деления делает прокрутку бесконечной
        self._offset = (self._offset + speed) % WIDTH