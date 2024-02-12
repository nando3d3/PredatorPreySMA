from mesa.model import Model
from mesa.time import RandomActivation
from .plant import Plant
from .prey import Prey
from .predator import Predator

class PredatorPreyModel(Model):
    def __init__(self, num_predator, num_prey, num_plant):
        self.schedule = RandomActivation(self)
        self.num_predator = num_predator
        self.num_prey = num_prey
        self.num_plant = num_plant

        prey_agents = []
        plant_agents = []
        
        for i in range(self.num_plant):
            plant = Plant(i + self.num_predator + self.num_prey, self)
            self.schedule.add(plant)
            plant_agents.append(plant)
            
        for i in range(self.num_prey):
            prey = Prey(i + self.num_predator, self, plant_agents)
            self.schedule.add(prey)
            prey_agents.append(prey)
            print(f'Prey {i}')
            
        for i in range(self.num_predator):
            pred = Predator(i, self, prey_agents)
            self.schedule.add(pred)
            print(f'Predator {i}')
               
    def step(self):
        self.schedule.step()