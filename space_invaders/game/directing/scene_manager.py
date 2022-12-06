#import required libraries
import csv #import the file reading library csv
from constants import * #import all constants
#import required classes
from game.casting.animation import Animation #import Animation class
from game.casting.ball import Ball #import Ball class - convert to bullet
from game.casting.body import Body #import Body class - used for physics, probably not necessary for the basic game, but we can keep it for now just in case
from game.casting.brick import Brick #imports the Brick class - convert to the alien class
from game.casting.image import Image #imports the Image class - used for creating images of the game objects and allowing minor image adjustments
from game.casting.label import Label #imports the Label class - used to create labels for the HUD
from game.casting.point import Point #imports the Point class - used to indicate the location of game objects on a cartesian plane (a graphical interpetation of a 2D space)
from game.casting.racket import Racket #imports the Racket class - convert to ship
from game.casting.stats import Stats #imports the Stats class - manages player lives
from game.casting.text import Text #imports the Text class - manages the text displaying in the HUD and on screen
from game.scripting.scene_actions.change_scene_action import ChangeSceneAction #imports the ChangeSceneAction class - changes the screen when ENTER is pressed
from game.scripting.scene_actions.check_over_action import CheckOverAction #imports the CheckOverAction - checks the cast list of aliens, if it is empty it signals to move to the next level
from game.scripting.collision_actions.collide_borders_action import CollideBordersAction #imports the CollideBordersAction which detects if the ball touches an edge of the screen and if it does what happens (a bounce or a loss) - we won't have bouncing but we will need to detect collision with the bottom to detect a loss and the starting point for the aliens will need to be under the HUD area
from game.scripting.collision_actions.collide_brick_action import CollideBrickAction #imports the CollideBrickAction class which detects if the ball hits a brick causing the ball to bounce the brick to be removed and the points to be added to the score - we will not need the bounce but score will need to be added and alien/brick removed upon the collision of a bullet with an alien
from game.scripting.collision_actions.collide_racket_action import CollideRacketAction #imports the CollideRacketAction which handles the ball hitting the racket and bouncing - this will be adjusted to a bullet hitting the ship and triggering a loss
from game.scripting.control_actions.control_racket_action import ControlRacketAction #this imports the ControlRacketAction class which manages the key input to control the racket for play - this will need to be converted to the control ship action which will move the ship left and right and fire bullets
from game.scripting.drawing_actions.draw_ball_action import DrawBallAction #imports the DrawBallAction class that include the code to display the ball on the screen - will need to be converted to bullet
from game.scripting.drawing_actions.draw_bricks_action import DrawBricksAction #imports the DrawBricksAction class that is the code to display the bricks - will need to be converted to aliens
from game.scripting.drawing_actions.draw_dialog_action import DrawDialogAction #imports the DrawDialog action class which is responsible for displaying the messages in the middle of the screen (count down to level start)
from game.scripting.drawing_actions.draw_hud_action import DrawHudAction #imports the DrawHusActions class responsible for displaying the HUD at the top of the screen
from game.scripting.drawing_actions.draw_racket_action import DrawRacketAction #imports the DrawRacketAction class responsible for displaying the racket to the screen - will need to be converted to the ship
from game.scripting.drawing_actions.end_drawing_action import EndDrawingAction #imports the EndDrawingAction class responsible for clearing the screen in preparation for the next screen
from game.scripting.game_start_actions.initialize_devices_action import InitializeDevicesAction #imports the InitializeDevicesAction responsible for starting the video and sound services for game play
from game.scripting.game_start_actions.load_assets_action import LoadAssetsAction #imports the LoadAssetsAction responsible for loading the level data, images and sounds for game play
from game.scripting.movement_actions.move_ball_action import MoveBallAction #imports MoveBallAction responsible for the movement of the ball from frame to frame - to be converted to bullet
from game.scripting.movement_actions.move_racket_action import MoveRacketAction #imports MoveRacketAction responsible for movement of racket from frame to frame - to be converted to ship
from game.scripting.sound_actions.play_sound_action import PlaySoundAction #imports PlaySoundAction responsible for playing a given sound when called
from game.scripting.game_end_actions.release_devices_action import ReleaseDevicesAction #imports ReleaseDevicesAcion responsible for ending the video and sound services when game is closed
from game.scripting.drawing_actions.start_drawing_action import StartDrawingAction #imports StartDrawingAction responsible for starting the display of game items
from game.scripting.scene_actions.timed_change_scene_action import TimedChangeSceneAction #imports TimedChangeSceneAction responsible for changing the scene based on a time delay (for the count down to the start of the level)
from game.scripting.game_end_actions.unload_assets_action import UnloadAssetsAction #import UnloadAssestsAction responsible for releasing the memory buffer holding the loaded assets when the game screen is closed
from game.services.raylib.raylib_audio_service import RaylibAudioService #imports the audio service class used to produce sounds for game play
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService #imports the keyboard service class used to convert keyboard input into game actions
from game.services.raylib.raylib_physics_service import RaylibPhysicsService #imports the physics service to manage the physics and bouncing of the ball - unnecessary for invaders game
from game.services.raylib.raylib_video_service import RaylibVideoService #imports the video service to open the and manage the game screen and displays

