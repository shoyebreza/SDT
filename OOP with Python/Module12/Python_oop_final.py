from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
        self.balance = 0
        self.order_history = []

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item not available!")
            else:
                self.cart.add_item(item, quantity)
                print("Item added to cart.")
        else:
            print("Item not found.")

    def pay_bill(self):
        total = self.cart.total_price
        if self.balance >= total:
            self.balance -= total
            self.order_history.append(self.cart.items.copy())
            self.cart.clear()
            print(f"Amount : {total} paid successfully. balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def add_funds(self, amount):
        self.balance += amount
        print(f"Amount : {amount} added. Current balance: {self.balance}")

    def view_order_history(self):
        print("**Order History**")
        for i, order in enumerate(self.order_history, 1):
            print(f"Order {i}:")
            for item, qty in order.items():
                print(f"  {item.name} - {qty} x {item.price}")
        if not self.order_history:
            print("Cart is empty!.")


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_customer(self, restaurant, customer):
        restaurant.add_customer(customer)

    def remove_customer(self, restaurant, customer_email):
        restaurant.remove_customer(customer_email)

    def view_customers(self, restaurant):
        restaurant.view_customers()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def update_item(self, restaurant, item_name, new_price, new_quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            item.price = new_price
            item.quantity = new_quantity
            print(f"Item : '{item_name}' updated!!.")
        else:
            print("Item not found.")

    def remove_item(self, restaurant, item_name):
        restaurant.menu.remove_item(item_name)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer_email):
        for customer in self.customers:
            if customer.email == customer_email:
                self.customers.remove(customer)
                print(f"Customer '{customer.name}' removed.")
                return
        print("Customer not found.")

    def view_customers(self):
        print("**Customer List**")
        for customer in self.customers:
            print(f"{customer.name} - {customer.email}")


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def clear(self):
        self.items.clear()

    @property
    def total_price(self):
        return sum(item.price * qty for item, qty in self.items.items())


class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"Item : {item_name} removed.")
        else:
            print("Item not found.")

    def show_menu(self):
        print("**Menu**")
        print("Name - Price - Qty")
        for item in self.items:
            print(f"{item.name} - {item.price} - {item.quantity}")

def customer_menu(restaurant):
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    customer = Customer(name, phone, email, address)
    restaurant.add_customer(customer)

    while True:
        print(f"\nWelcome {customer.name}!")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Add Funds")
        print("6. View Order")
        print("7. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer.view_menu(restaurant)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            customer.add_to_cart(restaurant, item_name, quantity)
        elif choice == 3:
            customer.cart.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            amount = float(input("Enter Amount to Add: "))
            customer.add_funds(amount)
        elif choice == 6:
            customer.view_order_history()
        elif choice == 7:
            break
        else:
            print("Invalid Input!")


def admin_menu(restaurant):
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")
    admin = Admin(name, phone, email, address)

    while True:
        print(f"\nWelcome Admin {admin.name}!")
        print("1. Add New Item to Menu")
        print("2. Update Item in Menu")
        print("3. Remove Item from Menu")
        print("4. View Menu")
        print("5. Add New Customer")
        print("6. Remove Customer")
        print("7. View All Customers")
        print("8. Exit")

        choice = int (input("Enter Your Choice: "))
        if choice == 1:
            item_name = input("Enter Item Name: ")
            item_price = float(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(restaurant, item)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            new_price = float(input("Enter New Price: "))
            new_quantity = int(input("Enter New Quantity: "))
            admin.update_item(restaurant, item_name, new_price, new_quantity)
        elif choice == 3:
            item_name = input("Enter Item Name: ")
            admin.remove_item(restaurant, item_name)
        elif choice == 4:
            admin.view_menu(restaurant)
        elif choice == 5:
            customer_name = input("Enter Customer Name: ")
            customer_email = input("Enter Customer Email: ")
            customer_phone = input("Enter Customer Phone: ")
            customer_address = input("Enter Customer Address: ")
            customer = Customer(customer_name, customer_phone, customer_email, customer_address)
            admin.add_customer(restaurant, customer)
        elif choice == 6:
            customer_email = input("Enter Customer Email to Remove: ")
            admin.remove_customer(restaurant, customer_email)
        elif choice == 7:
            admin.view_customers(restaurant)
        elif choice == 8:
            break
        else:
            print("Invalid Input!")


def main():
    restaurant = Restaurant("Amar Restaurant")

    while True:
        print("\nWelcome to Amar Restaurant!")
        print("1. Customer Menu")
        print("2. Admin Menu")
        print("3. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            customer_menu(restaurant)
        elif choice == 2:
            admin_menu(restaurant)
        elif choice == 3:
            print("Thank you for visiting Amar Restaurant!")
            break
        else:
            print("Invalid Input!")


main()

