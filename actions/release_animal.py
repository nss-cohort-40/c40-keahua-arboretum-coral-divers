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
        animal == RiverDolphin()
    if choice == "3":
        animal == NeneGoose()
    if choice == "4":
        animal == Kikakapu()
    if choice == "5":
        animal == Pueo()
    if choice == "6":
        animal == Ulae()
    if choice == "7":
        animal == Opeapea()
    if choice == "8":
        animal == HappyFacedSpider()

    for key, value in arboretum.__dict__.items():
        if type(value) is list:
            for biome in value:
                allBiomes.append(biome)
                
    for index, biome in enumerate(allBiomes):
        print(f'{index + 1}. {biome}: [{biome.id}]')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].animals.append(animal)


