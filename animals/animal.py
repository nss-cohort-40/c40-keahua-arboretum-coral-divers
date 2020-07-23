import random

class Animal:

<<<<<<< HEAD
    def __init__(self, species, prey, locations, minimum_release_age):
        self.species = species
        self.prey = prey
        self.locations = locations
        self.minimum_release_age = minimum_release_age
=======
    def __init__(self, species, prey, location, minimum_release_age):
        self.__species = species
        self.__prey = prey
        self.__location = location
        self.__minimum_release_age = minimum_release_age
        self.__age = random.randrange(1, 16)

    @property
    def species(self):
        return self.__species

    @property
    def prey(self):
        return self.__prey

    @property
    def location(self):
        return self.__location

    @property
    def minimum_release_age(self):
        return self.minimum_release_age

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The {self.species} ate {prey} for a meal')
        else:
            print(f'The {self.species} rejects the {prey}')
>>>>>>> 819b10f712e6b93cec2198efabfb2c1142acb075

    def move(self, propulsion, speed):
        return f"{self.species} moves at {speed} meters/sec by {propulsion}"

    def __str__(self):
        return f'{self.species} {self.id} says: '
