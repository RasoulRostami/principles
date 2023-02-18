from abc import ABC, abstractmethod


class Device(ABC):
    # called 'device' in books
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_channel(self):
        pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass


class RemoteInterface(ABC):
    def __init__(self, device: Device) -> None:
        self.device = device


class Remote(RemoteInterface):
    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()


class AdvanceRemote(RemoteInterface):
    # called 'client' in books
    def set_channel(self):
        self.device.set_channel()


class MovieRemote(RemoteInterface):
    def play(self):
        self.device.play()

    def pause(self):
        self.device.pause()


# Implement remote for sony
class SonyRemote(Device):
    def turn_on(self):
        print("Turn on sony TV")

    def turn_off(self):
        print("Turn off sony TV")

    def set_channel(self):
        print("set channel sony TV")

    def play(self):
        print("play video in sony TV")

    def pause(self):
        print("pause video in sony TV")


if __name__ == "__main__":
    sony = SonyRemote()
    ad_sony = AdvanceRemote(sony)
    mo_sony = MovieRemote(sony)

    sony.turn_on()
    ad_sony.set_channel()
    mo_sony.play()

    # Now when we add new TV Brand we only need one class
    # And when we add new type of remote we only need one class
