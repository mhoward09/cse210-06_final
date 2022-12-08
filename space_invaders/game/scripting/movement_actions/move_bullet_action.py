from constants import *
from space_invaders.game.scripting.action import Action


class MoveBulletAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ship_bullets = cast.get_all_actors(SHIP_BULLET_GROUP)
        alien_bullets = cast.get_all_actors(ALIEN_BULLET_GROUP)

        all_bullets = ship_bullets.extend(alien_bullets)

        for bullet in all_bullets:
            body = bullet.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)