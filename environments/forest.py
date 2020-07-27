from .biome import Biome
from attributes import Flying


class Forest(Biome, Flying):

    def __init__(self):
        Biome.__init__(self, "Forest", 32, 20, {"Rainy", "Shady"})
        Flying.__init__(self)
       

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if animal.terrestrial and (animal.terrestrial.is_reptile or animal.wing_count):
                    self.animals.append(animal)
                else:
                    raise AttributeError('Cannot add non-terrestrial animal to a forest')
            else:
                raise AttributeError('Too many animals in this forest!')
        except AttributeError as err:
            print(f'Cannot add animal! {err}')

            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if plant.sunlight.lower() == 'shade':
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add this plant/tree to this forest")
