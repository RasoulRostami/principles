"""
Design logistic library.
"""


class Truck:
    def delivery(self):
        print("truck delivery")


class Logistic:
    def delivery(self):
        truch = Truck()
        truch.delivery()


if __name__ == "__main__":
    logistic = Logistic()
    logistic.delivery()

    # Add new transaction by other developer
    class Ship(Truck):
        def delivery(self):
            print("ship delivery")

    class SeaLogistic(Logistic):
        def delivery(self):
            truch = Ship()
            truch.delivery()

    logistic = SeaLogistic()
    logistic.delivery()


# Proble
# As you see the above problem works but there are some issue
# 1. Other developer can't add new transaction plan easily.
# 2. many duplicate code
# 3. increase risk of mistake
