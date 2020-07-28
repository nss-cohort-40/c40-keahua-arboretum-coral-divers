from attributes import ContainsAnimals
from attributes import ContainsPlants
from attributes import Identifiable


class Biome(ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self, name, plant_capacity, animal_capacity, characteristics):
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.name = name
        self.plant_capacity = plant_capacity
        self.animal_capacity = animal_capacity
        self.characteristics = characteristics

    def __str__(self):
        return f'{self.name}'
