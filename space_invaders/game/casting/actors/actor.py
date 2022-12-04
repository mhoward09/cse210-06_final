from game.casting.text import Text


class Actor:
    """A thing that participates in the game."""
    
    def __init__(self, debug = False):
        """Constructs a new Actor.
        
        Args:
            debug: boolean, the debugging state of the actor
        """
        self._debug = debug
        
    def is_debug(self):
        """Whether or not the actor is being debugged.
        
        Returns:
            True if the actor is being debugged; False if otherwise.
        """
        return self._debug