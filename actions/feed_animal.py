from animals import GoldDustDayGecko
from animals import HappyFacedSpider
from animals import Kikakapu
from animals import NeneGoose
from animals import Opeapea
from animals import Pueo
from animals import RiverDolphin
from animals import Ulae


def feed_animal(arboretum):
    # pueo = Pueo()
    # river_dolphin = RiverDolphin()
    # ulae = Ulae()

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
    choice = input("Choose animal to feed. > ")

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
            if animal.species.lower() == "river dolphin":
                river_dolphin_collection.append(animal)
            else:
                kikakapu_collection.append(animal)
    for swamp in arboretum.swamps:
        for animal in swamp.animals:
            if animal.species.lower() == "kikakapu":
                kikakapu_collection.append(animal)
            else:
                hawaiian_happy_faced_spider_collection.append(animal)
    for coastline in arboretum.coastlines:
        for animal in coastline.animals:
            if animal.species.lower() == "ulae":
                ulae_collection.append(animal)
            else:
                river_dolphin_collection.append(animal)
    for grassland in arboretum.grasslands:
        for animal in grassland.animals:
            if animal.species.lower() == "pueo":
                pueo_collection.append(animal)
            else:
                nene_goose_collection.append(animal)
    for forest in arboretum.forests:
        for animal in forest.animals:
            if animal.species.lower() == "pueo":
                pueo_collection.append(animal)
            if animal.species.lower() == "opeapea":
                opeapea_collection.append(animal)
            else:
                gold_dust_day_gecko_collection.append(animal)
    for mountain in arboretum.mountains:
        for animal in mountain.animals:
            opeapea_collection.append(animal)

    print("Select which animal you would like to feed:")
    if choice == "1":
        for index, animal in enumerate(pueo_collection):
            print(f"{index + 1}. {animal.species} [{animal.id}]")
        animal_selected = animal.species.lower()
    if choice == "2":
        for index, animal in enumerate(river_dolphin_collection):
            print(f"{index + 1}. {animal.species} [{animal.id}]")
        animal_selected = animal.species.lower()
    if choice == "3":
        for index, animal in enumerate(ulae_collection):
            print(f"{index + 1}. {animal.species} [{animal.id}]")
        animal_selected = animal.species.lower()
    if choice == "4":
        for index, animal in enumerate(gold_dust_day_gecko_collection):
            print(f"{index + 1}. {animal.species} [{animal.id}]")
        animal_selected = animal.species.lower()
    if choice == "5":
        for index, animal in enumerate(nene_goose_collection):
            print(f"{index + 1}. {animal.species} [{animal.id}]")
        animal_selected = animal.species.lower()
    if choice == "6":
        for index, animal in enumerate(kikakapu_collection):
            print(f"{index + 1}. {animal.species} [{animal.id}]")
        animal_selected = animal.species.lower()
    if choice == "7":
        for index, animal in enumerate(opeapea_collection):
            print(f"{index + 1}. {animal.species} [{animal.id}]")
        animal_selected = animal.species.lower()
    if choice == "8":
        for index, animal in enumerate(hawaiian_happy_faced_spider_collection):
            print(f"{index + 1}. {animal.species} [{animal.id}]")
        animal_selected = animal.species.lower()
    option = input("> ")

    if animal_selected == "pueo":
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")
        option = input(
            f"Select the food you'd like to feed the {animal.species}: > ")
        print(
            f"The {animal.species} enjoyed the {animal.prey[int(option) - 1]}!")
    if animal_selected == "river dolphin":
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")
        option = input(
            f"Select the food you'd like to feed the {animal.species}: > ")
        print(
            f"The {animal.species} enjoyed the {animal.prey[int(option) - 1]}!")
    if animal_selected == "ulae":
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")
        option = input(
            f"Select the food you'd like to feed the {animal.species}: > ")
        print(
            f"The {animal.species} enjoyed the {animal.prey[int(option) - 1]}!")
    if animal_selected == "gold dust day gecko":
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")
        option = input(
            f"Select the food you'd like to feed the {animal.species}: > ")
        print(
            f"The {animal.species} enjoyed the {animal.prey[int(option) - 1]}!")
    if animal_selected == "nene goose":
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")
        option = input(
            f"Select the food you'd like to feed the {animal.species}: > ")
        print(
            f"The {animal.species} enjoyed the {animal.prey[int(option) - 1]}!")
    if animal_selected == "kikakapu":
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")
        option = input(
            f"Select the food you'd like to feed the {animal.species}: > ")
        print(
            f"The {animal.species} enjoyed the {animal.prey[int(option) - 1]}!")
    if animal_selected == "opeapea":
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")
        option = input(
            f"Select the food you'd like to feed the {animal.species}: > ")
        print(
            f"The {animal.species} enjoyed the {animal.prey[int(option) - 1]}!")
    if animal_selected == "hawaiian happy-faced spider":
        for index, prey in enumerate(animal.prey):
            print(f"{index + 1}. {prey}")
        option = input(
            f"Select the food you'd like to feed the {animal.species}: > ")
        print(
            f"The {animal.species} enjoyed the {animal.prey[int(option) - 1]}!")

    input("> ")
