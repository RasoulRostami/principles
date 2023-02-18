# We are going to desing an image filter application.
from abc import ABC, abstractmethod


class Image:
    def __init__(self, path) -> None:
        self.path = path


class Filter(ABC):
    @abstractmethod
    def apply(self, img: Image):
        pass


class TokyoFilter(Filter):
    def apply(self, image: Image):
        print("Apply tokyo filter")


# we have implement a few of filters and now we want to use a library and add lots of filter to our
# application. but the library interface is like below

# --------- library
class VividFilter:
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


# How we can manage our codes, Shall we use different  interface
if __name__ == "__main__":
    image = Image("/tmp/a.png")

    tokyo = TokyoFilter()
    tokyo.apply(image)
    print("---------------")
    vivid = VividFilter()
    vivid.init(image)
    vivid.render()
