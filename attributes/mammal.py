from attributes import Terrestrial


class Mammal(Terrestrial):
    def __init__(self):
        super().__init__()
        self.is_mammal = True
