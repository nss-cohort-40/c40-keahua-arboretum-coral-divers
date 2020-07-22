# from environments import Stagnant
from environments import Biome
import sys
sys.path.append('../')

# from animals.


class Swamp(Biome):

    def __init__(self, name):
        self.name = name
        self.inhabitants = []

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def addInhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} is not of type IStagnant")
        self.inhabitants.append(item)

    def __str__(self):
        return self.name