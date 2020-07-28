from .biome import Biome

class Grassland(Biome):

    def __init__(self):
        Biome.__init__(self, "Grassland", 15, 22, {"little Rainfall", "No Shade"})
        

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if animal.species_type == "bird":
                    self.animals.append(animal)
                    print(f'{animal.species} was added to the grassland!')
                    input('Please press enter to continue...')
                else:
                    raise AttributeError('Cannot add non-terrestrial animal to a grassland!')
            else:
                animal_accepted = False
                return animal_accepted
                raise AttributeError('Too many animals in this grassland!')
        except AttributeError as err:
            print(err)
            input('Press enter to continue...')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.sunlight.lower() == "partial" and plant.insecticide_resistance.lower() == "medium":
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the grassland!')
                    input('Press enter to continue...')
                elif plant.sunlight.lower() == "full" and plant.insecticide_resistance.lower() == "high":
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the grassland!')
                    input('Press enter to continue...')
            else:
                raise AttributeError('Grassland has already reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')