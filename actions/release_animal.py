from animals import GoldDustDayGecko
from animals import RiverDolphin
from animals import NeneGoose
from animals import Kikakapu
from animals import Pueo
from animals import Ulae
from animals import Opeapea
from animals import HappyFacedSpider


def release_animal(arboretum):
    animal = None
    allBiomes = list()

    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-")
    print("+ C H O O S E  A N I M A L  F O R  R E L E A S E +")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-")
    print("1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider")
    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = GoldDustDayGecko()
    if choice == "2":
        animal = RiverDolphin()
    if choice == "3":
        animal = NeneGoose()
    if choice == "4":
        animal = Kikakapu()
    if choice == "5":
        animal = Pueo()
    if choice == "6":
        animal = Ulae()
    if choice == "7":
        animal = Opeapea()
    if choice == "8":
        animal = HappyFacedSpider()
    # Changing the Arboretum to a dictionary and looping through it.
    for (key, value) in arboretum.__dict__.items():
        # When the loop finds a list...
        if type(value) is list:
            # ...then loop through that list and reference each index.
            for index, biome in enumerate(value):
                # Smash the index number into a new property on the object at that list index...
                biome.original_index = index
                # ...so that when it is appended into a new list it can be referenced later.
                allBiomes.append(biome)
                
    for index, biome in enumerate(allBiomes):
        print(f'{index + 1}. {biome}: [{biome.id}]')

    print("Release the animal into which biome?")
    choice = input("> ")
    index = int(choice) - 1
    selected_biome = allBiomes[index]
    original_biome_index = selected_biome.original_index
    if selected_biome.name == "Coastline":
        arboretum.coastlines[original_biome_index].animals.append(animal)
    if selected_biome.name == "Forest":
        arboretum.forests[original_biome_index].animals.append(animal)
    if selected_biome.name == "Grassland":
        arboretum.grasslands[original_biome_index].animals.append(animal)
    if selected_biome.name == "Mountain":
        arboretum.mountains[original_biome_index].animals.append(animal)
    if selected_biome.name == "River":
        arboretum.rivers[original_biome_index].animals.append(animal)
    if selected_biome.name == "Swamp":
        arboretum.swamps[original_biome_index].animals.append(animal)