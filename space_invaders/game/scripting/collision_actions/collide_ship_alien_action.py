#import constants
from constants import *

#import necessary classes
from game.casting.sound import Sound #import sound class for collision sound
from game.scripting.action import Action #import action class as parent class


class CollideShipAlien(Action):
    '''checks for and resolves collisions between ship and an alien.
        
        Arguments:
            physics service: an instance of physics_service
            audio service: an instance of audio_service
    '''
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service #assigns _physics_service attribute from args
        self._audio_service = audio_service #assigns _audio_service attribute from args
        
    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        aliens = cast.get_all_actors(ALIEN_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        over_sound = Sound(OVER_SOUND) #assigns variable to game over sound
        
        for alien in aliens:
            alien_body = alien.get_body()
            ship_body = ship.get_body()

            if self._physics_service.has_collided(ship_body, alien_body):
                #if the body of the ship has collided with the body of an alien the player loses a life
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
