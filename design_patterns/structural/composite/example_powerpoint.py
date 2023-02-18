from abc import abstractmethod, ABC


class Component(ABC):
    # Called 'component' in books
    @abstractmethod
    def move(self):
        pass


class Group(Component):
    # called 'composite' in books
    def __init__(self) -> None:
        self.nodes = []

    def add(self, node: Component):
        self.nodes.append(node)

    def move(self):
        for node in self.nodes:
            node.move()


class Square(Component):
    # called 'Leaf' in books
    def move(self):
        print("Moving squre")


class Circle(Component):
    # called 'Leaf' in books
    def move(self):
        print("Moving circle")


if __name__ == "__main__":
    s1 = Square()
    s2 = Square()
    c1 = Circle()
    c2 = Circle()

    group1 = Group()
    group1.add(s1)
    group1.add(s2)

    group2 = Group()
    group2.add(c1)
    group2.add(c2)

    group1.move()
    group2.move()

    print("---- main group ----")
    main_group = Group()
    main_group.add(group1)
    main_group.add(group2)
    main_group.move()

    # As you see there is no error or warning
