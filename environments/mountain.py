from .biome import Biome



class Mountain(Biome):

    def __init__(self):
        Biome.__init__(self, "Mountain", 4, 6, "High Elevation")

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if animal.mammal and animal.flying and animal.terrestrial:
                    self.animals.append(animal)
                else:
                    raise AttributeError('Cannot add aquatic animals to a mountain environment.')
            else:
                raise AttributeError('Too many animals on this mountain!')
        except AttributeError as err:
            print(f'Cannot add animal! {err}')

            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if plant.sunlight.lower() == "partial":
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError(
                "Mountain flora require partial sunlight.")
