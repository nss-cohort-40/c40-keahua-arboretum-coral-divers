from .plant import Plant
from attributes import Terrestrial

class MountainAppleTree(Plant, Terrestrial):
    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree", "Grassland", "partial", 17, "high")
        Terrestrial.__init__(self)

    def __str__(self):
        return f"{self.species} [{self.id}]"

    

