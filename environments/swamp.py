from attributes import Stagnant
from .biome import Biome

class Swamp(Biome, Stagnant):

    def __init__(self):
        Biome.__init__(self, "Swamp", 12, 8, "Stagnant Freshwater")
        Stagnant.__init__(self)

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if animal.aquatic and animal.current_speed == 0:
                    self.animals.append(animal)
                else:
                    raise AttributeError('Cannot add non-aquatic or saltwater animals to a swamp')
            else:
                raise AttributeError('Too many animals in this swamp!')
        except AttributeError as err:
            print(f'Cannot add animal! {err}')

            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if plant.current_speed == 0:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-stagnant water plants to a swamp")
