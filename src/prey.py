from .creature import Creature
from .config import WHITE

class Prey(Creature):
    def __init__(self, uid, model, food = ()):
        self.color = WHITE
        self.size = 2
        self.vmax = 2
        self.food = food
        super().__init__(uid, model, self.color, self.size, self.food)