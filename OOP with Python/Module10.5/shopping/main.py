from user import User
from customer import Customer
from seller import Seller,Product




class EShoppingApp:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []

    def create_customer_account(self, email, password):
        customer = Customer(email, password)
        self.customers.append(customer)
        print("Customer account created successfully.")
        return customer

    def create_seller_account(self, email, password):
        seller = Seller(email, password)
        self.sellers.append(seller)
        print("Seller account created successfully.")
        return seller

    def list_all_products(self):
        for product in self.products:
            if product.stock > 0:
                print(f"{product.name} - ${product.price} - Stock: {product.stock}")

    def list_all_customers(self):
        for customer in self.customers:
            print(f"Customer Email: {customer.email}")

# Example Usage
app = EShoppingApp()

def menu():
    while True:
        print("\nMenu:")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Add Product")
        print("4. View Products")
        print("5. Buy Product")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter customer email: ")
            password = input("Enter customer password: ")
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            app.create_customer_account(email, password, name, address)
        elif choice == "2":
            print("\nCustomers:")
            app.list_all_customers()
        elif choice == "3":
            email = input("Enter seller email: ")
            password = input("Enter seller password: ")
            seller = app.create_seller_account(email, password)
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            product = seller.publish_product(name, price, stock)
            app.products.append(product)
        elif choice == "4":
            print("\nAvailable Products:")
            app.list_all_products()
        elif choice == "5":
            email = input("Enter customer email: ")
            customer = next((c for c in app.customers if c.email == email), None)
            if customer:
                print("\nAvailable Products:")
                customer.view_products(app.products)
                product_name = input("Enter the product name to buy: ")
                quantity = int(input("Enter the quantity: "))
                product = next((p for p in app.products if p.name == product_name), None)
                if product:
                    customer.place_order(product, quantity)
                else:
                    print("Product not found.")
            else:
                print("Customer not found.")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
