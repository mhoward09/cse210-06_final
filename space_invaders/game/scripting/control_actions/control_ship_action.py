from constants import *

from game.casting.point import Point
from game.casting.body import Body
from game.casting.image import Image
from game.casting.actors.bullet import Bullet
from game.scripting.action import Action


class ControlShipAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        ship_body = ship.get_body()

        if self._keyboard_service.is_key_down(ENTER): 
            position = ship_body.get_position()
            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
            velocity = Point(0, 1)
            body = Body(position, size, velocity)
            image = Image(BULLET_IMAGE)
            bullet = Bullet(body, image, True)
            cast.add_actor(SHIP_BULLET_GROUP, bullet)

        if self._keyboard_service.is_key_down(LEFT): 
            ship.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            ship.move_right()  
        else: 
            ship.stop_moving()        
