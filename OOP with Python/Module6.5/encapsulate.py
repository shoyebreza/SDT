class Product:
    def __init__(self, name, price, quantity):
        self.name = name         # Public
        self._price = price      # Protected
        self.__quantity = quantity  # Private

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("Quantity cannot be negative.")

# Example Usage
p = Product("Phone", 800, 10)
print(p.name)            # Public: Accessible
print(p._price)          # Protected: Accessible but should be used carefully
print(p.get_quantity())  # Private: Accessible via getter
p.set_quantity(5)        # Modify private attribute via setter
print(p.get_quantity())
