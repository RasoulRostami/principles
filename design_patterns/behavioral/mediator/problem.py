# Design GUI framework that other developer uses.
from abc import ABC


class UIContorler(ABC):
    pass


class TextBox(UIContorler):
    def __init__(self) -> None:
        self.__content = ""

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content


class Button(UIContorler):
    def __init__(self) -> None:
        self.__disable = True

    def active(self):
        self.__disable = False

    def deactivate(self):
        self.__disable = True

    @property
    def activation(self):
        return self.__disable


class ListBox(UIContorler):
    def __init__(self) -> None:
        self.__selection = ""

    def select(self, selection):
        self.__selection = selection


# lets implement below scenario
# If TextBox is empty botton will be disable
# If users select from list, TextBox will be filled by selected item
# If TextBox is not empty button will be Anabel.

# As far as I said, we are going to design GUI framework, so developer has not access to
# the source codes, Developers must change main source codes.
# So in application layer we will have:


class CustomButton(Button):
    def toggle_active(self, text_box: TextBox):
        if text_box.content != "" or text_box.content is None:
            self.deactivate()
        else:
            self.active()


class CustomListBox(ListBox):
    def __init__(self, text_box: TextBox) -> None:
        self.__text_box = text_box

    def select(self, selection):
        super().select(selection)
        self.__text_box.content = selection


if __name__ == "__main__":
    button = CustomButton()
    text_box = TextBox()
    list_box = CustomListBox(text_box)

    list_box.select("A")
    assert text_box.content == "A"

    button.toggle_active(text_box)
    assert button.activation == True

    list_box.select("")
    button.toggle_active(text_box)
    assert button.activation == False

# This is really a very bad implementation. and codes have many coupling.
# As far as i said, this will be GUI framework, so:
# Developer has not access to the source code.
# If have access they can't change it. If they
# change the source code, they can't update framework
# because changes are not backward compatible.
