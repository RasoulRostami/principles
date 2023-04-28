"""
Imagin we want to develop an application like power-point
There are some shape and a context-menu by some options.
One of the options is duplicate object.
Now are implementing this option.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def render(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int = 0) -> None:
        self.radius = radius

    def render(self):
        print(f"circle {self.radius}")


class Square(Shape):
    def __init__(self, width: int = 0, length: int = 0) -> None:
        self.width = width
        self.length = length

    def render(self):
        print(f"square {self.width} {self.length}")


class ContextMenu:
    def duplicate(self, shape: Shape):
        if isinstance(shape, Circle):
            new_instance = Circle(shape.radius)
        elif isinstance(shape, Square):
            new_instance = Square(shape.width, shape.length)
        return new_instance


if __name__ == "__main__":
    circle = Circle(20)
    new = ContextMenu().duplicate(circle)
    circle.render()
    new.render()

# Problem
# As you see above code works correctly, But there are some issues.
# 1. Violate Open/Close principal. When we add new Shape we need to modify `duplicate` method.
# 2. There are coupling in ContextMenu class.
# 3. ContextMenu need lots of knowledge about Shapes.
