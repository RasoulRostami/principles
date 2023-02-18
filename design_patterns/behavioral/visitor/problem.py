# Designing an HTML editor
import abc


class HTMLNode(abc.ABC):
    @abc.abstractmethod
    def highlighting(self):
        pass


class HeadingNode(HTMLNode):
    def highlighting(self):
        print("Heading highlighting")


class AnchorNode(HTMLNode):
    def highlighting(self):
        print("Anchor highlighting")


class HTMLDocument:
    def __init__(self) -> None:
        self.__nodes = []

    def add_node(self, node: HTMLNode):
        self.__nodes.append(node)

    def highlighting(self):
        for node in self.__nodes:
            node.highlighting()

    def click(self):
        pass


if __name__ == "__main__":
    heading = HeadingNode()
    anchor = AnchorNode()
    document = HTMLDocument()
    document.add_node(heading)
    document.add_node(anchor)

    document.highlighting()

# Problems
# 1. If we want to add a new operation like 'click' we need to add click method
# to HTMLNode interface and all subclasses, also we need to implement this method
# to HTMLDocument class and modifying our codes (so it is not open/close code and
# it means we need to write a lot of codes)
#
# 2. We separete operation algorithms between multi classes(HeadingNode, AncherNode)
