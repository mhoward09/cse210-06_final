#import necessary classes
from space_invaders.game.casting.actors.actor import Actor #import Actor class to be the parent class

class Label(Actor):
    """A label to be displayed."""
 
    def __init__(self, text, position, debug = False):
        """Constructs a new Label.
        
        Args:
            text: An instance of Text.
            position: An instance of Point.
        """
        super().__init__(debug) #inherits Actor init
        self._text = text #assigns text arg to an attribute - the text to be displayed as the label
        self._position = position #assigns position arg to an attribute - where the label will be positioned on the screen
        
    def get_position(self):
        """Gets the label's position.
        
        Returns:
            An instance of Point.
        """
        return self._position
    
    def get_text(self):
        """Gets the label's text.
        
        Returns:
            An instance of Text.
        """
        return self._text    