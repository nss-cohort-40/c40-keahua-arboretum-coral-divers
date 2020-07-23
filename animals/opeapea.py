
from animals import Animal
from attributes import Flying
from attributes import Terrestrial
from attributes import Identifiable
from attributes import Mammal


class Opeapea(Animal, Flying, Terrestrial, Identifiable, Mammal):
    def __init__(self):
        Animal.__init__(self, 'Opeapea', ['Moths', 'Beetles', 'Termites', 'Fruit'], [
                        'Forest', 'Mountain'], 5)
        Flying.__init__(self)
        Terrestrial.__init__(self)
        Identifiable.__init__(self)
        Mammal.__init__(self)

    def __str__(self):
        return super().__str__() + '"SREEECH!"'
