from .biome import Biome

class Grassland(Biome):

    def __init__(self):
        Biome.__init__(self, "Grassland", 15, 22, {"little Rainfall", "No Shade"})
        

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if animal.terrestrial and animal.species_type == "bird":
                    self.animals.append(animal)
                else:
                    raise AttributeError('Cannot add non-terrestrial animal to a grassland!')
            else:
                raise AttributeError('Too many animals in this grassland!')
        except AttributeError as err:
            print(f'Cannot add animal {err}')

            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if plant.sunlight.lower() == "full" and plant.insecticide_resistance.lower() == "high" or plant.sunlight.lower() == "partial" and plant.insecticide_resitance.lower() == "medium":
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add this plant/tree to this forest")