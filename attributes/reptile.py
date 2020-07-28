from attributes import Terrestrial


class Reptile(Terrestrial):
    def __init__(self):
        super().__init__()
        self.is_reptile = True
