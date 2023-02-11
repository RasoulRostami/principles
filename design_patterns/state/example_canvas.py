# Design canvas application
from abc import ABC, abstractmethod


class Tool(ABC):
    # called "State" interface in books
    @abstractmethod
    def mouse_up(self):
        pass

    @abstractmethod
    def mouse_down(self):
        pass


class Brush(Tool):
    # called "CreateStateA" in books
    def mouse_up(self):
        print("This is brush")

    def mouse_down(self):
        print("Draw a black line")


class Selection(Tool):
    # called "CreateStateB" in books
    def mouse_up(self):
        print("This is selection")

    def mouse_down(self):
        print("Draw a rectangle")


class Canvas:
    # called "Context" in books
    def __init__(self) -> None:
        self.__tool = None

    @property
    def tool(self) -> Tool:
        return self.__tool

    @tool.setter
    def tool(self, tool: Tool):
        self.__tool = tool

    def mouse_up(self):
        self.tool.mouse_up()

    def mouse_down(self):
        self.tool.mouse_down()


# create new tool
class Eraser(Tool):
    # called "CreateStateB" in books
    def mouse_up(self):
        print("This is eraser")

    def mouse_down(self):
        print("erase a line")


if __name__ == "__main__":
    canvas = Canvas()
    canvas.tool = Brush()
    canvas.mouse_up()
    canvas.mouse_down()

    # These code is extensible easy, for example we want to add eraser tool
    print("------------ Add a new tool")

    canvas.tool = Eraser()
    canvas.mouse_up()
    canvas.mouse_down()

    # As you see this code is extensible easy without modifying
    # this is called "Open/Close principle"
    # mean this is open to extention and close to modification
