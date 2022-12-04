class Color:
    """A color."""
    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            red: An int between 0 and 255 representing the red value.
            green: An int between 0 and 255 representing the green value.
            blue: An int between 0 and 255 representing the blue value.
            alpha: An int between 0 and 255 representing the alpha or opacity.
        """
        self._red = red #defines the red attribute from the args - the red portion of an RGB color
        self._green = green #defines the green attribute from the args - the green portion of an RGB color
        self._blue = blue #defines the blue attribute from the args - the blue portion of an RGB color
        self._alpha = alpha #defines the alpha attribute from the args - the alpha/opacity portion of an RGB color

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).

        Returns:
            The color as a Tuple of four values (red, green, blue, alpha)
        """
        return (self._red, self._green, self._blue, self._alpha)   