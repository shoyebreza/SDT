from abc import ABC, abstractmethod


class Description:
    def __init__(self, description):
        self.__description = description

    def get_description(self):
        return self.__description


class Media(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    @abstractmethod
    def play(self):
        pass


class Music(Media, Description):
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)

    def play(self):
        print(f"Music title: {self.title}")

    def info(self):
        print(f"Music title: {self.title} Duration: {self.duration} Description: {self.get_description()}")


class Video(Media, Description):
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)

    def play(self):
        print(f"Video title: {self.title}")

    def info(self):
        print(f"Video title: {self.title} Duration: {self.duration} Description: {self.get_description()}")


class AudioBook(Media, Description):
    def __init__(self, title, duration, description):
        Media.__init__(self, title, duration)
        Description.__init__(self, description)

    def play(self):
        print(f"AudioBook title: {self.title}")

    def info(self):
        print(f"AudioBook title: {self.title} Duration: {self.duration} Description: {self.get_description()}")


class Library:
    def __init__(self):
        self.__media_items = []
        self.__media_by_genre = {}

    def get_media_items(self):
        return self.__media_items

    def get_media_by_genre(self):
        return self.__media_by_genre

    def add_media(self, media):
        self.__media_items.append(media)
        genre = None

        if isinstance(media, Music):
            genre = "Music"
        elif isinstance(media, Video):
            genre = "Video"
        elif isinstance(media, AudioBook):
            genre = "AudioBook"

        if genre:
            if genre in self.__media_by_genre:
                self.__media_by_genre[genre].append(media)
            else:
                self.__media_by_genre[genre] = [media]


class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play_media(self):
        pass


class FreeUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genre = None

    def set_favourite_genre(self, genre):
        self.__favourite_genre = genre

    def play_media(self, library):
        if self.__favourite_genre and self.__favourite_genre in library.get_media_by_genre():
            for media in library.get_media_by_genre()[self.__favourite_genre]:
                media.play()


class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genre = ""

    def set_favourite_genre(self, genre):
        self.__favourite_genre = genre

    def get_favourite_genre(self):
        return self.__favourite_genre


# Sample usage
library = Library()
music1 = Music("Music 1", "3.55", "This is the music title description")
music2 = Music("Music 2", "4.55", "This is the music title description 2")
video1 = Video("Video 1", "4.55", "This is the video title description 1")
video2 = Video("Video 2", "4.55", "This is the video title description 2")
video3 = Video("Video 3", "4.55", "This is the video title description 3")

library.add_media(music1)
library.add_media(music2)
library.add_media(video1)
library.add_media(video2)
library.add_media(video3)

freeuser = FreeUser("Person 1")
freeuser.set_favourite_genre("Music")  # Set favorite genre for FreeUser
freeuser.play_media(library)

music1.play()
music1.info()
