# Designing GUI famework
# Framework layer
from abc import ABC, abstractmethod


class Form(ABC):
    # Is called 'Mediator' in design pattern books
    @abstractmethod
    def change(self, ui_contorler):
        pass


class UIContorler(ABC):
    # Is called 'Component' in design pattern books
    def __init__(self, form: Form) -> None:
        self._form = form
        # form attribute must be 'protected' type,
        # because we want to use it in UIContorler subclasses
        # but we don't want other developer have access to it


class TextBox(UIContorler):
    def __init__(self, form: Form) -> None:
        super().__init__(form)
        self.__content = ""

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content
        self._form.change(self)


class Button(UIContorler):
    def __init__(self, form: Form) -> None:
        super().__init__(form)
        self.__disable = True

    def active(self):
        self.__disable = False
        self._form.change(self)

    def deactivate(self):
        self.__disable = True
        self._form.change(self)

    @property
    def activation(self):
        return not self.__disable


class ListBox(UIContorler):
    def __init__(self, form: Form) -> None:
        super().__init__(form)
        self.__selection = ""

    def select(self, selection):
        self.__selection = selection
        self._form.change(self)

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

    class EducationForm(Form):
        def __init__(self) -> None:
            self.button = Button(self)
            self.text = TextBox(self)
            self.list_box = ListBox(self)

        def change(self, ui_contorler):
            if isinstance(ui_contorler, ListBox):
                self.text.content = ui_contorler.selected
            elif isinstance(ui_contorler, TextBox):
                if ui_contorler.content == "" or ui_contorler.content == None:
                    self.button.deactivate()
                else:
                    self.button.active()
            elif isinstance(ui_contorler, Button):
                pass

    education_form = EducationForm()

    education_form.text.content = None
    assert education_form.button.activation is False

    education_form.text.content = "Hello"
    assert education_form.button.activation is True

    education_form.list_box.select("Buy")
    assert education_form.button.activation is True
    assert education_form.text.content == "Buy"

# As you see, without any changes and overriding we implement the scenario
