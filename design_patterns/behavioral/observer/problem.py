# Design sheet application
class Chart:
    def update_chart(self):
        print("Chart Updated")


class SpreadSheet:
    def update_spread(self):
        print("Spread Sheet Updated")


class DataSource:
    def __init__(self) -> None:
        self.__value = None
        self.chart = Chart()
        self.spread = SpreadSheet()

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        # notify and update other objects
        self.chart.update_chart()
        self.spread.update_spread()


if __name__ == "__main__":
    data = DataSource()
    data.value = 20

# As you see firstly we can notify and update other objects easily
# But when we need to add new objects we should modify our codes
# so it is not 'open/close'.
# secondly we violate 'single principal', DataSource is responsible for updating value and
# notifying other objects
# above all this is not extensible easily and our DataSource method will be fat in the future.
