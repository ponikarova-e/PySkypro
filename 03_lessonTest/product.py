class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_Name(self):
        return self.name

    def get_Price(self):
        return self.price

    def get_NamePrice(self):
        return f"Product: {self.name}, Price: {self.price}"
