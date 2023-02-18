from enum import Enum


class PointType(Enum):
    COFFEE = 1
    SCHOOL = 2
    POLICE = 3


class PointIcon:
    # called 'flyweight' in books
    # flyweight is shared data
    def __init__(self, type_, image) -> None:
        self._type = type_
        self.image = image


class PointIconFactory:
    # Called 'FlyweightFactory' in books
    def __init__(self) -> None:
        self.point_icon = {}

    def get_point(self, type_: str, image=b"323423424") -> PointIcon:
        if type_ not in self.point_icon:
            print("create point icon")
            self.point_icon[type_] = PointIcon(type_, image)

        return self.point_icon.get(type_)


class Point:
    # called 'content' in books
    def __init__(self, x, y, icon: PointIcon) -> None:
        self.x = x
        self.y = y
        self.icon = icon

    def draw(self):
        print(f"{self.x} {self.y} {self.icon._type} {self.icon.image}")


class PointService:
    def __init__(self) -> None:
        self.points = []

    def add(self, point: Point):
        self.points.append(point)


if __name__ == "__main__":
    # get from db
    factory = PointIconFactory()

    p1 = Point(1, 2, factory.get_point(PointType.COFFEE.value, b"123123131"))
    p2 = Point(2, 2, factory.get_point(PointType.COFFEE.value, b"123123131"))
    p3 = Point(3, 2, factory.get_point(PointType.COFFEE.value, b"123123131"))
    p4 = Point(4, 2, factory.get_point(PointType.COFFEE.value, b"123123131"))
    #
    point_service = PointService()
    point_service.add(p1)
    point_service.add(p2)
    point_service.add(p3)
    point_service.add(p4)

    for p in point_service.points:
        p.draw()

    # As you see we create one icon and use it many time and save the memory
