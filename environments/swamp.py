from attributes import Stagnant
from attributes import ContainsAnimals
from attributes import ContainsPlants
from .biome import Biome
# import sys
# sys.path.append('../')

# from animals.

class Swamp(Biome, ContainsAnimals, ContainsPlants, Stagnant):

    def __init__(self):
        Biome.__init__(self, "Swamp", 8, 12)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Stagnant.__init__(self)
        # self.inhabitants = []



    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.current_speed == 0:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic or saltwater animals to a swamp")

    def add_plant(self, plant):
        try:
            if plant.current_speed == 0:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-stagnant water plants to a swamp")
  

    # def __str__(self):
    #     return f"Swamp {self.id}"
