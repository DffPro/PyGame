import os

import pygame
import pygame.freetype

from Setting import (BLACK, DINO_SIZE, FONT_BIG, FONT_SMALL, GRAY,
                      GROUND_HEIGHT, GROUND_IMAGE_Y, IMAGE_DIR,
                      STATE_GAME_OVER, STATE_MENU, STATE_PLAYING,
                      WHITE, WIDTH)


class GameView:
    """Только рисует то, что ему дала модель. Ничего не считает."""

    def __init__(self, screen):
        self._screen = screen
        self._big_font = pygame.freetype.Font(None, FONT_BIG)
        self._small_font = pygame.freetype.Font(None, FONT_SMALL)

        self._dino_image = self._load('Dino.jpg', DINO_SIZE)
        self._ground_image = self._load('ground.png', (WIDTH, GROUND_HEIGHT))
        self._cactus_source = self._load('Cactus.jpg')
        self._cactus_cache = {}       # картинки кактусов по размерам

    def draw(self, model):
        self._screen.fill(WHITE)

        if model.state == STATE_MENU:
            self._draw_menu(model)
        else:
            self._draw_world(model)
            if model.state == STATE_GAME_OVER:
                self._draw_game_over(model)

        pygame.display.flip()

    def _load(self, name, size=None):
        image = pygame.image.load(os.path.join(IMAGE_DIR, name)).convert_alpha()
        if size:
            image = pygame.transform.scale(image, size)
        return image

    def _get_cactus_image(self, size):
        if size not in self._cactus_cache:
            self._cactus_cache[size] = pygame.transform.scale(self._cactus_source, size)
        return self._cactus_cache[size]

    def _draw_text(self, text, y, font, color=BLACK, x=None):
        surface, rect = font.render(text, color)
        rect.y = y
        if x is None:
            rect.centerx = WIDTH // 2
        else:
            rect.x = x
        self._screen.blit(surface, rect)

    def _draw_world(self, model):
        offset = model.ground.offset
        top = GROUND_IMAGE_Y
        self._screen.blit(self._ground_image, (offset - WIDTH, top))
        self._screen.blit(self._ground_image, (offset, top))

        for cactus in model.cactuses:
            image = self._get_cactus_image(cactus.rect.size)
            self._screen.blit(image, cactus.rect)

        self._screen.blit(self._dino_image, model.dino.rect)

        self._draw_text(str(model.score), 30, self._big_font, x=WIDTH - 80)
        self._draw_text(f'Рекорд: {model.high_score}', 30,
                        self._small_font, GRAY, x=20)

    def _draw_menu(self, model):
        self._draw_text('Dino-Reverse', 150, self._big_font)
        self._draw_text(f'Рекорд: {model.high_score}', 230, self._small_font)
        self._draw_text('SPACE - играть', 300, self._small_font)
        self._draw_text('ESC - выход', 340, self._small_font)

    def _draw_game_over(self, model):
        self._draw_text('Game over :(', 150, self._big_font)
        self._draw_text(f'Счёт: {model.score}', 210, self._small_font)
        self._draw_text('SPACE - заново, M - меню', 250, self._small_font)