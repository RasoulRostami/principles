from abc import ABC, abstractmethod


class Image:
    def __init__(self, path) -> None:
        self.path = path


# --------- library
class Vivid:
    # called 'service' in books
    def __init__(self) -> None:
        self.inited = False

    def init(self, image: Image):
        print("init vivid")
        self.inited = True

    def render(self):
        if self.inited:
            print("Apply Vivid Filter")
        else:
            raise ValueError()


# --------- Our codes


class Filter(ABC):
    # called 'existing class' in books
    @abstractmethod
    def apply(self, img: Image):
        pass


class TokyoFilter(Filter):
    def apply(self, image: Image):
        print("Apply tokyo filter")


class VividFilter(Filter):
    # called 'Adapter' in books
    def __init__(self) -> None:
        self.vivid = Vivid()

    def apply(self, image: Image):
        self.vivid.init(image)
        self.vivid.render()


# we have implement a few of filters and now we want to use a library and add lots of filter to our
# application. but the library interface is like below

# How we can manage our codes, Shall we use different  interface
if __name__ == "__main__":
    image = Image("/tmp/a.png")

    tokyo = TokyoFilter()
    tokyo.apply(image)
    print("---------------")
    vivid = VividFilter()
    vivid.apply(image)
