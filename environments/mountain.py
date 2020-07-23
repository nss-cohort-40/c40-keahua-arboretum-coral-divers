from animals import Identifiable
from .contains_animals import ContainsAnimals
from .contains_plants import ContainsPlants

class Mountain(Identifiable, ContainsAnimals, ContainsPlants):

    def __init__(self):
        Identifiable.__init__(self)
        ContainsAnimals.__init__(self)
        ContainsPlants.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.