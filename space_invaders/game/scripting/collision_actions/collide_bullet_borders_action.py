#import constants
from constants import *

#import necessary classes
from space_invaders.game.casting.sound import Sound #we probably won't need a sound 
from space_invaders.game.scripting.action import Action #import Action class as parent class


class CollideBulletBordersAction(Action):
    """Detects and resolves collisions with the borders of the playing field.
    
    Args:
        physics_service: an instance of the physics service
        audio_service: an instance of the audio service
    """

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ship_bullets = cast.get_actors(SHIP_BULLET_GROUP)
        alien_bullets = cast.get_actors(ALIEN_BULLET_GROUP)
            
        for bullet in ship_bullets:
            body = bullet.get_body()
            position = body.get_position()
            x = position.get_x()
            y = position.get_y()
                    
            #if x < FIELD_LEFT:
                #cast.remove_actor(SHIP_BULLET_GROUP, bullet)

            #elif x >= (FIELD_RIGHT - BALL_WIDTH):
                #cast.remove_actor(SHIP_BULLET_GROUP, bullet)

            if y < FIELD_TOP:
                cast.remove_actor(SHIP_BULLET_GROUP, bullet)

            else:
                pass

            #for bullet in alien_bullets:
                #body = bullet.get_body()
                #position = body.get_position()
                #x = position.get_x()
                #y = position.get_y()

                #if y >= (FIELD_BOTTOM):
                    #cast.remove_actor#(ALIEN_BULLET_GROUP, bullet)

                #else:
                    #pass