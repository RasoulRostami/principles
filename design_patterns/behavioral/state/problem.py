# Design a canvas application
from enum import Enum


class ToolType(Enum):
    BRUSH = 1
    SELECTION = 2
    ERASER = 3


class Canvas:
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


if __name__ == "__main__":
    canvas = Canvas()
    canvas.current_tool = ToolType.BRUSH
    canvas.mouse_up()
    canvas.mouse_down()

# --------------------------- Problems
# There will be some problems,
# 1. If you implement app like above you might have got many dublicate code.
# 2. It is hard to maintenance. we have lots of code, and too many duplicate codes and conditions
# 3. this code is not extensible, When you want to add a new tool you need to modify all methods
