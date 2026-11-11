import os

WIDTH, HEIGHT = 900, 600    
FPS = 60

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'Image')
SCORE_FILE = os.path.join(BASE_DIR, 'highscore.txt')

FLOOR_Y = 560          
START_SPEED = 5
MAX_SPEED = 12
SPEED_UP_EVERY = 5     
GRAVITY = 0.8
JUMP_FORCE = -17

CACTUS_EVENT = 25      