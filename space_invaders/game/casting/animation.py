#import necessary libraries
import time

#import constants
from constants import *

#import necessary classes
from game.casting.image import Image #imports the Image class to use for the animation frames


class Animation:
    """An animation."""
    
    def __init__(self, images, rate = 6, delay = 0):
        """Constructs a new Animation."""
        self._delay = delay #how long between animation cycles
        self._images = images #the images that make up the animation cycle
        self._rate = rate #how fast the animation is in frames
        self._index = 0 #the index for the starting image of the animation
        self._frame = 0 #the creation of a counter for timing the changing of the images of the animation 
        self._start = time.time() #the time when the animation starts based on video service start
        
    def get_delay(self):
        """Gets the delay between animation cycles.
        
        Returns:
            A number representing the delay in seconds.
        """
        return self._delay

    
    def get_images(self):
        """Gets the images that make up the animation.
        
        Returns:
            A list of strings containing the image names.
        """
        return self._images

    def get_rate(self):
        """Gets the rate of animation in frames.
        
        Returns:
            The rate of animation in frames.
        """
        return self._rate

    def next_image(self):
        """Gets the next image to display.

        Returns:
           An instance of Image.
        """
        filename = self._images[self._index] #declares the filename is the first image in the list of images for the animation
        image = Image(filename) #using the file from above an Image object is created
        current = time.time() #declares what the currant time is in real time
        elapsed = current - self._start #declares that the time elapsed is the current time minus the start time

        if elapsed > self._delay:
            self._frame += 1 #if the time elapsed is greater than the declared delay time move add one to the frame
            
            if self._frame >= self._rate:
            #when the number of frames has become equal to the rate move to the next image in the list and reset the frame count to 0
                self._index = (self._index + 1) % len(self._images) #this is a loop because a % b = a if a < b and a % b = 0 if a = b
                self._frame = 0
            filename = self._images[self._index]
            image = Image(filename)
            
            if self._index >= len(self._images) - 1:
                #if you are at the last index restart the delay timer
                self._start = current

        return image