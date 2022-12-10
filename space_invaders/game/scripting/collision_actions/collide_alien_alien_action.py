from constants import *
#import necessary classes
from space_invaders.game.scripting.action import Action #import Action class as parent class


class CollideAlienAlienAction(Action):

    def __init__(self, physics_service):
        self._physics_service = physics_service    
        
    def execute(self, cast, script, callback):
        aliens = cast.get_actors(ALIEN_GROUP)
        for i in range(len(aliens)):
            for j in range(i + 1, len(aliens)):
                alien1 = aliens[i]
                alien2 = aliens[j]

                alien_body_1 = alien1.get_body()
                alien_body_2 = alien2.get_body()

                if self._physics_service.has_collided(alien_body_1, alien_body_2):
                    alien1.reverse_x()