"""
Design application that can export value as PDF, Movie and etc
"""
from abc import ABC, abstractmethod


class Slide:
    def __init__(self, text) -> None:
        self.text = text


# exporter
class Movie:
    def __init__(self) -> None:
        self.frames = []

    def add_frame(self, slide, duration):
        self.frames.append(slide)
        print("add frame")


class PDFDocument:
    def __init__(self) -> None:
        self.pages = []

    def add_page(self, slide):
        self.pages.append(slide)
        print("add page")


# Builder
class Builder(ABC):
    @abstractmethod
    def add_slide(self, slide: Slide):
        pass


class MovieBuilder(Builder):
    def __init__(self) -> None:
        self.movie = Movie()

    def add_slide(self, slide: Slide):
        self.movie.add_frame(slide, 3)

    def get_movie(self):
        print("Movie export")


class PDFBuilder(Builder):
    def __init__(self) -> None:
        self.pdf = PDFDocument()

    def add_slide(self, slide: Slide):
        self.pdf.add_page(slide)

    def get_pdf(self):
        print("PDF export")


class Presentation:
    def __init__(self) -> None:
        self.list_of_slide = []

    def add_slice(self, slide: Slide):
        self.list_of_slide.append(slide)

    def export(self, builder: Builder):
        for slide in self.list_of_slide:
            builder.add_slide(slide)


if __name__ == "__main__":
    p = Presentation()
    p.add_slice(Slide("HI"))
    p.add_slice(Slide("Good Morning"))

    movie_builder = MovieBuilder()
    p.export(movie_builder)
    movie_builder.get_movie()

    pdf_builder = PDFBuilder()
    p.export(pdf_builder)
    pdf_builder.get_pdf()
