# Design GUI framework
#
# Framework layer
import abc


class Command(abc.ABC):
    # called 'Command' in design patterns books
    @abc.abstractmethod
    def execute(self):
        pass


class Button:
    # called 'Invoker' in design patterns books
    def __init__(self, command: Command) -> None:
        self.__command = command
        self.__lable = None

    @property
    def lable(self):
        return self.__lable

    @lable.setter
    def lable(self, lable: str):
        self.__lable = lable

    def click(self):
        self.__command.execute()


# Application layer
class SaveClient(Command):
    def execute(self):
        print("Save client")


class AddClient(Command):
    def execute(self):
        print("add client")


class RemoveClient(Command):
    def execute(self):
        print("remove client")


if __name__ == "__main__":
    add_button = Button(AddClient())
    save_button = Button(SaveClient())
    remove_button = Button(RemoveClient())

    add_button.click()
    save_button.click()
    remove_button.click()
