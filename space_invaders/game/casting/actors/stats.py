#import constants
from constants import *

#import necessary classes
from game.casting.actors.actor import Actor #import Actor class to act as parent class


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug) #inherits actor init
        self._level = 1 #creates level attribute -- used for increasing lives by level advancement
        self._lives = DEFAULT_LIVES #creates lives attribute to track and manage how often player can try again or continue playing -- lives are lost via aliens reaching the bottom of the screen or ship collision with a bullet
        self._score = 0 #creates the attribute of player score to track how many points the player has made by destroying aliens

    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_LIVES:
            self._lives += 1 

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        return self._lives
  
    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score

    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0