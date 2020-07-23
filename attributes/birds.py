from attributes import Terrestrial

class Birds(Terrestrial):

    def __init__(self):
        super().__init__()
        self.species_type = "bird"