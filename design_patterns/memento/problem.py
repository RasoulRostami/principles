# Design editor application
#
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
# 1. If we have dozens of attributes we will have messy and crowded class
# 2. Violation of single responsibility principles

# ------------------ Solution three
class Editor3State:
    def __init__(self) -> None:
        self.title = ""
        self.content = ""


class Editor3:
    def __init__(self) -> None:
        # When editor state is changed we create EditorState instance and save it
        self.__title = ""
        self.__content = ""

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title


# --- problems
# 1. How does we manage the EditorState?
# 2. How does we fill EditorState, how to save and restore that,
# 3. How does we have history of changes
