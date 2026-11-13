import os


WIDTH = 900
HEIGHT = 600
FPS = 60
TITLE = 'Dino-Reverse'


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'Image')
SAVE_FILE = os.path.join(BASE_DIR, 'save.json')

#S
STATE_MENU = 'menu'
STATE_PLAYING = 'playing'
STATE_GAME_OVER = 'game_over'


FLOOR_Y = 560           
GROUND_IMAGE_Y = 479     
GROUND_HEIGHT = 142


DINO_SIZE = (120, 120)
DINO_X = 800
GRAVITY = 0.8
JUMP_FORCE = -17
HITBOX_SHRINK = (-40, -30)   


CACTUS_HEIGHTS = (60, 80, 100)
CACTUS_RATIO = 0.75          
MIN_SPAWN_DELAY = 90         
MAX_SPAWN_DELAY = 220


START_SPEED = 5
MAX_SPEED = 12
SPEED_UP_EVERY = 5           

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
FONT_BIG = 40
FONT_SMALL = 28