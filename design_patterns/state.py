"""
Description:
State design patterns is used when we have multi state in our application which have different behavior

Problems:
Imagine we want to implement photoshop application, in photoshop we have diffrent tools which have different behavior
when we mouse up or mouse down. how shall we handle them?

Example:
We will implement Canvas application with invalid pattern and then we will fix the problems

Note:
You will see (Open Close principle) in these example
"Open to extention, close for modification"
"""
from enum import Enum


class ToolType(Enum):
    BRUSH = 1
    SELECTION = 2
    ERASER = 3


class Canvas0:
    def __init__(self) -> None:
        self.current_tool = None

    def mouse_up(self):
        if self.current_tool == ToolType.BRUSH:
            print("This is brush")
        elif self.current_tool == ToolType.SELECTION:
            print("This is selection")
        elif self.current_tool == ToolType.ERASER:
            print("This is eraser")

    def mouse_down(self):
        if self.current_tool == ToolType.BRUSH:
            print("Draw a black line")
        elif self.current_tool == ToolType.SELECTION:
            print("Draw a rectangle")
        elif self.current_tool == ToolType.ERASER:
            print("Erase the line")


print("------------ Canvas incorrect implementation")
canvas0 = Canvas0()
canvas0.current_tool = ToolType.BRUSH
canvas0.mouse_up()
canvas0.mouse_down()

# --------------------------- Problems
# There will be some problems,
# 1. If you implement app like above you may doblicate this code in defferent places (Violation DRY)
# 2. It is hard to maintenance. we have lots of code, and too many duplicate codes
# 3. this code is not extensible, When you want to add a new tool you need to modify all methods

# --------------------------- State Design pattern
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


print("------------ Canvas correct implementation")
canvas = Canvas()
canvas.tool = Brush()
canvas.mouse_up()
canvas.mouse_down()

# These code is extensible easy, for example we want to add eraser tool
print("------------ Add a new tool")


class Eraser(Tool):
    # called "CreateStateB" in books
    def mouse_up(self):
        print("This is eraser")

    def mouse_down(self):
        print("erase a line")


canvas.tool = Eraser()
canvas.mouse_up()
canvas.mouse_down()

# As you see this code is extensible easy without modifying
# this is called "Open/Close principle"
# mean this is open to extention and close to modification
