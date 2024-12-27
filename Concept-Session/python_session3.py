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
        print(f"Music title : {self.title} duration : {self.duration} description : {self.get_description()}")


class Video(Media,Description):
    def __init__(self,title,duration,description):
        Media.__init__(self,title,duration)
        Description.__init__(self,description)

    def play(self):
        print(f"Video title : {self.title}")


    def info(self):
        print(f"Video title : {self.title} duration : {self.duration} description : {self.get_description()}")


class AudioBook(Media,Description):
    def __init__(self,title,duration,description):
        Media.__init__(self,title,duration)
        Description.__init__(self,description)

    def play(self):
        print(f"AudioBook title : {self.title}")


    def info(self):
        print(f"AudioBook title : {self.title} duration : {self.duration} description : {self.get_description()}")




class Library:
    def __init__(self):
        self.__media_items = []
        self.__media_by_genre = []


    def get_media_items(self):
        return self.__media_items

    def get_media_by_genre(self):
        return self.__media_by_genre

    def add_media(self,media):






music1 = Music("music1","3.45", "this is the music title ")
music2 = Music("music2","3.40", "this is the music title2 ")

music1.play()
music1.info()