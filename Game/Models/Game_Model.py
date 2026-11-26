import random

from Models.Cactus import Cactus
from Models.Dino import Dino
from Models.Ground import Ground
from Setting import (CACTUS_HEIGHTS, MAX_SPAWN_DELAY, MAX_SPEED,
                      MIN_SPAWN_DELAY, SPEED_UP_EVERY, START_SPEED,
                      STATE_GAME_OVER, STATE_MENU, STATE_PLAYING)


class GameModel:

    def __init__(self, high_score=0):
        self.dino = Dino()
        self.ground = Ground()
        self.state = STATE_MENU
        self.high_score = high_score
        self._cactuses = []
        self._score = 0
        self._speed = START_SPEED
        self._spawn_timer = 0
        self._next_spawn = MIN_SPAWN_DELAY

    @property
    def score(self):
        return self._score

    @property
    def speed(self):
        return self._speed

    @property
    def cactuses(self):
        return tuple(self._cactuses)

    def start(self):
        self.dino.reset()
        self._cactuses.clear()
        self._score = 0
        self._speed = START_SPEED
        self._spawn_timer = 0
        self._next_spawn = self._random_delay()
        self.state = STATE_PLAYING

    def go_to_menu(self):
        self.state = STATE_MENU

    def jump(self):
        if self.state == STATE_PLAYING:
            self.dino.jump()

    def add_cactus(self, cactus):
        self._cactuses.append(cactus)

    def update(self):
        if self.state != STATE_PLAYING:
            return

        self.ground.update(self._speed)
        self.dino.update()
        for cactus in self._cactuses:
            cactus.update(self._speed)

        self._spawn_timer += 1
        if self._spawn_timer >= self._next_spawn:
            self._spawn_cactus()

        self._remove_passed_cactuses()
        self._check_collisions()

    def _random_delay(self):
        return random.randint(MIN_SPAWN_DELAY, MAX_SPAWN_DELAY)

    def _spawn_cactus(self):
        self.add_cactus(Cactus(random.choice(CACTUS_HEIGHTS)))
        self._spawn_timer = 0
        self._next_spawn = self._random_delay()

    def _remove_passed_cactuses(self):
        # Кактус ушёл за экран, значит динозавр его перепрыгнул: очко
        for cactus in self._cactuses[:]:
            if cactus.is_off_screen():
                self._cactuses.remove(cactus)
                self._score += 1
                self._update_speed()

    def _update_speed(self):
        # Чем больше очков, тем быстрее игра, но не быстрее MAX_SPEED
        self._speed = min(START_SPEED + self._score // SPEED_UP_EVERY, MAX_SPEED)

    def _check_collisions(self):
        for cactus in self._cactuses:
            if cactus.rect.colliderect(self.dino.hitbox):
                self._game_over()
                return

    def _game_over(self):
        self.state = STATE_GAME_OVER
        if self._score > self.high_score:
            self.high_score = self._score