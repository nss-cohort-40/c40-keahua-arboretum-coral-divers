def build_facility_report(arboretum):
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-")
    print("+ S E E  L I S T  O F  A N I M A L  A N D  +")
    print("+      B I O M E S  A V A I L A B L E      +")
    print("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-")
    for river in arboretum.rivers:
        print(f'River [{river.id}]')
        for animal in river.animals:
            print(f"      {animal.species}  [{animal.id}]")
        for plant in river.plants:
            print(f"      {plant.species}   [{plant.id}]")
    for swamp in arboretum.swamps:
        print(f'Swamp [{swamp.id}]')
        for animal in swamp.animals:
            print(f"      {animal.species}  [{animal.id}]")
        for plant in swamp.plants:
            print(f"      {plant.species}   [{plant.id}]")
    for coastline in arboretum.coastlines:
        print(f'Coastline [{coastline.id}]')
        for animal in coastline.animals:
            print(f"      {animal.species}  [{animal.id}]")
        for plant in coastline.plants:
            print(f"      {plant.species}   [{plant.id}]")
    for grassland in arboretum.grasslands:
        print(f'Grassland [{grassland.id}]')
        for animal in grassland.animals:
            print(f"      {animal.species}  [{animal.id}]")
        for plant in grassland.plants:
            print(f"      {plant.species}   [{plant.id}]")
    for forest in arboretum.forests:
        print(f'Forest [{forest.id}]')
        for animal in forest.animals:
            print(f"      {animal.species}  [{animal.id}]")
        for plant in forest.plants:
            print(f"      {plant.species}   [{plant.id}]")
    for mountain in arboretum.mountains:
        print(f'Mountain [{mountain.id}]')
        for animal in mountain.animals:
            print(f"      {animal.species}  [{animal.id}]")
        for plant in mountain.plants:
            print(f"      {plant.species}   [{plant.id}]")

    input("\n\nPress any key to continue...")
