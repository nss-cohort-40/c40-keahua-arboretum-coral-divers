from animals import Identifiable
from .contains_animals import ContainsAnimals
from .contains_plants import ContainsPlants


class Mountain(Identifiable, ContainsAnimals, ContainsPlants):

    def __init__(self):
        Identifiable.__init__(self)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.flying and animal.terrestrial and animal.mammal:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-mammal or aquatic animals to a mountain environment.")

    def add_plant(self, plant):
        try:
            if plant.location == "mountain":
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-mountainous plants to a mountain environment.")
