class Product:
    def __init__(self, name, price, quantity):
        """Initialize a product with name, price, and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"


class Shop:
    def __init__(self):
        """Initialize the shop with an empty product list."""
        self.products = []

    def add_product(self, product):
        """Add a product to the shop."""
        self.products.append(product)
        print(f"{product.name} added to the shop.")

    def buy_product(self, product_name, quantity):
        """Buy a product from the shop if available."""
        for product in self.products:
            if product.name == product_name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f"Congratulations! You successfully bought {quantity} {product_name}(s).")
                    return
                else:
                    print(f"Sorry, only {product.quantity} {product_name}(s) available.")
                    return
        print(f"Product {product_name} not found in the shop.")


# Example Usage
shop = Shop()

# Adding products
p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 50, 10)
shop.add_product(p1)
shop.add_product(p2)

# Buying products
shop.buy_product("Laptop", 2)
shop.buy_product("Mouse", 12)
shop.buy_product("Keyboard", 1)


class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def __str__(self):
        return f"Electronics(name={self.name}, price={self.price}, quantity={self.quantity}, warranty={self.warranty})"

# Example Usage
e1 = Electronics("TV", 500, 3, "2 years")
print(e1)
