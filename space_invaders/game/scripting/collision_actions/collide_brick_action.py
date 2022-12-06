from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideAlienAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        alien = cast.get_actors(ALIEN_GROUP)
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
