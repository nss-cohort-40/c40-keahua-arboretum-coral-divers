from animals import Animal
from attributes import Freshwater
from attributes import Identifiable
from attributes import Swimming


class RiverDolphin(Animal, Freshwater, Swimming, Identifiable):
    def __init__(self):
        Animal.__init__(self, 'River Dolphin', ['Trout', 'Mackarel', 'Salmon', 'Sardine'], ['River', 'Coastline'], 13)
        Freshwater.__init__(self)
        Swimming.__init__(self)
        Identifiable.__init__(self)

    def __str__(self):
        return super().__str__() + '"EEEEEEEEEE."'
