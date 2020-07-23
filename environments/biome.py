from attributes import Identifiable

class Biome:

    def __init__(self, name, capacity_animal, capacity_plant):
        Identifiable.__init__(self)
        self.name = name
        self.capacity_animal = capacity_animal
        self.capacity_plant = capacity_plant
        self.plants = list()
        self.animals = list()

    def animal_count(self):
        return f"This place has {len(self.animals)} animals in it."

    def plant_count(self):
        return f"This place has {len(self.plants)} plants in it."

    #Add amimal method and add plant method could live here or on individual environments
        
