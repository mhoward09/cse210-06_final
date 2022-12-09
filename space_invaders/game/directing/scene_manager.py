#import required libraries
import csv #import the file reading library csv
from constants import * #import all constants
#import required classes
from space_invaders.game.casting.animation import Animation #import Animation class
from space_invaders.game.casting.actors.bullet import Bullet #import Ball class - convert to bullet
from space_invaders.game.casting.body import Body #import Body class - used for physics, probably not necessary for the basic game, but we can keep it for now just in case
from space_invaders.game.casting.actors.alien import Alien #imports the Brick class - convert to the alien class
from space_invaders.game.casting.image import Image #imports the Image class - used for creating images of the game objects and allowing minor image adjustments
from space_invaders.game.casting.actors.label import Label #imports the Label class - used to create labels for the HUD
from space_invaders.game.casting.point import Point #imports the Point class - used to indicate the location of game objects on a cartesian plane (a graphical interpetation of a 2D space)
from space_invaders.game.casting.actors.ship import Ship #imports the Racket class - convert to ship
from space_invaders.game.casting.actors.stats import Stats #imports the Stats class - manages player lives
from space_invaders.game.casting.text import Text #imports the Text class - manages the text displaying in the HUD and on screen
from space_invaders.game.scripting.scene_actions.change_scene_action import ChangeSceneAction #imports the ChangeSceneAction class - changes the screen when ENTER is pressed
from space_invaders.game.scripting.scene_actions.check_over_action import CheckOverAction #imports the CheckOverAction - checks the cast list of aliens, if it is empty it signals to move to the next level
from space_invaders.game.scripting.collision_actions.collide_bullet_borders_action import CollideBulletBordersAction #imports the CollideBordersAction which detects if the ball touches an edge of the screen and if it does what happens (a bounce or a loss) - we won't have bouncing but we will need to detect collision with the bottom to detect a loss and the starting point for the aliens will need to be under the HUD area
from space_invaders.game.scripting.collision_actions.collide_alien_action import CollideAlienAction #imports the CollideBrickAction class which detects if the ball hits a brick causing the ball to bounce the brick to be removed and the points to be added to the score - we will not need the bounce but score will need to be added and alien/brick removed upon the collision of a bullet with an alien
from space_invaders.game.scripting.collision_actions.collide_ship_alien_action import CollideShipAlienAction
from space_invaders.game.scripting.collision_actions.collide_ship_action import CollideShipAction #imports the CollideRacketAction which handles the ball hitting the racket and bouncing - this will be adjusted to a bullet hitting the ship and triggering a loss
from space_invaders.game.scripting.control_actions.control_ship_action import ControlShipAction #this imports the ControlRacketAction class which manages the key input to control the racket for play - this will need to be converted to the control ship action which will move the ship left and right and fire bullets

#FROM GREG
from space_invaders.game.scripting.control_actions.alien_fire_action import AlienBulletAction #controls the firing of alien bullets not sure if
#this belongs in the control_actions folder or movement_actions folder

from space_invaders.game.scripting.drawing_actions.draw_bullet_action import DrawBulletAction #imports the DrawBallAction class that include the code to display the ball on the screen - will need to be converted to bullet
from space_invaders.game.scripting.drawing_actions.draw_aliens_action import DrawAliensAction #imports the DrawBricksAction class that is the code to display the bricks - will need to be converted to aliens
from space_invaders.game.scripting.drawing_actions.draw_dialog_action import DrawDialogAction #imports the DrawDialog action class which is responsible for displaying the messages in the middle of the screen (count down to level start)
from space_invaders.game.scripting.drawing_actions.draw_hud_action import DrawHudAction #imports the DrawHusActions class responsible for displaying the HUD at the top of the screen
from space_invaders.game.scripting.drawing_actions.draw_ship_action import DrawShipAction #imports the DrawRacketAction class responsible for displaying the racket to the screen - will need to be converted to the ship
from space_invaders.game.scripting.drawing_actions.end_drawing_action import EndDrawingAction #imports the EndDrawingAction class responsible for clearing the screen in preparation for the next screen
from space_invaders.game.scripting.game_start_actions.initialize_devices_action import InitializeDevicesAction #imports the InitializeDevicesAction responsible for starting the video and sound services for game play
from space_invaders.game.scripting.game_start_actions.load_assets_action import LoadAssetsAction #imports the LoadAssetsAction responsible for loading the level data, images and sounds for game play
from space_invaders.game.scripting.movement_actions.move_bullet_action import MoveBulletAction #imports MoveBallAction responsible for the movement of the ball from frame to frame - to be converted to bullet

#FROM GREG
from space_invaders.game.scripting.movement_actions.move_alien_action import MoveAlienAction #imports MoveBallAction responsible for the movement of the ball from frame to frame - to be converted to aliens


