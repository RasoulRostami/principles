# Design image upload API
class Image:
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

        print(f"image: {image_name} saved")


if __name__ == "__main__":
    img = Image("JPEG", "Tokyo")
    img.save("a")


# Problem:
# We need to save an uploaded image, but before saving we need to do some changes. like compress,
# add filter, resize and so on.
# If one class do all this thing, the class violate single responsibility principle. and this class
# will not be extensible and maintainable easily. we need to have better implementation
