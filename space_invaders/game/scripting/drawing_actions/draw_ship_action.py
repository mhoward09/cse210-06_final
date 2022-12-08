#import constants
from constants import *

#import necessary classes
from space_invaders.game.scripting.action import Action #import action class as parent class


class DrawShipAction(Action):
    """Draws a ship in the buffer to display for game play

        Arguments:
            video_service: and instance of video service
    """
    def __init__(self, video_service):
        self._video_service = video_service #assign _video_service attribute from args
        
    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SHIP_GROUP) #assign ship actor to a variable
        body = ship.get_body() #assign ship's body to a variable

        if ship.is_debug(): 
            #if the ship is in debug mode draw the ship's rectangle instead of its image
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        #animation = ship.get_animation() -- animation not implemented - future update feature
        image = ship.get_image() #assign ship image to a variable
        position = body.get_position() #assign ship's body postion to a variable
        self._video_service.draw_image(image, position) #uses video_service method to draw the image of the ship at the position of the ship's body
