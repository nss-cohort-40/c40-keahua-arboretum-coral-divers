from animals import Animal
from attributes import Stagnant


class HappyFacedSpider(Animal, Stagnant):
    def __init__(self):
        Animal.__init__(self, 'Hawaiian Happy-Faced Spider', "Insects", "Swamp", .5)
        Stagnant.__init__(self)
        

    def __str__(self):
        return super().__str__() + '"Whatever.  I\'m a spider. Boo!"'