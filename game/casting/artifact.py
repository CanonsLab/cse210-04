from game.casting.actor import Actor
import random
class Artifact(Actor):
    
    def __init__(self):
        super().__init__()
        self._type = random.randint(0, 1)

    def Collision(self):
        if self.type == 0:
            return -10
        else:
            return 10

    def Get_Type(self):
        return self._type