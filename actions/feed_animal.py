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
    print("8. Hawaiian Happy-Face Spider")
    print("")
    print("Choose animal to feed.")
    choice = input("> ")

    if choice == "1":
        for grassland in arboretum.grasslands:
            for animal in grassland.animals:
                if animal.species.lower() == "pueo":
                    print(f"{animal.species}")
                    input("\n\nPress any key to continue...")



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
