from .creature import Creature
from .config import GREEN

class Plant(Creature):
    def __init__(self, uid, model):
        self.size = 3
        self.color = GREEN
        super().__init__(uid, model, self.color, self.size)
        self.vmax = 0