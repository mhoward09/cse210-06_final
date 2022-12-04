#import necessary classes
from game.casting.point import Point #import Point class for positioning uses
from game.casting.rectangle import Rectangle #import Rectangle to define body edges


class Body:
    """A rigid body used for physics operations - the solid part of items."""
    
    def __init__(self, position = Point(), size = Point(), velocity = Point()):
        """Constructs a new Body."""
        self._position = position #defines the position attribute as a point in the args - the position of the object represented by the body
        self._size = size #defines the size attribute from the args - determines the size of the body
        self._velocity = velocity #defines the velocity attribute from the args - the direction and speed the body is moving in
    
    def get_position(self):
        """Gets the body's position.
        
        Returns:
            An instance of Point containing the x and y coordinates.
        """
        return self._position

    def get_size(self):
        """Gets the body's size.
        
        Returns:
            An instance of Point containing the width and height.
        """
        return self._size

    def get_velocity(self):
        """Gets the body's velocity.
        
        Returns:
            An instance of Point containing the horizontal and vertical speed.
        """
        return self._velocity

    def get_rectangle(self):
        """Gets the rectangle enclosing the body.
        
        Returns:
            An instance of Rectangle.
        """
        return Rectangle(self._position, self._size)
        
    def set_position(self, position):
        """Sets the position to the given value.
        
        Args:
            position: An instance of Point.
        """
        self._position = position

    def set_size(self, size):
        """Sets the size to the given value.
        
        Args:
            size: An instance of Point.
        """
        self._size = size

    def set_velocity(self, velocity):
        """Sets the velocity to the given value.
        
        Args:
            velocity: An instance of Point.
        """
        self._velocity = velocity