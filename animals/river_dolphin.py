from animals import Animal
from attributes import Euryhaline
from attributes import Swimming


class RiverDolphin(Animal, Euryhaline, Swimming):
    def __init__(self):
        Animal.__init__(self, 'River Dolphin', ['Trout', 'Mackarel', 'Salmon', 'Sardine'], ['River', 'Coastline'], 13)
        Swimming.__init__(self)
        Euryhaline.__init__(self)

    def __str__(self):
        return super().__str__() + '"EEEEEEEEEE."'
