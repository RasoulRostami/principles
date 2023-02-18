# Design GUI framework
# Use mediator and observer design patterns
# Framework layer
from abc import ABC, abstractmethod
from typing import Callable


class EventHandler(ABC):
    @abstractmethod
    def change(self):
        pass


class UIContorler(ABC):
    def __init__(self) -> None:
        self._event_handlers = []

    def add_avent(self, event: Callable):
        self._event_handlers.append(event)

    def call_event(self):
        for event in self._event_handlers:
            event()


class TextBox(UIContorler):
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content
        self.call_event()


class Button(UIContorler):
    def active(self):
        self.__disable = False
        self.call_event()

    def deactivate(self):
        self.__disable = True
        self.call_event()

    @property
    def activation(self):
        return not self.__disable


class ListBox(UIContorler):
    def select(self, selection):
        self.__selection = selection
        self.call_event()

    @property
    def selected(self):
        return self.__selection


# lets implement below scenario
# If TextBox is empty botton will be disable
# If users select from list, TextBox will be filled by selected item
# If TextBox is not empty button will be Anabel.
#
# application layer
if __name__ == "__main__":

    class EducationForm:
        def __init__(self) -> None:
            self.button = Button()
            self.text = TextBox()
            self.list_box = ListBox()
            self.text.add_avent(self.change_text_content)
            self.list_box.add_avent(self.select_item)

        def select_item(self):
            self.text.content = self.list_box.selected

        def change_text_content(self):
            if self.text.content == "" or self.text.content == None:
                self.button.deactivate()
            else:
                self.button.active()

    education_form = EducationForm()

    education_form.text.content = None
    assert education_form.button.activation is False

    education_form.text.content = "Hello"
    assert education_form.button.activation is True

    education_form.list_box.select("Buy")
    assert education_form.button.activation is True
    assert education_form.text.content == "Buy"

# As you see, without any changes and overriding we implement the scenario
