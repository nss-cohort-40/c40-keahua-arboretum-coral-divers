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
                    print(f'{animal.species} was added to the swamp!')
                    input('Please press enter to continue...')
                else:
                    raise AttributeError('Cannot add non-aquatic or saltwater animals to a swamp')
            else:
                animal_accepted = False
                return animal_accepted
        except AttributeError as err:
            print(err)
            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.current_speed == 0:
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the swamp!')
                    input('Press enter to continue...')
                else:
                    raise AttributeError('Plant cannot grow in the swamp!')
            else:
                raise AttributeError('Swamp has already reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')
