from animals import GoldDustDayGecko
from animals import HappyFacedSpider
from animals import Kikakapu
from animals import NeneGoose
from animals import Opeapea
from animals import Pueo
from animals import RiverDolphin
from animals import Ulae


def feed_animal(arboretum):
    pueo = Pueo()
    river_dolphin = RiverDolphin()

    print("+-++-++-++-++-++-++-++-++-++-")
    print("+ F E E D  A N  A N I M A L +")
    print("+-++-++-++-++-++-++-++-++-++-")
    print("1. Pueo")
    print("2. River Dolphin")
    print("3. \'Ulae")
    print("4. Gold Dust Day Gecko")
    print("5. Nene Goose")
    print("6. Kīkākapu")
    print("7. Ope\'ape\'a")
    print("8. Hawaiian Happy-Faced Spider")
    print("")
    print("Choose animal to feed.")
    choice = input("> ")

    animal_collection = []
    river_dolphin_collection = []
    kikakapu_collection = []
    pueo_collection = []
    ulae_collection = []
    gold_dust_day_gecko_collection = []
    nene_goose_collection = []
    opeapea_collection = []
    hawaiian_happy_faced_spider_collection = []

    for river in arboretum.rivers:
        for animal in river.animals:
            if animal.species == "river dolphin":
                river_dolphin_collection.append(animal)
            else:
                kikakapu_collection.append(animal)
            print(f"{animal.species} {animal.id}")
    for swamp in arboretum.swamps:
        for animal in swamp.animals:
            if animal.species == "kikakapu":
                kikakapu_collection.append(animal)
            else:
                hawaiian_happy_faced_spider_collection.append(animal)
            print(f"{animal.species} {animal.id}")
    for coastline in arboretum.coastlines:
        for animal in coastline.animals:
            if animal.species == "ulae":
                ulae_collection.append(animal)
            else:
                river_dolphin_collection.append(animal)
            print(f"{animal.species} {animal.id}")
    for grassland in arboretum.grasslands:
        for animal in grassland.animals:
            if animal.species == "pueo":
                pueo_collection.append(animal)
            else:
                nene_goose_collection.append(animal)
            print(f"{animal.species} {animal.id}")
    for forest in arboretum.forests:
        for animal in forest.animals:
            if animal.species == "pueo":
                pueo_collection.append(animal)
            if animal.species == "opeapea":
                opeapea_collection.append(animal)
            else:
                gold_dust_day_gecko_collection.append(animal)
            print(f"{animal.species} {animal.id}")
    for mountain in arboretum.mountains:
        for animal in mountain.animals:
            opeapea_collection.append(animal)
            print(f"{animal.species} {animal.id}")
    input("Press ENTER to continue")

    if choice == "1":
        for index, animal in enumerate(pueo_collection):
            print(f"{index + 1} {animal.species} {animal.id}")







    # for river in arboretum.rivers:
    #     for animal in river.animals:
    #         animal_collection.append(animal)
    # for swamp in arboretum.swamps:
    #     for animal in swamp.animals:
    #         animal_collection.append(animal)
    # for coastline in arboretum.coastlines:
    #     for animal in coastline.animals:
    #         animal_collection.append(animal)
    # for grassland in arboretum.grasslands:
    #     for animal in grassland.animals:
    #         animal_collection.append(animal)
    # for forest in arboretum.forests:
    #     for animal in forest.animals:
    #         animal_collection.append(animal)
    # for mountain in arboretum.mountains:
    #     for animal in mountain.animals:
    #         animal_collection.append(animal)

    # if choice == "1":
    #     for animal in animal_collection:
    #         if animal.species.lower() == "pueo":
    #             print(f"{animal.species} {animal.id}")
    # if choice == "2":
    #     for animal in animal_collection:
    #         if animal.species.lower() == "river dolphin":
    #             print(f"{animal.species} {animal.id}")
    # if choice == "3":
    #     for animal in animal_collection:
    #         if animal.species.lower() == "ulae":
    #             print(f"{animal.species} {animal.id}")
    # if choice == "4":
    #     for animal in animal_collection:
    #         if animal.species.lower() == "gold dust day gecko":
    #             print(f"{animal.species} {animal.id}")
    # if choice == "5":
    #     for animal in animal_collection:
    #         if animal.species.lower() == "nene goose":
    #             print(f"{animal.species} {animal.id}")
    # if choice == "6":
    #     for animal in animal_collection:
    #         if animal.species.lower() == "kikakapu":
    #             print(f"{animal.species} {animal.id}")
    # if choice == "7":
    #     for animal in animal_collection:
    #         if animal.species.lower() == "opeapea":
    #             print(f"{animal.species} {animal.id}")
    # if choice == "8":
    #     for animal in animal_collection:
    #         if animal.species.lower() == "hawaiian happy-faced spider":
    #             print(f"{animal.species} {animal.id}")


# More bad code to reference:
    # if choice == "1":
    #     for grassland in arboretum.grasslands:
    #         for animal in grassland.animals:
    #             if animal.species.lower() == "pueo":
    #                 print(f"{animal.species}")
    #                 input("\n\nPress any key to continue...")


# Previous code to reference:

    # if choice == "1":
    #     pueo = Pueo().__dict__
    #     for index, item in enumerate(pueo.):
    #         print(f"{index + 1}. {item}")
    # if choice == "2":
    #     river_dolphin = RiverDolphin.__dict__
    #     for index, item in enumerate(river_dolphin.items()):
    #         print(f"{index + 1}. {item}")
    #         print("What would you like to feed the dolphins today?")
    #         choice = input("> ")
    # if choice == "3":
    #     animal = Ulae()
    #     for index, item in enumerate(Ulae.Animal.__prey):
    #         print(f"{index + 1}. {item}")
    # if choice == "4":
    #     animal = GoldDustDayGecko()
    #     for index, item in enumerate(GoldDustDayGecko.Animal.__prey):
    #         print(f"{index + 1}. {item}")
    # if choice == "5":
    #     animal = NeneGoose()
    #     for index, item in enumerate(NeneGoose.Animal.__prey):
    #         print(f"{index + 1}. {item}")
    # if choice == "6":
    #     animal = Kikakapu()
    #     for index, item in enumerate(Kikakapu.Animal.__prey):
    #         print(f"{index + 1}. {item}")
    # if choice == "7":
    #     animal = Opeapea()
    #     for index, item in enumerate(Opeapea.Animal.__prey):
    #         print(f"{index + 1}. {item}")
    # if choice == "8":
    #     animal = HappyFacedSpider()
    #     for index, item in enumerate(Opeapea.Animal.__prey):
    #         print(f"{index + 1}. {item}")
