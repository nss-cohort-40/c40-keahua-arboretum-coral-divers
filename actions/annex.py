import os
from environments import River
from environments import Swamp
from environments import Coastline
from environments import Grassland
from environments import Forest
from environments import Mountain

from arboretum import Arboretum


def annex_habitat(Arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\u001b[47m\u001b[30;1m+-++-++-++-++-++-++-++-++-++-++-++")
    print("+ C H O O S E  A  H A B I T A T  +")
    print("+-++-++-++-++-++-++-++-++-++-++-++\u001b[0m\n")
    print("\u001b[32m1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Forest")
    print("6. Mountain\u001b[0m")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River()
        print('Your river was added to the arboretum!')
        input("Press enter to continue...")
        Arboretum.rivers.append(river)
    if choice == "2":
        swamp = Swamp()
        print('Your swamp was added to the arboretum!')
        input("Press enter to continue...")
        Arboretum.swamps.append(swamp)
    if choice == "3":
        coastline = Coastline()
        print('Your coastline was added to the arboretum!')
        input("Press enter to continue...")
        Arboretum.coastlines.append(coastline)
    if choice == "4":
        grassland = Grassland()
        print('Your grassland was added to the arboretum!')
        input("Press enter to continue...")
        Arboretum.grasslands.append(grassland)
    if choice == "5":
        forest = Forest()
        print('Your forest was added to the arboretum!')
        input("Press enter to continue...")
        Arboretum.forests.append(forest)
    if choice == "6":
        mountain = Mountain()
        print('Your mountain was added to the arboretum!')
        input("Press enter to continue...")
        Arboretum.mountains.append(mountain)
