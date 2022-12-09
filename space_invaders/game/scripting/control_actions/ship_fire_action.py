from constants import *

from space_invaders.game.scripting.action import Action
from space_invaders.game.casting.point import Point
from space_invaders.game.casting.body import Body
from space_invaders.game.casting.image import Image
from space_invaders.game.casting.actors.bullet import Bullet
from space_invaders.game.casting.actors.ship import Ship
from space_invaders.game.casting.actors.alien import Alien
from space_invaders.game.casting.sound import Sound

class FireBulletAction(Action):
    """creates a bullet from an origin (ship or alien) object.
    
    Arguments:
        origin: an instance of a ship or an alien with a position
        sound: an instance of a sound
    """

    def __init__(self, origin):
        super().__init__()
        self._origin = origin 
        #self._sound = sound

    def execute(self, cast, script, callback):

        if isinstance(self._origin, Ship):
            origin_body = self._origin.get_body()
            position = origin_body.get_position()
            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
            velocity = Point(0, 1)
            body = Body(position, size, velocity)
            image = Image(SHIP_BULLET_IMAGE)
            bullet = Bullet(body, image, True)
            cast.add_actor(SHIP_BULLET_GROUP, bullet)
            print("bullet fired")
        else:
            origin_body = self._origin.get_body()
            position = origin_body.get_position()
            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
            velocity = Point(0, -1)
            body = Body(position, size, velocity)
            image = Image(ALIEN_BULLET_IMAGE)
            bullet = Bullet(body, image, True)
            cast.add_actor(ALIEN_BULLET_GROUP, bullet)