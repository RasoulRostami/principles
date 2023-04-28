# Design GUI Framework
#
# Framework layer
from typing import Optional


class Input:
    def __init__(self, lable: Optional[str] = None) -> None:
        self.__lable = lable

    @property
    def lable(self):
        return self.__lable

    @lable.setter
    def lable(self, lable: str):
        self.__lable = lable

    def click(self):
        # implement depends on developer and scenarios.
        # we will use polymorphis to have better design.
        pass


# Application layer
class AddClientButton(Input):
    def click(self):
        print("Add client")


class SaveClientButton(Input):
    def click(self):
        print("Save Client")


class RemoveClientButton(Input):
    def click(self):
        print("Remove Client")


if __name__ == "__main__":
    add_client_botton = AddClientButton("add")
    save_client_button = SaveClientButton("save")
    remove_client_button = RemoveClientButton("remove")

    add_client_botton.click()
    save_client_button.click()
    remove_client_button.click()

# As you see, it works but it is not a good design.
# in the above implemtation we use inheritance and overide the behavior of a class
# This is not the currect solution.
# What happens if we want to modify Input class in framework?
# What happens if we want to rename click method in framework?
# What happens if you want to do something before and after the click main function?
