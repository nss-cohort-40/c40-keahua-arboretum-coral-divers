from animals import Identifiable
from .contains_animals import ContainsAnimals
from .contains_plants import ContainsPlants


class Mountain(ContainsAnimals, ContainsPlants, Identifiable):

    def __init__(self):
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.plant_capacity = 4
        self.animal_capacity = 6
        self.characteristics = ["high elevation"]

    def add_animal(self, animal):
        try:
            if animal.terrestrial:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add aquatic animals to a mountain")

    def add_plant(self, plant):
        try:
            if plant.location == "Mountain":
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-mountainous plants to a mountain biome")
