# We have and application like power-point, we need a group of objects and treat the same way
# Note: Dynamic type language like python and javascript don't encounter with this problem

import abc


class Node(abc.ABC):
    @abc.abstractmethod
    def move(self):
        pass


class Square(Node):
    def move(self):
        print("Moving squre")


class Circle(Node):
    def move(self):
        print("Moving circle")


class Group:
    def __init__(self) -> None:
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def move(self):
        for node in self.nodes:
            node.move()


if __name__ == "__main__":
    s1 = Square()
    s2 = Square()
    c1 = Circle()
    c2 = Circle()

    group1 = Group()
    group1.add_node(s1)
    group1.add_node(s2)

    group2 = Group()
    group2.add_node(c1)
    group2.add_node(c2)

    group1.move()
    group2.move()

    print("---- main group ----")
    main_group = Group()
    main_group.add_node(group1)
    main_group.add_node(group2)
    main_group.move()

    # As you see in python and other dynamic type language we have not any issue to implement this.
    # but in static type language like Jave in is not impossible.
    # - we can not add group instead of node in 'add_node'
    # - we can not run move method in group class
    # - and a few more issues
    # in the next implementation we will see how implement this in Java or other static language
