class Address:
    def __init__(self, index, citi, street, house, apartment):
        self.index = index
        self.citi = citi
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return (f"{self.index}, {self.citi}, {self.street},"
                f" {self.house}- {self.apartment}")
