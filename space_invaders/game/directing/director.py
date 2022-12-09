#import needed constants and classes
from constants import * #imports all constants
from space_invaders.game.casting.cast import Cast #imports Cast class
from space_invaders.game.directing.scene_manager import SceneManager #impports SceneManager class
from space_invaders.game.directing.action_callback import ActionCallback #imports ActionCallback class
from space_invaders.game.scripting.script import Script #imports Script class

#Director class
class Director(ActionCallback):
    """A person who directs the game."""

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service #gives the parameter video_service an attribute variable to manage the game window
        self._cast = Cast() #defines the _cast attribute as an instance of the Cast class to manage all actors/game objects
        self._script = Script() #defines the _script attribute as an instance of the Script class to manage all the movements of the actors/game objects
        self._scene_manager = SceneManager() #define the _scene_manager attribute as an instance of the SceneManager class to manage all the visuals in a given screen/level/scene
        self._counter = 0
        
    def on_next(self, scene):
        """Overridden ActionCallback method transitions to next scene.
        
        Args:
            A number representing the next scene to transition to.
        """
        self._scene_manager.prepare_scene(scene, self._cast, self._script) #calls the SceneManager class method prepare_scene which runs through logic to decide what screen/scene to display in the game window

    def start_game(self):
        """Starts the game. Runs the main game loop."""
        self.on_next(NEW_GAME) #calls the director on_next method from above given the parameter for the new game screen to be displayed
        self._execute_actions(INITIALIZE) #calls the _execute_actions method from below given the parameter Initialize to call the group of script actions to initialize or begin the raylib audio and video services of the game -- it opens the window and prepares the sounds of the game played through the raylib library
        self._execute_actions(LOAD)
        while self._video_service.is_window_open():

            #I need a counter to time alien movements/actions
            if self._counter % 480 == 0:
                self._counter = 0
            self._counter += 1
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)
        self._execute_actions(UNLOAD)
        self._execute_actions(RELEASE)
        
    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script, self)          