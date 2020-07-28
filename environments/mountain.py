from .biome import Biome


class Mountain(Biome):

    def __init__(self):
        Biome.__init__(self, "Mountain", 4, 1, "High Elevation")

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if animal.is_mammal and animal.wing_count:
                    self.animals.append(animal)
                    print(f'{animal.species} was added to the mountain!')
                    input('Please press enter to continue...')
                else:
                    raise AttributeError(
                        'Cannot add aquatic animals to a mountain environment.')
            else:
                animal_accepted = False
                return animal_accepted
                raise AttributeError('Too many animals on this mountain!')
        except AttributeError as err:
            print(err)
            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.sunlight.lower() == "partial":
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the mountain!')
                    input('Press enter to continue...')
                else:
                    raise AttributeError('Plant cannot grow on the mountain!')
            else:
                raise AttributeError(
                    'Mountain has already reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')
