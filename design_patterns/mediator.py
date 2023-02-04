"""
Description:
Mediator is useful design pattern when have got couple of objects which have to talk each other.
With this design pattern we can design open/close and single responsible application.

Example:
We want to implement and GUI framework that other developer use.
"""

# ====================== Framework side ====================================
import abc


class UIContorler(abc.ABC):
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


class ListBox(UIContorler):
    def __init__(self) -> None:
        self.__selection = ""

    def select(self, selection):
        self.__selection = selection


# Scenario:
# If User select option from ListBox, TextBox.content = ListBox.selection
# When TextBox.content != "" or TextBox.content != null => botton.disable = False
# As you see when state change in ListBox or TextBox somethings will be happend.
# But use in application layer has not access to the framework source code, and if access
# he can not change the class because these are reusable classes.
# How other objecs are notified about changes

# ===================== Framework layer, mediator pattern, version 1 ================
# In Mediator design pattern we have a midelware class and all nodes know who is middelware class
# Here we create Form interface as middelware objects
class Form(abc.ABC):
    # called Mediator in books
    @abc.abstractmethod
    def changes(self, contoroller):
        pass


class UIContorlerV1(abc.ABC):
    def __init__(self, form: Form) -> None:
        self.form = form


class TextBoxV1(UIContorlerV1):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.__content = ""

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content
        self.form.changes(self)


class ButtonV1(UIContorlerV1):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.__disable = True

    @property
    def status(self):
        return self.__disable

    def active(self):
        self.__disable = False

    def deactive(self):
        self.__disable = True


class ListBoxV1(UIContorlerV1):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.__selection = ""

    def select(self, selection):
        self.__selection = selection
        self.form.changes(self)

    @property
    def selection(self):
        return self.__selection


# ========== application layer
class EducationForm(Form):
    def __init__(self) -> None:
        self.save_button = ButtonV1(self)
        self.education_list = ListBoxV1(self)
        self.text_box = TextBoxV1(self)

    def changes(self, contoroller):
        if isinstance(contoroller, ListBoxV1):
            if contoroller.selection is not None or contoroller.selection != "":
                self.save_button.active()
                self.text_box.content = contoroller.selection
        elif isinstance(contoroller, TextBoxV1):
            if contoroller.content == "" or contoroller.content is None:
                self.save_button.deactive()


education_from = EducationForm()
print("before changes")
print(education_from.save_button.status)  # expect is True
print(education_from.text_box.content)  # expect is ""
education_from.education_list.select("x")
print(education_from.save_button.status)  # expect is False
print(education_from.text_box.content)  # expect is X
education_from.text_box.content = None
print(education_from.save_button.status)  # expect is True

# This is very good, but when we have lots of nodes and attributes, changes fucntion will be very fat
# and unreadable,
# good idea is use observer and mediator togther
# ===================== Framework layer, mediator pattern, version 2 ================
class EventHandler(abc.ABC):
    @abc.abstractmethod
    def changes(self):
        pass


class UIContorlerV2(abc.ABC):
    def __init__(self) -> None:
        self.event_list = []

    def add_event(self, event):
        self.event_list.append(event)

    def call_events(self):
        for event in self.event_list:
            event()


class TextBoxV2(UIContorlerV2):
    def __init__(self) -> None:
        super().__init__()
        self.__content = ""

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content
        self.call_events()


class ButtonV2(UIContorlerV2):
    def __init__(self) -> None:
        super().__init__()
        self.__disable = True

    @property
    def status(self):
        return self.__disable

    def active(self):
        self.__disable = False

    def deactive(self):
        self.__disable = True


class ListBoxV2(UIContorlerV2):
    def __init__(self) -> None:
        super().__init__()
        self.__selection = ""

    def select(self, selection):
        self.__selection = selection
        self.call_events()

    @property
    def selection(self):
        return self.__selection


# ============= application layer
class CarForm:
    def __init__(self) -> None:
        self.save_button = ButtonV2()
        self.car_list = ListBoxV2()
        self.text_box = TextBoxV2()
        self.car_list.add_event(self.select_car)
        self.text_box.add_event(self.change_content)

    def select_car(self):
        if self.car_list.selection is not None or self.car_list.selection != "":
            self.save_button.active()
            self.text_box.content = self.car_list.selection

    def change_content(self):
        if self.text_box.content == "" or self.text_box.content is None:
            self.save_button.deactive()


print("============= use observer and mediator together")
car_form = CarForm()
print("before changes")
print(car_form.save_button.status)  # expect is True
print(car_form.text_box.content)  # expect is ""
car_form.car_list.select("BMW")
print(car_form.save_button.status)  # expect is False
print(car_form.text_box.content)  # expect is BMW
car_form.text_box.content = None
print(car_form.save_button.status)  # expect is True
