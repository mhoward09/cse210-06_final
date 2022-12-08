from constants import *

from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
from game.casting.actors.bullet import Bullet
from game.scripting.action import Action

class FireBulletAction(Action):

    def __init__(self, origin):
            super().__init__()



position = ship_body.get_position()
            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
            velocity = Point(0, 1)
            body = Body(position, size, velocity)
            image = Image(BULLET_IMAGE)
            bullet = Bullet(body, image, True)
            cast.add_actor(SHIP_BULLET_GROUP, bullet)