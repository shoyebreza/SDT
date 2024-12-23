
class Customer(User):
    def __init__(self, email, password, name, address):
        super().__init__(email, password)
        self.name = name
        self.address = address
        self.orders = []

    def view_products(self, products):
        available_products = [product for product in products if product.stock > 0]
        for product in available_products:
            print(f"{product.name} - ${product.price} - Stock: {product.stock}")

    def place_order(self, product, quantity):
        if product.stock >= quantity:
            product.stock -= quantity
            self.orders.append((product, quantity))
            print(f"Order placed: {product.name} x{quantity}")
        else:
            print(f"Not enough stock for {product.name}. Available: {product.stock}")