#scene manager class
class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""

    #these are attribute references - similar to global constants but only for this class

    #service references
    AUDIO_SERVICE = RaylibAudioService() #assigns the attribute reference for the audio service class
    KEYBOARD_SERVICE = RaylibKeyboardService() #assigns the attribute reference for the keyboard service class
    PHYSICS_SERVICE = RaylibPhysicsService() #assign the attribute reference for the physics service - unnecessary for invaders game
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT) #assings the attribute reference for the video service

    #action references

    #scene references
    CHECK_OVER_ACTION = CheckOverAction()

    #collision references
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_BRICKS_ACTION = CollideBrickAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_RACKET_ACTION = CollideRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE)

    #game control references
    CONTROL_RACKET_ACTION = ControlRacketAction(KEYBOARD_SERVICE)

    #drawing/display references
    DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    DRAW_BRICKS_ACTION = DrawBricksAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_RACKET_ACTION= DrawRacketAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)

    #game start up references
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    #movement references
    MOVE_BALL_ACTION = MoveBallAction()
    MOVE_RACKET_ACTION = MoveRacketAction()

    #game closing refernces
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass #all attributes were referenced above and thus will not be in the init statement and will not require the "self." to be called

    def prepare_scene(self, scene, cast, script):
        """function to determine what scene to prepare next"""
        #each scene was assigned a number in the constants file for easy boolean comparison
        if scene == NEW_GAME: 
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL: 
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_ball(cast)
        self._add_bricks(cast)
        self._add_racket(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_ball(cast)
        self._add_bricks(cast)
        self._add_racket(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_ball(cast)
        self._add_racket(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_ball(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_RACKET_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_ball(cast)
        self._add_racket(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        ball.release()

    def _add_ball(self, cast):
        cast.clear_actors(BALL_GROUP)
        x = CENTER_X - BALL_WIDTH / 2
        y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)

    def _add_bricks(self, cast):
        cast.clear_actors(BRICK_GROUP)
        
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):

                    x = FIELD_LEFT + c * BRICK_WIDTH
                    y = FIELD_TOP + r * BRICK_HEIGHT
                    color = column[0]
                    frames = int(column[1])
                    points = BRICK_POINTS 
                    
                    if frames == 1:
                        points *= 2
                    
                    position = Point(x, y)
                    size = Point(BRICK_WIDTH, BRICK_HEIGHT)
                    velocity = Point(0, 0)
                    images = BRICK_IMAGES[color][0:frames]

                    body = Body(position, size, velocity)
                    animation = Animation(images, BRICK_RATE, BRICK_DELAY)

                    brick = Brick(body, animation, points)
                    cast.add_actor(BRICK_GROUP, brick)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_racket(self, cast):
        cast.clear_actors(RACKET_GROUP)
        x = CENTER_X - RACKET_WIDTH / 2
        y = SCREEN_HEIGHT - RACKET_HEIGHT
        position = Point(x, y)
        size = Point(RACKET_WIDTH, RACKET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(RACKET_IMAGES, RACKET_RATE)
        racket = Racket(body, animation)
        cast.add_actor(RACKET_GROUP, racket)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        script.add_action(OUTPUT, self.DRAW_BRICKS_ACTION)
        script.add_action(OUTPUT, self.DRAW_RACKET_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BRICKS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_RACKET_ACTION)
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)