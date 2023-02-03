"""
Description:
it is very useful design pattern that we can see in lots of frameworks
imagine we want to design a framework witch has some objects, these objects has some
common attribute and behavior but some of behavior are depends on situation and application
developers who use our framework must define these behavior

What is best design to develop above scenarios,

Command pattern is used to undo scenario too. As we saw we use memento design pattern for undo
Memento save an objects in every changes and we take lots of snapshout in our application, but
some time it is not good solutions, For example in video-editor application we can't take many
snapshouts because we lost many memory.
In this cases we use command design patter, every behaviors have to undo their actions.

# Example:
We want to design and implement GUI framework.
"""

# first design
# framework layer
class Input:
    def __init__(self) -> None:
        self.__lable = None

    @property
    def lable(self):
        return self.__lable

    @lable.setter
    def lable(self, lable: str):
        self.__lable = lable

    def click(self):
        # implement depends on users and other developers, what is the best way to design.
        # we use polymorphis to have better design.
        pass


# application layer
class AddClientButton(Input):
    def click(self):
        print("Add client")


# using
print("============ without command design pattern ============")
add_client_botton = AddClientButton()
add_client_botton.click()

# problems
# in the above implemtation we use inheritance and overide the behavior of a class
# This is not the currect solution.
# What happens if you want to modify Input class?
# What hallens if you want to rename click method?
# What happens if you want to do something before and after the click main function?

# impelementt with command design pattern
# framework layer
import abc


class Command(abc.ABC):
    # called Command in books
    @abc.abstractmethod
    def execute(self):
        pass


class Button:
    # called 'Invoker' in books
    def __init__(self, client_command: Command) -> None:
        self.__client_command = client_command
        self.__lable = None

    @property
    def lable(self):
        return self.__lable

    @lable.setter
    def lable(self, lable: str):
        self.__lable = lable

    def click(self):
        self.__client_command.execute()


# application layer
class ClientService:
    # clladed 'Receiver' in books
    def add_client(self):
        print("Add Client")


class AddClientCommand(Command):
    # called 'Concerate-Command' in books
    def __init__(self, service: ClientService) -> None:
        self.service = service

    def execute(self):
        self.service.add_client()


# useing, bring all of them together
print("================ Using Command design pattern")
service = ClientService()
command = AddClientCommand(service)
botton = Button(command)
botton.click()

# Use Command for undo system
# we want to design and develop HTML Editor
#
# framework layout
class Action(abc.ABC):
    # called 'Command' in books
    @abc.abstractmethod
    def execute(self):
        pass


class UndoableAction(Action):
    # called 'UndoCommand' in books
    # We seprate action and undo-action because some actions
    # has not undo, for example save action has no undo
    @abc.abstractmethod
    def unexecute(self):
        pass


class History:
    def __init__(self) -> None:
        self.__commands = []

    def push(self, command: Action):
        self.__commands.append(command)

    def pop(self) -> UndoableAction:
        return self.__commands.pop()


# application layer


class HTMLEditor:
    # Called 'reciver'
    def __init__(self) -> None:
        self.__content = ""

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    def make_bold(self):
        self.__content = "<br> " + self.__content + " </br>"

    def make_div(self):
        self.__content = "<div> " + self.__content + " </div>"


class BoldContentCommand(UndoableAction):
    # called 'concerate-command'
    def __init__(self, editor: HTMLEditor) -> None:
        self.prev_content = ""
        self.ediitor = editor

    def execute(self):
        self.prev_content = self.ediitor.content
        self.ediitor.make_bold()

    def unexecute(self):
        self.ediitor.content = self.prev_content


# using
editor = HTMLEditor()
editor.content = "Hello Word"
bold = BoldContentCommand(editor)

print("================ Using Command design pattern for undo command")
print(editor.content)
bold.execute()
print(editor.content)
bold.unexecute()
print(editor.content)

# also we can have history of all activies
class DivContentCommand(UndoableAction):
    # called 'concerate-command'
    def __init__(self, editor: HTMLEditor, history: History) -> None:
        self.ediitor = editor
        self.history = history

    def execute(self):
        self.prev_content = self.ediitor.content
        self.ediitor.make_div()
        self.history.push(self)

    def unexecute(self):
        self.ediitor.content = self.prev_content


class UndoAction(Action):
    def __init__(self, history: History) -> None:
        self.history = history

    def execute(self):
        self.history.pop().unexecute()


print("================ Using Command design pattern for undo used commands")
editor.content = "Hi Guys"
history = History()
div = DivContentCommand(editor, history)
print(editor.content)
div.execute()
print(editor.content)
undo = UndoAction(history)
undo.execute()
print(editor.content)
