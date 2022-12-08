#import constants
from constants import *

#import necessary classes
from game.casting.actors.actor import Actor #imports Actor class for use as parent class
from game.casting.point import Point #imports Point class for use in positioning and movement of the bullets


class Bullet(Actor):
    """A solid projectile shot from the ship or an alien."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bullet.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug) #inherits the init of Actor class
        self._body = body #assigns the body arg and attribute - the solid part of the bullet for detecting collisions -- hit box
        self._image = image #assigns the image arg and attribute - the image object made from the file of the picture to represent the bullet

    def get_body(self):
        """Gets the bullet's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the bullet's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        