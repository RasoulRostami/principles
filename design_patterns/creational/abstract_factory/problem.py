"""
We are designing GUI application with some widgets and themes.
"""
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


# enum
class Theme(Enum):
    Material = 1
    Ant = 2


# Form
class Form:
    def render(self, theme):
        if theme == Theme.Ant:
            button = AntButton().render()
            text_box = AntTextBox().render()
        elif theme == Theme.Material:
            button = MaterialButton().render()
            text_box = MaterialTextBox().render()


if __name__ == "__main__":
    form = Form()
    form.render(Theme.Ant)
    form.render(Theme.Material)

# Problem
# The above codes works correctly but:
# 1. Violate Open/Close, Update Form if new theme or widget is added
# 2. Coupling in Form class
# 3. increase developer mistake
