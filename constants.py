'''constants regarding game play'''
#import some sort of file path converting library
from space_invaders.game.casting.color import Color #import the Color class from the color file which creates a color object to be used when drawing/displaying the game objects in the video service

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Invaders" #the name of the game for reference and display purposes
FRAME_RATE = 60 #the rate of screen refresh: how fast the game will go based on how often the screen is redrawn to show the movement/animation of the objects. This will determine how smooth the animation is and how responsive the game controls are

# SCREEN - the game window
SCREEN_WIDTH = 1040 #the decided width of the game window in pixels
SCREEN_HEIGHT = 680 #the chosen height of the game window in pixels
CENTER_X = SCREEN_WIDTH / 2 #the graphical half way point in the width, the x component of the center point of the game window
CENTER_Y = SCREEN_HEIGHT / 2 #the graphical half way point in the height, the y component of the center point of the game window

# FIELD - determines the field of play where the ball is able to move, we need this for the bounds of the ship and the aliens rather than the ball/bullet class
FIELD_TOP = 60 #the top of the ball's play area - 60 pixels from the top of the screen to allow for the HUD
FIELD_BOTTOM = SCREEN_HEIGHT #the bottom of the play area - the bottom of the screen - point (0,0) is the upper left corner of the screen
FIELD_LEFT = 0 #the left side of the play screen
FIELD_RIGHT = SCREEN_WIDTH #the right side of the play screen

# FONT - the font used for the game
FONT_FILE = "space_invaders/assets/fonts/SpaceMission-rgyw9.otf" #file that contains the font for the printed items on the screen
FONT_SMALL = 32 #size of small font
FONT_LARGE = 48 #size of large font

# SOUND - game play sounds
BULLET_SOUND = "space_invaders/assets/sounds/pewpew.wav" #sound of a bouncing ball - to be replaced with sound of bullet being fired
WELCOME_SOUND = "space_invaders/assets/sounds/start.wav" #sound of the opening screen - replace with sound of choice
OVER_SOUND = "space_invaders/assets/sounds/over.wav" #sound of game over - replace with sound of choice
#ALIEN_SOUND - will be the sound made when the aliens are destroyed

# TEXT 
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS - basic colors used in the game
BLACK = Color(0, 0, 0) 
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS - the keys used during game play assigned to variable for easy use. 
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES - numbers assigned to the different screens in game play for easy use as a parameter in the director class method
NEW_GAME = 0 #the screen for a new game
TRY_AGAIN = 1 #the screen asking the player if they want to try again
NEXT_LEVEL = 2 #the screen for the next level of play
IN_PLAY = 3 
GAME_OVER = 4 #the screen for when the game ends

# LEVELS - the file directory to the level data
LEVEL_FILE = "space_invaders/assets/level_data/level-001.txt" #the file directory for the level foundation text
BASE_LEVELS = 3 

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES - the different game phases of play
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS - player stats
STATS_GROUP = "stats" #the group that the stats are held in in the cast class
DEFAULT_LIVES = 3 #starting lives
MAXIMUM_LIVES = 5 #the max number of live the player can have

# HUD - the heads up display to display the stats of the player screen/scene
HUD_MARGIN = 15 #the space around the HUD to differentiate it from the rest o9f the screen and prevent overlap
LEVEL_GROUP = "level" #the cast group for the level being played
LIVES_GROUP = "lives" #the cast group for the lives of the player
SCORE_GROUP = "score" #the cast group for the player's score
LEVEL_FORMAT = "LEVEL: {}" #the displaying of the level being played
LIVES_FORMAT = "LIVES: {}" #the displaying of the number of live the player has
SCORE_FORMAT = "SCORE: {}" #the displaying of the player's score

# BULLET - The constants for the bullet class 
SHIP_BULLET_GROUP = "bullets"
ALIEN_BULLET_GROUP = "alien_bullets" #the cast group for the bullet 
SHIP_BULLET_IMAGE = "space_invaders/assets/images/ship_bullet.png" #file for bullet image 
ALIEN_BULLET_IMAGE = "space_invaders/assets/images/alien_bullet.png" #file for bullet image 
BULLET_WIDTH = 28 #width of bullet image
BULLET_HEIGHT = 28 #height of bullet image
BULLET_VELOCITY = 1 #speed of the bullet in frames -- bullets only move up or down based on who fired them (positive or negative y dimension) 

# SHIP - the constants for the ship class
SHIP_GROUP = "ships" #the cast group for ships 
SHIP_IMAGES = "space_invaders/assets/images/Human-Fighter.png" #the file path for the racket image - convert to ship
SHIP_WIDTH = 106 #the width of the ship image 
SHIP_HEIGHT = 100 #the height of the ship image 
SHIP_RATE = 6 #the frame rate of ship animation
SHIP_VELOCITY = 7 #the speed the ship moves 

# ALIEN - the constants for the aliens class 
ALIEN_GROUP = "aliens" #the cast group for aliens 
ALIEN_IMAGES = {
    "a": "space_invaders/assets/images/alien1.png",
    "b": "space_invaders/assets/images/alien2.png",
    "m": "space_invaders/assets/images/alien5.png"
} #the alien images
ALIEN_WIDTH = 70 #the width of a alien image
ALIEN_HEIGHT = 32 #the height of a alien image
ALIEN_DELAY = 0.5 #the delay in animation of aliens
ALIEN_RATE = 4 #the frame rate of alien animation
ALIEN_POINTS = 50 #the number of points breaking a alien is worth - convert to aliens -- each alien image is worth different amounts of points
<<<<<<< Updated upstream
ALIEN_VELOCITY_Y = 12
ALIEN_VELOCITY_X = 6
=======
ALIEN_HITPOINTS = 1
>>>>>>> Stashed changes

# DIALOG - the messages printed on the the screen for the player to read and to give direction
DIALOG_GROUP = "dialogs"
SPACE_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"