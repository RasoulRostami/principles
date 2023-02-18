# Framework layer
import abc


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


class BoldAction(UndoableAction):
    # called 'concerate-command'
    # Undoable command without hsitory
    def __init__(self, editor: HTMLEditor) -> None:
        self.prev_content = ""
        self.ediitor = editor

    def execute(self):
        self.prev_content = self.ediitor.content
        self.ediitor.make_bold()

    def unexecute(self):
        self.ediitor.content = self.prev_content


class DivAction(UndoableAction):
    # called 'concerate-command'
    # Undoable command with history
    def __init__(self, editor: HTMLEditor, history: History) -> None:
        self.ediitor = editor
        self.history = history
        self.pre_content = ""

    def execute(self):
        self.pre_content = self.ediitor.content
        self.history.push(self)
        self.ediitor.make_div()

    def unexecute(self):
        self.ediitor.content = self.history.pop().pre_content


if __name__ == "__main__":
    editor = HTMLEditor()
    editor.content = "Hello Word"
    bold = BoldAction(editor)

    print("pre bold: ", editor.content)
    bold.execute()
    print("after bold: ", editor.content)
    bold.unexecute()
    print("after undo: ", editor.content)

    print("------ test history ------")
    editor.content = "Hi Guys"
    history = History()
    div = DivAction(editor, history)
    print("pre div: ", editor.content)
    div.execute()
    print("after div: ", editor.content)
    div.unexecute()
    print("after undo: ", editor.content)
