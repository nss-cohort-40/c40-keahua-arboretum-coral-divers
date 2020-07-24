from plants import MountainAppleTree
from plants import Silversword
from plants import RainbowEucalyptusTree
from plants import BlueJadeVine


def add_plant(Arboretum):
    
   plant = None

   print("1. Mountain Apple Tree")
   print("2. Silversword")
   print("3. Rainbow Eucalyptus Tree")
   print("4. Blue Jade Vine")

   choice = input("Choose plant to cultivate > ")

   if choice == "1":
       plant = MountainAppleTree()
       print(plant)
       input("\n\nPress enter to continue...")
    #    pass

   if choice == "2":
        plant = Silversword()
        print(plant)
        

   if choice == "3":
        # plant RainbowEucalyptusTree()
        pass

   if choice == "4":
        # plant = BlueJadeVine()
        pass

   biomes = [Arboretum.rivers, Arboretum.grasslands, Arboretum.swamps]

   options = []

   for biome in biomes:
       for environment in biome:
           if len(environment.plants) < environment.plant_capacity:
               options.append(environment)

   for index, option in enumerate(options):
       print(f'{index + 1}. {option} ({len(option.plants)} plants)')

   if len(options) > 0:
       print(f"Where would you like to plant {plant}?")
       choice = input("> _")

   else:
       print("error")
       input("Press enter to continue")