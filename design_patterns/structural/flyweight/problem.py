# Developing a mobile map like google map
from enum import Enum


class PointType(Enum):
    COFFEE = 1
    SCHOOL = 2
    POLICE = 3


class Point:
    def __init__(self, x, y, type_, icon) -> None:
        self.x = x
        self.y = y
        self._type = type_
        self.icone = icon

    def draw(self):
        print(f"{self.x} {self.y} {self._type}")


class PointService:
    def __init__(self) -> None:
        self.points = []

    def add(self, point: Point):
        self.points.append(point)


if __name__ == "__main__":
    # get from db
    p1 = Point(1, 2, PointType.COFFEE, b"12312312312312313")
    p2 = Point(2, 2, PointType.COFFEE, b"12312312312312313")
    p3 = Point(3, 2, PointType.COFFEE, b"12312312312312313")
    p4 = Point(4, 2, PointType.COFFEE, b"12312312312312313")
    #
    point_service = PointService()
    point_service.add(p1)
    point_service.add(p2)
    point_service.add(p3)
    point_service.add(p4)

    for p in point_service.points:
        p.draw()

    # In real application we have got thousent of point and we add icon of points to
    # memory each time. all caffe point just have one icon, we can create one and load in
    # memory and use them in other caces
