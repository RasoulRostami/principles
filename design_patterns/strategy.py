"""
Description:
Strategy is a design pattern that help us to handle different strategy of a class easily
and implement maintainable and extensible application and implement open/close and single responsibly
principles.

Problem:
We need to save an uploaded image, but before saving we need to do some changes. like compress,
add filter, resize and other.
If one class do all this thing, the class violate single responsibility principle. and this class
will not be extensible and maintainable easily. we need to have better implementation
"""


class Image0:
    def __init__(self, compressor: str, layout: str) -> None:
        self.compressor = compressor
        self.layout = layout

    def save(self, image_name: str):
        if self.compressor == "JPEG":
            print("JPEG compressing")
        elif self.compressor == "PNG":
            print("PNG compressing")

        if self.layout == "BlackAndWhite":
            print("Black and white filter")
        elif self.layout == "Tokyo":
            print("Tokyo filter")

        print(f"{image_name} saved")


print("============ Normal codes ============")
img0 = Image0("JPEG", "Tokyo")
img0.save("a")

# As you see this is awful and spaghetti code.
# Now let's go use Strategy design patterns


import abc


class Compressor(abc.ABC):
    @abc.abstractmethod
    def compress(self):
        pass


class PNGCompressor(Compressor):
    def compress(self):
        print("PNG compresses")


class JPEGCompressor(Compressor):
    def compress(self):
        print("JPEG compresses")


class Filtering(abc.ABC):
    @abc.abstractmethod
    def filtering(self):
        pass


class BlackWhite(Filtering):
    def filtering(self):
        print("Back and white filter")


class Tokyo(Filtering):
    def filtering(self):
        print("Tokyo filter")


class Image:
    def __init__(self, compressor: Compressor, filtering: Filtering) -> None:
        self.compressor = compressor
        self.filtering = filtering

    def save(self, image_name):
        self.compressor.compress()
        self.filtering.filtering()
        print(f"{image_name} saved")


print("====================== Strategy Design pattern example 1")
img = Image(PNGCompressor(), Tokyo())
img.save("b")
# is it clean, isn't it?
# In te above code we use polymorphous, Single responsibility and open/close principle
# we can write image class and save method with other way


class Picture:
    def save(self, image_name: str, compressor: Compressor, filtering: Filtering):
        compressor.compress()
        filtering.filtering()
        print(f"{image_name} saved")


print("====================== Strategy Design pattern example 2")
pic = Picture()
pic.save("c", JPEGCompressor(), BlackWhite())
# strategy vs state design pattern
# If you see strategy and state design pattern UML, they are same
# so what is different?
#
# In State we have one current state, and all behavior are presents by sub classes of Tools
# But in Strategy we haven't an state and we have different behavior that present we different strategy objects
