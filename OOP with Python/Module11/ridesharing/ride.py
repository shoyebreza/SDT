
from datetime import datetime
class Ride:
    def __init__(self,start_location,end_location)->None:
        self.start_location= start_location
        self.end_location = end_location
        self.driver = None
        self.ride = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None


    def set_driver(self,driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self):
        return f"Ride Details started {self.start_location} to {self.end_location}"


class RideRequest:
    def __init__(self,rider,end_location)->None:
        self.rider = rider
        self.end_location = end_location


    def find_request(self,ride_request):
        if len(self.available_drivers)>0:
            print("Looking for driver .....")
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider,)
