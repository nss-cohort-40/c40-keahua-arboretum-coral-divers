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
    for (key, value) in arboretum.__dict__.items():
        if type(value) is list:
            for index, biome in enumerate(value):
                if len(biome.animals) < biome.animal_capacity:
                    biome.original_index = index
                    allBiomes.append(biome)
                
    if len(allBiomes) == 0:
        print('There are no biomes with space available.')
        input('Please press enter to continue...')
    else:
        for index, biome in enumerate(allBiomes):
            print(f'{index + 1}. {biome} [{biome.id}] ({len(biome.animals)} animals)')

        print("Release the animal into which biome?")
        choice = input("> ")
        index = int(choice) - 1
        selected_biome = allBiomes[index]
        original_biome_index = selected_biome.original_index
        # Unless there is a way to dynamically access object properties in Python, this is the best I can do.
        if selected_biome.name == "Coastline":
            arboretum.coastlines[original_biome_index].add_animal(animal)
        if selected_biome.name == "Forest":
            arboretum.forests[original_biome_index].add_animal(animal)
        if selected_biome.name == "Grassland":
            arboretum.grasslands[original_biome_index].add_animal(animal)
        if selected_biome.name == "Mountain":
            arboretum.mountains[original_biome_index].add_animal(animal)
        if selected_biome.name == "River":
            arboretum.rivers[original_biome_index].add_animal(animal)
        if selected_biome.name == "Swamp":
            arboretum.swamps[original_biome_index].add_animal(animal)