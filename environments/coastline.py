from environments import Biome

class Coastline(Biome):

    def __init__(self):
        Biome.__init__(self, 'Coastline', 3, 15, 'Saltwater')

    def add_animal(self, animal):
        try:
            if animal.aquatic and animal.cell_type == "hypotonic":
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-saltwater fish to a coastline")
