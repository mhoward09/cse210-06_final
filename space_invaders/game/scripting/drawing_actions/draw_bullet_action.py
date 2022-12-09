from constants import *
from space_invaders.game.scripting.action import Action


class DrawBulletAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ship_bullets = cast.get_actors(SHIP_BULLET_GROUP)
        
        for bullet in ship_bullets:
            body = bullet.get_body()
            
            if bullet.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle,PURPLE)
                
            image = bullet.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)