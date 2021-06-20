class Product:

    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', price={self.price}, quantity={self.quantity})"
