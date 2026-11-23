import pygame


class GameObject:
    """Базовый класс для всех объектов мира. Хранит только прямоугольник."""

    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)

    def update(self, speed):
        raise NotImplementedError('Каждый объект сам решает, как обновляться')