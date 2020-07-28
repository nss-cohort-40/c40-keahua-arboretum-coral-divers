from animals import GoldDustDayGecko
from animals import RiverDolphin
from animals import NeneGoose
from animals import Kikakapu
from animals import Pueo
from animals import Ulae
from animals import Opeapea
from animals import HappyFacedSpider
import os


def build_release_animal_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        "\u001b[47m\u001b[30;1m+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-")
    print("+ C H O O S E  A N I M A L  F O R  R E L E A S E +")
    print(
        "+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-\u001b[0m\n")

    print("\u001b[32m1. Gold Dust Day Gecko")
    print("2. River Dolphin")
    print("3. Nene Goose")
    print("4. Kīkākapu")
    print("5. Pueo")
    print("6. 'Ulae")
    print("7. Ope'ape'a")
    print("8. Happy-Face Spider\u001b[0m")


def release_animal(arboretum):
    build_release_animal_menu()
    animal = None
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
    build_biome_choices(animal, arboretum, True)


def build_biome_choices(animal, arboretum, animal_accepted):
    if animal_accepted == False:
        print("****   That biome is not large enough   ****")
        print("****     Please choose another one      ****")
        print("")
    available_biomes = list()
    for (key, value) in arboretum.__dict__.items():
        if type(value) is list:
            for index, biome in enumerate(value):
                biome.original_index = index
                available_biomes.append(biome)

    if len(available_biomes) == 0:
        print('There are no biomes available.')
        input('Please press enter to continue...')
    else:
        for index, biome in enumerate(available_biomes):
            print(
                f'{index + 1}. {biome} [{biome.id}] ({len(biome.animals)} animals)')
    handle_biome_choice(available_biomes, animal, arboretum)


def handle_biome_choice(available_biomes, animal, arboretum):
    print("Choose biome to release animal or enter x to go back.")
    choice = input("> ")
    if choice == "x":
        pass
    else:
        index = int(choice) - 1
        selected_biome = available_biomes[index]
        original_biome_index = selected_biome.original_index
        if selected_biome.name == "Coastline":
            animal_accepted = arboretum.coastlines[original_biome_index].add_animal(
                animal)
            if animal_accepted == False:
                build_biome_choices(animal, arboretum, animal_accepted)
        if selected_biome.name == "Forest":
            animal_accepted = arboretum.forests[original_biome_index].add_animal(
                animal)
            if animal_accepted == False:
                build_biome_choices(animal, arboretum, animal_accepted)
        if selected_biome.name == "Grassland":
            animal_accepted = arboretum.grasslands[original_biome_index].add_animal(
                animal)
            if animal_accepted == False:
                build_biome_choices(animal, arboretum, animal_accepted)
        if selected_biome.name == "Mountain":
            animal_accepted = arboretum.mountains[original_biome_index].add_animal(
                animal)
            if animal_accepted == False:
                build_biome_choices(animal, arboretum, animal_accepted)
        if selected_biome.name == "River":
            animal_accepted = arboretum.rivers[original_biome_index].add_animal(
                animal)
            if animal_accepted == False:
                build_biome_choices(animal, arboretum, animal_accepted)
        if selected_biome.name == "Swamp":
            animal_accepted = arboretum.swamps[original_biome_index].add_animal(
                animal)
            if animal_accepted == False:
                build_biome_choices(animal, arboretum, animal_accepted)
