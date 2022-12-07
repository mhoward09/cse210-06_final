#import constants
from constants import *

#import necessary classes
from game.casting.sound import Sound #import sound class for playing game sounds
from game.scripting.action import Action #import action class as parent class


class CollideAlienAction(Action):
    '''checks for and resolves collisions between ship bullets or the ship and an alien
        
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
        
        for alien in bricks:
            ball_body = ball.get_body()
            alien_body = alien.get_body()

            if self._physics_service.has_collided(ball_body, alien_body):
                ball.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = alien.get_points()
                stats.add_points(points)
                cast.remove_actor(ALIEN_GROUP, alien)
