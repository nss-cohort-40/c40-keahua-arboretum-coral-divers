from attributes import Identifiable

class Plant(Identifiable):

    def __init__(self, species, locations, sunlight, seeds_produced, insecticide_resistance):
      Identifiable.__init__(self)
      self.__species = species
      self.__locations = locations
      self.__sunlight = sunlight
      self.__seeds_produced = seeds_produced
      self.__insecticide_resistance = insecticide_resistance


    @property
    def species(self):
        return self.__species

    @property
    def locations(self):
        return self.__locations

    @property
    def sunlight(self):
        return self.__sunlight

    @property
    def seeds_produced(self):
        return self.__seeds_produced

    @property
    def insecticide_resistance(self):
        return self.__insecticide_resistance


