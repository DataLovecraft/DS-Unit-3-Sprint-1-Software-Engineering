from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sampel to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []

    for _ in range(num_products):
        name = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]

        prod = Product(name=name,
                       price=randint(5, 100),
                       weight=randint(5, 100),
                       flammability=uniform(0.0, 2.5))

        products.append(prod)

    return products

def inventory_report(products):

    num_prod = len(products)

    total_price, total_weight, total_flammability = 0, 0, 0
    for product in products:
        total_price += product.price
        total_weight += product.weight
        total_flammability += product.flammability

    avg_price = total_price / num_prod
    avg_weight = total_weight / num_prod
    avg_flammability = total_flammability / num_prod

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print("Unique product names:", len(set(products)))
    print("Average price:", avg_price)
    print("Average weight:", avg_weight)
    print("Average flammability:", avg_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())
