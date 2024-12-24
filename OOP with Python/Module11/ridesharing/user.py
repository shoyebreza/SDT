

from abc import ABC

class User(ABC):
    def __init__(self,name,email,nid)->None:
        self.wallet = 0


    @abstractmethod
    def display_profile(self):
        raise NotImplementedError


class Rider(User):
    def __init__(self,name,email,nid)->None:
        super().__init__(name,email,nid,current_location,):