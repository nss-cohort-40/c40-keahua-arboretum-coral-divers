from animals import Animal
from attributes import Swimming
from attributes import Saltwater

class Ulae(Animal, Swimming, Saltwater):
    def __init__(self):
        Animal.__init__(self, '\'Ulae', ['Angelfish', 'Butterflyfish', 'Trout', 'Salmon'], ['Coastline'], 1)
        Swimming.__init__(self)
        Saltwater.__init__(self)

    def __str__(self):
        return super().__str__() + '"Glug glug glug"'