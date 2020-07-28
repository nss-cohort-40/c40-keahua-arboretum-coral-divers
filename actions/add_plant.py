from plants import MountainAppleTree
from plants import Silversword
from plants import RainbowEucalyptusTree
from plants import BlueJadeVine

def add_plant(Arboretum):
    
   plant = None

   print("")
   print("1. Mountain Apple Tree")
   print("2. Silversword")
   print("3. Rainbow Eucalyptus Tree")
   print("4. Blue Jade Vine")
   print("")

   choice = input("Choose plant to cultivate > ")

   if choice == "1":
       plant = MountainAppleTree()
       print("")
       print(plant)
       
       input("Press enter to continue...")
      
   if choice == "2":
        plant = Silversword()
        print("")
        print(plant)
        input("Press enter to continue...")

   if choice == "3":
        plant = RainbowEucalyptusTree()
        print("")
        print(plant)
        input("Press enter to continue...")

   if choice == "4":
        plant = BlueJadeVine()
        print("")
        print(plant)
        input("Press enter to continue...")

   
   biomes = [Arboretum.rivers, Arboretum.grasslands, Arboretum.swamps, Arboretum.mountains, Arboretum.forests]

   options = []

   for environment in biomes:
       for biome in environment:
          if len(biome.plants) < biome.plant_capacity:
             options.append(biome)

   for index, option in enumerate(options):
       print("")
       print(f'{index + 1}. {option} ({len(option.plants)} plants)')

   if len(options) > 0:
       print("")
       print(f"Where would you like to plant {plant}?")
       choice = input("> _")
       options[int(choice) - 1].add_plant(plant)

   else:
       print("")
       print("There have been no biomes annexed yet")
       print("")
       input("Press enter to continue")
