from .plant import Plant
from attributes import Terrestrial

class RainbowEucalyptusTree(Plant, Terrestrial):
    def __init__(self):
        Plant.__init__(self, "RainbowEucalyptusTree", "Forest", "shade", 8, "low")
        Terrestrial.__init__(self)


