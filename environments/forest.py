from .biome import Biome
from attributes import Flying


class Forest(Biome, Flying):

    def __init__(self):
        Biome.__init__(self, "Forest", 32, 20, {"Rainy", "Shady"})
        Flying.__init__(self)
       

    def add_animal(self, animal):
        try:
            if animal.terrestial and (animal.terrestial.is_reptile or animal.wing_count):
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add animal to this biome")

    def add_plant(self, plant):
        try:
            if plant.sunlight.lower() == 'shade':
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add this plant/tree to this forest")
