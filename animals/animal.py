class Animal:

    def __init__(self, species, prey, locations, minimum_release_age):
        self.species = species
        self.prey = prey
        self.locations = locations
        self.minimum_release_age = minimum_release_age

    def move(self, propulsion, speed):
        return f"{self.species} moves at {speed} meters/sec by {propulsion}"
