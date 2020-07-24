from .biome import Biome



class Mountain(Biome):

    def __init__(self):
        Biome.__init__(self, "Mountain", 4, 6, "High Elevation")

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
