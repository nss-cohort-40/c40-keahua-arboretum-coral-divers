from animals import Animal
from attributes import Flying
from attributes import Terrestrial

class Pueo(Animal, Flying, Terrestrial):
    def __init__(self):
        Animal.__init__(self, 'Pueo', ['Rats', 'Mongoose'], ['Grassland', 'Forest'], 8)
        Flying.__init__(self)
        Terrestrial.__init__(self)

    def __str__(self):
        return super().__str__() + '"WHOOOO WHOOOO!"'
