import asyncio
from constants import *

from space_invaders.game.casting.point import Point
from space_invaders.game.casting.body import Body
from space_invaders.game.casting.image import Image
from space_invaders.game.casting.actors.bullet import Bullet
#from space_invaders.game.scripting.control_actions.ship_fire_action import ShipFireAction
from space_invaders.game.scripting.action import Action
from space_invaders.game.scripting.sound_actions.play_sound_action import PlaySoundAction


class ControlShipAction(Action):

    def __init__(self, keyboard_service, audio_service):
        self._keyboard_service = keyboard_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP)
        ship_body = ship.get_body()

        if self._keyboard_service.is_key_pressed(SPACE): 
            if len(cast.get_actors(SHIP_BULLET_GROUP)) < BULLET_MAX:
                ship_position = ship_body.get_position()
                x = ship_position.get_x()
                y = ship_position.get_y()
                position = Point(x + SHIP_WIDTH/2.45, y + SHIP_HEIGHT/11)
                size = Point(BULLET_WIDTH, BULLET_HEIGHT)
                velocity = Point(0, -BULLET_VELOCITY)
                body = Body(position, size, velocity)
                image = Image(SHIP_BULLET_IMAGE, .5)
                bullet = Bullet(body, image)
                cast.add_actor(SHIP_BULLET_GROUP, bullet)

                script.add_action(OUTPUT, PlaySoundAction(self._audio_service, SHIP_BULLET_SOUND))
                

        if self._keyboard_service.is_key_down(LEFT): 
            ship.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            ship.move_right()  
        else: 
            ship.stop_moving()        
