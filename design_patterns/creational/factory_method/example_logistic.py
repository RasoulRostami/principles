from abc import ABC, abstractmethod


class Transaction(ABC):
    @abstractmethod
    def delivery(self):
        pass


class Truck(Transaction):
    def delivery(self):
        print("truck delivery")


class Ship(Transaction):
    def delivery(self):
        print("ship delivery")


class Logistic(ABC):
    def delivery(self):
        plan = self.delivery_plan()
        plan.delivery()

    @abstractmethod
    def delivery_plan() -> Transaction:
        pass


class RoadLogistic(Logistic):
    def delivery_plan(self) -> Transaction:
        return Truck()


class SeaLogistic(Logistic):
    def delivery_plan(self) -> Transaction:
        return Ship()


if __name__ == "__main__":
    logistic = RoadLogistic()
    logistic.delivery()

    logistic = SeaLogistic()
    logistic.delivery()

    # Add new trasport by developer

    class Airplan(Transaction):
        def delivery(self):
            print("Airplane delivery")

    class AirLogistic(Logistic):
        def delivery_plan(self) -> Transaction:
            return Airplan()

    logistic = AirLogistic()
    logistic.delivery()
