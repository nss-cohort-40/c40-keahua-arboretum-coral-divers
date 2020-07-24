def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(f'River [{river.id}]')
    for swamp in arboretum.swamps:
        print(f'Swamp [{swamp.id}]')
    for coastline in arboretum.coastlines:
        print(f'Coastline [{coastline.id}]')
    for grassland in arboretum.grasslands:
        print(f'Grassland [{grassland.id}]')
    for forest in arboretum.forests:
        print(f'Forest [{forest.id}]')
    for mountain in arboretum.mountains:
        print(f'Mountain [{mountain.id}]')
        for plant in mountain.plants:
            print(f'     {plant} [{plant.id}]')

    input("\n\nPress any key to continue...")
