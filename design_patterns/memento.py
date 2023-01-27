"""
Description:
Memento design pattern is used when we have undo mechanism

Problems:
If you want to have undo mechanism in an application there will be some problems
that Memento help you solve them in below codes we will see some of the problems

Example:
Imagine we are developing an editor application and we need to have client's previous contents

Note:
You will see (Single Responsible Principle) in these examples
"""

# ------------------ Solution one
class Editor0:
    def __init__(self) -> None:
        # save previous state when title and content is changed
        self.title = ""
        self.content = ""
        self.previous_title = ""
        self.previous_content = ""


# --- problems
# # 1. we can only have last state not any more


# ------------------ Solution two
class Editor1:
    def __init__(self) -> None:
        # append previous state when title and content is changed
        self.title = ""
        self.content = ""
        self.previous_title = list
        self.previous_content = list


# --- problems
# 1. If we have dozens of attribute we will have messy and crowded class
# 2. Violation of single responsibility principles

# ------------------ Solution three
class Editor3:
    def __init__(self) -> None:
        # When editor state is changed we create EditorState instance and save it
        self.title = ""
        self.content = ""


class Editor3State:
    def __init__(self) -> None:
        self.title = ""
        self.content = ""


# --- problems
# 1. How does we manage the EditorState?

# ------------------ Solution four (Memento design patterns)


class EditorState:
    """Store editor state in this model"""

    # EditorState is called "Memento" in books

    def __init__(self, content: str) -> None:
        self.__content = content

    @property
    def content(self):
        return self.__content


class Editor:
    # Editor is called "Originator" in books
    def __init__(self) -> None:
        self.__content = ""

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str) -> None:
        self.__content = content

    def save(self) -> EditorState:
        # save or create snapshot or create state
        # save current state
        return EditorState(self.__content)

    def undo(self, state: EditorState) -> None:
        # undo or restore
        # return previous state
        self.__content = state.content


class History:
    # History is called "Caretaker" is books
    def __init__(self) -> None:
        self.__list = []

    def push(self, state: EditorState):
        # push or add
        # Add new state to list
        self.__list.append(state)

    def pop(self):
        # pop or get
        # remove and return last state
        return self.__list.pop()


if __name__ == "__main__":
    editor = Editor()
    history = History()

    editor.content = "A"
    history.push(editor.save())

    editor.content = "B"
    history.push(editor.save())

    editor.content = "C"

    print("# Editor current state is {}".format(editor.content))
    editor.undo(history.pop())
    print("-> After restore editor content")
    print("# Editor current state is {}".format(editor.content))
