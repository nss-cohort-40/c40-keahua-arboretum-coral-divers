from animals import Animal
from attributes import Terrestrial
from attributes import Flying
from attributes import Identifiable

class NeneGoose(Animal, Terrestrial, Flying, Identifiable):
    def __init__(self):
        Animal.__init__(self, 'Nene Goose', ['Leaves', 'Seeds', 'Fruit', 'Flowers'], ['Grassland'], 7)
        Terrestrial.__init__(self)
        Flying.__init__(self)
        Identifiable.__init__(self)

    def __str__(self):
        return super().__str__() + '"HONK!"'
