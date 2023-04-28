"""
Design application that can export value as PDF, Movie and etc
"""
from enum import Enum


class ExportType(Enum):
    MOVIE = 1
    PDF = 2


class Slide:
    def __init__(self, text) -> None:
        self.text = text


class Movie:
    def __init__(self) -> None:
        self.frames = []

    def add_frame(self, slide, duration):
        self.frames.append(slide)

    def get_movie(self):
        print("Movie export")


class PDFDocument:
    def __init__(self) -> None:
        self.pages = []

    def add_page(self, slide):
        self.pages.append(slide)

    def get_pdf(self):
        print("PDF export")


class Presentation:
    def __init__(self) -> None:
        self.list_of_slide = []

    def add_slice(self, slide: Slide):
        self.list_of_slide.append(slide)

    def export(self, export_type: ExportType):
        if export_type == ExportType.MOVIE:
            movie = Movie()
            for slide in self.list_of_slide:
                movie.add_frame(slide, 3)
            return movie

        elif export_type == ExportType.PDF:
            pdf = PDFDocument()
            for slide in self.list_of_slide:
                pdf.add_page(slide)
            return pdf


if __name__ == "__main__":
    p = Presentation()
    p.add_slice(Slide("HI"))
    p.add_slice(Slide("Good Morning"))

    result = p.export(ExportType.MOVIE)
    result.get_movie()

    result = p.export(ExportType.PDF)
    result.get_pdf()

# Problems
# 1. Violate Open/Clse
# 2. Violate Single Responsibility
# 3. Coupling
# 4. Presentation should have many knowledge about other classes
