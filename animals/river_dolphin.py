from animals import Animal
from attributes import Freshwater
from attributes import Identifiable
from attributes import Swimming


class RiverDolphin(Animal, Freshwater, Swimming, Identifiable):
    def __init__(self):
<<<<<<< HEAD
        Animal.__init__(self, "River dolphin", {
                        "Trout", "Mackarel", "Salmon", "Sardine"}, {"River", "Coastline"}, 13)
=======
        Animal.__init__(self, 'River Dolphin', ['Trout', 'Mackarel', 'Salmon', 'Sardine'], ['River', 'Coastline'], 13)
>>>>>>> 819b10f712e6b93cec2198efabfb2c1142acb075
        Freshwater.__init__(self)
        Swimming.__init__(self)
        Identifiable.__init__(self)
<<<<<<< HEAD

    # @property
    # def prey(self):
    #     return self.prey

    def feed(self, prey):
        if prey in self.prey:
            print(f'The dolphin ate {prey} for a meal')
        else:
            print(f'The dolphin rejects the {prey}')
=======
>>>>>>> 819b10f712e6b93cec2198efabfb2c1142acb075

    def __str__(self):
        return super().__str__() + '"EEEEEEEEEE."'
