from animals import Animal
from attributes import Swimming
from attributes import Saltwater
from attributes import Identifiable

class Kikakapu(Animal, Swimming, Saltwater, Identifiable):
    def __init__(self):
        Animal.__init__(self, 'Kikakapu', ['Shrimp', 'Crab', 'Squid', 'Mussel'], ['Swamp', 'River'], 1)
        Swimming.__init__(self)
        Saltwater.__init__(self)
        Identifiable.__init__(self)

    def __str__(self):
        return super().__str__() + '"Whatever.  I\'m a fish."'
