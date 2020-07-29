from .plant import Plant
from attributes import Terrestrial
from attributes import Stagnant

class BlueJadeVine(Plant, Terrestrial, Stagnant):
    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine", {"Grassland", "Swamp"}, "partial", 0, "medium")
        Terrestrial.__init__(self)
        Stagnant.__init__(self)

    def __str__(self):
        return f"{self.species} [{self.id}]"


