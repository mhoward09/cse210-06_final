class Sound:
    """A sound that can be heard.

    The responsibility of Sound is keep track of the audio asset information.
    """

    def __init__(self, filename, volume = 1, repeated = False):
        """Constructs a new Sound."""
        self._filename = filename #defines the filename attribute from the args - this will the the file path to the sound file
        self._volume = volume #defines the volume attribute from the args - this will be the volume of the sound relative to the game not the computer
        self._repeated = repeated #defines the repeated attribute from the args - tells if the sound is repeated or not (background music repeats, exploded alien sound only happens once when the alien explodes)

    def get_filename(self):
        """Gets the filename for the sound.
        
        Returns:
            A string containing the filename.
        """
        return self._filename

    def get_volume(self):
        """Gets the volume the sound should be played at.
        
        Returns:
            A number representing the volume.
        """
        return self._volume

    def is_repeated(self):
        """Whether or not the sound should be repeatedly played.
        
        Returns:
            True if the sound should be repeated; False if otherwise.
        """
        return self._repeated