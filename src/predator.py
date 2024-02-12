from .creature import Creature
from .config import RED
class Predator(Creature):
    def __init__(self, uid, model, food = ()):
        self.color = RED
        self.size = 4
        self.vmax = 2.5
        self.food = food
        super().__init__(uid, model, self.color, self.size, self.food)