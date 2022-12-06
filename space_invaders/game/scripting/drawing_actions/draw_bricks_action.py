from constants import *
from game.scripting.action import Action


class DrawAliensAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        alien = cast.get_actors(ALIEN_GROUP)
        
        for alien in aliens:
            body = alien.get_body()

            if alien.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = alien.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
