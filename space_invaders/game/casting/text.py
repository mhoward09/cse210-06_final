#import constants
from constants import * 

class Text:
    """A text message."""

    def __init__(self, value, fontfile = FONT_FILE, size = FONT_LARGE, alignment = ALIGN_LEFT):
        """Constructs a new Text."""
        self._value = value #defines the value attribute from the args - this is the string that the text will display
        self._fontfile = fontfile #defines the fontfile attribute from the args - this is the file path for the type of font to use in the game -- stored in the constants file under FONT_FILE
        self._size = size #defines the size attribute from the args - this is the size of the display text -- stored in constants file under FONT constants
        self._alignment = alignment #defines the alignment attribute from the args - this is where on the screen the text will be shown -- an integer stored under constants

    def get_alignment(self):
        """Gets the alignment for the text.
        
        Returns:
            A number representing the text alignment.
        """
        return self._alignment

    def get_fontfile(self):
        """Gets the font file for the text.
        
        Returns:
            A string containing the font file.
        """
        return self._fontfile

    def get_size(self):
        """Gets the font size of the text.
        
        Returns:
            A number representing the font size.
        """
        return self._size

    def get_value(self):
        """Gets the text's value.
        
        Returns:
            A string containing the text's value.
        """
        return self._value

    def set_value(self, value):
        """Sets the text's value.
        
        Args:
            A string containing the text's value.
        """
        self._value = value