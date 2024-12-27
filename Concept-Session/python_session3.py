from abc import ABC, abstractmethod


class Description:
    def __init__(self,description):
        self.__description = description

    def get_description(self):
        return self.__description


class Media(ABC):
    def __init__(self,title,duration):
        self.title = title
        self.duration = duration

    @abstractmethod
    def play(self):
        pass


class Music(Media,Description):
    def __init__(self,title,duration,description):
        Media.__init__(self,title,duration)
        Description.__init__(self,description)

    def play(self):
        print(f"Music title : {self.title}")


    def info(self):
        print(f"Music title : {self.title} duration : {self.duration} description : {self.get_descriptio()}")

music1 = Music("music1","3.45", "this is the music title ")

music1.play()
music1.info()