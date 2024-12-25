

from abc import ABC

class User(ABC):
    def __init__(self,name,email,nid)->None:
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0


    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self,name,email,nid,cuerrent_location,initial_amount)->None:
        super().__init__(name,email,nid)
        self.cuerrent_ride = None
        self.wallet = initial_amount
        self.cuerrent_location = cuerrent_location

    def display_profile(self):
        print(f" Rider : {self.name} and email : {self.email}")


    def load_cash(self,amount):
        if amount >0:
            self.wallet +=amount
        else:
            print("Invalid amount")

    def update_location(self,cuerrent_location):
        self.cuerrent_location = cuerrent_location


    def request_ride(self,ride_sharing,destination):
        pass


    def show_current_ride(self):
        print(self.cuerrent_ride)


class Driver(User):
    def __init__(self,name,email,nid,cuerrent_location)->None:
        super().__init__(name,email,nid)
        self.cuerrent_location = cuerrent_location
        self.wallet = 0

    def display_profile(self):
        print(f"Driver name : {self.name}")

    def accept_ride(self,ride):
        pass