from animals import Animal
from attributes import Swimming
from attributes import Freshwater

class Kikakapu(Animal, Swimming, Freshwater):
    def __init__(self):
        Animal.__init__(self, 'Kikakapu', ['Shrimp', 'Crab', 'Squid', 'Mussel'], ['Swamp', 'River'], 1)
        Swimming.__init__(self)
        Freshwater.__init__(self)

    def __str__(self):
        return super().__str__() + '"Whatever.  I\'m a fish."'
