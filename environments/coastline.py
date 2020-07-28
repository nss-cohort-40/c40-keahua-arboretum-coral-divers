from .biome import Biome


class Coastline(Biome):

    def __init__(self):
        Biome.__init__(self, 'Coastline', 3, 15, 'Saltwater')

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if animal.cell_type == "hypotonic" or animal.is_euryhaline:
                    self.animals.append(animal)
                    print(f'{animal.species} was added to the coastline!')
                    input('Please press enter to continue...')
                else:
                    raise AttributeError(
                        'Cannot add non-aquatic or freshwater animals to a coastline!')
            else:
                animal_accepted = False
                return animal_accepted
        except AttributeError as err:
            print(err)
            input('Press enter to continue...')
