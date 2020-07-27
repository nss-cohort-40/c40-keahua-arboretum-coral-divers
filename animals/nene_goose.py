from animals import Animal
from attributes import Birds
from attributes import Flying

class NeneGoose(Animal, Birds, Flying):
    def __init__(self):
        Animal.__init__(self, 'Nene Goose', ['Leaves', 'Seeds', 'Fruit', 'Flowers'], ['Grassland'], 7)
        Flying.__init__(self)
        Birds.__init__(self)

    def __str__(self):
        return super().__str__() + '"HONK!"'
