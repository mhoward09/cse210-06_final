#import constants
from constants import *

#import necessary classes
from space_invaders.game.casting.sound import Sound #import sound class for playing game sounds
from space_invaders.game.scripting.action import Action #import action class as parent class


class CollideSbulletSbulletAction(Action):
    '''checks for and resolves collisions between ship bullets and ship bullets to prevent over lap of bullet collisions.
        
        Arguments:
            physics service: an instance of physics_service
            audio service: an instance of audio_service
    '''
    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service #assigns _physics_service attribute from args
        self._audio_service = audio_service #assigns _audio_service attribute from args
        
    def execute(self, cast, script, callback):
        bullets = cast.get_actors(SHIP_BULLET_GROUP)
        if len(bullets) > 1:
            for i in range(len(bullets)):
                for j in range(i+1,len(bullets)):

                    bullet_1 = bullets[i]
                    bullet_2 = bullets[j]
                    bullet_body_1 = bullet_1.get_body()
                    bullet_body_2 = bullet_2.get_body()

                    if self._physics_service.has_collided(bullet_body_1, bullet_body_2):
                        cast.remove_actor(SHIP_BULLET_GROUP, bullet_2)