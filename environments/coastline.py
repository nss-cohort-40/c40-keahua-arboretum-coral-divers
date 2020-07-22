from .contains_animals import ContainsAnimals
from animals import Identifiable

class Coastline(ContainsAnimals, Identifiable):

    def __init__(self):
        ContainsAnimals.__init__(self)
        Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.cell_type == "hypotonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-saltwater animals to a coastline")
