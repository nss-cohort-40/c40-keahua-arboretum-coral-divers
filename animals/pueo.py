from animals import Animal
from attributes import Flying
from attributes import Reptile
from attributes import Birds


class Pueo(Animal, Flying, Birds, Reptile):
    def __init__(self):
        Animal.__init__(self, 'Pueo', ['Rats', 'Mongoose'], [
                        'Grassland', 'Forest'], 8)
        Flying.__init__(self)
        Birds.__init__(self)
        Reptile.__init__(self)

    def __str__(self):
        return super().__str__() + '"WHOOOO WHOOOO!"'
