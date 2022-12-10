from constants import *
#import necessary classes
from space_invaders.game.casting.sound import Sound #we probably won't need a sound 
from space_invaders.game.scripting.action import Action #import Action class as parent class


class CollideAlienBorderAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        aliens = cast.get_actors(ALIEN_GROUP)
        for alien in aliens:
            body = alien.get_body()
            position = body.get_position()
            x = position.get_x()
            y = position.get_y()
            over_sound = Sound(OVER_SOUND)

            if x <= FIELD_LEFT:
                for alien in aliens:
                    alien.move_down()
            elif x >= (FIELD_RIGHT - ALIEN_WIDTH):
                for alien in aliens:
                    alien.move_down()

            if x <= FIELD_LEFT:
                for alien in aliens:
                    alien.reverse_x()
            elif x >= (FIELD_RIGHT - ALIEN_WIDTH):
                for alien in aliens:
                    alien.reverse_x()

            if y >= (FIELD_BOTTOM - ALIEN_WIDTH):
                stats = cast.get_first_actor(STATS_GROUP)
                stats.lose_life()
                
                if stats.get_lives() > 0:
                    callback.on_next(TRY_AGAIN) 
                else:
                    callback.on_next(GAME_OVER)
                    self._audio_service.play_sound(over_sound)