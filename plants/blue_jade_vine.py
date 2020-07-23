from .plant import Plant
from attributes import Terrestrial
from attributes import Stagnant

class BlueJadeVine(Plant, Terrestrial):
    def __init__(self):
        Plant.__init__(self, "BlueJadeVine", {"Grassland", "Swamp"}, "partial", 0, "medium")
        Terrestrial.__init__(self)


