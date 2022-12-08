#import constants
from constants import *

#import necessary classes
from game.casting.sound import Sound #import sound class for playing game sounds
from game.scripting.action import Action #import action class as parent class


class CollideAlienAction(Action):
    '''checks for and resolves collisions between ship bullets and an alien
        
        Arguments:
            physics service: an instance of physics_service
            audio service: an instance of audio_service
    '''
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service #assigns _physics_service attribute from args
        self._audio_service = audio_service #assigns _audio_service attribute from args
        
    def execute(self, cast, script, callback):
        bullets = cast.get_all_actors(SHIP_BULLET_GROUP)
        aliens = cast.get_all_actors(ALIEN_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for alien in aliens:
            for bullet in bullets:
                bullet_body = bullet.get_body()
                alien_body = alien.get_body()

                if self._physics_service.has_collided(bullet_body, alien_body):
                    cast.remove_actor(SHIP_BULLET_GROUP, bullet)
                    points = alien.get_points()
                    stats.add_points(points)
                    cast.remove_actor(ALIEN_GROUP, alien)
