
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

    def add_employee(self,name,email,phone,address):
        employee = Employee(name,email,phone,address) # employee class a object hoya jaba 
        self.employees.append(employee)
        print(f"{name} is added !!")


    def view_employee(self):
        print("Employee List")
        for emp in employees:
            print(emp.name, emp.email, emp.phone, emp.address)

            
