import random

class Product:
    '''
    Acme Corporation product details

    Parameters
    ==========
    name : str
        name of the product
    price : int
        price of the product (default is 10)
    weight : int
        weight of the product (default is 20)
    flammability : float
        how flamable is the product (default is 0.5)
    identifier : int
        random identifier number

    '''

    # Part 1 - Keeping it Classy

    def __init__(self, name,
                       price=10,
                       weight=20,
                       flammability=0.5,
                       identifier=random.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    # part 2 - Objects that Go!

    def stealability(self):
        '''
        Identifies if a product is easy to steal based on weight
        '''
        steal = self.price / self.weight
        if steal < 0.5:
            return 'Not so stealable'
        elif (steal >= 0.5) & (steal < 1.0):
            return 'Kinda stealable'
        else:
            return 'Very stealable'

    def explode(self):
        '''
        calculates flammability times the weight
        '''
        boom = self.flammability * self.weight
        if boom < 10:
            return '...fizzle'
        elif (boom >= 10) & (boom < 50):
            return '...boom'
        else:
            return '...BABOOM'
