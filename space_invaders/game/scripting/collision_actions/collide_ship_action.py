#import constants
from constants import *

#import necessary classes
from game.casting.sound import Sound #import sound class for collision sound
from game.scripting.action import Action #import action class as parent class


class CollideShipAction(Action):
    """ Checks and resolves a collision between an alien bullet and the ship.

        arguments:
            physics_service: an instance of the physics service
            audio_service: an instance of the audio service
    """
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service #assign _physics_service atrribute from args
        self._audio_service = audio_service #assign _audio_service atrribute from args
        
    def execute(self, cast, script, callback):
        """Overwriting parent execute action. To check for collision with bullet from alien and resolve the collision.
        """
        bullets = cast.get_all_actors(ALIEN_BULLET_GROUP) #gets the list of all bullets in the ALIEN_BULLET_GROUP from the cast class and assigns it a variable
        ship = cast.get_first_actor(SHIP_GROUP) #gets the instance of ship in play and assigns it a variable
        
        bullet_body = bullet.get_body() #assigns a variable to the body of a bullet
        ship_body = ship.get_body() #assigns a variable to the body of the ship

        over_sound = Sound(OVER_SOUND) #assigns variable to game over sound

        for bullet in bullets:
            #for all the bullets in the alien bullet group check for collision
            if self._physics_service.has_collided(bullet_body, ship_body):
                #if the body of the ship has collided with the body of a bullet the player loses a life
                stats = cast.get_first_actor (STATS_GROUP) #assign the stats object a variable
                stats.lose_life() #call the stats lose life method
                #self._audio_service.play_sound(sound) - not implemented in this version   
                if stats.get_lives() > 0:
                    #if there is still a life available move to try_again scene
                    callback.on_next(TRY_AGAIN)
                else:
                    #if that was the las life move to game over screen and play game over sound
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(over_sound)