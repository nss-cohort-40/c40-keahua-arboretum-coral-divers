from attributes import ContainsAnimals
from attributes import ContainsPlants
from attributes import Flying


class Forest():

    def __init__(self):
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.plant_capacity = 32
        self.animal_capacity = 20
        self.characteristics = ["rainy", "shady"]

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
