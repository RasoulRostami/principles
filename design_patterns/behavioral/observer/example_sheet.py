# Design sheet application
from abc import ABC, abstractmethod


class Observer(ABC):
    # Called 'Subscriber' in design pattern books
    @abstractmethod
    def update(self):
        pass


class Chart(Observer):
    def update(self):
        print("Chart updated")


class SpreadSheet(Observer):
    def update(self):
        print("Spread updated")


class Subject:
    # Called 'publisher' in design patterns books
    def __init__(self) -> None:
        self.__observers = []

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update()


class DataSource(Subject):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.notify()


if __name__ == "__main__":
    data = DataSource()
    data.add_observer(Chart())
    data.add_observer(SpreadSheet())
    data.value = "Hello"

# New when we need new observer, the only thig we do is create new class
# and add it to the publisher, without any modifying.
