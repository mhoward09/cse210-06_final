from constants import *
from space_invaders.game.scripting.action import Action


class MoveBulletAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ship_bullets = cast.get_actors(SHIP_BULLET_GROUP)
        alien_bullets = cast.get_actors(ALIEN_BULLET_GROUP)

        if len(ship_bullets) != 0:

            for bullet in ship_bullets:
                body = bullet.get_body()
                position = body.get_position()
                velocity = body.get_velocity()
                position = position.add(velocity)
                body.set_position(position)

        else:
            pass

        if len(alien_bullets) != 0:

            for bullet in alien_bullets:
                body = bullet.get_body()
                position = body.get_position()
                velocity = body.get_velocity()
                position = position.add(velocity)
                body.set_position(position)

        else:
            pass