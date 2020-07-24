import os
from environments import River
from arboretum import Arboretum


def annex_habitat(Arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("+-++-++-++-++-++-++-++-++-++-++-++")
    print("+ C H O O S E  A  H A B I T A T +")
    print("+-++-++-++-++-++-++-++-++-++-++-++")
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    print("5. Forest")
    print("6. Mountain")

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River()
        Arboretum.rivers.append(river)
    if choice == "2":
        pass
