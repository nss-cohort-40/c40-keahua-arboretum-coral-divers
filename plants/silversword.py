from .plant import Plant
from attributes import Terrestrial

class Silversword(Plant, Terrestrial):
    def __init__(self):
        Plant.__init__(self, "Silversword", "Grassland", "full", 22, "high")
        Terrestrial.__init__(self)

    def __str__(self):
        return f"{self.species} [{self.id}]"



