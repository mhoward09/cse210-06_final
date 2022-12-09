from constants import *
from space_invaders.game.casting.point import Point
from space_invaders.game.scripting.action import Action


class MoveAlienAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
            aliens = cast.get_actors(ALIEN_GROUP)
            for alien in aliens:
                body = alien.get_body()
                position = body.get_position()
                velocity = body.get_velocity()
                position = position.add(velocity)
                body.set_position(position)
