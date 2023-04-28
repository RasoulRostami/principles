from abc import ABC, abstractmethod
from enum import Enum

# Widgets
class Widget(ABC):
    @abstractmethod
    def render(self):
        pass


class Button(Widget, ABC):
    @abstractmethod
    def render(self):
        pass


class TextBox(Widget, ABC):
    @abstractmethod
    def render(self):
        pass


# Themes
class MaterialButton(Button):
    def render(self):
        print("Material button")


class AntButton(Button):
    def render(self):
        print("Ant button")


class MaterialTextBox(TextBox):
    def render(self):
        print("Material text box")


class AntTextBox(TextBox):
    def render(self):
        print("Ant text box")


# Biulder
class WidgetFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_text_box(self) -> TextBox:
        pass


class MaterialFactory(WidgetFactory):
    def create_button(self) -> Button:
        return MaterialButton()

    def create_text_box(self) -> TextBox:
        return MaterialTextBox()


class AntFactory(WidgetFactory):
    def create_button(self) -> Button:
        return AntButton()

    def create_text_box(self) -> TextBox:
        return AntTextBox()


# Form
class Form:
    def render(self, builder: WidgetFactory):
        builder.create_button().render()
        builder.create_text_box().render()


if __name__ == "__main__":
    form = Form()
    form.render(AntFactory())
    form.render(MaterialFactory())
