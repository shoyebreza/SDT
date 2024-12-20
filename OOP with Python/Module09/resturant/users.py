
# customer
# employee
# Admin


from abc import ABC

class User(ABC):
    def __init__(self,name,phone,email,address):
       self.name = name 
       self.phone = phone 
       self.email = email 
       self.address = address


class Employee(User):
    def __init__(self,name,email,phone,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self,name,email,phone,address):
        super().__init__(name,phone,email,address)
        self.employees = [] # eta hocche database

    def add_employee(self,Resturant,employee):
        Resturant.add_employee(employee)


    def view_employee(self,Resturant):
        Resturant.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self, restaurent, item):
        restaurent.menu.remove_item(item)
            

class Resturant:
    def __init__(self,name):
        self.name =name
        self.employees = [] # ata database
        self.menu = FoodItem

    def add_employee(self,employee):
        self.employees.append(employee)


    def view_employee(self):
        print("Employee List")
        for emp in employees:
            print(emp.name, emp.email, emp.phone, emp.address)





class Menu:
    def __init__(self):
        self.items =[] # items ar runtime database

    def add_menu_item(self,item):
        self.items.append(item)


    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None


    def remove_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("items not found")

    def show_menu(self):
        print("****Menu****")
        print("name\t price\t quantity")   
        for item in self.items:
            print(f"{item.name}\t {item.price}\t {item.quantity}")
    

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity