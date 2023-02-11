# Design upload image API
import abc


class Compressor(abc.ABC):
    # Called 'route strategy' in design pattern books
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
    # Called 'route strategy' in books
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
    # Called 'Navigator' in design pattern books
    def __init__(self, compressor: Compressor, filtering: Filtering) -> None:
        self.compressor = compressor
        self.filtering = filtering

    def save(self, image_name):
        self.compressor.compress()
        self.filtering.filtering()
        print(f"image: {image_name} saved")


# Or we can do
class Picture:
    def save(self, image_name: str, compressor: Compressor, filtering: Filtering):
        compressor.compress()
        filtering.filtering()
        print(f"{image_name} saved")


if __name__ == "__main__":
    img = Image(PNGCompressor(), Tokyo())
    img.save("b")

    pic = Picture()
    pic.save("c", JPEGCompressor(), BlackWhite())
