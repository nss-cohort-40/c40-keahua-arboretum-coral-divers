from .biome import Biome
from attributes import Flying


class Forest(Biome, Flying):

    def __init__(self):
        Biome.__init__(self, "Forest", 32, 20, {"Rainy", "Shady"})
        Flying.__init__(self)

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if animal.terrestrial and (animal.is_reptile or animal.wing_count):
                    self.animals.append(animal)
                    print(f'{animal.species} was added to the forest!')
                    input('Please press enter to continue...')
                else:
                    raise AttributeError(
                        'Cannot add non-terrestrial animal to a forest')
            else:
                animal_accepted = False
                return animal_accepted
        except AttributeError as err:
            print(err)
            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.sunlight.lower() == 'shade':
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the forest!')
                    input('Press enter to continue...')
                else:
                    raise AttributeError('Plant cannot grow in the forest!')
            else:
                raise AttributeError('Forest has reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')
