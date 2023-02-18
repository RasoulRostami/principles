# Design Sheet application.
from abc import ABC, abstractmethod
from typing import Any


class Observer(ABC):
    # Called 'Subscriber' in design pattern books
    @abstractmethod
    def update(self):
        pass


class Chart(Observer):
    def update(self, data_source: Any):
        print("Chart updated, new value is '{}'".format(data_source.value))


class SpreadSheet(Observer):
    def update(self, data_source: Any):
        print("Spread updated, new value is '{}'".format(data_source.value))


class Subject:
    # Called 'publisher' in design patterns books
    def __init__(self) -> None:
        self.__observers = []

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.__observers.remove(observer)

    def notify(self, data_source: Any):
        for observer in self.__observers:
            observer.update(data_source)


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
        self.notify(self)


if __name__ == "__main__":
    data = DataSource()
    data.add_observer(Chart())
    data.add_observer(SpreadSheet())
    data.value = "Hello"
