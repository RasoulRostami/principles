from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def clone(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int = 0) -> None:
        self.radius = radius

    def render(self):
        print(f"circle {self.radius}")

    def clone(self):
        return Circle(self.radius)


class Square(Shape):
    def __init__(self, width: int = 0, length: int = 0) -> None:
        self.width = width
        self.length = length

    def render(self):
        print(f"square {self.width} {self.length}")

    def clone(self):
        return Square(self.width, self.length)


class ContextMenu:
    def duplicate(self, shape: Shape) -> Shape:
        return shape.clone()


if __name__ == "__main__":
    circle = Circle(20)
    new = ContextMenu().duplicate(circle)
    circle.render()
    new.render()

# For soving problems, we add clone method in Shape interface.
