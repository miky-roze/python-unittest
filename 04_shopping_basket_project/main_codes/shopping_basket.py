from main_codes.product import Product


class ShoppingBasket:

    def __init__(self):
        self.products = list()

    def __len__(self):
        return sum([product.quantity for product in self.products])

    def add_product(self, name, price, quantity=1):
        for product in self.products:
            if product.name == name:
                product.quantity += 1
                return self

        self.products.append(Product(name, price, quantity))
        return self

    def get_product(self, index):
        return self.products[index]

    def total(self, tax=21):
        netValue = sum([product.price * product.quantity for product in self.products])

        return round(netValue * (1 + tax / 100), 2)

    def display(self):
        print('In the basket:')
        for product in self.products:
            print('\t', product)
