#import constants
from constants import *

#import necessary classes
from game.casting.actors.actor import Actor #import Actor class to be parent class
from game.casting.point import Point #import Point class to use for positioning and movement of ship


class Ship(Actor):
    """The ship representing the player protecting against the invaders."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Ship.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug) #inherits the Actor init
        self._body = body #assings body arg to an attribute - the solid part of the ship for detecting collisions
        self._animation = animation #assigns animation arg to an attribute - the animation of the ship

    def get_animation(self):
        """Gets the ship's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the ship's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the ship using its velocity."""
        position = self._body.get_position() #defines the ship's position for method use
        velocity = self._body.get_velocity() #defines the ship's velocity for method use
        new_position = position.add(velocity) #adjusts the ship's position by adding the velocity point to the position point using Point class method
        self._body.set_position(new_position) #sets the ship's position to the new position

    def move_left(self):
        """moves the ship to the left."""
        velocity = Point(-SHIP_VELOCITY, 0) #defines left-ward velocity as a point with negative x component of the ship's velocity
        self._body.set_velocity(velocity) #sets the velocity of the the ship's body to the left-ward velocity above
        
    def move_right(self):
        """moves the ship to the right."""
        velocity = Point(SHIP_VELOCITY, 0) #defines right-ward velocity as a point with positive x component of the ship's velocity
        self._body.set_velocity(velocity) #sets the velocity of the the ship's body to the right-ward velocity above
    
    def stop_moving(self):
        """Stops the ship from moving."""
        velocity = Point(0, 0) #defines no movement as a velocity with zero x or y components
        self._body.set_velocity(velocity) #sets the velocity of the the ship's body to the zero velocity above