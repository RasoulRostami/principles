# Designing HTML editor
import abc


class Operation(abc.ABC):
    # Is called `Visitor` in design pattern books
    # Note: In Java language we can use method overloading to implement thin design pattern
    # Note: We need this interface otherwise we will forget implement methods for all elements
    @abc.abstractmethod
    def heading_execute(self):
        pass

    @abc.abstractmethod
    def anchor_execute(self):
        pass


class Highlighting(Operation):
    # Highlighting operation
    def heading_execute(self):
        print("Heading higlighting")

    def anchor_execute(self):
        print("anchor higlighting")


class Click(Operation):
    # Click Operation
    def heading_execute(self):
        print("Heading click")

    def anchor_execute(self):
        print("anchor click")


class HTMLNode(abc.ABC):
    # Is called 'Element' in design pattern books
    @abc.abstractmethod
    def execute(self, operation: Operation):
        pass


class AnchorNode(HTMLNode):
    def execute(self, operation: Operation):
        operation.anchor_execute()


class HeadingNode(HTMLNode):
    def execute(self, operation: Operation):
        operation.heading_execute()


class HTMLDocument:
    def __init__(self) -> None:
        self.__nodes = []

    def add_node(self, node: HTMLNode):
        self.__nodes.append(node)

    def execute(self, operation: Operation):
        for node in self.__nodes:
            node.execute(operation)


if __name__ == "__main__":
    heading = HeadingNode()
    anchor = AnchorNode()
    document = HTMLDocument()
    document.add_node(heading)
    document.add_node(anchor)

    document.execute(Highlighting())

    # Now we gather all operation logic in one object
    # When we need to add new operation, all thing we do is create new operation class and instance
    document.execute(Click())
