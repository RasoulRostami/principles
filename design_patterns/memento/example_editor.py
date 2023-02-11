# Design Editor application


class EditorState:
    """Store editor state in this model"""

    # Called "Memento" in books

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
    # Save history of editor changes
    def __init__(self) -> None:
        self.__list = []

    def push(self, state: EditorState):
        # push / add
        # Add new state to list
        self.__list.append(state)

    def pop(self):
        # pop / get
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
    print("-> After double restore")
    editor.undo(history.pop())
    print("# Editor current state is {}".format(editor.content))
