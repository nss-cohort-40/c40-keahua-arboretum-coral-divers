from .biome import Biome
from attributes import ContainsAnimals
from attributes import ContainsPlants


class Mountain(ContainsAnimals, ContainsPlants, Biome):

    def __init__(self):
        Identifiable.__init__(self)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Biome.__init__(self, "Mountain", 4, 6)

    def add_animal(self, animal):
        try:
            if animal.mammal and animal.flying and animal.terrestrial:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add aquatic animals to a mountain environment.")

    def add_plant(self, plant):
        try:
            if plant.sunlight.lower() == "partial":
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Mountain flora require partial sunlight.")
