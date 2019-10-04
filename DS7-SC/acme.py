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
