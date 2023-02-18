# Design Django signals

## framework layer
from abc import ABC, abstractmethod
from typing import Callable


class Signal(ABC):
    def __init__(self) -> None:
        self._receivers = []

    def add_receiver(self, receiver: Callable):
        self._receivers.append(receiver)

    def remove_receiver(self, receiver: Callable):
        self._receivers.remove(receiver)

    @abstractmethod
    def publish(self, obj):
        pass


class ModelSignal(Signal):
    def publish(self, model):
        for receiver in self._receivers:
            receiver(model.__class__.__name__, model)


post_save = ModelSignal()


class Model(ABC):
    # Called 'publisher' in design patterns books
    def __init__(self) -> None:
        self.__post_signals = post_save

    def write_in_db(self):
        pass

    def save(self):
        self.write_in_db()
        self.__post_signals.publish(self)


### aplication layer
class Student(Model):
    def __init__(self, name) -> None:
        super().__init__()
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


def change_logs(sender, obj, *args):
    print("Model {} is changed".format(sender))


def send_mail(sender, obj, *args):
    print("send mail to {}".format(obj.name))


post_save.add_receiver(change_logs)
post_save.add_receiver(send_mail)

if __name__ == "__main__":
    studnt = Student("John")
    studnt.save()
    studnt.name = "Tom"
    studnt.save()
