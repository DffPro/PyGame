import os

WIDTH, HEIGHT = 900, 600
FPS = 60

# Путь считается от самого файла, поэтому игра запустится на любом компьютере
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'Image')
SCORE_FILE = os.path.join(BASE_DIR, 'highscore.txt')

FLOOR_Y = 560          # уровень пола (низ динозавра и кактусов)
START_SPEED = 5
MAX_SPEED = 12
SPEED_UP_EVERY = 5     # каждые 5 очков игра ускоряется

GRAVITY = 0.8
JUMP_FORCE = -17

CACTUS_EVENT = 25      # pygame.USEREVENT + 1