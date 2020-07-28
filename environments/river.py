from .biome import Biome


class River(Biome):

    def __init__(self):
        Biome.__init__(self, "River", 6, 1, "Fresh Water")

    def add_animal(self, animal):
        try:
            if len(self.animals) < self.animal_capacity:
                if hasattr(animal, 'is_euryhaline'):
                    self.animals.append(animal)
                    print(f'{animal.species} was added to the river!')
                    input('Please press enter to continue...')
                elif hasattr(animal, 'aquatic') and animal.cell_type == "hypertonic":
                    self.animals.append(animal)
                    print(f'{animal.species} was added to the river!')
                    input('Please press enter to continue...')
                else:
                    raise AttributeError(f'{animal.species} cannot live in a river!')
            else:
                # animal_accepted = False
                # return animal_accepted
                raise Exception('This river has already reached capacity!')
        except (AttributeError, Exception) as err:
            print(err)
            raise
            input('Press enter to continue')

    def add_plant(self, plant):
        try:
            if len(self.plants) < self.plant_capacity:
                if plant.freshwater and plant.requires_current:
                    self.plants.append(plant)
                    print(f'{plant.species} was added to the river!')
                    input('Press enter to continue...')
                else:
                    raise AttributeError('Plant cannot grow in the river!')
            else:
                raise AttributeError(
                    'River has already reached plant capacity!')
        except AttributeError as err:
            print(err)

            input('Press enter to continue...')

# def add_money(amount):
#     balance = 0
#     """Add money to a bank account

#     Arguments:
#       amount - A numerical value by which the bank account's balance will increase
#     """
#     try:
#         if amount >= 1:
#             balance += amount
#             print(f"Your deposit of ${round(float(balance), 2)} was successful")
#             return balance
#         else:
#             raise ArithmeticError("Amount needs to be a positive number")

#     except TypeError:
#         print('(Error): The add_money method requires a numeric value')
#         raise
#     except ArithmeticError as err:
#         print(f"Your deposit was not successful. Error: {err}")
#         raise

# add_money(0)