import random

from constants import *

from space_invaders.game.scripting.action import Action
from space_invaders.game.casting.point import Point
from space_invaders.game.casting.body import Body
from space_invaders.game.casting.image import Image
from space_invaders.game.casting.actors.bullet import Bullet
from space_invaders.game.casting.actors.ship import Ship
from space_invaders.game.casting.actors.alien import Alien
from space_invaders.game.casting.sound import Sound

from space_invaders.game.scripting.sound_actions.play_sound_action import PlaySoundAction

#from Greg maybe we can rename this ShipBulletAction
#I will create AlienBulletAction to handle alien firings
class AlienBulletAction(Action):
    """creates a bullet from an origin (ship or alien) object.
    
    Arguments:
        origin: an instance of a ship or an alien with a position
        sound: an instance of a sound
    """

    def __init__(self, audio_service):
        super().__init__() 
        self._audio_service = audio_service

    def execute(self, cast, script, callback):
        #fires every 80, 160, 240, 320, 400, 480 cycle of the while loop in director
        if callback._counter in [80, 160, 240, 320, 400, 480]:
            #get a random brick/alien
            alien = cast.get_actors(ALIEN_GROUP)
            print(f'this is alien length please check {len(alien)}')
            ran_index = random.randint(0, len(alien) - 1)

            alien_body = alien[ran_index].get_body()
            position = alien_body.get_position()
            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
            velocity = Point(0, BULLET_VELOCITY) #I figured 6 should be fast enough for bullet travel
            abody = Body(position, size, velocity)
            image = Image(ALIEN_BULLET_IMAGE)
            bullet = Bullet(abody, image, True)
            cast.add_actor(ALIEN_BULLET_GROUP, bullet)

            script.add_action(OUTPUT, PlaySoundAction(self._audio_service, ALIEN_BULLET_SOUND))

        #optional is we can also make a move alien bullet here 
        #this is what I did with my code

        """
        #move the bullet
        bullets = cast.get_actors(BULLET_GROUP)
        for bullet in bullets:
            body = bullet.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
        """