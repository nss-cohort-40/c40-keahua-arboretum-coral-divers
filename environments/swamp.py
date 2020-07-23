from animals import Stagnant
from animals import Identifiable
from .contains_animals import ContainsAnimals
from .contains_plants import ContainsPlants
from .biome import Biome
# import sys
# sys.path.append('../')

# from animals.

class Swamp(Biome, ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self):
        Biome.__init__(self, "Swamp", 8, 12)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.inhabitants = []

    # def animal_count(self):
    #     return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        # if not isinstance(item, Stagnant):
        #     raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)

    # def add_animal(self, animal):
    #     try:
    #         if animal.aquatic and animal.cell_type == "hypertonic":
    #             self.animals.append(animal)
    #     except AttributeError:
    #         raise AttributeError(
    #             "Cannot add non-aquatic, or saltwater animals to a river")
  

    def __str__(self):
        return f"Swamp {self.id}"
