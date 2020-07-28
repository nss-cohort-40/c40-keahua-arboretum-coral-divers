from .biome import Biome

class River(Biome):

    def __init__(self):
        Biome.__init__(self, "River", 6, 12, "Fresh Water")

    def add_animal(self, animal):
        try:
<<<<<<< HEAD
            if hasattr(animal, 'is_euryhaline'):
                self.animals.append(animal)
                print(f'{animal.species} was added to the river!')
                input('Please press enter to continue...')
            elif animal.aquatic and animal.cell_type == "hypertonic":
                self.animals.append(animal)
                print(f'{animal.species} was added to the river!')
                input('Please press enter to continue...')
        except AttributeError:
            print("Cannot add non-aquatic, or saltwater animals to a river")

=======
            if len(self.animals) < self.animal_capacity:
                if hasattr(animal, 'is_euryhaline'):
                    self.animals.append(animal)
                    print(f'{animal.species} was added to the river!')
                    input('Please press enter to continue...')
                elif animal.aquatic and animal.cell_type == "hypertonic":
                    self.animals.append(animal)
                    print(f'{animal.species} was added to the river!')
                    input('Please press enter to continue...')
                else:
                    raise AttributeError('This animal does not belong in the river!')
            else:
                animal_accepted = False
                return animal_accepted
                raise AttributeError('The river has already reached capacity!')
        except AttributeError as err:
            print(err)
>>>>>>> master
            input('Press enter to continue')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.freshwater and plant.requires_current:
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the river!')
                    input('Press enter to continue...')
                else:
                    raise AttributeError('Plant cannot grow in the river!')
            else:
                raise AttributeError(
                    'River has already reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')
