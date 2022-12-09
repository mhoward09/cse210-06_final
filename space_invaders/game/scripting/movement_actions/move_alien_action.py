from constants import *
from game.scripting.action import Action


class MoveAlienAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
            aliens = cast.get_actors(ALIEN_GROUP)
            for alien in aliens:
                
                if callback._counter == 120:
                    #move aliens down
                    alien.move_down()
                    #change alien direction
                    alien.move_opposite()
                    
                body = alien.get_body()

                position = body.get_position()
                velocity = position.get_velocity()
                position = position.add(velocity)
                body.set_position(position)
                #after moving down, stop moving down
                alien.stop_y()
            
