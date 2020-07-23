from animals import Animal
from attributes import Terrestrial
from attributes import Walking

class GoldDustDayGecko(Animal, Terrestrial, Walking):
    def __init__(self):
        Animal.__init__(self, 'Gold Dust Day Gecko', ['Crickets', 'Spiders', 'Mealworms', 'Flies'], ['Forest'], 2)
        Terrestrial.__init__(self)
        Walking.__init__(self)

    def __str__(self):
        return super().__str__() + '"I don\'t know what Geckos sound like."'
