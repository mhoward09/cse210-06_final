from constants import *

from space_invaders.game.casting.point import Point
from space_invaders.game.casting.body import Body
from space_invaders.game.casting.image import Image
from space_invaders.game.casting.actors.bullet import Bullet
#from space_invaders.game.scripting.control_actions.ship_fire_action import ShipFireAction
from space_invaders.game.scripting.action import Action


class ControlShipAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        ship_body = ship.get_body()

        if self._keyboard_service.is_key_pressed(SPACE): 
            ship_position = ship_body.get_position()
            x = ship_position.get_x()
            y = ship_position.get_y()
            position = Point(x + SHIP_WIDTH/2, y + SHIP_HEIGHT/2)
            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
            velocity = Point(0, -1)
            body = Body(position, size, velocity)
            image = Image(SHIP_BULLET_IMAGE)
            bullet = Bullet(body, image)
            cast.add_actor(SHIP_BULLET_GROUP, bullet)

        if self._keyboard_service.is_key_down(LEFT): 
            ship.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            ship.move_right()  
        else: 
            ship.stop_moving()        
