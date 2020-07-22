# from animals import Aquatic
from animals import Identifiable
from .contains_animals import ContainsAnimals
from .contains_plants import ContainsPlants
# from animals import RiverDolphin


class River(ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self):
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.plant_capacity = 6
        self.animal_capacity = 12
        self.characteristics = ["fresh water"]

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.freshwater and plant.requires_current:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add plants that require brackish water or stagnant water to a river biome")