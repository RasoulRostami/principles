"""
Description:
We use observer design pattern when state of object changes and we want to notify other objects about thins changes.

Program:
Imagine we have designed zoo applcation, what happend in the morning and at night?
look at the examlpe
"""


class Animal:
    state = "wake-up"

    def update(self):
        if self.state == "sleep":
            self.state = "wake-up"
        elif self.state == "wake-up":
            self.state = "sleep"


class Lion(Animal):
    pass


class Owl(Animal):
    state = "sleep"


class Sheep(Animal):
    pass


lion = Lion()
owl = Owl()
sheep = Sheep()


class Day:
    def morning(self):
        lion.update()
        sheep.update()
        owl.update()

    def night(self):
        lion.update()
        sheep.update()
        owl.update()


print("===================== without Observer")
day = Day()
day.night()
print(lion.state)
print(sheep.state)
print(owl.state)
# Problem:
# As you see we have got duplicate codes and many coupling


# implement by Observer
import abc


class Observer(abc.ABC):
    # called 'subscriber' in books
    @abc.abstractmethod
    def update(self):
        pass


class Chart(Observer):
    def update(self):
        print("Chart Updated")


class SpreadSheet(Observer):
    def update(self):
        print("Spread Sheet Updated")


class Subject:
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
    # called 'subject' or 'Publisher' is books
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


print("====================== with oberser design pattern")
data = DataSource()
spread_sheet = SpreadSheet()
chart = Chart()
data.add_observer(spread_sheet)
data.add_observer(chart)
data.value = 20

# send object new state to observers
# Comiunicate style (Push method)
class ObserverV2(abc.ABC):
    # called 'subscriber' in books
    @abc.abstractmethod
    def update(self, new_value):
        pass


class ChartV2(ObserverV2):
    def update(self, new_value):
        print(f"ChartV2 Updated new value {new_value}")


class SpreadSheetV2(ObserverV2):
    def update(self, new_value):
        print(f"Spread Sheet Updated new vlue {new_value}")


class SubjectV2:
    def __init__(self) -> None:
        self.__observers = []

    def add_observer(self, observer: ObserverV2):
        self.__observers.append(observer)

    def remove_observer(self, observer: ObserverV2):
        self.__observers.remove(observer)

    def notify(self, new_value):
        for observer in self.__observers:
            observer.update(new_value)


class DataSourceV2(SubjectV2):
    # called 'subject' or 'Publisher' is books
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.notify(value)


print("====================== with oberser design pattern, Push method cominucation")
data_v2 = DataSourceV2()
spread_sheet_v2 = SpreadSheetV2()
chart_v2 = ChartV2()
data_v2.add_observer(spread_sheet_v2)
data_v2.add_observer(chart_v2)
data_v2.value = 20


# pull Style
# we get data from object directly, if we need new attr we needn't to add new prometers to update methods and modify codes
class ObserverV3(abc.ABC):
    # called 'subscriber' in books
    def __init__(self, data_source) -> None:
        self.data_source = data_source

    @abc.abstractmethod
    def update(self):
        pass


class ChartV3(ObserverV3):
    def update(self):
        print(f"ChartV3 Updated new value {self.data_source.value}")


class SpreadSheetV3(ObserverV3):
    def update(self):
        print(f"Spread Sheet Updated new vlue {self.data_source.value}")


class SubjectV3:
    def __init__(self) -> None:
        self.__observers = []

    def add_observer(self, observer: ObserverV3):
        self.__observers.append(observer)

    def remove_observer(self, observer: ObserverV3):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update()


class DataSourceV3(SubjectV3):
    # called 'subject' or 'Publisher' is books
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


print("====================== with oberser design pattern, Push method cominucation")
data_v3 = DataSourceV3()
spread_sheet_v3 = SpreadSheetV3(data_v3)
chart_v3 = ChartV3(data_v3)
data_v3.add_observer(spread_sheet_v3)
data_v3.add_observer(chart_v3)
data_v3.value = 30

# we can send data-source object as parameter to update method directlry
class ObserverV4(abc.ABC):
    # called 'subscriber' in books
    @abc.abstractmethod
    def update(self, obj):
        pass


class ChartV4(ObserverV4):
    def update(self, obj):
        print(f"ChartV4 Updated new value {obj.value}")


class SpreadSheetV4(ObserverV4):
    def update(self, obj):
        print(f"Spread Sheet Updated new vlue {obj.value}")


class SubjectV4:
    def __init__(self) -> None:
        self.__observers = []

    def add_observer(self, observer: ObserverV4):
        self.__observers.append(observer)

    def remove_observer(self, observer: ObserverV4):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update(self)


class DataSourceV4(SubjectV4):
    # called 'subject' or 'Publisher' is books
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


print("====================== with oberser design pattern, Push method cominucation")
data_v4 = DataSourceV4()
spread_sheet_v4 = SpreadSheetV4()
chart_v4 = ChartV4()
data_v4.add_observer(spread_sheet_v4)
data_v4.add_observer(chart_v4)
data_v4.value = 40
