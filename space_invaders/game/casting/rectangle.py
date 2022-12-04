#import necessary classes
from game.casting.point import Point #import Point class for position and size uses


class Rectangle:
    """A 4-sided flat shape with straight sides used to form the bodies of solid game objects."""

    def __init__(self, position, size):
        """Constructs a new Rectangle."""
        self._position = Point() #the position of the rectangle's top left corner
        self._size = Point() #the size of the rectangle where the x component is the width of the rectangle and the y component is the height of the rectangle

    def get_position(self):
        """Gets the top left point of the rectangle.
        
        Returns:
            An instance of Point containing the top left coordinates.
        """
        return self._position

    def get_size(self):
        """Gets the size of the rectangle.
        
        Returns:
            An instance of Point containing the width and height.
        """
        return self._size