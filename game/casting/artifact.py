from game.casting.actor import Actor
import random
class Artifact(Actor):
    
    def __init__(self):
        super().__init__()
        self._type = random.randint(0, 1)
        self.duration = 40

    def Collision(self):
        if self._type == 0:
            return -10
        else:
            return 10

    def Get_Type(self):
        return self._type

    def move_next(self, max_x, max_y, cast):
        self.duration -= 1
        if self.duration <= 0:
            cast.remove_actor('artifacts', self)
        return super().move_next(max_x, max_y)