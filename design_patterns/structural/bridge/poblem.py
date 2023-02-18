# developing universal mobile remote control
# Application have some kind of remote,
# Basic remote -> turn on, turn off
# Advance remote -> set channel
# Movie remote -> play, pause and etc
from abc import ABC, abstractmethod


class Remote(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class AdvanceRemote(ABC):
    @abstractmethod
    def set_channel(self):
        pass


class MovieRemote(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass


# Implement remote for sony
class SonyRemote(Remote):
    def turn_on(self):
        print("Turn on sony TV")

    def turn_off(self):
        print("Turn off sony TV")


class SonyAdvanceRemote(AdvanceRemote):
    def set_channel(self):
        print("set channel sony TV")


class SonyMovieRemote(MovieRemote):
    def play(self):
        print("play video in sony TV")

    def pause(self):
        print("pause video in sony TV")


if __name__ == "__main__":
    sony = SonyRemote()
    ad_sony = SonyAdvanceRemote()
    mo_sony = SonyMovieRemote()

    sony.turn_on()
    ad_sony.set_channel()
    mo_sony.play()

    # problem
    # We we add new TV Brand we need to add three classes
    # If we have new type of remote we need to implement new class for each brand
    # It is very inlexible.
