from animals import Animal
from attributes import Terrestrial
from attributes import Walking
from attributes import Reptile


class GoldDustDayGecko(Animal, Walking, Reptile):
    def __init__(self):
        Animal.__init__(self, 'Gold Dust Day Gecko', [
                        'Crickets', 'Spiders', 'Mealworms', 'Flies'], ['Forest'], 2)
        Walking.__init__(self)
        Reptile.__init__(self)

    def __str__(self):
        return super().__str__() + '"I don\'t know what Geckos sound like."'
