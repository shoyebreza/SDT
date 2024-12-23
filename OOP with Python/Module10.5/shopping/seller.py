
class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def publish_product(self, name, price, stock):
        product = Product(name, price, stock, self)
        self.products.append(product)
        return product

class Product:
    def __init__(self, name, price, stock, seller):
        self.name = name
        self.price = price
        self.stock = stock
        self.seller = seller
