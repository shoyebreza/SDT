from abc import ABC, abstractmethod

class Account(ABC):
    accounts = []

    def __init__(self, name, accNo, password, acc_type):
        self.name = name
        self.accNo = accNo
        self.password = password
        self.type = acc_type
        self.balance = 0  # Initialize balance to 0
        Account.accounts.append(self)

    # Single changeInfo method with default argument
    def changeInfo(self, newName, newPass=None):
        self.name = newName
        if newPass:
            self.password = newPass  # Update password if provided
        print(f"Name changed to {newName}.")
        if newPass:
            print(f"Password changed.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount  # Subtract amount for withdrawal
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    @abstractmethod
    def showinfo(self):
        pass


class SavingAccount(Account):
    def __init__(self, name, accNo, password, limit):
        super().__init__(name, accNo, password, "Savings")
        self.limit = limit

    def showinfo(self):
        print(f"Account name : {self.name}")
        print(f"Account type : {self.type}")


class SpecialAccount(Account):

    def __init__(self, name, accNo, password, limit):
        super().__init__(name, accNo, password, "Special")
        self.limit = limit

    def showinfo(self):
        print(f"Account name : {self.name}")
        print(f"Account type : {self.type}")


# Example usage:
myAcc = SavingAccount("Rayon", 1234, "password123", 5000)  # Create a SavingAccount
myAcc.changeInfo("Tazul")  # Change name only
myAcc.changeInfo("Tazul", "newpassword456")  # Change name and password
myAcc.deposit(500)  # Deposit money
myAcc.withdraw(200)  # Withdraw money
myAcc.showinfo()  # Show account information