from space_invaders.game.scripting.movement_actions.move_ship_action import MoveShipAction #imports MoveRacketAction responsible for movement of racket from frame to frame - to be converted to ship
from space_invaders.game.scripting.sound_actions.play_sound_action import PlaySoundAction #imports PlaySoundAction responsible for playing a given sound when called
from space_invaders.game.scripting.game_end_actions.release_devices_action import ReleaseDevicesAction #imports ReleaseDevicesAcion responsible for ending the video and sound services when game is closed
from space_invaders.game.scripting.drawing_actions.start_drawing_action import StartDrawingAction #imports StartDrawingAction responsible for starting the display of game items
from space_invaders.game.scripting.scene_actions.timed_change_scene_action import TimedChangeSceneAction #imports TimedChangeSceneAction responsible for changing the scene based on a time delay (for the count down to the start of the level)
from space_invaders.game.scripting.game_end_actions.unload_assets_action import UnloadAssetsAction #import UnloadAssestsAction responsible for releasing the memory buffer holding the loaded assets when the game screen is closed
from space_invaders.game.services.audio.raylib_audio_service import RaylibAudioService #imports the audio service class used to produce sounds for game play
from space_invaders.game.services.keyboard.raylib_keyboard_service import RaylibKeyboardService #imports the keyboard service class used to convert keyboard input into game actions
from space_invaders.game.services.physics.raylib_physics_service import RaylibPhysicsService #imports the physics service to manage the physics and bouncing of the ball - unnecessary for invaders game
from space_invaders.game.services.video.raylib_video_service import RaylibVideoService #imports the video service to open the and manage the game screen and displays

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
    COLLIDE_BULLET_BORDERS_ACTION = CollideBulletBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_ALIEN_ACTION = CollideAlienAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_SHIP_ACTION = CollideShipAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_SHIP_ALIEN_ACTION = CollideShipAlienAction(PHYSICS_SERVICE, AUDIO_SERVICE)

    #game control references
    CONTROL_SHIP_ACTION = ControlShipAction(KEYBOARD_SERVICE)

    #drawing/display references
    DRAW_BULLET_ACTION = DrawBulletAction(VIDEO_SERVICE)
    DRAW_ALIEN_ACTION = DrawAliensAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_SHIP_ACTION= DrawShipAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)

    #game start up references
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    #movement references
    MOVE_BULLET_ACTION = MoveBulletAction()
    MOVE_SHIP_ACTION = MoveShipAction()

    #FROM GREG
    MOVE_ALIEN_ACTION = MoveAlienAction()
    ALIEN_BULLET_ACTION = AlienBulletAction()

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
        self._add_aliens(cast)
        self._add_ship(cast)
        self._add_dialog(cast, SPACE_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_aliens(cast)
        self._add_ship(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_aliens(cast)
        self._add_ship(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_SHIP_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_ship(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    #from GREG 
    #Starts the alien moving
    def _activate_bricks(self, cast):
        aliens = cast.get_actors(ALIEN_GROUP)
        for alien in aliens:
            alien.release()

    def _add_aliens(self, cast):
        cast.clear_actors(ALIEN_GROUP)
        
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        filename = LEVEL_FILE.format(level)

        with open(filename, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)

            for r, row in enumerate(reader):
                for c, column in enumerate(row):
                
                    x = FIELD_LEFT + c * ALIEN_WIDTH
                    y = FIELD_TOP + r * ALIEN_HEIGHT
                    alien_type = column[0]
                    frames = int(column[1])
                    hitPoints = ALIEN_HITPOINTS
                    points = ALIEN_POINTS 
                    
                    if frames == 2:
                        hitPoints *= 2
                        points *= 2
                    elif frames == 5:
                        hitPoints *= 5
                        points *= 5
                    
                    position = Point(x, y)
                    size = Point(ALIEN_WIDTH, ALIEN_HEIGHT)
                    velocity = Point(0, 0)
                    image_file = ALIEN_IMAGES[alien_type]
                    body = Body(position, size, velocity)
                    image = Image(image_file, .5)

                    alien = Alien(body, image, hitPoints, points)
                    cast.add_actor(ALIEN_GROUP, alien)

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

    def _add_ship(self, cast):
        cast.clear_actors(SHIP_GROUP)
        x = CENTER_X - SHIP_WIDTH / 2
        y = SCREEN_HEIGHT - SHIP_HEIGHT
        position = Point(x, y)
        size = Point(SHIP_WIDTH, SHIP_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(SHIP_IMAGES)
        ship = Ship(body, image)
        cast.add_actor(SHIP_GROUP, ship)

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
        script.add_action(OUTPUT, self.DRAW_BULLET_ACTION)
        script.add_action(OUTPUT, self.DRAW_ALIEN_ACTION)
        script.add_action(OUTPUT, self.DRAW_SHIP_ACTION)
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
        script.add_action(UPDATE, self.MOVE_BULLET_ACTION)
        script.add_action(UPDATE, self.MOVE_SHIP_ACTION)

        #FROM GREG adding the alien bullet action to the script
        script.add_action(UPDATE, self.ALIEN_BULLET_ACTION)
        
        script.add_action(UPDATE, self.COLLIDE_BULLET_BORDERS_ACTION)
        #script.add_action(UPDATE, self.COLLIDE_ALIEN_ACTION)
        #script.add_action(UPDATE, self.COLLIDE_SHIP_ACTION)
        #script.add_action(UPDATE, self.COLLIDE_SHIP_ALIEN_ACTION)
        script.add_action(UPDATE, self.MOVE_SHIP_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
        
